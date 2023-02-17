$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-action").modal("show");
            },
            success: function (data) {
                $("#modal-action .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function () {
        var form = $(this);
        var formData = new FormData(form[0]);
        $.ajax({
            url: form.attr("action"),
            data: formData,
            type: form.attr("method"),
            dataType: 'json',
            async: true,
            cache: false,
            contentType: false,
            enctype: form.attr("enctype"),
            processData: false,
            success: function (data) {
                if (data.form_is_valid) {
                    $("#action-table tbody").html(data.html_action_list);
                    $("#modal-action").modal("hide");
                } else {
                    $("#modal-action .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create action
    $(".js-create-action").click(loadForm);
    $("#modal-action").on("submit", ".js-action-create-form", saveForm);

    // view action
    $("#action-table").on("click", ".js-view-action", loadForm);
    $("#modal-action").on("submit", ".js-action-view-form", saveForm);

    // Update action
    $("#action-table").on("click", ".js-update-action", loadForm);
    $("#modal-action").on("submit", ".js-action-update-form", saveForm);

    // Delete action
    $("#action-table").on("click", ".js-delete-action", loadForm);
    $("#modal-action").on("submit", ".js-action-delete-form", saveForm);

});
