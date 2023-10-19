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

    $("tr #agregarServicios").click(function () {
        
        Swal.fire({
            title:  'Datos de Servicios',

            html:   '<div class="input-group mb-3">' +
                        '<span class="input-group-text">Nombre</span>' +
                        '<input type="text" id="nombre" class="form-control" required>' +
                    '</div>',
                    
            focusConfirm: false,
            allowOutsideClick: false,
            showCancelButton: true,
            confirmButtonText: "Guardar",
            cancelButtonText: "Cancelar",
            dangerMode: true,

            preConfirm: () => {
                const nombre = Swal.getPopup().querySelector('#nombre').value

                if (!nombre) {
                    Swal.showValidationMessage('¡Ingrese datos por favor!')
                }
                return { nombre }
            }

        }).then((result) => {
            if (result.isConfirmed) {
                $.ajax({
                    type: 'POST',
                    url: '/administrador/agregarServicios',
                    
                    data: {
                        nombre: result.value.nombre,
                    },

                    beforeSend: function(xhr, settings) {
                        if (!this.crossDomain) {
                            xhr.setRequestHeader("X-CSRFToken", csrftoken);
                        }
                    },
                    
                    success: function () {
                        Swal.fire('Servicio registrado', 'El servicio se ha registrado con éxito.', 'success');
                    },

                    error: function() {
                        Swal.fire('Error', 'Hubo un problema al registrar el servicio. Inténtalo de nuevo.', 'error');
                    }
                });
                
            } else {
                Swal.fire("¡Registro no guardado!");
            }
        })

    });
})