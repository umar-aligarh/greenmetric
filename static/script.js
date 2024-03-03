function getGreenScore() {
    var latitude = document.getElementById('latitudeInput').value;
    var longitude = document.getElementById('longitudeInput').value;

    if (latitude && longitude) {
        var coordinates = {
            latitude: parseFloat(latitude),
            longitude: parseFloat(longitude)
        };

        fetch('/segment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ coordinates: coordinates })
        })
        .then(response => response.json())
        .then(data => {
            // Open a new tab
            var newTab = window.open('');

            // Write HTML content to the new tab
            newTab.document.write('<html><head><title>Green Score Result</title></head><body>');

            // Display map
            newTab.document.write('<div class="map-container"><iframe id="mapFrame" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d250592.2455357074!2d-74.25987507441943!3d40.69767000571747!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c3c8e6c3d97803%3A0x5058ea3f9e0dd0c4!2sNew%20York%2C%20NY%2C%20USA!5e0!3m2!1sen!2sin!4v1646398454972!5m2!1sen!2sin" width="800" height="600" style="border:0;" allowfullscreen="" loading="lazy"></iframe></div>');

            // Display original image
            newTab.document.write('<h2>Original Image</h2><img src="' + data.original_image_url + '">');

            // Display mask image
            newTab.document.write('<h2>Mask Image</h2><img src="' + data.mask_image_url + '">');

            // Add button to display green score
            newTab.document.write('<button onclick="showGreenScore(' + data.green_score + ')">Show Green Score</button>');

            // Close the HTML content and tab
            newTab.document.write('</body></html>');
            newTab.document.close();

            // Close the new tab after 10 seconds (adjust as needed)
            setTimeout(function() {
                newTab.close();
            }, 10000);
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert("Please enter both latitude and longitude values.");
    }
}

function showGreenScore(score) {
    alert("Green Score: " + score);
}
