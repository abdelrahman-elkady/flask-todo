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
