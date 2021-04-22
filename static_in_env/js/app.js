
const cords = document.querySelector('#find-me');
// console.log(cords);


function geoFindMe() {

    const status = document.querySelector('#status');
    const mapLink = document.querySelector('#map-link');

    mapLink.href = '';
    mapLink.textContent = '';

    function success(position) {
        const latitude  = position.coords.latitude;
        const longitude = position.coords.longitude;

        status.textContent = '';
        mapLink.href = `https://www.openstreetmap.org/#map=18/${latitude}/${longitude}`;
        mapLink.textContent = `Latitude: ${latitude} °, Longitude: ${longitude} °`;
    }

    function error() {
        status.textContent = 'Unable to retrieve your location';
    }

    if(!navigator.geolocation) {
        status.textContent = 'Geolocation is not supported by your browser';
    } else {
        status.textContent = 'Locating…';
        navigator.geolocation.getCurrentPosition(success, error);
    }

}

// cords.addEventListener('click', geoFindMe);

$(window).scroll(function() {
    $('.fadedfx').each(function(){
    var imagePos = $(this).offset().top;

    var topOfWindow = $(window).scrollTop();
        if (imagePos < topOfWindow+500) {
            $(this).addClass("fadeIn");
        }
    });
});

// Side bar (Sort By Brand)

var count_brand=9; // Initialize a counter with 9
$('#sort_brand').click(function(e){
    for(var i=0;i<4;i++)
    {
        count_brand++;// Increment counter so that it will be used in further appended product id
        template=`<div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" id="brand${count_brand}">
                <label class="custom-control-label" for="brand${count_brand}">${count_brand}</label>
          </div>`
        $("#append_brand").append(template);
    }
    e.preventDefault();
    });

// Side bar (Sort by Category)

var count_cat=9;
$('#sort_cat').click(function(e){
    for(var i=0;i<4;i++)
    {
        count_cat++;
        template=`<div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" id="brand${count_cat}">
                <label class="custom-control-label" for="brand${count_cat}">${count_cat}</label>
          </div>`
        $("#append_cat").append(template);
    }
    e.preventDefault();
    });

 