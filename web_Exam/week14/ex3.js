$(document).ready(function(){
    $("nav").hover(
        function(){
            $(this).animate({top:"+=35px"},1000);
        },function(){
            $(this).animate({'top':"-=35"},1000);
        }
    );
    let c = $("li").css("color");
    $("li").hover(
        function(){
            $(this).css({"color":"black","text-decoration" : 'underline'});
        }, function(){
            $(this).css({"color":c,"text-decoration":'none'});
        }
    );
});
