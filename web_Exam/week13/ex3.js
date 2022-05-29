$(document).ready(function(){
    let add = $("#add")
    let remove = $("#remove")
    let result = $("[type=text]");
    let ul = $(".menu");
    add.on('click',()=>{
        ul.append(`<li>${result.val()}</li>`);
        result.val("");
    });
    remove.on('click',()=>{
        let li = $("li")
        li.each(function(i){
            if($(this).text() === result.val())
                $(this).remove();
        });
        result.val("");
    });
});