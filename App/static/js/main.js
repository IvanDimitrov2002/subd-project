const changeSearch = () => {
    const searchInput = document.querySelectorAll('.form-input')[0]
    const searchForm = document.querySelectorAll('.content-form')[0]

    if(event.target.value === "author"){
        searchInput.placeholder = "Search by author name..."
        searchInput.name = "name"
        searchForm.action = "/authors"
    } else if(event.target.value === "book"){
        searchInput.placeholder = "Search by book name..."
        searchInput.name = "title"
        searchForm.action = "/books"
    } else if(event.target.value === "genre"){
        searchInput.placeholder = "Search by book genre..."
        searchInput.name = "genre"
        searchForm.action = "/books"
    }
}

const disableRadio = () => {
    const radios = document.querySelectorAll('.radio')
    radios.forEach(radio => {
        radio.setAttribute('disabled', 'disabled')
    })
}