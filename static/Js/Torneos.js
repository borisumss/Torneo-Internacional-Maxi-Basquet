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
