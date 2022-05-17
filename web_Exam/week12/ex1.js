$(document).ready(function(){
    $('a').css('text-decoration','none' )
    $('div').css({"text-align":"center","line-height":"100px"}).addClass("circle");
    $('div').first().css("background","red");
    $('div').eq(1).css("background","green");
    $('div').last().css("background","yellow");
});
