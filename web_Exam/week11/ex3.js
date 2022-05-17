function childNodeAdd(){
    let elem = document.createElement('p');
    let text = document.createTextNode(document.getElementById('name').value);
    elem.appendChild(text);
    document.getElementById('list').appendChild(elem);
}
function childNodeDelete(){
    let target = document.querySelectorAll('p');
    let del;
    for(let i of target){
        if(i.textContent == document.getElementById('name').value){
            del = i;
            break;
        }
    }
    document.getElementById('list').removeChild(del);
}
