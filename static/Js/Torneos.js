// init Isotope
var primer = $('.filter-button-group button:first').attr('data-filter');
$('.filter-button-group button:first').addClass('seleccionado');
var $grid = $('#product-list').isotope({
    filter: primer
});
  


// filter items on button click
$('.filter-button-group').on('click', 'button', function () {
    var filterValue = $(this).attr('data-filter');
    $('.filter-button-group button').removeClass('seleccionado');
    $(this).addClass('seleccionado');
    $grid.isotope({ filter: filterValue });
});

function cargar(){
    Swal.fire({
        title: "Generando Enfrentamientos...",
        icon: "info",
        closeOnConfirm: true,
        closeOnCancel: true,
        allowOutsideClick: false,
        showCancelButton: false,
        showConfirmButton: false,


      });
}