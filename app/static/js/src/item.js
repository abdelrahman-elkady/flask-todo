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
