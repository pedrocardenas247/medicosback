$(function () {

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-medicos").modal("show");
      },
      success: function (data) {
        $("#modal-medicos .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#medicos-table tbody").html(data.html_medicos_list);
          $("#modal-medicos").modal("hide");
        }
        else {
          $("#modal-medicos .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


   //CREATE
   //en el boton de create que se encuentra en medicos_list
  $(".js-create-medicos").click(loadForm);
  //en el form post  de partial_medicos_create
  $("#modal-medicos").on("submit", ".js-medico-create-form", saveForm);

  // ACTUALIZAR MEDICOS
  $("#medicos-table").on("click", ".js-update-medicos", loadForm);
  $("#modal-medicos").on("submit", ".js-medico-update-form", saveForm);

  //ELIMINAR MEDICOS
$("#medicos-table").on("click", ".js-delete-medicos", loadForm);
$("#modal-medicos").on("submit", ".js-medicos-delete-form", saveForm);

});