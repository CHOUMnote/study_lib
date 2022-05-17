window.onload = () =>{

    document.querySelector("[type=button]").addEventListener("click", function(){
        let list = document.querySelectorAll(":checked");
        let str = "";
        for(let i of list){
            str += `${i.value}\n`;
        }
        alert(str);
    })
}