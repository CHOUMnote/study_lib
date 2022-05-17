window.onload = function (){
    let className = document.querySelectorAll(".hallym")
    let cnt = 0;
    for(let i of className){
        i.style.width = "100px";
        if(cnt++ % 2  == 0){
            i.style.backgroundColor="yellow";
        }
        else {
            i.style.backgroundColor="gray";
        }
    }
}
