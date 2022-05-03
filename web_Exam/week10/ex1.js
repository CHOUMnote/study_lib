let play={
    name:"이소라",
    song:"바람이 분다",
    time: 3.5,
    play:function(cnt){
        for(let i = 1; i<=cnt; i++){
            document.write(`가수 : ${this.name}, 제목 : ${this.song}, 재생시간 : ${this.time*i} => ${i}번째 재생<br>`);
        }
    }
}
play.play(5);