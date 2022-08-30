(function() {
  const $latField = $('#id_lat_lavoura');
  const $lonField = $('#id_lon_lavoura');
  const $dataField = $('#data_colheita');
  const $eventoField = $('#id_evento');
  let encontrado = false;

  $(":input").on('blur', function(){
    $.ajax({
      url: $('.container-data').data('url'),
      type: 'GET',
      dataType: 'json',
      success: function(resp) {
        let distancia = 0;
        resp.forEach((item) => {
          if (!encontrado) {
            if ($dataField.val() == item.data_colheita
                  && $eventoField.val() != item.evento
                  && $eventoField.val() != "") {
              distancia = distance($latField.val(),
                           $lonField.val(),
                           item.lat_lavoura,
                           item.lon_lavoura, "K")
              if (distancia < 10) {
                encontrado = true;
                $.confirm({
                  title: 'Alerta!',
                  content: 'Já existe uma confirmação de perda, com evento divergente, cadastrada neste dia em um raio de menos de 10km.',
                  type: 'red',
                  typeAnimated: true,
                  columnClass: 'col-6',
                  buttons: {
                    tryAgain: {
                      text: 'Continuar mesmo assim',
                      btnClass: 'btn-red',
                      action: function(){
                      }
                    },
                  }
                });
              }
            }
          }
        })
      }
    });
  });

  // função para calcular as distâncias (GeoDataSource.com)
  function distance(lat1, lon1, lat2, lon2, unit) {
    if ((lat1 == lat2) && (lon1 == lon2)) {
        return 0;
    }
    else {
        var radlat1 = Math.PI * lat1/180;
        var radlat2 = Math.PI * lat2/180;
        var theta = lon1-lon2;
        var radtheta = Math.PI * theta/180;
        var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
        if (dist > 1) {
            dist = 1;
        }
        dist = Math.acos(dist);
        dist = dist * 180/Math.PI;
        dist = dist * 60 * 1.1515;
        if (unit=="K") { dist = dist * 1.609344 }
        if (unit=="N") { dist = dist * 0.8684 }
        return dist;
    }
  }

}())
