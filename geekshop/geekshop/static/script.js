window.onload = function() {
	$('.basket_list').on( types: 'click', selector: 'input[type="number"]', data: function() {
		var t_href = event.target;
		$ajax( url: {
			url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",

			success:  function(data) {
 				$('.basket_list').html(data.result);
			},
		});
		event.preventDefault();
	});
}