const userId = document.getElementById("userid").value;
const inputElement = document.getElementById('adddriverbutton');
const apiUrl = 'http://127.0.0.1:5000/driver/'+ userId;
inputElement.addEventListener("click", function() {
  // Get values from form fields
 
  var adrs1 = document.getElementById("adrs1").value;
  var adrs2 = document.getElementById("adrs2").value;
  var city = document.getElementById("city").value;
 
  var firstname = document.getElementById("firstname").value;
 
  var email = document.getElementById("email").value;
  var middlename = document.getElementById("middlename").value;
  var phone = document.getElementById("phone").value;
  var postalcode = document.getElementById("postalcode").value;
  var suffix = document.getElementById("suffix").value;
 
  var lastname = document.getElementById("lastname").value;

  // Create payload for POST request
  var data1 = {
    u_id: userId, 
    d_id: 'Empty',
    firstname: firstname,
    middlename: middlename,
    lastname: lastname,
    suffix: suffix,
    address_line_1: adrs1,
    address_line_2: adrs2,
    city: city,
    email: email,
    postal_code: postalcode,
    phone: phone
  
  };

  console.log(data1);

  // Make POST request
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
    alert('Records updated successfully')
  })
  .catch((error) => {
    console.error('Error:', error);
    alert("Error in updating");
  });
});