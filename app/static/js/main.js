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
    'list_id':list_id,
    'content': $('input[name=item-content]').val(),
  };

  $.ajax({
    url: "/items/new",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify(content),
    success: function(res) {
      $('input[name=item-content]').val('');
      window.location.reload(true); // ineffecient enough :3
    },
    error: function(error) {
      console.log(error);
    }
  });

};

deleteItem = function(event,caller,id) {
  event.preventDefault();

  $.ajax({
    url: "/items/delete/" + id,
    type: "POST",
    success: function(res) {
      caller.closest('li').fadeOut(250);
    },
    error: function(error) {
      console.log(error);
    }
  });

  return false;
};


deleteList = function(event,caller,id) {
  event.preventDefault();

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

  return false;
};
