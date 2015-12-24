// Clearning alerts after 3 seconds
var alertTimeoutId = setTimeout(function() {
  $('.alert-box a.close').trigger('click');
}, 3000);

$('.alert-box a.close').click(function() {
  clearTimeout(alertTimeoutId);
});
