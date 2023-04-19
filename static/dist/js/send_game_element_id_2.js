function send_game_element_id_2(game_element_id,type) {
  
    if (type=='#modify'){
      $("#ge_id_").val(game_element_id);
    }
    else{
      $("#ge_id").val(game_element_id);
    }
    
    
    $.confirmation(type);
      
  }
