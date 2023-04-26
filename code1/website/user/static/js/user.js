const body = document.querySelector('body'),
      sidebar = body.querySelector('nav'),
      toggle = body.querySelector(".toggle"),
      searchBtn = body.querySelector(".search-box"),
      modeSwitch = body.querySelector(".toggle-switch"),
      modeText = body.querySelector(".mode-text");
      maincontent = body.querySelector('.maincontainter')


toggle.addEventListener("click" , () =>{
    sidebar.classList.toggle("close");
    maincontent.classList.toggle("content-shifted")

})