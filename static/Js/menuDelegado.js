
$(function(){
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
});