$(function () {
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-news").modal("show");
            },
            success: function (data) {
                $("#modal-news .modal-content").html(data.html_form);
            }
        });
    };
    $("#news-table").on("click", ".js-view-news", loadForm);
}
);