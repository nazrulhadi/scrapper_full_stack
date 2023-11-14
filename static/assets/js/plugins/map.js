// Initialize the map
var map = L.map('map', {
  center: [2.1896, 102.2501],
  zoom: 5
});

// Add a tile layer to the map (using OpenStreetMap)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Check if outletsData has values
if (outletsData && outletsData.length > 0) {
  // Function to add a circle to the map
  function addCircle(lat, lon, radius) {
    L.circle([lat, lon], { radius: radius * 1000 }).addTo(map);
  }

  // Iterate through outlets data and add circles
  outletsData.forEach(function (outlet) {
    addCircle(outlet.latitude, outlet.longitude, 5);

    // You can customize the popup content as needed
    L.marker([outlet.latitude, outlet.longitude])
      .bindPopup('<b>Outlet</b><br>' + 'Latitude: ' + outlet.latitude + '<br>Longitude: ' + outlet.longitude)
      .addTo(map);
  });

  // Create a feature group for the markers
  var markers = L.featureGroup(outletsData.map(function (outlet) {
    return L.marker([outlet.latitude, outlet.longitude])
      .bindPopup('<b>Outlet</b><br>' + 'Latitude: ' + outlet.latitude + '<br>Longitude: ' + outlet.longitude);
  }));

  // Fit the map bounds to include all markers
  map.fitBounds(markers.getBounds());
  map.setZoom(map.getZoom() - 1);
} else {
  // If outletsData is empty, just show the default map centered on Melaka
  map.setView([2.1896, 102.2501], 12);
}
