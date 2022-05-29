$(document).ready(() => {
    let color = ["red", "orange", "blue", "yellow", "green"];
    $("div").each(function (i) {
        $(this).css({
            "height": "100px", "width": "100px", "background-color": color[i], "display": "inline-block", "line-height": "100px",
            "text-align": "center"
        });
        $(this).addClass("n_" + i);
    });
    setInterval(slide, 2000);
});
function slide() {
    let d = $("div").eq(4).prependTo("body");
}