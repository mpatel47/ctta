
/*
const url = 'http://127.0.0.1:5000/expiringmembers'; // Replace with the URL of the JSON API

// Fetch data on page load

const tableBody = document.querySelector("tbody");

fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(data => {
    // Iterate over each object in the JSON response and append a row to the table
    let dataArray = data;
    if (data.hasOwnProperty('payload')) {
      dataArray = data.payload;
    }
    if (!Array.isArray(dataArray)) {
      console.error("Error: Expected array data, but got", dataArray);
      return;
    }
    console.log(dataArray);
    dataArray.forEach(item => {
      const row = tableBody.insertRow();
      row.insertCell().textContent = item.name;
      row.insertCell().textContent = item.association;
      row.insertCell().textContent = item.tier;
      row.insertCell().textContent = item.expiration_date;
      row.insertCell().textContent = item.expiring_email;
    });
})
.catch(error => {
  console.error("Error fetching data:", error);
});  

*/

const sendEmailsButton = document.getElementById("sendemails");

sendEmailsButton.addEventListener("click", () => {
  const confirmed = confirm("Are you sure you want to send reminder emails?");
  if (confirmed) {
    fetch("http://127.0.0.1:5000/admins/sendreminder", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      }
    })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        alert("Reminder emails sent successfully!");
      })
      .catch(error => {
        console.error("Error sending reminder emails:", error);
        alert("Error sending reminder emails. Please try again later.");
      });
  }
});
