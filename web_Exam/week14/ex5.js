$(document).ready(function(){
    $(".outer-menu-item").hover(
        function(){
            $(this).find(".inner-menu").show(1000);
        }, function(){
            $(this).find(".inner-menu").hide(1000);
        }
    );
});