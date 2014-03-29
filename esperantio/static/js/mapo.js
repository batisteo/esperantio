
function object_list(mapo, options) {
    $(".object").each(function(){
        var o = $(this)
        var lat = o.attr('lat');
        var long = o.attr('long');
        var nomo = o.attr('nomo');
        var jaro = o.attr('jaro');
        var urbo = o.attr('urbo');
        var marker = L.marker([lat, long]).addTo(mapo);
        var msg = "<strong>"+ nomo +" " + jaro + "</strong><br/>"+ urbo;
        marker.bindPopup(msg);
    });
};


function object_detail(mapo, options) {
    var o = $('#object')
    var lat = o.attr('lat');
    var long = o.attr('long');
    var nomo = o.attr('nomo');
    var jaro = o.attr('jaro');
    var urbo = o.attr('urbo');

    mapo.setView([lat, long], 13);
    var marker = L.marker([lat, long]).addTo(mapo);
    var msg = "<strong>" + nomo + " " + jaro + "</strong><br/>" + urbo;
    marker.bindPopup(msg).openPopup();
};


function object_form(mapo, options) {
    var o = $('#object')
    var lat = o.attr('lat');
    var long = o.attr('long');
    if (lat && long) {
        mapo.setView([lat, long], 13);
        var marker = L.marker([lat, long]).addTo(mapo);
    }
    else {
        mapo.setView([30,0],2);
        var marker = L.marker([30,0]).addTo(mapo);
    }

    function onMapClick(e) {
        $("[id$='lat']").val(e.latlng.lat);
        $("[id$='long']").val(e.latlng.lng);
        marker.setLatLng(e.latlng);
        var msg = "Lat: <strong> "+e.latlng.lat.toFixed(5) +"</strong><br/>Long: <strong>"+ e.latlng.lng.toFixed(5) +"</strong>";
        marker.bindPopup(msg).openPopup();
    }

    mapo.on('click', onMapClick);
};
