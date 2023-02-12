function getData() {
    fetch('https://api.kanye.rest')
        .then((response) => response.json())
        .then((json) => {
            document.getElementById('q').innerHTML = json.quote;
            console.log(`received response`);
        })
        .catch((error) => {
            console.log(error);
            document.getElementById('q').innerHTML = `error occured`;
            document.getElementById('q').setAttribute("class", "text-danger")
        });
    console.log(`request sent`);
}