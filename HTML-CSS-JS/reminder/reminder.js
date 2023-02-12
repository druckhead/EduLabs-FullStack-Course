function btnClickHandler() {
    console.log(`button clicked`);
}

function btn2ClickHandler() {
    console.log(`button 2 clicked`);
}

function loadCompleteHandler() {
    document.getElementById('btn1').addEventListener("click", btnClickHandler);
    document.getElementById('btn2').addEventListener("click", btn2ClickHandler);
    document.getElementById('btn1').setAttribute('disabled', true);

    document.getElementById('btn2').onclick = () => {
        console.log(`blah`);
        document.getElementById('my-p').innerHTML = new Date();
    };
}

window.addEventListener("load", loadCompleteHandler);