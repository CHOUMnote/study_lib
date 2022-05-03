class Vaccin{
    constructor(a,b){
        this.vaccin = a;
        this.count = 0;
        this.phone = b;
    }
    isFinished(){
        if(this.count==0){
            return "미 접종";
        }else if(this.count == 2){
            return "접종 완료";
        }else{
            return "추가 1회";
        }
    }
    addShot(){
        if(this.count < 2){
            this.count++;
        }
    }
    changeTel(value){
        this.phone = value;
    }
}

let kim = new Vaccin('화이자', '010-2193-5234');
console.log(`백신 종류 : ${kim.vaccin}, 연락처 : ${kim.phone}, 접종현황 : ${kim.isFinished()}`);
kim.addShot()
console.log(`백신 종류 : ${kim.vaccin}, 연락처 : ${kim.phone}, 접종현황 : ${kim.isFinished()}`);
kim.changeTel('010-6543-7968')
console.log("연락처 변경 후 출력");
console.log(`백신 종류 : ${kim.vaccin}, 연락처 : ${kim.phone}, 접종현황 : ${kim.isFinished()}`);
kim.addShot()
console.log(`백신 종류 : ${kim.vaccin}, 연락처 : ${kim.phone}, 접종현황 : ${kim.isFinished()}`);
kim.addShot()
console.log(`백신 종류 : ${kim.vaccin}, 연락처 : ${kim.phone}, 접종현황 : ${kim.isFinished()}`);