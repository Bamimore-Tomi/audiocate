document.getElementById('footer').innerHTML = '&copy;SAUCECODE TEAM GREEN ' + new Date().getFullYear() + '.';

$(document).ready(function(){
  if($(window).width() > 1080) {
    $("#img").attr("src", "./images/male-reader.jpg");
  }
  else {$("#img").attr("src", "./images/onbook.jpg");

    }
  })