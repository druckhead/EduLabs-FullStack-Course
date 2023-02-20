'use strict';

const toggleDisabled = () => {
    const start = document.getElementById('start-btn')
    const cancel = document.getElementById('cancel-btn')
    const secondInput = document.getElementById(`second-input`)
    const elements = [start, cancel, secondInput]

    elements.forEach(element => element.toggleAttribute(`disabled`));
}

const loadCompleteHandler = () => {
    const start = document.getElementById('start-btn')
    const cancel = document.getElementById('cancel-btn')
    const input = document.getElementById(`second-input`)
    
    start.onclick = startTimer
    cancel.onclick = cancelTimer
    input.oninput = (event) => {
        const inputValue = event.target.value
        if (inputValue && inputValue !== `0`) {
            if (start.hasAttribute(`disabled`)) {
                start.removeAttribute(`disabled`)
            }
        } else {
            start.toggleAttribute(`disabled`)
        }
    }
}

const cancelTimer = () => {
    document.getElementById(`second-input`).value = ""
    toggleDisabled()
}

const startTimer = () => {
    const updateTimer = (seconds) => {
        const secondsSpan = document.getElementById(`timer`)
        secondsSpan.innerText = seconds
        toggleDisabled()
        console.warn(`LOG: ${seconds} second timer started`);
        const interval = setInterval(() => {
            seconds--
            secondsSpan.innerText = seconds
            if (seconds === 0) {
                clearInterval(interval)
                toggleDisabled()
                document.getElementById(`second-input`).value = 0
                document.getElementById(`start-btn`).toggleAttribute(`disabled`)
                const clearTimerTimeout = setTimeout(() => {
                    secondsSpan.innerText = ""
                    clearTimeout(clearTimerTimeout)
                }, 1000);
            }
        }, 1000);
    }

    const secondsInput = document.getElementById(`second-input`)
    const seconds = secondsInput.value
    updateTimer(seconds)
    secondsInput.value = ""

    const timeout = setTimeout(() => {
        console.warn(`LOG: Timer ${timeout} (${seconds} second) completed.`)
        clearTimeout(timeout)
    }, seconds * 1000);
}

window.onload = loadCompleteHandler