$(".seat").click(function () {
    var favorite = [];
    $.each($("input[name='check']:checked"), function () {
      favorite.push($(this).val());
    });

    $("#slots").empty().append(favorite.join(", "));

  });