


$(function () {


    function removeOptions(selectElement) {
        var i, L = selectElement.options.length - 1;
        for (i = L; i >= 0; i--) {
            selectElement.remove(i);
        }
    }
    $('#id_project').on('change', function () {

        removeOptions(document.getElementById('id_area'));
        removeOptions(document.getElementById('id_time_restriction'));
        var id = $(this).val();
        $.ajax({
            url: /game_element_view/,
            type: 'POST',
            data: {
                'action': 'search_time_restriction_id',
                'id': id
            },
            dataType: 'json',
        }).done(function (data) {
            if (!data.hasOwnProperty('error')) {
   
                $.each(data[0], function (key, value) {
                    let opt = document.createElement('option');
                    opt.value = value.id;
                    opt.innerHTML = value.name;
                    document.getElementById('id_time_restriction').appendChild(opt);
                });
                $.each(data[2], function (key, value) {
                    let opt = document.createElement('option');
                    opt.value = value.id;
                    opt.innerHTML = 'Área '+value.number;
                    document.getElementById('id_area').appendChild(opt);
                });    
               
                viewInMap(data[2]);

            }
            else{
              
            }

        }).fail(function (jqXHR, textStatus, errorThrown) {
            viewInMap(null);
        })
    });


});