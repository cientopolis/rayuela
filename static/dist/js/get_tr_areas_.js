console.log($('#id_project').val())
        $.ajax({
            url: /game_element_view/,
            type: 'POST',
            data: {
                'action': 'search_time_restriction_id',
                'id': $('#id_project').val()
            },
            dataType: 'json',
            
        }).done(function (data) {
            $.each(data[2], function (key, value) {
                let opt = document.createElement('option');
                opt.value = value.id;
                opt.innerHTML = 'Área '+value.number;
                document.getElementById('id_area').appendChild(opt);
            });   
                     
            viewInMap(data[2]);

           

        }).fail(function (jqXHR, textStatus, errorThrown) {
            viewInMap(null);
        })
    


