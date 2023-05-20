let PostOptionBTN = document.getElementById("PostOptionBTN")
let postOptionMenu = document.getElementById("postOptionMenu")
let lovePost = document.getElementById("lovePost")
let savePost = document.getElementById("savePost")
let lovePostParent = document.getElementById("lovePostParent")
let commentPostParent = document.getElementById("commentPostParent")
let commentSection = document.getElementById("commentSection")
let savePostParent = document.getElementById("savePostParent")
let special = document.getElementById("special")
let specialNav = document.getElementById("specialNav")
let aboutOptionBTN = document.getElementById("aboutOptionBTN")
let aboutOptionMenu = document.getElementById("aboutOptionMenu")
let introOptionBTN = document.getElementById("introOptionBTN")
let introOptionMenu = document.getElementById("introOptionMenu")
let insertOptionBTN = document.getElementById("insertOptionBTN")
let insertOptionMenu = document.getElementById("insertOptionMenu")

PostOptionBTN?.addEventListener("click", () => {
    postOptionMenu.classList.toggle("active")
})

lovePostParent?.addEventListener("click", () => {
    lovePostParent.classList.toggle("active")
    lovePost.classList.toggle("fa-solid")
})

savePostParent?.addEventListener("click", () => {
    savePostParent.classList.toggle("active")
    savePost.classList.toggle("fa-solid")
})

commentPostParent?.addEventListener("click", () => {
    commentPostParent.classList.toggle("active")
    commentSection.classList.toggle("active")
})


notifi?.addEventListener("click", () => {
    notifi.classList.toggle("active")
})

special?.addEventListener("mouseenter", () => {
    specialNav.style.width = 'calc(100%/12 *2)'
})

special?.addEventListener("mouseleave", () => {
    specialNav.style.width = '120px'
})

aboutOptionBTN?.addEventListener("click", () => {
    aboutOptionMenu.classList.toggle("active")
})

introOptionBTN?.addEventListener("click", () => {
    introOptionMenu.classList.toggle("active")
})
insertOptionBTN?.addEventListener("click", () => {
    insertOptionMenu.classList.toggle("active")
})