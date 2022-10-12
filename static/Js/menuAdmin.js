(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
          form.classList.add('was-validated')
        
        }, false)
      })
  })()

$(function(){
    $('ul.tabs li:first').addClass('active');
    $('.secciones article').hide();
    $('.secciones article:first').show();
});

$('ul.tabs li').click(function(){
    $('ul.tabs li').removeClass('active');
    $(this).addClass('active');
    $('.secciones article').hide();

    var activeTab = $(this.firstElementChild).attr('href');
    if(activeTab == '#Tab5'){
      $('body').addClass('fondoTab5');
      $('body').removeClass('fondoTab4');
      $('body').removeClass('fondoTab3');
      $('body').removeClass('fondoTab2');
      $('body').removeClass('fondoTab1');
    }else if( activeTab == '#Tab4'){
      $('body').addClass('fondoTab4');
      $('body').removeClass('fondoTab5');
      $('body').removeClass('fondoTab3');
      $('body').removeClass('fondoTab2');
      $('body').removeClass('fondoTab1');
    }else if( activeTab == '#Tab3'){
      $('body').addClass('fondoTab3');
      $('body').removeClass('fondoTab5');
      $('body').removeClass('fondoTab4');
      $('body').removeClass('fondoTab2');
      $('body').removeClass('fondoTab1');
    }else if( activeTab == '#Tab2'){
      $('body').addClass('fondoTab2');
      $('body').removeClass('fondoTab5');
      $('body').removeClass('fondoTab4');
      $('body').removeClass('fondoTab3');
      $('body').removeClass('fondoTab1');
    }else if( activeTab == '#Tab1'){
      $('body').addClass('fondoTab1');
      $('body').removeClass('fondoTab5');
      $('body').removeClass('fondoTab4');
      $('body').removeClass('fondoTab3');
      $('body').removeClass('fondoTab2');
    }
   
    $(activeTab).show();
    return false;
});

$('.burger').click(function(){
    
    let x = $('#side_nav').width();
    if(x<=55){
        $('#side_nav').addClass('menu-expanded');
        $('#side_nav').removeClass('menu-collapsed');
    }else{
        $('#side_nav').addClass('menu-collapsed');
        $('#side_nav').removeClass('menu-expanded');
    }

    return false;
});


$('#Tab5 .tarjeta .back').click(function(){
  //'#Tab5 .tarjeta .front'
  $(this.parentElement.children[0]).removeClass('girar');
  //'#Tab5 .tarjeta .back'
  $(this).removeClass('girarDoble');

  return false;
});

let fullImg = document.getElementById('imgFull');

$('#Tab5 .tarjeta .back .card .card-body #img').click(function(){
  fullImg.src = this.src;
  return false;
});

$('#Tab5 .tarjeta .front .card .card-body').click(function(){
  //'#Tab5 .tarjeta .front'
  $(this.parentElement.parentElement).addClass('girar');
  
  //'#Tab5 .tarjeta .back'
  $(this.parentElement.parentElement.parentElement.children[1]).addClass('girarDoble');
  

  return false;
});

$('#Tab5 .tarjeta .front .card .card-header').click(function(){
  //'#Tab5 .tarjeta .front'
  $(this.parentElement.parentElement).addClass('girar');
  
  //'#Tab5 .tarjeta .back'
  $(this.parentElement.parentElement.parentElement.children[1]).addClass('girarDoble');
  

  return false;
});

function enviar() {
    let mail = document.getElementById('correo_modalInput');
    let name = document.getElementById('name_modalInput');
    let pass = document.getElementById('pass_modalInput');
   
    if (mail.checkValidity() && name.checkValidity() && pass.checkValidity()) {
        

    } else {
        let formu = document.getElementById('modalValid');
        formu.classList.add('was-validated')
        
    }

}