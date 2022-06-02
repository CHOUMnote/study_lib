$(document).ready(function () {
    $('mark').click(function() {
        $(this).fadeTo(1000,Math.random());
    });
    $("summary").hover(function () {
        $("em").stop().show(500);
    },function(){
        $("em").stop().hide(500);
    });
    $("p").animate({
        margin : "+=100",
        "font-size":"+=10"
    }, 1000, a);
});
function a(){
    $("p").delay(3000).animate({
        margin : "-=100",
        "font-size":"-=10"
    },500);
}

