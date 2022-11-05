
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