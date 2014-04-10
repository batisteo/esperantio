
function object_list(mapo, options) {
    $(".object").each(function(){
        var o = $(this)
        var id = o.attr('object_id');
        var url = o.attr('url');
        var lat = o.attr('lat');
        var long = o.attr('long');
        var nomo = o.attr('nomo');
        var jaro = o.attr('jaro');
        var urbo = o.attr('urbo');
        var marker = L.marker([lat, long]).addTo(mapo);
        var msg = "<strong><a href='"+ url +"'>"+ nomo +" "+ jaro + "</a></strong><br/>"+ urbo;
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
        var marker = L.marker([lat, long], {draggable:true}).addTo(mapo);
    }
    else {
        mapo.setView([40,0],2);
            var marker = L.marker([40,0], {
                    draggable:true,
                    opacity:0
            }).addTo(mapo);
        
    }

    function onMapClick(e) {
        $("[id$='lat']").val(e.latlng.lat);
        $("[id$='long']").val(e.latlng.lng);
        marker.setLatLng(e.latlng).setOpacity(1);
        mapo.setView(e.latlng, mapo.getZoom()+2);
    }

    mapo.on('click', onMapClick);
};
