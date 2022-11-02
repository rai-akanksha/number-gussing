const name = document.getElementById('name')
const password = document.getElementById('password')
const password = document.getElementById('form')
const password = document.getElementById('error')

FormData.addEventListener('submit', (e) => {
    let messages = []
    if (name.value === '' || name.value == null) {
        messages.push('Nmae is required')
    }

    if (password.value.length <= 6) {
        messages.push('Password must be longer than 6 character')
    }
    if (password.value.length >= 20) {
        messages.push('Password must be less than 20 character')
    }
    if (password.value === 'password') {
        messages.push('Password cannot be password ')

    }
    if (messages.length > 0) {
        e.preventDefault()
        errorElement.innerText = messages.join(', ')

    }
})