
$(function() {
    $("form[name='registration']").validate({
        rules: {

            username: {
                required: true,
            },
            first_name:{
                required: true,
            },
            last_name:{
                required: true,
            },
            email:{
                required: true,
                email: true,
            },
            password1: {
                required: true,
            },
            password2:{
                required:true,
            }
        },
        messages: {
            username: {
                required: "Please enter username",
            },
            first_name:{
                required: "Please enter first name",
            },
            last_name:{
                required: "Please enter last name",
            },
            email:{
                required: "Please enter email",
                email: "Please enter valid email",
            },
            password1: {
                required: "Please enter password",
            },
            password2:{
                required:"Please enter password",
            },
            password: {
                required: "Please enter password",

            }

        },
        submitHandler: function(form) {
            form.submit();
        }
    });
});


