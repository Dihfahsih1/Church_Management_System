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
    }
);