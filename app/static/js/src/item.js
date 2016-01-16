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
