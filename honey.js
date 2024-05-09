function submitIP() {
    var ipAddress = document.getElementById('ipAddress').value;
    var trimmedIP = ipAddress.trim(); // Remove leading and trailing spaces

    if (trimmedIP === '') {
        alert('Brother, Try Again and Think Positive');
    } else if (!isNaN(trimmedIP) && parseInt(trimmedIP) > 4) {
        alert('Wait please for checking.'); // Message for integer values greater than 4
    } else if (isNaN(trimmedIP)) {
        alert('eis sai kam nahi chelege'); // Message for any string input
    } else {
        console.log('Submitted IP:', trimmedIP);
        alert('IP Address to Short ' + trimmedIP); // Example alert (customize as needed)
    }
}

// Listen for Enter key press in the input box
document.getElementById('ipAddress').addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        submitIP(); // Call the submitIP function when Enter is pressed

        
    }
});
