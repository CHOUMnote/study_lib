window.onload = ()=>{
    let id = document.querySelectorAll('input')[0]
    let password = document.querySelectorAll('input')[1]
    let ADDbtn = document.querySelectorAll('input')[2]
    let box = document.getElementById('container');

    id.addEventListener("keydown", (e)=>{
        if(id.value.length >= 8){
            password.focus();
        }
    });

    password.addEventListener("keydown", (e)=>{
        if(e.keyCode === 8 && password.value.length === 0){
            id.focus();
        }
    });

    ADDbtn.addEventListener("click", (e)=>{
        alert(`데이터 처리 완료\nid=${id.value} password=${password.value}`);
        let a = document.createElement('p');
        let b = document.createTextNode(`id=${id.value} password=${password.value}`);
        a.appendChild(b);
        box.appendChild(a);
        id.value = "";
        password.value = "";
    });
}