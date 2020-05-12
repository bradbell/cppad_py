// Child table for section numeric_seirwd_model
document.write('\
<select onchange="numeric_seirwd_model_child(this)">\
<option>numeric_seirwd_model-&gt;</option>\
<option>numeric_seirwd_model_xam.py</option>\
</select>\
');
function numeric_seirwd_model_child(item)
{	var child_list = [
		'numeric_seirwd_model_xam.py.htm'
	];
	var index = item.selectedIndex;
	item.selectedIndex = 0;
	if(index > 0)
		document.location = child_list[index-1];
}
