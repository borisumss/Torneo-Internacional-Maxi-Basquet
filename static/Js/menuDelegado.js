
/*$(function(){
    $('ul.tabs li:first').addClass('active');
    $('.secciones article').hide();
    $('.secciones article:first').show();
});

$('ul.tabs li').click(function(){
    $('ul.tabs li').removeClass('active');
    $(this).addClass('active');
    $('.secciones article').hide();

    var activeTab = $(this.firstElementChild).attr('href');
    console.log(activeTab);
    $(activeTab).show();
    return false;
});*/

$('.burger').click(function(){
    
    let x = $('#side_nav').width();
    if(x<=55){
        $('#side_nav').addClass('menu-expanded');
        $('#side_nav').removeClass('menu-collapsed');
    }else{
        $('#side_nav').addClass('menu-collapsed');
        $('#side_nav').removeClass('menu-expanded');
    }

    return false;
});

$('#btn-infor').click(function(){
    
    $('#btn-guardar').removeClass('guardar');
    $('#btn-guardar').addClass('btn-guardarBlock');
    var billingItems = document.querySelectorAll('input');
    for (var i = 0; i < billingItems.length; i++) {
      billingItems[i].disabled = false;
    }

    return false;
});