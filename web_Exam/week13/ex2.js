$(document).ready(function(){
    let box = $(".box1");
    let a = box.find("a");
    $("button").on("click",()=>{
        let radio = $("input:checked");
        let selected = $("#imglist").children(":selected");
        a.attr("href",radio.val()).text(radio.val());
        box.find("img").attr("src",selected.val());
        console.log(selected.val());
    });
});