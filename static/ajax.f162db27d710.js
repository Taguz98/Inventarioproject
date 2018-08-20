$(document).ready(function(){
  $("busqueda").submit(function(e){
    e.preventDefault();
    console.log("Holaaa");

    $.ajax({
      url: $(this).attr('action'),
      type: $(this).attr('method'),
      data: $(this).serialize(),
      succes: function(json){
        console.log(json)
      }
    });
  });
});
