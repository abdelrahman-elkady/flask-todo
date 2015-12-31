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
