// adds, removes and clears LI elements from a list when user clicks on div
$(document).ready(() => {
    list = $('UL.my_list');
    $('DIV#add_item').click(() => {
        list.append('<li>Item</li>');
    });
    $('DIV#remove_item').click(() => {
        $('UL.my_list li').last().remove();
    });
    $('DIV#clear_list').click(() => {
        list.empty();
    });
});
