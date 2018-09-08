$('volume').click(Hemorrage(request)) {
    $.ajax({
        url: emergency.html,
        method: 'POST',
        data: {
            name: value, 
            click: true
        }
        success: function (data) {
            // success callback
            // you can process data returned by function from views.py
        }
    });
});