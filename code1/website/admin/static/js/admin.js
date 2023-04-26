$(document).ready(function () {
    $('#example').DataTable(

        {     
            "aLengthMenu": [[10, 20, 50, 100, -1], [10, 20, 50, 10, "All"]],
              "iDisplayLength": 10
             } 


    );
});




const body = document.querySelector('body'),
      sidebar = body.querySelector('nav'),
      toggle = body.querySelector(".toggle"),
      searchBtn = body.querySelector(".search-box"),
      modeSwitch = body.querySelector(".toggle-switch"),
      modeText = body.querySelector(".mode-text");
      maincontent = body.querySelector('.maincontainer')


toggle.addEventListener("click" , () =>{
    sidebar.classList.toggle("close");
    maincontent.classList.toggle("content-shifted")

})




