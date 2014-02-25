$(function() {

    var map = L.map('mapo').setView([45.1, 3.9], 2);
    var tiles = 'http://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png'
    L.tileLayer(tiles, {
        attribution: 'Mapaj datumoj &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> kontribuantoj',
        maxZoom: 19,
        minZoom: 2
    }).addTo(map);
    
    $(".evento").each(function(){
       var nomo = $(this).children(".nomo").text();
       var urbo = $(this).children(".urbo").text();
       var lat = $(this).children(".lat").text();
       var long = $(this).children(".long").text();
       var marker = L.marker([lat, long]).addTo(map);
       var msg = "<strong>"+ nomo +"</strong><br/>"+ urbo;
       marker.bindPopup(msg);
    });
        
});
