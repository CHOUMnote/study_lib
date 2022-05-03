class Gugudan{
    constructor(){
        this.sum = 0;
        this.play()
    }
    play(){
        let a;
        let b;
        for(let i = 0; i<10; i++){
            a = Math.floor(Math.random()*8)+2 //0~7 + 2 => 2~9
            b = Math.floor(Math.random()*9)+1 //0~8 + 1 => 1~9
            this.calc(i+1,a,b);
        }
        this.result(this.sum);
    }
    calc(i,x,y){
        let result = x * y;
        if(prompt(i+') '+x+"*"+y+" = ?") == result){
            this.sum+=10;
        }
    }
    result(a){
        if(a >= 90){ alert('점수 : '+ a +"-> 친구와 놀아도 됩니다."); }
        else if(a>=80){ alert('점수 : '+ a +"-> 한번 더 연습하세요."); }
        else if(a>=70){ alert('점수 : '+ a +"-> 두번 더 연습하세요."); }
        else{ alert('점수 : '+ a +"-> 친구와 놀 수 없습니다"); }
    }
}

let gugu = new Gugudan();