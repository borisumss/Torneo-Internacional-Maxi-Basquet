function validarQR(){
    let divQR = document.getElementById("qr")
    let infoPago = document.getElementById("info")
    const tiempoTranscurrido = Date.now() //Obtiene el tiempo actual en milisegundos
    const hoy = new Date(tiempoTranscurrido) //Convierte en formato "DiaSemana Mes Dia Año GTM"
    let fechaActual = hoy.toLocaleDateString() //Convierte en formato "dia/mes/año"
    let fechaRezBD = "20/10/2022"  //Extraer de la BD,ultima fecha pago monto minimo 
    let fechaLimRezBD = "25/10/2022" //Ultima fecha de rezagados y cierre de preinscripcion

    if(fechaActual <= fechaRezBD){
        divQR.innerHTML = '<img class="qr" src="/static/imagenes/qrs/qrcode_classroom.png">'
        infoPago.innerHTML = 'Esta en etapa de pre-inscripción, el monto es {250}$'

    }else if(fechaActual > fechaRezBD && fechaActual <= fechaLimRezBD){
        divQR.innerHTML = '<img class="qr" src="/static/imagenes/qrs/qrcode_websis.png">'
        infoPago.innerHTML = 'Esta en etapa de pre-inscripción, el monto es {400}$'

    }else{
        let mensaje = document.getElementById("principal")
        mensaje.innerHTML = 
        `<div class="container d-flex align-items-center justify-content-center vh-100">
            Lo sentimos, termino el plazo para pre-inscripcion
        </div>`
    }
}