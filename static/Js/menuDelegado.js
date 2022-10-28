
/*$(function(){
    $('ul.tabs li:first').addClass('active');
    $('.secciones article').hide();
    $('.secciones article:first').show();
});

$('ul.tabs li').click(function(){
    $('ul.tabs li').removeClass('active');
    $(this).addClass('active');
    $('.secciones article').hide();

    var activeTab = $(this.firstElementChild).attr('href');
    console.log(activeTab);
    $(activeTab).show();
    return false;
});*/

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

$('#btn-infor').click(function(){
    
    $('#btn-guardar').removeClass('guardar');
    $('#btn-guardar').addClass('btn-guardarBlock');
    $('#labelFile').removeClass('guardar');
    $('#labelFile').addClass('btn-guardarBlock');
    $('#inputFile').removeClass('guardar');
    $('#inputFile').addClass('btn-guardarBlock');

    $('#portadaLabel').removeClass('guardar');
    $('#portadaLabel').addClass('btn-guardarBlock');
    $('#portadaInput').removeClass('guardar');
    $('#portadaInput').addClass('btn-guardarBlock');
    var billingItems = document.querySelectorAll('input');
    for (var i = 0; i < billingItems.length; i++) {
      billingItems[i].disabled = false;
    }

    return false;
});

const $seleccionArchivos = document.querySelector("#inputFile"),
  $imagenPrevisualizacion = document.querySelector("#img-escudo");

  $seleccionArchivos.addEventListener("change", () => {
    // Los archivos seleccionados, pueden ser muchos o uno
    const archivos = $seleccionArchivos.files;
    // Si no hay archivos salimos de la función y quitamos la imagen
    if (!archivos || !archivos.length) {
      $imagenPrevisualizacion.src = "";
      return;
    }
    // Ahora tomamos el primer archivo, el cual vamos a previsualizar
    const primerArchivo = archivos[0];
    // Lo convertimos a un objeto de tipo objectURL
    const objectURL = URL.createObjectURL(primerArchivo);
    // Y a la fuente de la imagen le ponemos el objectURL
    $imagenPrevisualizacion.src = objectURL;
  });

  const $seleccionArchivos2 = document.querySelector("#portadaInput"),
  $imagenPrevisualizacion2 = document.querySelector("#img-portada");

  $seleccionArchivos2.addEventListener("change", () => {
    // Los archivos seleccionados, pueden ser muchos o uno
    const archivos2 = $seleccionArchivos2.files;
    // Si no hay archivos salimos de la función y quitamos la imagen
    if (!archivos2 || !archivos2.length) {
      $imagenPrevisualizacion2.src = "";
      return;
    }
    // Ahora tomamos el primer archivo, el cual vamos a previsualizar
    const primerArchivo2 = archivos2[0];
    // Lo convertimos a un objeto de tipo objectURL
    const objectURL2 = URL.createObjectURL(primerArchivo2);
    // Y a la fuente de la imagen le ponemos el objectURL
    $imagenPrevisualizacion2.src = objectURL2;
  });