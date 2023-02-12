'use strict';

function formatDate(date) {
    const year = date.toLocaleString("default", { year: "numeric", });
    const month = date.toLocaleString("default", { month: "2-digit", });
    const day = date.toLocaleString("default", { day: "2-digit", });
    const hours = date.toLocaleString("default", { hour: "2-digit" });
    const minutes = date.toLocaleString("default", { minute: "2-digit" });
    const seconds = date.toLocaleString("default", { second: "2-digit" });

    return `${day}-${month}-${year} ${hours}:${minutes}:${seconds}`;
};

function toggleDate() {
    let btn = document.getElementById('date-btn');
    const p = document.getElementById('date-paragraph');

    const currDate = formatDate(new Date());

    if (btn.innerHTML === 'Show Date') {
        p.innerHTML = currDate;
        btn.innerHTML = "Hide Date";
    } else if (btn.innerHTML === 'Hide Date') {
        p.innerHTML = "";
        btn.innerHTML = "Show Date";
    }
}

function togglePhoto(event) {
    const btn = event.target
    const target = btn.parentNode.children[0]
    if (target.hasAttribute('hidden')) {
        btn.innerText = `Hide Photo`
        target.removeAttribute('hidden')
        console.log(`shown`);
    } else {
        btn.innerText = `Show Photo`
        target.setAttribute('hidden', true)
        console.log(`hidden`);
    }
}