/* global Swal */

$(document).ready(function () {

    $("tr #agregarUsuarios").click(function () {
        Swal.fire({
            title:  'DATOS DE SERVICIOS',

            html:   '<div class="input-group mb-3">' +
                        '<span class="input-group-text">Nombre</span>' +
                        '<input type="text" id="nombre" class="form-control" required>' +
                    '</div>',
                    
            allowOutsideClick: false,
            showCancelButton: true,
            confirmButtonText: 'Guardar',
            cancelButtonText: 'Cancelar',
            dangerMode: true,

            preconfirm: () => {
                const nombre = Swal.getPopup().querySelector('#nombre').value
            }         

        }).then((result) => {

            if (result.isConfirmed) {
                $.ajax({
                    type: 'POST',
                    url: '/equipos/',
                    
                    data: {
                        'nombre': nombre
                    },
                    
                    success: function () {
                        Swal.fire({
                            title: 'Nombre=${nombre}'
                        })
                    }
                })
                
            } else {
                Swal.fire("¡Registro no guardado!")
            }
        });
    });
})