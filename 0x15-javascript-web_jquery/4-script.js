// Toggle the class of the <header> element when the user clicks on div
$('DIV#toggle_header').click(() => {
    header = $('header');
    if (header.hasClass('red')) {
        header.removeClass('red');
        header.addClass('green');
    } else {
        header.removeClass('green');
        header.addClass('red');
    }
});
