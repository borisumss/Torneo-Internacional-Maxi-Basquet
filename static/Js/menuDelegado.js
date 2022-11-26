
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
        //Swal.fire('Tiene que llenar todos los campos', '', 'error');
        form.classList.add('was-validated')

      }, false)
    })
})()

$(function () {
  var billingItems = document.querySelectorAll('input');
  for (var i = 0; i < billingItems.length; i++) {
    if (billingItems[i].value == "None") {
      billingItems[i].value = "";
    }
  }
});
/*
$('ul.tabs li').click(function(){
    $('ul.tabs li').removeClass('active');
    $(this).addClass('active');
    $('.secciones article').hide();

    var activeTab = $(this.firstElementChild).attr('href');
    console.log(activeTab);
    $(activeTab).show();
    return false;
});*/

$('.burger').click(function () {

  let x = $('#side_nav').width();
  if (x <= 55) {
    $('#side_nav').addClass('menu-expanded');
    $('#side_nav').removeClass('menu-collapsed');
  } else {
    $('#side_nav').addClass('menu-collapsed');
    $('#side_nav').removeClass('menu-expanded');
  }

  return false;
});

$('#btn-infor').click(function () {
  $('#btn-infor').addClass('guardar');
  $('#btn-guardar').removeClass('guardar');
  $('#btn-guardar').addClass('btn-guardarBlock');
  $('#btn-cancelar').removeClass('guardar');
  $('#btn-cancelar').addClass('btn-guardarBlock');
  $('#labelFile').removeClass('guardar');
  $('#labelFile').addClass('btn-guardarBlock');
  $('#inputFile').removeClass('guardar');
  $('#inputFile').addClass('btn-guardarBlock');

  $('#portadaLabel').removeClass('guardar');
  $('#portadaLabel').addClass('btn-guardarBlock');
  $('#portadaInput').removeClass('guardar');
  $('#portadaInput').addClass('btn-guardarBlock');
  $('.escudo').addClass('subirImagenes');
  $('.portada').addClass('subirImagenes');
  var billingItems = document.querySelectorAll('input');
  
  for (var i = 0; i < billingItems.length; i++) {
    billingItems[i].disabled = false;
  }

  return false;
});

let seleccionArchivos = document.getElementById("inputFile"),
  imagenPrevisualizacion = document.getElementById("img-escudo");

function cambiarEscudo() {
  var archivoRuta = seleccionArchivos.value;
  var extesiones = /(.jpg|.jpeg|.png)$/i;;

  if (!extesiones.exec(archivoRuta)) {
    Swal.fire('Sólo se permiten imágenes (.jpg .jpeg .png)', '', 'error');
    seleccionArchivos.value = '';
    imagenPrevisualizacion.src = "";
    return false;
  } else {
    // Los archivos seleccionados, pueden ser muchos o uno
    const archivos = seleccionArchivos.files;
    // Si no hay archivos salimos de la función y quitamos la imagen
    if (!archivos || !archivos.length) {
      imagenPrevisualizacion.src = "";
      return;
    }
    // Ahora tomamos el primer archivo, el cual vamos a previsualizar
    const primerArchivo = archivos[0];
    // Lo convertimos a un objeto de tipo objectURL
    const objectURL = URL.createObjectURL(primerArchivo);
    // Y a la fuente de la imagen le ponemos el objectURL
    imagenPrevisualizacion.src = objectURL;
  }
}
let test = document.getElementById("test");

function cambiar() {

  alert(test.value)
}
let seleccionArchivos2 = document.getElementById("portadaInput"),
  imagenPrevisualizacion2 = document.getElementById("img-portada");

function cambiarPortada() {
  var archivoRuta = seleccionArchivos2.value;
  var extesiones = /(.jpg|.jpeg|.png)$/i;;

  if (!extesiones.exec(archivoRuta)) {
    Swal.fire('Sólo se permiten imágenes (.jpg .jpeg .png)', '', 'error');
    seleccionArchivos2.value = '';
    imagenPrevisualizacion2.src = "";
    return false;
  } else {

    // Los archivos seleccionados, pueden ser muchos o uno
    const archivos2 = seleccionArchivos2.files;
    // Si no hay archivos salimos de la función y quitamos la imagen
    if (!archivos2 || !archivos2.length) {
      imagenPrevisualizacion2.src = "";
      return;
    }
    // Ahora tomamos el primer archivo, el cual vamos a previsualizar
    const primerArchivo2 = archivos2[0];
    // Lo convertimos a un objeto de tipo objectURL
    const objectURL2 = URL.createObjectURL(primerArchivo2);
    // Y a la fuente de la imagen le ponemos el objectURL
    imagenPrevisualizacion2.src = objectURL2;
  }
}

function validarFechas(fechaIni, fechaFin) {
  const tiempoTranscurrido = Date.now() //Obtiene el tiempo actual en milisegundos
  const hoy = new Date(tiempoTranscurrido) //Convierte en formato "DiaSemana Mes Dia Año GTM"
  //let fechaActual = hoy.toLocaleDateString()

  let fechaRezIni = new Date(fechaIni);
  //fechaRezIni = fechaRezIni.toLocaleDateString();

  let fechaRezFin = new Date(fechaFin);
  //fechaRezFin = fechaRezFin.toLocaleDateString();
  let boton = document.getElementById("btn-infor");
  let boton2 = document.getElementById("btn-jug");
  let boton3 = document.getElementById("btn-coach");
  let boton4 = document.getElementById("btn-danger");
  if (boton != null) {
    if (hoy >= fechaRezIni && hoy <= fechaRezFin) {
        console.log("si se puede inscribir")
    } else {
      boton.style.display = 'none';
      boton2.style.display = 'none';
      boton3.style.display = 'none';
      boton4.style.display = 'none';
    }

  }
}

function validarNombre(aux){
  let nombres = aux.split('-')
  let input = document.getElementById("title");
  let nombre = input.value.toLowerCase()
  for(let i=0; i< nombres.length;i++){

      if(nombre == nombres[i].toLowerCase()){
        Swal.fire('Este nombre ya está registrado', '', 'error');
        input.value = "";
      }
  }
}