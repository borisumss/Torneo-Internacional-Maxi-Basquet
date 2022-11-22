
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

function validarPuntos(){
   puntosA = document.getElementById('ptsEquipoA');
   puntosB = document.getElementById('ptsEquipoB');

   if (puntosA.value == puntosB.value){
    Swal.fire('Debe haber un ganador', '', 'error');
      puntosA.value = puntosA.value - 1;
   }
}