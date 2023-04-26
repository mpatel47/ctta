$(document).ready(() => {

    const cl_id = $('#cl_id').val();

    const api_url = '/class?cl_id=' + cl_id;

    $.getJSON(api_url, (response) => {

        payload = response.payload

        console.log(payload)

        var date = new Date(payload[0]['cl_time']);
        
        var time = date.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
        var formattedDate = date.toLocaleDateString([], {year: 'numeric', month: 'long', day: 'numeric'});
        var formatedDateTime = formattedDate + ' ' + time;

    
        $('#current-time').text(formatedDateTime);
        $('#current-link').text(payload[0]['cl_zoom_link']);
    })
    .fail(() => {
        console.error('Error fetching JSON from class endpoint')
    })

    $('#class-form').submit(function(e) {
        e.preventDefault();

        var formData = $(this).serialize(); // Serialize form data

        $.ajax({
            url: '/class', // URL to send AJAX request
            type: 'PUT',
            data: formData,
            success: function(response) {
                console.log('Form data submitted successfully!');
                location.reload(); // Reload page after form data is submitted
            },
            error: function() {
                console.log('Error submitting form data!');
            }
        });
    })

    $('#delete-course').click(() => {

        

        $.ajax({
            url: '/class', // URL to send AJAX request
            type: 'DELETE',
            data: {"cl_id": cl_id},
            success: function(response) {
                console.log('Form data submitted successfully!');
                window.location.href = '/admins/courseinfo' // Reload page after form data is submitted
            },
            error: function() {
                console.log('Error submitting form data!');
            }
        });
    })
});