
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

  
  function validarNombre(aux){
    let nombres = aux.split('-')
    let input = document.getElementById("nombreEquipo");
    let nombre = input.value.toLowerCase()
    for(let i=0; i< nombres.length;i++){
  
        if(nombre == nombres[i].toLowerCase()){
          Swal.fire('Este nombre ya está registrado', '', 'error');
          input.value = "";
        }
    }
  }
  'use strict';

  ;( function ( document, window, index )
  {
      var inputs = document.querySelectorAll( '.inputfile' );
      Array.prototype.forEach.call( inputs, function( input )
      {
          var label	 = input.nextElementSibling,
              labelVal = label.innerHTML;
  
          input.addEventListener( 'change', function( e )
          {
              var fileName = '';
              if( this.files && this.files.length > 1 )
                  fileName = ( this.getAttribute( 'data-multiple-caption' ) || '' ).replace( '{count}', this.files.length );
              else
                  fileName = e.target.value.split( '\\' ).pop();
  
              if( fileName )
                  label.querySelector( 'span' ).innerHTML = fileName;
              else
                  label.innerHTML = labelVal;
          });
      });
  }( document, window, 0 ));

  function validarImg(elemento) {

    var archivoInput = document.getElementById(elemento);
    var archivoRuta = archivoInput.value;
    var extesiones = /(.jpg|.jpeg|.png)$/i;;

    if (!extesiones.exec(archivoRuta)) {
        Swal.fire('Sólo se permiten imágenes (.jpg .jpeg .png)', '', 'error');
        archivoInput.value = '';
        return false;
    }
}
