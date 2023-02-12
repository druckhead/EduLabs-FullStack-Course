'use strict';

function formSubmitHandler(event) {
    event.preventDefault();

    const item = document.createElement('li');
    item.setAttribute('class', 'list-group-item d-flex justify-content-between align-items-center');

    const deleteButton = document.createElement('button');
    deleteButton.setAttribute('class', 'btn btn-outline-danger form-control-sm');
    deleteButton.innerHTML = "X";
    deleteButton.addEventListener("click", (event) => {
        const isConfirmed = confirm('Are you sure?')
        if (isConfirmed) {
            const deleteTarget = event.target.parentElement.parentElement
            deleteTarget.remove();
        }
    });

    const addButton = document.createElement('button');
    addButton.setAttribute('class', 'btn btn-outline-primary form-control-sm');
    addButton.innerHTML = "+";
    addButton.addEventListener("click", (event => {
        const incTarget = event.target.parentElement.parentElement.children[0].children[1];
        incTarget.innerText++
    }));

    const subtractButton = document.createElement('button');
    subtractButton.setAttribute('class', 'btn btn-outline-primary form-control-sm');
    subtractButton.innerHTML = "-";
    subtractButton.addEventListener("click", (event) => {
        const incTarget = event.target.parentElement.parentElement.children[0].children[1];
        incTarget.innerText--
    });

    const btnContainer = document.createElement('div');
    btnContainer.setAttribute("class", "container-fluid-sm d-flex gap-2");
    btnContainer.appendChild(addButton);
    btnContainer.appendChild(subtractButton);
    btnContainer.appendChild(deleteButton);

    const productItem = document.createElement('div');
    productItem.setAttribute("class", "d-flex gap-3 fs-3 p-2 bg-primary rounded");

    const list = document.getElementById('products');
    const fd = new FormData(event.target);

    let exists = false
    let tagElement = null

    for (const pair of fd.entries()) {
        if (pair[0] === 'product') {
            for (const item of Array.from(list.children).filter(item => item.tagName.toLowerCase() === 'li')) {
                const tag = item.children[0].children[0]
                if (tag.innerText === pair[1]) {
                    exists = true
                    tagElement = tag
                    break
                }
            }
            if (!exists) {
                const p = document.createElement('p');
                p.setAttribute("class", "my-auto text-white")
                p.innerHTML = pair[1];
                productItem.appendChild(p);
                item.appendChild(productItem);
                list.appendChild(item);
            }
        } else if (pair[0] === 'product-amnt') {
            if (exists) {
                tagElement.parentElement.children[1].innerText = Number(tagElement.parentElement.children[1].innerText) + Number(pair[1])
            } else {
                const span = document.createElement('span');
                span.setAttribute("class", "my-auto badge text-bg-secondary");
                span.innerHTML = pair[1];
                productItem.appendChild(span);
                item.appendChild(productItem);
                list.appendChild(item);
                item.appendChild(btnContainer);
            }
        }
    }
    event.target.reset()
}

function clearAll() {
    if (isConfirmed) {
        const list = document.getElementById('products');
        let toRemove = [];
        for (const item of list.children) {
            if (item.tagName.toLowerCase() === 'li') {
                toRemove.push(item);
            }
        }
        for (const item of toRemove) {
            item.remove()
        }
    }
}