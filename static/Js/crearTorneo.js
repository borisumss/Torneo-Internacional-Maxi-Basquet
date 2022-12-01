// Example starter JavaScript for disabling form submissions if there are invalid fields

(function () {
    'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
    var tabla = document.getElementById('tablaCategorias');
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                    if (tabla.rows.length == 1) {

                        Swal.fire('Debe ingresar al menos una Categoria', '', 'error');
                    }
                } else if (tabla.rows.length == 1) {
                    Swal.fire('Debe ingresar al menos una Categoria', '', 'error');
                    event.preventDefault()
                    event.stopPropagation()
                }
                form.classList.add('was-validated')

            }, false)
        })
})()

var nroCate = 0;
function validacionMin() {
    let min = document.getElementById('minimoModal_input');
    let max = document.getElementById('maximoModal_input');
    if (min.value < 30) {
        min.value = 30;
    } else if (min.value > 60) {
        min.value = 60;
    } else if (max.value > 0 && min.value > max.value) {
        Swal.fire('La edad mínima no puede ser mayor a la máxima', '', 'error');
        min.value = max.value;
    }
}

function validacionMax() {
    let max = document.getElementById('maximoModal_input');
    let min = document.getElementById('minimoModal_input');
    if (max.value < 30) {
        max.value = 30;
    } else if (max.value > 60) {
        max.value = 60;
    } else if (min.value > max.value) {
        Swal.fire('La edad mínima no puede ser mayor a la máxima', '', 'error');
        min.value = max.value;
    }
}

function insertarFila() {
    let name = document.getElementById('nombreModal_input');
    let min = document.getElementById('minimoModal_input');
    let max = document.getElementById('maximoModal_input');
    if (min.checkValidity() && name.checkValidity() && max.checkValidity()) {
        let tablaCategorias = document.getElementById('tablaCategorias');
    
        let esDistint = true;
        for (let i = 1; i < tablaCategorias.rows.length; i++) {
            if (tablaCategorias.rows[i].cells[0].firstChild.value == name.value) {
                esDistint = false;
            }
        }

        if (!esDistint) {
            Swal.fire('', 'Ya existe una categoria con este nombre', 'error');
        } else {
            let tablaCategorias = document.getElementById('tablaCategorias').insertRow(1);
            


            if (min.value > max.value) {
                Swal.fire('La edad mínima no puede ser mayor a la máxima', '', 'error');
            } else if (min.value < 30 && max.value < 30) {
                Swal.fire('La edad mínima es de 30 años', '', 'error');
            } else {
                const nameCell = tablaCategorias.insertCell(0);
                let minCell = tablaCategorias.insertCell(1);
                let maxCell = tablaCategorias.insertCell(2);
                nroCate = nroCate + 1;

                nameCell.innerHTML = "<input class='tablaInput form-control' onfocus='this.blur()' value='" + name.value + "' name='" + "nombreCategoria" + "'  >";
                minCell.innerHTML = "<input class='tablaInput form-control' onfocus='this.blur()' value='" + min.value + "' name='" + "minCategoria" + "' >";
                maxCell.innerHTML = "<input class='tablaInput form-control' onfocus='this.blur()' value='" + max.value + "' name='" + "maxCategoria" + "'>";
                let cerrar = document.getElementById('modalCancelar');
                cerrar.click();
            }

        }
    } else {
        let formu = document.getElementById('modalValid');
        formu.classList.add('was-validated')
        Swal.fire('LLene correctamente todos los campos', '', 'error');
    }
}

let inicio = document.getElementById('fechaIni_input');
let fin = document.getElementById('fechaFin_input');
let inicioPre = document.getElementById('fechaPreIni_input');
let finPre = document.getElementById('fechaPreFin_input');
let inicioRez = document.getElementById('fechaInsIni_input');
let finRez = document.getElementById('fechaInsFin_input');

let fechaActual = new Date(Date.now());
let now = moment(fechaActual).format('YYYY-MM-DD')

function fechasTorneoRez() {
    if (inicio.value.length == 0 || fin.value.length == 0 || inicioPre.value.length == 0 || finPre.value.length == 0) {
        Swal.fire('Debe llenar primero las anteriores fechas', '', 'error');
        finRez.value = "";
        inicioRez.value = "";
    } else {
        if (finRez.value.length > 0 && inicioRez.value.length > 0) {
            if (inicioRez.value <= finPre.value || inicioRez.value >= inicio.value || finRez.value <= finPre.value || finRez.value >= inicio.value) {
                Swal.fire('Las fechas de rezagados tiene que estar dentro los limites establecidos', '', 'error');

                finRez.value = "";
                inicioRez.value = "";
            } else {
                if (finRez.value < inicioRez.value) {
                    Swal.fire('La fecha final de Rezagados tiene que ser mayor a la de inicio', '', 'error');
                    finRez.value = "";
                }
            }
        } else {
            if (finRez.value.length == 0) {
                if (inicioRez.value <= finPre.value || inicioRez.value >= inicio.value) {
                    Swal.fire('Las fechas de rezagados tiene que estar dentro los limites establecidos', '', 'error');
                    finRez.value = "";
                    inicioRez.value = "";
                }
            } else {
                if (finRez.value <= finPre.value || finRez.value >= inicio.value) {
                    Swal.fire('Las fechas de rezagados tiene que estar dentro los limites establecidoss', '', 'error');
                    finRez.value = "";
                    inicioRez.value = "";
                }
            }
        }
    }
}

function fechasTorneoPre() {
    if (inicio.value.length == 0 || fin.value.length == 0) {
        Swal.fire('Debe llenar primero las fechas del torneo', '', 'error');
        finPre.value = "";
        inicioPre.value = "";
    } else {
        if (finPre.value.length > 0 && inicioPre.value.length > 0) {
            if (inicioPre.value >= inicio.value || finPre.value >= inicio.value) {
                Swal.fire('Las fechas de pre-inscripcion tiene que estar dentro el limite de las fechas del torneo', '', 'error');
                finPre.value = "";
                inicioPre.value = "";
            } else {
                if (finPre.value < inicioPre.value) {
                    Swal.fire('La fecha final de Pre-inscripcion tiene que ser mayor a la de inicio', '', 'error');
                    finPre.value = "";
                } else {
                    if (inicioPre.value < now) {
                        inicioPre.value = now;
                        finPre.value = "";
                    }
                }
            }
        } else {
            if (finPre.value.length == 0) {
                if (inicioPre.value >= inicio.value) {
                    Swal.fire('Las fechas de pre-inscripcion tiene que ser antes de que comience el torneo', '', 'error');
                    finPre.value = "";
                    inicioPre.value = "";
                } else {
                    if (inicioPre.value < now) {
                        inicioPre.value = now;
                        finPre.value = "";
                    }
                }
            } else {
                if (finPre.value >= inicio.value) {
                    Swal.fire('Las fechas de pre-inscripcion tiene que ser antes de que comience el torneo', '', 'error');
                    finPre.value = "";
                    inicioPre.value = "";
                } else {
                    if (finPre.value < now) {
                        inicioPre.value = now;
                        finPre.value = "";
                    }
                }
            }
        }
    }

    if (finPre.value.length > 0) {
        //format('YYYY-MM-DD')
        var fechaIniRez = new Date($('#fechaPreFin_input').val());
        console.info(fechaIniRez)
        var dias = 2
        fechaIniRez.setDate(fechaIniRez.getDate() + dias);

        fechaIniRez = moment(fechaIniRez).format('YYYY-MM-DD')
        inicioRez.value = fechaIniRez;


    }
}

function fechasTorneo() {

    if (fin.value.length > 0 && inicio.value.length > 0) {
        if (inicio.value < now) {
            Swal.fire('No se permiten fechas pasadas', '', 'error');
            inicio.value = "";
            fin.value = "";
        } else {
            if (fin.value <= inicio.value) {
                Swal.fire('La fecha final del torneo tiene que ser mayor a la de inicio', '', 'error');
                fin.value = "";
            }
        }
    } else {
        if (fin.value.length == 0) {
            if (inicio.value < now) {
                Swal.fire('No se permiten fechas pasada', '', 'error');
                inicio.value = now;
                fin.value = "";
            }
        } else {
            if (fin.value < now) {
                Swal.fire('No se permiten fechas pasadas', '', 'error');
                inicio.value = "";
                fin.value = now;
            }
        }
    }
}

function cerrarModal() {
    let cerrar = document.getElementById('modalCancelar');
    let name = document.getElementById('nombreModal_input');
    let min = document.getElementById('minimoModal_input');
    let max = document.getElementById('maximoModal_input');

    name.value = "";
    min.value = "";
    max.value = "";
    cerrar.click();
}

function validarLogo() {

    var archivoInput = document.getElementById("logoTorneo");
    var archivoRuta = archivoInput.value;
    var extesiones = /(.jpg|.jpeg|.png)$/i;;

    if (!extesiones.exec(archivoRuta)) {
        Swal.fire('Sólo se permiten imágenes (.jpg .jpeg .png)', '', 'error');
        archivoInput.value = '';
        return false;
    }
}

function validarMontoIns(){
    var montoIns = document.getElementById("montoIns_input");
    var montoPre = document.getElementById("montoPre_input");

    if (parseInt(montoIns.value) < parseInt(montoPre.value)) {
        Swal.fire('El monto de Inscripción debe ser mayor o igual al monto de Preinscrición', '', 'error');
        montoIns.value = parseInt(montoPre.value);
      
        return false;
    }
}

function validarMontoPre(){
    var montoIns = document.getElementById("montoIns_input");
    var montoPre = document.getElementById("montoPre_input");

    if (montoIns.value != '' && parseInt(montoPre.value) > parseInt(montoIns.value) ) {
        Swal.fire('El monto de Inscripción debe ser mayor o igual al monto de Preinscrición', '', 'error');
        montoPre.value = parseInt(montoIns.value);
        return false;
    }
}