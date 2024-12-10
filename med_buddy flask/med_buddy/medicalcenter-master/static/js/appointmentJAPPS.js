document.getElementById('appointmentForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting normally
    
    // Get form values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;
    
    // Display a confirmation message
    const confirmationMessage = `Appointment booked successfully for ${name} on ${date} at ${time}. We will contact you at ${email} or ${phone}.`;
    document.getElementById('confirmationMessage').textContent = confirmationMessage;
    
    // Clear the form
    document.getElementById('appointmentForm').reset();
});
