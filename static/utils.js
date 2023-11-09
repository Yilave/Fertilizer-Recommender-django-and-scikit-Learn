document.addEventListener('htmx:afterSwap', () => {
    const navBartoggle = document.querySelector('.navbar-toggler')
    const collapse = document.querySelector('.collapse')

    navBartoggle.addEventListener('click', () => {
        console.log('clicked');
        // collapse.classList.contains('show') ? collapse.classList.remove('show') : collapse.classList.add('show')
        collapse.classList.toggle('show')
    })

    // COPY RIGHT DATE

    const date = document.querySelector('#date')
    date.innerHTML = new Date().getFullYear();
})


// AFTER HTMX SWAP
const navBartoggle = document.querySelector('.navbar-toggler')
const collapse = document.querySelector('.collapse')

navBartoggle.addEventListener('click', () => {
    collapse.classList.contains('show') ? collapse.classList.remove('show') : collapse.classList.add('show')

})

// COPY RIGHT DATE

const date = document.querySelector('#date')
date.innerHTML = new Date().getFullYear();