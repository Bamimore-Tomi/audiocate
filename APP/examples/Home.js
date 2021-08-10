document.addEventListener("DOMContentLoaded", () => {
  const sideBar = document.querySelector(".side-bar");

  document.querySelector(".menu-open").addEventListener("click", () => {
    sideBar.classList.add('open');
  })

  document.querySelector(".menu-close")
    .addEventListener("click", () => {
      sideBar.classList.remove('open');
    });
    
  document.querySelector(".overlay")
    .addEventListener("click", () => {
      sideBar.classList.remove('open');
    });
})