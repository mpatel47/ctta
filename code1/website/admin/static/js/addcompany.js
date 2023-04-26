$(document).ready(() => {
    $('#add-company-form').submit(function(e) {
        e.preventDefault();

        var formData = $(this).serialize(); // Serialize form data

        $.ajax({
            url: '/company', // URL to send AJAX request
            type: 'POST',
            data: formData,
            success: function(response) {
                console.log('Form data submitted successfully!');
                window.location.href = '/admins/home'
            },
            error: function() {
                console.log('Error submitting form data!');
            }
        });
    })
})