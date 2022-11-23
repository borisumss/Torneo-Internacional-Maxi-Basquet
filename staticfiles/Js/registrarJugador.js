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

  function validarFoto() {

    let archivoInput = document.getElementById("fotoJugador");
    let archivoRuta = archivoInput.value;
    let extesiones = /(.jpg|.jpeg|.png)$/i;;

    if (!extesiones.exec(archivoRuta)) {
        Swal.fire('Sólo se permiten imágenes (.jpg .jpeg .png)', '', 'error'); 
        archivoInput.value = '';
        return false;
    }
}
//Previsualizar foto
const $input = document.querySelector("#fotoJugador")
const $button = document.querySelector("#boton-foto")
const div = document.getElementById("contFoto")
const $img = document.querySelector("#imgprevisualizacion")

$button.addEventListener("click", ()=>{
    $input.click()
})

$input.addEventListener("change", ()=>{
    const photo = $input.files
    if (!photo || !photo.length) {
        $img.src = "";
        return;
      }
    const primerArchivo = photo[0]
    const URLimg = URL.createObjectURL(primerArchivo)
    $button.hidden = true
    $img.hidden = false
    $img.src = URLimg;
})

// Validar fecha de nacimiento
let fechaNac = document.getElementById("fechaNac")
let fechaActual = new Date(Date.now());
let now = fechaActual.toLocaleString()

function fechaNacimiento(categoriaMin,categoriaMax){    
    const anioActual = parseInt(fechaActual.getFullYear())
    const mesActual = parseInt(fechaActual.getMonth()) + 1
    const diaActual = parseInt(fechaActual.getDate())

    //Obtener datos del input formato 2020-06-01 ejm
    const anioNac = parseInt(String(fechaNac.value).substring(0, 4))
    const mesNac = parseInt(String(fechaNac.value).substring(5, 7))
    const diaNac = parseInt(String(fechaNac.value).substring(8, 10))

    let edad = anioActual - anioNac
    if(mesActual < mesNac){
        edad--;
    }else if(mesActual === mesNac){
        if(diaActual < diaNac){
            edad--;
        }
    }

    if(edad < categoriaMin){
        Swal.fire('La edad del jugador debe ser mínimo de '+categoriaMin +' años','','error');
        fechaNac.value = '';
    }else if(edad > categoriaMax){
        Swal.fire('La edad del jugador debe ser máximo de '+categoriaMax +' años','','error');
        fechaNac.value = '';
    }
}

function fechaNacimientoEnt(){    
    const anioActual = parseInt(fechaActual.getFullYear())
    const mesActual = parseInt(fechaActual.getMonth()) + 1
    const diaActual = parseInt(fechaActual.getDate())

    //Obtener datos del input formato 2020-06-01 ejm
    const anioNac = parseInt(String(fechaNac.value).substring(0, 4))
    const mesNac = parseInt(String(fechaNac.value).substring(5, 7))
    const diaNac = parseInt(String(fechaNac.value).substring(8, 10))

    let edad = anioActual - anioNac
    if(mesActual < mesNac){
        edad--;
    }else if(mesActual === mesNac){
        if(diaActual < diaNac){
            edad--;
        }
    }

    if(edad < 18){
        Swal.fire('La edad del jugador debe ser mínimo de 18 años','','error');
        fechaNac.value = '';
    }else if(edad > 100){
        Swal.fire('La edad del jugador debe ser máximo de 100 años','','error');
        fechaNac.value = '';
    }
}

function limpiarForm(){
    let foto = document.getElementById('fotoJugador')
    let imgPreviw = document.getElementById('imgprevisualizacion')
    let boton = document.getElementById('boton-foto')
    let nombre = document.getElementById('nombreJugador')
    let apodo = document.getElementById('apodoJugador')
    let posicion = document.getElementById('posicionJugador')
    let camiseta = document.getElementById('camiseta')
    let fechaNacJug = document.getElementById('fechaNac')
    let doc = document.getElementById('documento')
    let telef = document.getElementById('telefono')

    foto.value = ''
    imgPreviw.src = ''
    imgPreviw.hidden = true
    boton.hidden = false
    nombre.value = ''
    apodo.value = ''
    posicion.value = ''
    camiseta.value = ''
    fechaNacJug.value = ''
    doc.value = ''
    telef.value = ''
}


function limpiarFormEn(){
    let foto = document.getElementById('fotoJugador')
    let imgPreviw = document.getElementById('imgprevisualizacion')
    let boton = document.getElementById('boton-foto')
    let nombre = document.getElementById('nombreJugador')
    let apodo = document.getElementById('apodoJugador')
    let nacion = document.getElementById('nacionalidad')
    let fechaNacJug = document.getElementById('fechaNac')
    let doc = document.getElementById('documento')
    let telef = document.getElementById('telefono')
    foto.value = ''
    imgPreviw.src = ''
    imgPreviw.hidden = true
    boton.hidden = false
    nombre.value = ''
    apodo.value = ''
    nacion.value = ''
    fechaNacJug.value = ''
    doc.value = ''
    telef.value = ''
}


function validarCI(aux){
    let nombres = aux.split('*')
    let input = document.getElementById("documento");
    for(let i=0; i< nombres.length;i++){
        if(input.value == nombres[i]){
          Swal.fire('', 'Este C.I. ya está registrado', 'error');
          input.value = "";
        }
    }
  }

  function validarDorsal(aux){
    let nombres = aux.split('*')
    let input = document.getElementById("camiseta");
    for(let i=0; i< nombres.length;i++){
        if(input.value == nombres[i]){
          Swal.fire('', 'Este Número ya está registrado', 'error');
          input.value = "";
        }
    }
  }