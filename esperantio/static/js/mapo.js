
function object_list(mapo, options) {

    function onLocationFound(e) {
        console.log(e);
    };

    function getBoundariesURL (){
        bounds = mapo.getBounds();
        bnd = {
            'n': bounds.getNorthEast().lng,
            's': bounds.getSouthWest().lng,
            'e': bounds.getNorthEast().lat,
            'w': bounds.getSouthWest().lat
        }
        return "?n="+bnd['n'] +"&s="+bnd['s'] +"&e="+bnd['e'] +"&w="+bnd['w'];
    };

    function getData() {
        markers.clearLayers();
        url = $('#list-ajax-url').text() + getBoundariesURL();
        $.getJSON(url, function(data) {
            for (var i=0; i < data.length; i++){
                console.log(data[i].nomo);
                var id = data[i].object_id;
                var url = data[i].url;
                var lat = data[i].lat;
                var long = data[i].long;
                var nomo = data[i].nomo;
                var jaro = data[i].jaro;
                var urbo = data[i].urbo;

                var marker = L.marker([lat, long]);
                var msg = "<strong><a href='"+ url +"'>"+ nomo +" "+ jaro + "</a></strong><br/>"+ urbo;
                marker.bindPopup(msg);
                markers.addLayer(marker);
            }
        });
    };

    var markers = new L.FeatureGroup().addTo(mapo);

    mapo.on('dragend', getData);
    mapo.on('zoomend', getData);

    mapo.on('locationfound', onLocationFound);
    mapo.locate({setView: true, maxZoom: 10});

    getData();

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
    mapo.locate({setView: true, maxZoom: 6});

    $("#loko").hide();

    var lat = $("[id$='lat']").val();
    var long = $("[id$='long']").val();
    if (lat || long) {
        mapo.setView([lat, long]);
        var marker = L.marker([lat, long], {
                draggable:true
        }).addTo(mapo);
        $("#loko").show();
    }
    else {
        mapo.setView([40,0],2);
        var marker = L.marker([40,0], {
                draggable:true,
                opacity:0
        }).addTo(mapo);
    }

    function setPositionFields(latlng) {
        $("[id$='lat']").val(latlng.lat);
        $("[id$='long']").val(latlng.lng);
    };

    function setAddressFields(latlng) {
        var baseURL = 'http://nominatim.openstreetmap.org/reverse?format=json&accept-language=eo';
        $.getJSON(baseURL+'&lat='+latlng.lat+'&lon='+latlng.lng,
            function(data){
                var d = data['address'];
                if ('county' in d)        {var urbo = d['county'];}
                if ('neighbourhood' in d) {var urbo = d['neighbourhood'];}
                if ('hamlet' in d)        {var urbo = d['hamlet'];}
                if ('village' in d)       {var urbo = d['village'];}
                if ('town' in d)          {var urbo = d['town'];}
                if ('city' in d)          {var urbo = d['city'];}

                $("[id$='urbo']").val(urbo);
                $("[id$='posxtkodo']").val(d['postcode'].split(";")[0]);
                $("[id$='lando']").val(d['country_code'].toUpperCase());
                
                $("#loko").show();
            });
    };

    function zoomToCity(data) {
        var NE = [data.boundingbox[0], data.boundingbox[2]];
        var SW = [data.boundingbox[1], data.boundingbox[3]];
        mapo.fitBounds([NE, SW]);
        // marker.setLatLng([data.lat, data.lon]).setOpacity(1);
    };

    function setCityOnMap(city, country) {
        $(".atendilo").show();
        var baseURL = 'http://nominatim.openstreetmap.org/search?format=json&q=';
        $.getJSON(baseURL+city+', '+country)
        .done(function(data){
            if (data.length > 0) {
                var d = data[0];  // Nur uzas la unua rezulto
                zoomToCity(d);
            }
            if (data.length == 0 && country != '') {
                setCityOnMap(city, '');
            }
            if (data.length == 0 && country == '') {
                $("#urbo-ne-trovita").show();
            }
            $(".atendilo").hide();
        });
    };

    function onMapClick(e) {
        setPositionFields(e.latlng);
        setAddressFields(e.latlng);
        marker.setLatLng(e.latlng).setOpacity(1);
        mapo.setView(e.latlng, mapo.getZoom()+2);  /* Center and Zoom x2 */
    };

    function onMarkerDrag(e) {
        setPositionFields(e.target.getLatLng());
        setAddressFields(e.target.getLatLng());
    };

    marker.on('dragend', onMarkerDrag);
    mapo.on('click', onMapClick);
    $("#urbo-sercxo").click(function(e) {
        e.preventDefault();
        $("#urbo-ne-trovita").hide();
        setCityOnMap(
            $("[id$='urbo']").val(),
            $("[id$='lando'] option:selected").text()
        );
    });
};
