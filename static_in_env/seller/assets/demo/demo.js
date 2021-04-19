demo = {
  initDocumentationCharts: function() {
    if ($('#dailySalesChart').length != 0 && $('#websiteViewsChart').length != 0) {
      /* ----------==========     Daily Sales Chart initialization For Documentation    ==========---------- */

      dataDailySalesChart = {
        labels: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
        series: [
          [12, 17, 7, 17, 23, 18, 38]
        ]
      };

      optionsDailySalesChart = {
        lineSmooth: Chartist.Interpolation.cardinal({
          tension: 0
        }),
        low: 0,
        high: 50, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
        chartPadding: {
          top: 0,
          right: 0,
          bottom: 0,
          left: 0
        },
      }

      var dailySalesChart = new Chartist.Line('#dailySalesChart', dataDailySalesChart, optionsDailySalesChart);

      var animationHeaderChart = new Chartist.Line('#websiteViewsChart', dataDailySalesChart, optionsDailySalesChart);
    }
  },

  initDashboardPageCharts: function() {

    if ($('#dailySalesChart').length != 0 || $('#completedTasksChart').length != 0 || $('#websiteViewsChart').length != 0) {
      /* ----------==========     Daily Sales Chart initialization    ==========---------- */

      dataDailySalesChart = {
        labels: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
        series: [
          [12, 17, 7, 17, 23, 18, 38]
        ]
      };

      optionsDailySalesChart = {
        lineSmooth: Chartist.Interpolation.cardinal({
          tension: 0
        }),
        low: 0,
        high: 50, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
        chartPadding: {
          top: 0,
          right: 0,
          bottom: 0,
          left: 0
        },
      }

      var dailySalesChart = new Chartist.Line('#dailySalesChart', dataDailySalesChart, optionsDailySalesChart);

      md.startAnimationForLineChart(dailySalesChart);



      /* ----------==========     Completed Tasks Chart initialization    ==========---------- */

      dataCompletedTasksChart = {
        labels: ['12p', '3p', '6p', '9p', '12p', '3a', '6a', '9a'],
        series: [
          [230, 750, 450, 300, 280, 240, 200, 190]
        ]
      };

      optionsCompletedTasksChart = {
        lineSmooth: Chartist.Interpolation.cardinal({
          tension: 0
        }),
        low: 0,
        high: 1000, // creative tim: we recommend you to set the high sa the biggest value + something for a better look
        chartPadding: {
          top: 0,
          right: 0,
          bottom: 0,
          left: 0
        }
      }

      var completedTasksChart = new Chartist.Line('#completedTasksChart', dataCompletedTasksChart, optionsCompletedTasksChart);

      // start animation for the Completed Tasks Chart - Line Chart
      md.startAnimationForLineChart(completedTasksChart);


      /* ----------==========     Emails Subscription Chart initialization    ==========---------- */

      var dataWebsiteViewsChart = {
        labels: ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D'],
        series: [
          [542, 443, 320, 780, 553, 453, 326, 434, 568, 610, 756, 895]

        ]
      };
      var optionsWebsiteViewsChart = {
        axisX: {
          showGrid: false
        },
        low: 0,
        high: 1000,
        chartPadding: {
          top: 0,
          right: 5,
          bottom: 0,
          left: 0
        }
      };
      var responsiveOptions = [
        ['screen and (max-width: 640px)', {
          seriesBarDistance: 5,
          axisX: {
            labelInterpolationFnc: function(value) {
              return value[0];
            }
          }
        }]
      ];
      var websiteViewsChart = Chartist.Bar('#websiteViewsChart', dataWebsiteViewsChart, optionsWebsiteViewsChart, responsiveOptions);

      //start animation for the Emails Subscription Chart
      md.startAnimationForBarChart(websiteViewsChart);
    }
  },

  initGoogleMaps: function() {
    var myLatlng = new google.maps.LatLng(40.748817, -73.985428);
    var mapOptions = {
      zoom: 13,
      center: myLatlng,
      scrollwheel: false, //we disable de scroll over the map, it is a really annoing when you scroll through page
      styles: [{
        "featureType": "water",
        "stylers": [{
          "saturation": 43
        }, {
          "lightness": -11
        }, {
          "hue": "#0088ff"
        }]
      }, {
        "featureType": "road",
        "elementType": "geometry.fill",
        "stylers": [{
          "hue": "#ff0000"
        }, {
          "saturation": -100
        }, {
          "lightness": 99
        }]
      }, {
        "featureType": "road",
        "elementType": "geometry.stroke",
        "stylers": [{
          "color": "#808080"
        }, {
          "lightness": 54
        }]
      }, {
        "featureType": "landscape.man_made",
        "elementType": "geometry.fill",
        "stylers": [{
          "color": "#ece2d9"
        }]
      }, {
        "featureType": "poi.park",
        "elementType": "geometry.fill",
        "stylers": [{
          "color": "#ccdca1"
        }]
      }, {
        "featureType": "road",
        "elementType": "labels.text.fill",
        "stylers": [{
          "color": "#767676"
        }]
      }, {
        "featureType": "road",
        "elementType": "labels.text.stroke",
        "stylers": [{
          "color": "#ffffff"
        }]
      }, {
        "featureType": "poi",
        "stylers": [{
          "visibility": "off"
        }]
      }, {
        "featureType": "landscape.natural",
        "elementType": "geometry.fill",
        "stylers": [{
          "visibility": "on"
        }, {
          "color": "#b8cb93"
        }]
      }, {
        "featureType": "poi.park",
        "stylers": [{
          "visibility": "on"
        }]
      }, {
        "featureType": "poi.sports_complex",
        "stylers": [{
          "visibility": "on"
        }]
      }, {
        "featureType": "poi.medical",
        "stylers": [{
          "visibility": "on"
        }]
      }, {
        "featureType": "poi.business",
        "stylers": [{
          "visibility": "simplified"
        }]
      }]

    };
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

    var marker = new google.maps.Marker({
      position: myLatlng,
      title: "Hello World!"
    });

    // To add the marker to the map, call setMap();
    marker.setMap(map);
  }

}

// Validating Seller Contact form
function validateformsellercontact()
{
  // Checking aboutme field is null or empty
    var about=document.sellercontact.about_me.value;
    if(about==null || about=="")
    {
        alert("About_me can't be blank");
        return false;
    }

    // Validating From field for Special characters and Some Constraints
    var Regex = "[@_!#$%^&*()<>?/\|}{~:]";
    var validfirstname=document.sellercontact.first_name.value.match(Regex);
    if(validfirstname!=null)
    {
      alert("first_name should not contain special characters");
      return false;
    }
    var validlastname=document.sellercontact.last_name.value.match(Regex);
    if(validlastname!=null)
    {
      alert("last_name should not contain special characters");
      return false;
    }
    var promoter_first_name=document.sellercontact.promoter_first_name.value.match(Regex);
    if(promoter_first_name!=null)
    {
      alert("promoter_first_name should not contain special characters");
      return false;
    }
    var promoter_last_name=document.sellercontact.promoter_last_name.value.match(Regex);
    if(promoter_last_name!=null)
    {
      alert("promoter_last_name should not contain special characters");
      return false;
    }
    var designation=document.sellercontact.designation.value.match(Regex);
    var designation1=document.sellercontact.designation.value;
    if(designation!=null)
    {
      alert("designation should not contains special characters");
      return false;
    }
    if(typeof designation1==="number"){
      alert("Please enter a correct designation");
      return false;
    }
    var address_area=document.sellercontact.address_area.value.match(Regex);
    if(address_area!=null)
    {
      alert("address_area should not contains special characters");
      return false;
    }
    var landmark=document.sellercontact.landmark.value.match(Regex);
    var locality=document.sellercontact.locality.value.match(Regex);
    if(landmark!=null ||locality!=null )
    {
      alert("landmark or locality should not contains special characters");
      return false;
    }
    var city=document.sellercontact.city.value.match(Regex);
    var state=document.sellercontact.state.value.match(Regex);
    if(city!=null ||state!=null )
    {
      alert("city or state should not contains special characters");
      return false;
    }
    var country=document.sellercontact.country.value.match(Regex);
    if(country!=null)
    {
      alert("country should not contains special characters");
      return false;
    }
    var pincode=document.sellercontact.pincode.value;
    if(pincode.length!=6)
    {
      alert("Pincode should only contain 6 digit number");
      return false;
    }
    var gstin=document.sellercontact.gstin.value.match(Regex);
    if(gstin!=null)
    {
      alert("gstin should not contains special characters");
      return false;
    }
    var gstin=document.sellercontact.gstin.value;
    if(gstin.length!=15)
    {
      alert("Invalid GSTIN");
      return false;
    }
    var mobile=document.sellercontact.mobile.value;
    if(mobile.length!=10){
      alert("Invalid Mobile Number..")
      return false;
    }
    var alternative_mobile=document.sellercontact.alternative_mobile.value;
    if(alternative_mobile.length!=10){
      alert("Invalid alternative_mobile..")
      return false;
    }
    var landline_no=document.sellercontact.landline_no.value;
    if(landline_no.length>15){
      alert("Invalid landline_no..")
      return false;
    }
    var alternative_landline_no=document.sellercontact.alternative_landline_no.value;
    if(alternative_landline_no.length>15){
      alert("Invalid alternative_landline_no..")
      return false;
    }
}