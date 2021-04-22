

// require('jquery-validation');
$.validator.addMethod('strongPassword', function(value, element) {
    var re = /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z]).{6,}$/;
    return re.test(value);
  }, 'Your password must be at least 6 characters long and contain at least one number, one char and one special character.\'.')

$.validator.addMethod('checkemail', function(value, element) {
var re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
return re.test(value);
}, 'Please enter a valid email address')

$.validator.addMethod("lettersonly", function(value, element) {
return this.optional(element) || /^[a-z]+$/i.test(value);
}, "Letters only please"); 


$("#register").validate({
    rules:{
        first_name:{
            required:true,
            minlength:2,
            // nowhitespace: true,
            lettersonly: true,
        },
        last_name:{
            required:true,
            nowhitespace: true,
            lettersonly: true,
        },
        email:{
            required:true,
            checkemail:true,
        },
        mobile:{
            required:true,
            digits: true,
            minlength:10,
            maxlength:10,
        },
        state:{
            required:true,
            lettersonly: true,
        },
        pincode:{
            required:true,
            digits:true,
            minlength:6,
            maxlength:6,
        },
        business_type:{
            required: true ,
        },
        company_name:{
            required:true
        },
        nature_of_business:{
            required:true,
        },
        password1:{
            required:true,
            minlength:6,
            strongPassword:true,
        },
        password2:{
            required:true,
            // minlength:6,
            equalTo: "#id_password1",
        },
    },
    messages:{
        password2:{
            equalTo: 'password and confirm password must be same',
        },
        first_name:{
            nowhitespace:'white spaces not allowed',
        },
        pincode:{
            minlength:'Invalid pincode',
            maxlength:'Invalid pincode',
        },
        mobile:{
            minlength:'Invalid mobile number',
            maxlength:'Invalid mobile number',
        },
    }
});
