'use strict';

const toggleDisabled = () => {
    const start = document.getElementById('start-btn')
    const cancel = document.getElementById('cancel-btn')
    const secondInput = document.getElementById(`second-input`)
    const elements = [start, cancel, secondInput]

    elements.forEach(element => element.toggleAttribute(`disabled`));
}

const loadFromLocalStorage = () => {
    const secondsLeft = localStorage.getItem(`time-left`)
    return secondsLeft
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

    const timeLeft = localStorage.getItem(`time-left`)
    if (timeLeft) {
        const startedAt = localStorage.getItem(`timer-started`)
        const date = Date(startedAt)
        if (confirm(`You have a timer started at: ${date}\nWould you like to resume?`)) {
            updateTimer(timeLeft)
        } else {
            localStorage.clear()
        }
    }
}

const seLocalStorageItem = ({ timestamp = null, initialValue = null, secondsLeft = null, timerId = null }) => {
    if (timestamp) {
        localStorage.setItem(`timer-started`, timestamp)
    }
    if (initialValue) {
        localStorage.setItem(`initial-value`, initialValue)
    }
    if (secondsLeft) {
        localStorage.setItem(`time-left`, secondsLeft)
    }
    if (timerId) {
        localStorage.setItem(`timer-id`, timerId)
    }
}

const cancelTimer = () => {
    toggleDisabled()
    document.getElementById(`start-btn`).toggleAttribute(`diabled`)
    clearTimeout(localStorage.getItem(`timer-timeout`))
    clearTimeout(localStorage.getItem(`alert-timeout`))
    clearInterval(localStorage.getItem(`timer-interval`))
    document.getElementById(`timer`).innerText = ""
    localStorage.clear()

}

const updateTimer = (seconds) => {
    const secondsSpan = document.getElementById(`timer`)
    secondsSpan.innerText = seconds

    const timerData = { timestamp: Date.now(), initialValue: seconds, secondsLeft: seconds }
    seLocalStorageItem(timerData)

    toggleDisabled()
    console.warn(`LOG: ${seconds} second timer started`);

    const interval = setInterval(() => {
        seconds--
        secondsSpan.innerText = seconds
        seLocalStorageItem({ secondsLeft: seconds })
        if (seconds === 0) {
            const alert = document.getElementById(`alert-msg`)
            alert.classList.add(`alert-success`)
            alert.classList.remove(`d-none`)
            alert.innerText = `Timer completed.`

            localStorage.clear()

            clearInterval(interval)
            toggleDisabled()

            document.getElementById(`second-input`).value = 0
            document.getElementById(`start-btn`).toggleAttribute(`disabled`)

            const alertDisapear = setTimeout(() => {
                localStorage.setItem(`alert-timeout`, alertDisapear)
                alert.classList.remove(`alert-danger`)
                alert.classList.add(`d-none`)
                clearTimeout(alertDisapear)
            }, 2500);

            const clearTimerTimeout = setTimeout(() => {
                localStorage.setItem(`timer-timeout`, clearTimerTimeout)
                secondsSpan.innerText = ""
                clearTimeout(clearTimerTimeout)
            }, 500);
        }
    }, 1000);
    localStorage.setItem(`timer-interval`, interval)
}

const startTimer = () => {
    const secondsInput = document.getElementById(`second-input`)
    const seconds = secondsInput.value
    secondsInput.value = ""

    updateTimer(seconds)

    const timeout = setTimeout(() => {
        console.warn(`LOG: Timer ${timeout} (${seconds} second) completed.`)
        clearTimeout(timeout)
    }, seconds * 1000);
}

window.onload = loadCompleteHandler