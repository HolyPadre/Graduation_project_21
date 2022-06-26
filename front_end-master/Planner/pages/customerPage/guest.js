$(document).ready(function(){
    var i=1;
   $("#add_row").click(function(){
    $('#addr'+i).html("<td>"+ (i+1) +"</td><td><input name='name"+i+"' type='text' placeholder='name' class='form-control input-md'/></td><td><input  name='mail"+i+"' type='text' placeholder='email'  class='form-control input-md'></td><td> <select class='form-select' aria-label='Default'><option value='1'>Friends</option><option value='3'>Family</option></select></td><td><button type='button' class='btn btn-danger'>Delete</button></td>");

    $('#tab_logic').append('<tr id="addr'+(i+1)+'"></tr>');
    i++; 
});
});