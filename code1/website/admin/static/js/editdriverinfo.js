const driverId = document.getElementById("driverid").value;
const apiUrl = 'http://127.0.0.1:5000/editdrivers/'+ driverId; // Replace with the URL of the JSON API

// Fetch data on page load
fetch(apiUrl, {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  },
  
})
.then(response => response.json())
.then(data => {
  console.log(data);

  // Populate form fields with fetched data
  document.getElementById("email").value = data.payload['0'].email;
  document.getElementById("adrs1").value = data.payload['0'].d_address_line_1;
  document.getElementById("adrs2").value = data.payload['0'].d_address_line_2;
  document.getElementById("city").value = data.payload['0'].d_city;
  document.getElementById("firstname").value = data.payload['0'].firstname;
  document.getElementById("middlename").value = data.payload['0'].d_middle_name;
  document.getElementById("phone").value = data.payload['0'].phone;
  document.getElementById("postalcode").value = data.payload['0'].d_postal_code;
  document.getElementById("suffix").value = data.payload['0'].d_suffix;
  document.getElementById("lastname").value = data.payload['0'].lastname;
 
})
.catch(error => console.error(error));

// Attach event listener to button for post request
const inputElement = document.getElementById('editdriverbutton');
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
    d_id: driverId, 
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

