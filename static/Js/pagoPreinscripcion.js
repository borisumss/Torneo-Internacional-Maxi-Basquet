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

  function validarComprobante() {

    var archivoInput = document.getElementById("voucher");
    var archivoRuta = archivoInput.value;
    var extesiones = /(.jpg|.jpeg|.png)$/i;;

    if (!extesiones.exec(archivoRuta)) {
        Swal.fire('Sólo se permiten imágenes (.jpg .jpeg .png)', '', 'error'); 
        archivoInput.value = '';
        return false;
    }
}
