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
// Validating From field for Special characters and Some Constraints using Jquery
$.validator.addMethod("lettersonly", function(value, element) {
  return this.optional(element) || /^[a-z]+$/i.test(value);
}, "Letters only please"); 

$.validator.addMethod("loginRegex", function(value, element) {
  return this.optional(element) || /^[a-z0-9]+$/i.test(value);
}, "Should not contain special characters");

$.validator.addMethod('checkemail', function(value, element) {
  var re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
  return re.test(value);
}, 'Please enter a valid email address')

$.validator.addMethod("emailnotequal", function(value, element, param) {
  return this.optional(element) || value != $(param).val();
 }, "alternative_email and email should not be the same");

 $.validator.addMethod("mobnotequal", function(value, element, param) {
  return this.optional(element) || value != $(param).val();
 }, "alternative_mobile_no and mobile_no should not be the same");

 $.validator.addMethod("landlinenotequal", function(value, element, param) {
  return this.optional(element) || value != $(param).val();
 }, "alternative_landline_no and landline_no should not be the same");

$('#seller_form').validate({
  rules: {
    first_name:{
      required:true,
      lettersonly:true,
      minlength:2,
    },
    last_name:{
      required:true,
      lettersonly:true,
      minlength:2,
    },
    promoter_first_name:{
      required:true,
      lettersonly:true,
      minlength:2,
    },
    promoter_last_name:{
      required:true,
      lettersonly:true,
      minlength:2,
    },
    company:{
      required:true,
    },
    designation:{
      required:true,
    },
    address_building:{
      required:true,
    },
    address_area:{
      required:true,
    },
    landmark:{
      required:true,
    },
    locality:{
      required:true,
    },
    city:{
      required:true,
      lettersonly:true,
    },
    state:{
      required:true,
      lettersonly:true,
    },
    country:{
      required:true,
      lettersonly:true,
    },
    pincode:{
      required:true,
      minlength:6,
    },
    gstin:{
      required:true,
      minlength:15,
      loginRegex:true,
    },
    company_website:{
      required:true,
    },
    mobile:{
      required:true,
      minlength:10,
      mobnotequal:"#alternative_mobile",
    },
    alternative_mobile:{
      required:true,
      minlength:10,
      mobnotequal:"#mobile",
    },
    alternative_email:{
      required:true,
      minlength:10,
      checkemail:true,
      emailnotequal:"#email",
    },
    landline_no:{
      required:true,
      landlinenotequal:"#alternative_landline_no",
    },
    alternative_landline_no:{
      required:true,
      landlinenotequal:"#landline_no",
    },
    about_me:{
      required:true,
    }

  }
});

// Validating Business Profile Form
// Validating From field for Special characters and Some Constraints using Jquery

$('#business_profile').validate({
  rules: {
    comapny_name:{
      required:true,
      minlength:2,
    },
    year_of_est:{
      required:true,
      
      
    },
    add_contact_name:{
      required:true,
      minlength:2,
      
    },
    annual_turn:{
      required:true,
    },
    company_card_front:{
      required:true,
    
    },
    company_card_back:{
      required:true,
     
    }
  }
});


// Validating Satutory_form
// Validating From field for Special characters and Some Constraints using Jquery

$("#satutory_form").validate({
  rules:{
    gst_no:{
      required:true,
      minlength:15,
      loginRegex:true,
    },
    pan_no:{
      required:true,
      minlength:10,
      loginRegex:true,
    },
    tan_no:{
      required:true,
      minlength:10,
      loginRegex:true,
    },
    cin_no:{
      required:true,
    },
    dgft_ie_code:{
      required:true,
    },
    company_registration_no:{
      required:true,
    },
  }
});



// Validating Bank Details
// Validating From field for Special characters and Some Constraints using Jquery

$('#Bank_detail').validate({
  rules: {
    bank_name:{
      required:true,
      minlength:3,
    },
    account_no:{
      required:true,
      loginRegex:true,
      
    },
    bank_account_name:{
      required:true,
      minlength:2,
      
    },
    ifsc_code:{
      required:true,
    },
    account_type:{
      required:true,
    
    },
    alternative_bank_name:{
      required:true,
      minlength:3,
     
    },
    alternative_account_no:{
      required:true,
      loginRegex:true,
    
    },
    alternative_bank_account_name:{
      required:true,
      minlength:2,
     
    },
    alternative_bank_ifsc_code:{
      required:true,
    
    },
    alternative_bank_account_type:{
      required:true,
     
    }
  }
});

// Validating Add_products-Detils
// Validating From field for Special characters and Some Constraints using Jquery

$('#add_product').validate({
  rules: {
    inlineRadioOptions1:{
      required:true,
    },
    is_available:{
      required:true,
    },
    product_group:{
      required:true,
    },

    inlineRadioOptions2:{
      required:true,
    },
    inlineRadioOptions3:{
      required:true,
    },
    Product_name:{
      required:true,
      minlength:2,
    },
    color:{
      required:true,
    },
    price:{
      required:true,
    },
    unity_type:{
      required:true,
    },
    min_order_qty:{
      required:true,
    },
    product_grp:{
      required:true,
    },
    desc:{
      required:true,
    },
    packing_details:{
      required:true,
    },
    size:{
      required:true,
    },

    capacity:{
      required:true,
    },
    brandd:{
      required:true,
    },
    mat:{
      required:true,
    },
    product_type:{
      required:true,
    },
    power:{
      required:true,
    },
    warranty:{
      required:true,
    },
    model_no:{
      required:true,
    },
    rating:{
      required:true,
    },
    neck_size:{
      required:true,
    },
    closure_type:{
      required:true,
    },
    product_code:{
      required:true,
    },
    video_url:{
      required:true,

    image1:{
      required:true,
    },
    image2:{
      required:true,
    },
    image3:{
      required:true,
    },

    mat_radio:{
      required:true,
    },
    inlineRadioOptions:{
      required:true,
    },
    cap_radio:{
      required:true,
    },
    product_group:{
      required:true,
    }
  }
});
