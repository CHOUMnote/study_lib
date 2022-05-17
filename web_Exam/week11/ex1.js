window.onload = function (){
    let li = document.getElementsByTagName("li") ;
    for (let i of li){
        if(i.className == 'red'){
            i.style.color = 'green';
        }
        else{
            i.style.color = 'blue';
        }
    }
}
