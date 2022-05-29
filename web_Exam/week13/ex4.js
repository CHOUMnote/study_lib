$(document).ready(function(){
    let cnt = 0;
    let id;
    $('#play').on('click',()=>{
        id = setInterval(function(){
            let a = Math.floor(Math.random() * 31)+10
            $("#panel").append($(`<span>${cnt++} </span>`).css("font-size",a));
        }, 1000); 
    });
    $("#stop").on('click',()=>{
        clearInterval(id);
    })
});
