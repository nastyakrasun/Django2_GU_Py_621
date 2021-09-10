window.onload = function() {
    console.log(.basket_list)
	$('.basket_list').on( types: 'click', selector: 'input[type="number"]', data: function() {
		var t_href = event.target;
//		console.log(t_href);
		$ajax( url: {
			url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",

			success:  function(data) {
 				$('.basket_list').html(data.result);
			},
		});
		event.preventDefault();
	});
}