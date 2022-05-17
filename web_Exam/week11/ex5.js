function insert() {
    let arr = [];
    while(true){
        arr.push(prompt("여행지를 입력하세요. 더 이상 없으면 'f'를 입력하세요"));
        if(arr[arr.length-1]=='f'){
            arr.pop();
            break;
        }
    }
    for(let i of arr){
        document.querySelector('ul').innerHTML += `<li>${i}</li>`;
    }
    let li = document.querySelectorAll('li');
    let cnt = 0;
    for(let i of li){
        i.style.listStyle = 'decimal';
        if(cnt++%2 == 0){
            i.style.color = 'red'; 
        }
        else{
            i.style.color='green';
        }
    }
}