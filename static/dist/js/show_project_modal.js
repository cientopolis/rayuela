function showModal(name, description, image,id) {
    $('#myModal .modal-title').html(name)
    $('#myModal .project_img').attr('src', image)
    $('#myModal .description').html(description)
    $('#myModal .id').attr('value',id)
    $('#myModal').modal()
  }