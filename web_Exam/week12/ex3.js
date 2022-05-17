const add = ()=>{
    let str = "";
    $(":checked").each(function(){
        str+=this.value+" ";
    });
    $('div').text(str);
}
$(document).ready(function(){
    add();
    $('input').on('click',add);
});