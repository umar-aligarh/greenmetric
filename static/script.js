var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 40.7128, lng: -74.0060 }, // Default center (New York)
        zoom: 8
    });

    // Display initial coordinates
    updateCoordinates(map.getCenter());

    // Listen for map events
    map.addListener('zoom_changed', function() {
        // Update coordinates when zoom changes
        updateCoordinates(map.getCenter());
    });

    map.addListener('center_changed', function() {
        // Update coordinates when map center changes
        updateCoordinates(map.getCenter());
    });
}

function updateCoordinates(latLng) {
    // Display coordinates
    document.getElementById('coordinatesContainer').innerHTML = "Coordinates Only: Latitude: " + latLng.lat() + ", Longitude: " + latLng.lng();
}

function getCoordinates() {
    var latitude = document.getElementById('latitudeInput').value;
    var longitude = document.getElementById('longitudeInput').value;
    
    if (latitude && longitude) {
        var coordinates = {
            latitude: parseFloat(latitude),
            longitude: parseFloat(longitude)
        };
        
        updateCoordinates(coordinates);
    } else {
        alert("Please enter both latitude and longitude values.");
    }
}

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
        .then(response => response.text())
        .then(data => {
            document.getElementById('resultContainer').innerHTML = "Green Score: " + data;
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert("Please enter both latitude and longitude values.");
    }
}
