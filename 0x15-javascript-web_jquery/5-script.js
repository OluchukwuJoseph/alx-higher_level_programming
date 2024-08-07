//  Adds a <li> element to a list when the user clicks on <div>
$('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>');
});
