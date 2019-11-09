$(function(){
    $("#search_btn").click(function () {
        q = $( "#search" ).val();
        if (q!=''){
            var s = 'search_photos/'
            $.get(s, {'q': q}).done(function (data) {
                var elements = $();
                $.each(data['photos_url'], function(index, value) {
                    var res = '<button type="button" src=' + value + ' onclick="document.getElementById(\'id_photo_url\').value=\'' + value + '\'"; return false;" style="background-image: url(' + value + '); background-size: cover; height: 90px; width: 160px; border: 0px;border-radius: 10px;"/> </button>'
                    console.log(value);
                    elements = elements.add(res);
                })
                $('#results').html(elements);

            });
        }
        else {
            
        }
        
    });
});