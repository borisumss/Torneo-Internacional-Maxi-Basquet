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

  $('#btn-Generar').click(function(){
    let email = document.getElementById('correo_modalInput');
    let user = document.getElementById('name_modalInput');
    let correo = document.getElementById('modalEnviar').value;
    email.value = correo.split('@')[0]+"@delegacion.com";
    user.value = correo.split('@')[0]+"-"+document.getElementById('boton-rechazar').name;
    document.getElementById('boton-rechazar').name = null;
    $(this).hide();
    $('#boton-rechazar').show();
    $('#modalEnviar').show();
    return false;
});