$(document).ready(function(){
    let color = ["red","lime","blue"]
    $("div").each(function(i){
        $(this).css({
            'background-color':color[i],
            'width':100,
            "height":100,
            'position':"fixed",
            left:100+i*50,
            top:100+i*50
        });
    });
    $("div").click(function(){
        $("div").fadeTo(1000,Math.random())
    })
});