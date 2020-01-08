$(function () {

    /* Functions */

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-complain").modal("show");
            },
            success: function (data) {
                $("#modal-complain .modal-content").html(data.html_form);
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
                    $("#complain-table tbody").html(data.html_complain_list);
                    $("#modal-complain").modal("hide");
                } else {
                    $("#modal-complain .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create complain
    $(".js-create-complain").click(loadForm);
    $("#modal-complain").on("submit", ".js-complain-create-form", saveForm);

    // Update complain
    $("#complain-table").on("click", ".js-update-complain", loadForm);
    $("#modal-complain").on("submit", ".js-complain-update-form", saveForm);

    // view complain
    $("#complain-table").on("click", ".js-view-complain", loadForm);
    $("#modal-complain").on("submit", ".js-complain-view-form", saveForm);

    // Delete complain
    $("#complain-table").on("click", ".js-delete-complain", loadForm);
    $("#modal-complain").on("submit", ".js-complain-delete-form", saveForm);

});