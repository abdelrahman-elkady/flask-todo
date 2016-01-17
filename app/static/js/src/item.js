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
      caller.closest('li').css("color","$grey");
      caller.closest('li').css("text-decoration","line-through");
      caller.closest('li').fadeOut(400);
    },
    error: function(error) {
      console.log(error);
    }
  });

  return false;
};
