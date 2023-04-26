

$("#search1").keyup(function () {
  let searchText = $(this).val();
  if (searchText != "") {
    $.ajax({
      url: 'http://127.0.0.1:5000/autocomplete',
      method: 'POST',
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({
        search: searchText
      }),
      success: function (response) {
        if (response.success) {
          $("#show-list").html('');
          response.data.forEach(record => {
            const listItem = $('<a id = "ato"  class = "list-group-item list-group-item-action border-1">').text(record.c_name);
            $('#show-list').append(listItem);
          });
        }
      },
      error: function (error) {
        console.log(error);
      }
    });
  } else {
    $("#show-list").html("");
  }
});

$(document).on("click", "#ato", function () {
  $("#search1").val($(this).text());
  $("#show-list").html("");
});

driverId = document.getElementById("driverid").value;
apiUrl = 'http://127.0.0.1:5000/transfer/' + driverId;

$(document).on('click' , '#submit', function() {
  var value = $('#search1').val(); 
  var data1 = {
    c_name: value
  
  };
fetch(apiUrl, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data1)
})
.then(response => response.json())
.then(data => {
  console.log('Success:', data);
  alert('Transfered successfully')
})
.catch((error) => {
  console.error('Error:', error);
  alert("Error in updating");
});
});




