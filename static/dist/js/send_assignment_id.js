function send_assignment_id(assignment_id,type,bool) {
    
    console.log(assignment_id);
    console.log(type);
    console.log(bool);

    if (bool){
        $("#assignment_bool").val(true);
    }
    else{
        $("#assignment_bool").val(false); 
    }
    $("#assignment_id").val(assignment_id);


    
    
    $.confirmation(type);
      
  }
