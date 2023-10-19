/* global Swal */

$(document).ready(function () {

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    const csrftoken = getCookie('csrftoken');

    /****************************************************/

    $("tr #agregarTipo").click(function () {
        
        Swal.fire({
            title:  'Datos de Tipos de Equipos',

            html:   '<div class="input-group mb-3">' +
                        '<span class="input-group-text">Nombre</span>' +
                        '<input type="text" id="nombre" class="form-control" required>' +
                    '</div>' +
                    
                    '<div class="input-group mb-3">' +
                        '<input type="file" id="imagen" class="form-control">' +
                    '</div>',
                    
            focusConfirm: false,
            allowOutsideClick: false,
            showCancelButton: true,
            confirmButtonText: "Guardar",
            cancelButtonText: "Cancelar",
            dangerMode: true,

            preConfirm: () => {
                const nombre = Swal.getPopup().querySelector('#nombre').value;
                const imagen = Swal.getPopup().querySelector('#imagen').files[0]
                
                if (!nombre | !imagen) {
                    Swal.showValidationMessage('¡Ingrese datos por favor!')
                }
                return { nombre, imagen }
            }

        }).then((result) => {
            if (result.isConfirmed) {
                $.ajax({
                    type: 'POST',
                    url: '/administrador/agregarTipos',
                    
                    data: {
                        nombre: result.value.nombre,
                        imagen: result.value.imagen
                    },

                    processData: false,
                    contextType: false,

                    beforeSend: function(xhr, settings) {
                        if (!this.crossDomain) {
                            xhr.setRequestHeader("X-CSRFToken", csrftoken);
                        }
                    },
                    
                    success: function () {
                        Swal.fire('Tipo de equipo registrado', 'El Tipo de equipo se ha registrado con éxito.', 'success');
                    },

                    error: function() {
                        Swal.fire('Error', 'Hubo un problema al registrar el tipo de equipo. Inténtalo de nuevo.', 'error');
                    }
                });
                
            } else {
                Swal.fire("¡Registro no guardado!");
            }
        })

    });
})