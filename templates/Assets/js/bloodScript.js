$('volume').click(function() {
    $.ajax({
        url: "localhost:63342/bleeding",
        method: 'POST',
        data: {
            name: value,
            click: true
        },
        success: function (data) {
            alert("hello world")
            //localhost/Hemorrage(request);
        }
    });
});