$(function () {
    /* Functions */
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-members").modal("show");
            },
            success: function (data) {
                $("#modal-members .modal-content").html(data.html_form);
            }
        });
    };
    $("#members-table").on("click", ".js-view-members", loadForm);

    // var saveForm = function () {
    //     var form = $(this);
    //     var formData = new FormData(form[0]);
    //     $.ajax({
    //         url: form.attr("action"),
    //         data: formData,
    //         type: form.attr("method"),
    //         dataType: 'json',
    //         async: true,
    //         cache: false,
    //         contentType: false,
    //         enctype: form.attr("enctype"),
    //         processData: false,
    //         success: function (data) {
    //             if (data.form_is_valid) {
    //                 $("#invoice-table tbody").html(data.html_news_list);
    //                 $("#modal-members").modal("hide");
    //             } else {
    //                 $("#modal-members .modal-content").html(data.html_form);
    //             }
    //         }
    //     });
    //     return false;
    // };
    /* Binding */
    // view members
    //$("#modal-members").on("submit", ".js-members-view-form", saveForm);

});