const url = 'http://127.0.0.1:5000/driver/' + userId; // Replace with the URL of the JSON API
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
      row.insertCell().textContent = item.d_id;
      row.insertCell().textContent = item.firstname;
      row.insertCell().textContent = item.lastname;
      row.insertCell().textContent = item.email;
      row.insertCell().textContent = item.phone;

      // Add edit, delete, and transfer buttons to the row
      const editButton = document.createElement("button");
        editButton.textContent = "Edit";

        editButton.addEventListener("click", () => {
          const width = window.innerWidth / 2;
          const height = window.innerHeight / 2;
          const left = window.screenX + ((window.innerWidth - width) / 2);
          const top = window.screenY + ((window.innerHeight - height) / 2);
        
          const popup = window.open("/users/user/editdriver/" + item.d_id, "Edit", `width=${width},height=${height},left=${left},top=${top}`);
        
          popup.onunload = () => {
            location.reload();
          };
          
        });
        row.insertCell().appendChild(editButton);
        editButton.classList.add("btn", "btn-primary", "mx-2");
        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.classList.add("btn", "btn-danger", "mx-2");
        deleteButton.addEventListener("click", () => {
          if (confirm(`Are you sure you want to delete ${item.firstname} ${item.lastname}?`)) {
            fetch('http://127.0.0.1:5000/driver/' + item.d_id, {
              method: "DELETE"
            })
              .then(response => response.json())
              .then(result => {
                console.log(result);
                // Reload the page to refresh the table
                window.location.reload();
              })
              .catch(error => console.error(error));
          }
        });
        row.insertCell().appendChild(deleteButton);

        const transferButton = document.createElement("button");
        transferButton.textContent = "Transfer";

        transferButton.addEventListener("click", () => {
          const width = window.innerWidth / 2;
          const height = window.innerHeight / 2;
          const left = window.screenX + ((window.innerWidth - width) / 2);
          const top = window.screenY + ((window.innerHeight - height) / 2);
        
          const popup = window.open("/users/user/transferdriver/" + item.d_id, "Transfer", `width=${width},height=${height},left=${left},top=${top}`);
        
          popup.onunload = () => {
            location.reload();
          };
          
        });
        row.insertCell().appendChild(transferButton);
        transferButton.classList.add("btn", "btn-success", "mx-2");
    });
  })
  .catch(error => {
    console.error("Error fetching data:", error);
  });

  const add_driver = document.getElementById('add_driver');
add_driver.addEventListener("click", function() {
  console.log('True')
  const width = window.innerWidth / 2;
  const height = window.innerHeight / 2;
  const left = window.screenX + ((window.innerWidth - width) / 2);
  const top = window.screenY + ((window.innerHeight - height) / 2);

  const popup = window.open("/users/user/adddriver/" + userId, "Edit", `width=${width},height=${height},left=${left},top=${top}`);

  popup.onunload = () => {
    location.reload();
  };
});
