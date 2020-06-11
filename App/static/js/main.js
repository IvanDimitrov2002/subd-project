const changeSearch = () => {
    const searchInput = document.querySelectorAll('.form-input')[0]
    const searchForm = document.querySelectorAll('.content-form')[0]

    if(event.target.value === "author"){
        searchInput.placeholder = "Search by author name..."
        searchForm.action = "/authors"
    } else if(event.target.value === "book"){
        searchInput.placeholder = "Search by book name..."
        searchForm.action = "/books"
    }
}