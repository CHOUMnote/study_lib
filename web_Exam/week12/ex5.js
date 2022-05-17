$(document).ready(function(){
    $('li').each(function(){
        if($(this).attr('class') === 'red'){
            $(this).text("jQuery").css("color","green");
        }
        else{
            $(this).text("selector 연습").css("color","blue");
        }
    });
});