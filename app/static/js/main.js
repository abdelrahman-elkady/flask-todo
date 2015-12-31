$(document).foundation();


// Clearning alerts after 3 seconds
var alertTimeoutId = setTimeout(function() {
  $('.alert-box a.close').trigger('click');
}, 3000);

$('.alert-box a.close').click(function() {
  clearTimeout(alertTimeoutId);
});


deleteList = function(caller,id) {
  $.ajax({
    url: "/lists/delete/" + id,
    type: "POST",
    success: function(res) {
      caller.closest('div').fadeOut(250);
    },
    error: function(error) {
      console.log(error);
    }
  });
};
