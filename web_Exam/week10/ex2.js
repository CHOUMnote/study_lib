function car(a, b){
    this.number = a;
    this.dist = b;
}
car.prototype.addMileage = function(dist){
    this.dist += dist;
}
car.prototype.toString = function(){
    return `차량번호 : ${this.number} 주행거리 : ${this.dist}<br>`;
}
document.write(`<h1>결과를 출력합니다</h1><hr>`);

let arr = [];

while (true){
    let str = prompt("차량번호와 주행거리를 입력하세요\n더 이상 없으면 완료를 입력하세요");
    if(str == '완료'){
        break;
    }
    let sp = str.split(" ");
    arr.push(new car(sp[0], sp[1]));
}

for(let i = 0; i<arr.length; i++){
    document.write(arr[i].toString());
}