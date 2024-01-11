$(document).ready(function(){
    $('DIV#add_item').click(function(){
        $('<li>').text('item').appendTo('UL.my_list');
    });
});