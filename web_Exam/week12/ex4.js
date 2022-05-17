let changeColor = function(){
    let color = ["red","blue","green","yellow","black","gray"];
    $('#box').css("background",color[Math.floor(Math.random() * color.length)]);
    
}
$(document).ready(function(){
    $('h1').text("1초마다 색이 변경되는 박스")
    $('#box').css("width","100px").css("height","100px").css("background","blue").addClass("blue");
    setInterval(changeColor,1000);
});