$(document).foundation();


// Clearning alerts after 3 seconds
var alertTimeoutId = setTimeout(function() {
  $('.alert-box a.close').trigger('click');
}, 3000);

$('.alert-box a.close').click(function() {
  clearTimeout(alertTimeoutId);
});


createItem = function(list_id) {
  var content = {
    'content': $('input[name=item-content]').val(),
  };

  $.ajax({
    url: "/items/new",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify(content),
    success: function(res) {
      console.log('yaaaaaaay')
    },
    error: function(error) {
      console.log(error);
    }
  });

};


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
