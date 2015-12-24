$(document).ready(function() {
  $(document).foundation();

  var alertTimeoutId = setTimeout(function(){
    $('.alert-box a.close').trigger('click');
  }, 3000);

  $('.alert-box a.close').click(function(){
    clearTimeout(alertTimeoutId);
  });


});
