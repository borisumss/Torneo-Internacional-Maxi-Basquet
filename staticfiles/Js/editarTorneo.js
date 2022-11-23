
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

let seleccionArchivos2 = document.getElementById("qr1Input"),
  imagenPrevisualizacion2 = document.getElementById("img1");

function cambiarPortada(img_defecto) {
  var archivoRuta = seleccionArchivos2.value;
  var extesiones = /(.jpg|.jpeg|.png)$/i;;

  if (!extesiones.exec(archivoRuta)) {
    Swal.fire('Sólo se permiten imágenes (.jpg .jpeg .png)', '', 'error');
    seleccionArchivos2.value = img_defecto;
    
    return false;
  } else {
    const archivos2 = seleccionArchivos2.files;
    if (!archivos2 || !archivos2.length) {
      imagenPrevisualizacion2.src = "";
      return;
    }
    const primerArchivo2 = archivos2[0];
    const objectURL2 = URL.createObjectURL(primerArchivo2);
    imagenPrevisualizacion2.src = objectURL2;
  }
}

let seleccionArchivos = document.getElementById("qr2Input"),
  imagenPrevisualizacion = document.getElementById("img2");

function cambiarPortada2(img_defecto) {
  var archivoRuta = seleccionArchivos.value;
  var extesiones = /(.jpg|.jpeg|.png)$/i;;

  if (!extesiones.exec(archivoRuta)) {
    Swal.fire('Sólo se permiten imágenes (.jpg .jpeg .png)', '', 'error');
    seleccionArchivos.value = img_defecto;
    
    return false;
  } else {
    const archivos2 = seleccionArchivos.files;
    if (!archivos2 || !archivos2.length) {
      imagenPrevisualizacion.src = "";
      return;
    }
    const primerArchivo2 = archivos2[0];
    const objectURL2 = URL.createObjectURL(primerArchivo2);
    imagenPrevisualizacion.src = objectURL2;
  }
}

let valInicio = document.getElementById('fechaIni_input').value;
let valFin = document.getElementById('fechaFin_input').value;
let valInicioPre = document.getElementById('fechaIniPre_input').value;
let valFinPre = document.getElementById('fechaFinPre_input').value;
let valInicioRez = document.getElementById('fechaIniRez_input').value;
let valFinRez = document.getElementById('fechaFinRez_input').value;

let fechaActual = new Date(Date.now());
let now = moment(fechaActual).format('YYYY-MM-DD')

function fechasTorneoIniPre() {
  let inicio = document.getElementById('fechaIni_input');
let fin = document.getElementById('fechaFin_input');
let inicioPre = document.getElementById('fechaIniPre_input');
let finPre = document.getElementById('fechaFinPre_input');
let inicioRez = document.getElementById('fechaIniRez_input');
let finRez = document.getElementById('fechaFinRez_input');

      if (inicio.value == '' || fin.value == '' || inicioPre.value == '' || finPre.value == '' || inicioRez.value == '' || finRez.value == '') {
        Swal.fire('No se permiten campos vacíos', '', 'error');    
          inicio.value = valInicio;
          fin.value = valFin;
          inicioPre.value = valInicioPre;
          inicioRez.value = valInicioRez;
          finRez.value = valFinRez;
          finPre.value = valFinPre;
      } else {
          
          if(inicioPre.value < now) {
            Swal.fire('', 'No se permiten fechas pasadas', 'error');   
            inicioPre.value = valInicioPre;
          }else if(inicioPre.value > finPre.value) {
            Swal.fire('', 'La fecha inicial de Pre-inscripción debe ser menor a la final', 'error');   
            inicioPre.value = valInicioPre;
          }
        }
}

function fechasTorneoFinPre() {
  let inicio = document.getElementById('fechaIni_input');
let fin = document.getElementById('fechaFin_input');
let inicioPre = document.getElementById('fechaIniPre_input');
let finPre = document.getElementById('fechaFinPre_input');
let inicioRez = document.getElementById('fechaIniRez_input');
let finRez = document.getElementById('fechaFinRez_input');

  if (inicio.value == '' || fin.value == '' || inicioPre.value == '' || finPre.value == '' || inicioRez.value == '' || finRez.value == '') {
    Swal.fire('No se permiten campos vacíos', '', 'error');    
      inicio.value = valInicio;
      fin.value = valFin;
      inicioPre.value = valInicioPre;
      inicioRez.value = valInicioRez;
      finRez.value = valFinRez;
      finPre.value = valFinPre;
  } else {
      //format('YYYY-MM-DD')
      var fechaIniRez = new Date($('#fechaFinPre_input').val());
      var dias =  2
      fechaIniRez.setDate(fechaIniRez.getDate()+dias);  
      fechaIniRez= moment(fechaIniRez).format('YYYY-MM-DD') 
      inicioRez.value = fechaIniRez;

      if(finPre.value < inicioPre.value || finPre.value >= inicioRez.value) {
        Swal.fire('', 'La fecha Final de Preinscripción debe ser mayor a la inicial y menor a la fecha Inicial de Inscripción', 'error');   
          finPre.value = valFinPre;
          inicioRez.value = valInicioRez;
      }
      if(inicioRez.value <= finPre.value || inicioRez.value > finRez.value) {
        Swal.fire('', 'La fecha inicial de Inscripción debe ser mayor a fecha final de Preinscripción y menor a la fecha Final de Inscripción', 'error');   
          inicioRez.value = valInicioRez;
          finPre.value = valFinPre;
      }
      
  }
}

function fechasTorneoRezIni() {
  let inicio = document.getElementById('fechaIni_input');
let fin = document.getElementById('fechaFin_input');
let inicioPre = document.getElementById('fechaIniPre_input');
let finPre = document.getElementById('fechaFinPre_input');
let inicioRez = document.getElementById('fechaIniRez_input');
let finRez = document.getElementById('fechaFinRez_input');

  if (inicio.value == '' || fin.value == '' || inicioPre.value == '' || finPre.value == '' || inicioRez.value == '' || finRez.value == '') {
    Swal.fire('No se permiten campos vacíos', '', 'error');    
      inicio.value = valInicio;
      fin.value = valFin;
      inicioPre.value = valInicioPre;
      inicioRez.value = valInicioRez;
      finRez.value = valFinRez;
      finPre.value = valFinPre;
  } else {  
    if(inicioRez.value <= finPre.value || inicioRez.value > finRez.value) {
      Swal.fire('', 'La fecha inicial de Inscripción debe ser mayor a fecha final de Preinscripción y menor a la fecha Final de Inscripción', 'error');   
        inicioRez.value = valInicioRez;
    }
  }
}



function fechasTorneoRezFin() {
  let inicio = document.getElementById('fechaIni_input');
let fin = document.getElementById('fechaFin_input');
let inicioPre = document.getElementById('fechaIniPre_input');
let finPre = document.getElementById('fechaFinPre_input');
let inicioRez = document.getElementById('fechaIniRez_input');
let finRez = document.getElementById('fechaFinRez_input');


  if (inicio.value == '' || fin.value == '' || inicioPre.value == '' || finPre.value == '' || inicioRez.value == '' || finRez.value == '') {
    Swal.fire('No se permiten campos vacíos', '', 'error');    
      inicio.value = valInicio;
      fin.value = valFin;
      inicioPre.value = valInicioPre;
      inicioRez.value = valInicioRez;
      finRez.value = valFinRez;
      finPre.value = valFinPre;
  } else {
      
    if(finRez.value < inicioRez.value || finRez.value >= inicio.value) {
      Swal.fire('', 'La fecha final de Inscripción debe ser mayor a fecha inicial de Inscripción y menor a la fecha inicial del torneo', 'error');   
        finRez.value = valFinRez;
    }
  }
}

function fechasTorneoIni() {
  let inicio = document.getElementById('fechaIni_input');
let fin = document.getElementById('fechaFin_input');
let inicioPre = document.getElementById('fechaIniPre_input');
let finPre = document.getElementById('fechaFinPre_input');
let inicioRez = document.getElementById('fechaIniRez_input');
let finRez = document.getElementById('fechaFinRez_input');

  if (inicio.value == '' || fin.value == '' || inicioPre.value == '' || finPre.value == '' || inicioRez.value == '' || finRez.value == '') {
    Swal.fire('No se permiten campos vacíos', '', 'error');    
      inicio.value = valInicio;
      fin.value = valFin;
      inicioPre.value = valInicioPre;
      inicioRez.value = valInicioRez;
      finRez.value = valFinRez;
      finPre.value = valFinPre;
  } else {
    if(inicio.value <= finRez.value || inicio.value >= fin.value) {
      Swal.fire('', 'La fecha Inicial del torneo debe ser mayor a fecha final de Inscripción y menor a la fecha final del torneo', 'error');   
        inicio.value = valInicio;
    }
  } 
}

function fechasTorneoFin() {
  let inicio = document.getElementById('fechaIni_input');
let fin = document.getElementById('fechaFin_input');
let inicioPre = document.getElementById('fechaIniPre_input');
let finPre = document.getElementById('fechaFinPre_input');
let inicioRez = document.getElementById('fechaIniRez_input');
let finRez = document.getElementById('fechaFinRez_input');


  if (inicio.value == '' || fin.value == '' || inicioPre.value == '' || finPre.value == '' || inicioRez.value == '' || finRez.value == '') {
    Swal.fire('No se permiten campos vacíos', '', 'error');    
      inicio.value = valInicio;
      fin.value = valFin;
      inicioPre.value = valInicioPre;
      inicioRez.value = valInicioRez;
      finRez.value = valFinRez;
      finPre.value = valFinPre;
  } else {
      if(fin.value <= inicio.value) {
        Swal.fire('', 'La fecha Final del torneo debe ser mayor la fecha inicial del torneo', 'error');   
          fin.value = valFin;
      }
  } 
}