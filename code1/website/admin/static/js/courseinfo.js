$ ( document ).ready(() => {
    $.getJSON('/class', (response) => {

        payload = response.payload
    
        tbody = $('tbody')

    
        payload.forEach((el) => {
            tbody.append(`<tr><td>${el['cl_id']}</td><td>${el['cl_time']}</td><td>${el['cl_zoom_link']}</td></tr>`)
        })
    
        $('#data-table').DataTable();
    })
    .fail(() => {
        console.error('Error fetching JSON from class endpoint')
    })
})
