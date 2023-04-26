

const userId = document.getElementById("userid").value;
const apiUrl = 'http://127.0.0.1:5000/userinfo/' + userId;

// Fetch data on page load
fetch(apiUrl, {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
})
.then(response => response.json())
.then(data => {
  console.log(data);

  // Populate form fields with fetched data
  document.getElementById("name").value = data.payload['0'].name;
  document.getElementById("adrs1").value = data.payload['0'].address_line_1;
  document.getElementById("adrs2").value = data.payload['0'].address_line_2;
  document.getElementById("city").value = data.payload['0'].city;
  document.getElementById("fax").value = data.payload['0'].fax;
  document.getElementById("firstname").value = data.payload['0'].firstname;
  document.getElementById("fleet").value = data.payload['0'].fleetsize;
  document.getElementById("location").value = data.payload['0'].location;
  document.getElementById("middlename").value = data.payload['0'].middlename;
  document.getElementById("phone").value = data.payload['0'].phone;
  document.getElementById("postalcode").value = data.payload['0'].postal_code;
  document.getElementById("suffix").value = data.payload['0'].suffix;
  document.getElementById("website").value = data.payload['0'].website;
  document.getElementById("lastname").value = data.payload['0'].lastname;
  document.getElementById("internalcomment").value = data.payload['0'].internalcomment;
})
.catch(error => console.error(error));

// Attach event listener to button for post request
const inputElement = document.getElementById('updatecomment');
commentURL = 'http://127.0.0.1:5000/comment';
inputElement.addEventListener("click", function() {
  // Get values from form fields
  var c_comment = document.getElementById("internalcomment").value;
  

  // Create payload for POST request
  var data1 = {
    comment: c_comment, 
    u_id : userId
    
  };

  console.log(data1);

  // Make POST request
  fetch(commentURL, {
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



// Attach event listener to button for post request
const inputelement = document.getElementById('updateuserbutton');
inputelement.addEventListener("click", function() {
  // Get values from form fields
  var cname = document.getElementById("name").value;
  var adrs1 = document.getElementById("adrs1").value;
  var adrs2 = document.getElementById("adrs2").value;
  var city = document.getElementById("city").value;
  var fax = document.getElementById("fax").value;
  var firstname = document.getElementById("firstname").value;
  var fleet = document.getElementById("fleet").value;
  var location1 = document.getElementById("location").value;
  var middlename = document.getElementById("middlename").value;
  var phone = document.getElementById("phone").value;
  var postalcode = document.getElementById("postalcode").value;
  var suffix = document.getElementById("suffix").value;
  var website = document.getElementById("website").value;
  var lastname = document.getElementById("lastname").value;

  // Create payload for POST request
  var data1 = {
    name: cname, 
    firstname: firstname,
    middlename: middlename,
    lastname: lastname,
    suffix: suffix,
    address_line_1: adrs1,
    address_line_2: adrs2,
    city: city,
    location: location1,
    postal_code: postalcode,
    website: website,
    phone: phone,
    fax: fax,
    fleetsize: fleet
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

const inputElemen = document.getElementById('passwordreset');
passURL = 'http://127.0.0.1:5000/resetpassword';
inputElemen.addEventListener("click", function() {
  // Get values from form fields
  var new_pass = document.getElementById("password").value;

  // Check if password field is empty
  if (!new_pass) {
    alert('Please enter a password');
    return;
  }

  // Confirm password reset with user
  if (!confirm('Are you sure you want to reset your password?')) {
    return;
  }

  // Create payload for POST request
  var data1 = {
    password: new_pass,
    u_id: userId
  };

  console.log(data1);

  // Make POST request
  fetch(passURL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data1)
  })
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
    alert('Password reset successful')
  })
  .catch((error) => {
    console.error('Error:', error);
    alert("Error in resetting");
  });
});

