class Account{
    constructor(a,b){
        this.name = a;
        this.money = b;
        console.log("현재 상태 입니다.")
        this.display();
    }
    deposit(n){
        this.money+=n;
        console.log(n+"예금 후 상태입니다.");
        this.display();
    }
    withdraw(n){
        console.log(n+"을 인출하려고 합니다.");
        if(this.money - n < 0){
            console.log("잔액부족 : "+(n-this.money));
        }else{
            this.money-=n;
            console.log(n+"출금 후 상태입니다.");
            this.display();
        }
    }
    display(){
        console.log("예금주 : "+this.name);
        console.log("현재 잔액 : "+this.money);
        console.log("\n");
    }
}

let kim = new Account('김지호', 50000);
kim.deposit(50000);
kim.withdraw(1000000);