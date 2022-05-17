class object{
    constructor(name, cnt){
        this.name = name;
        this.cnt = cnt;
    }
    toString(){
        return `품목 : ${this.name},   구입개수 : ${this.cnt}`;
    }
}

$(document).ready(function(){
    let str = "";
    let sum = 0;
    while(true){
        let x = prompt("구입 품목과 개수를 입력하세요\n\
종료하려면 종료를 입력하세요").split(" ");
        if(x[0]==="종료") break;
        let obj = new object(x[0], x[1]);
        str+='<li>'+obj.toString()+"</li>";
        sum+=parseInt(obj.cnt);
    }
    $('ul').html(str);
    $('li').each(function(i){
        if(i%2 == 0){
            $(this).css("color","pink")
        }
        else{
            $(this).css("color","green");
        }
    });
    $('h2:last-of-type').text(`총 구매 개수는 ${sum} 입니다.`);

});