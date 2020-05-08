// Child table for section numeric_seirs_model
document.write('\
<select onchange="numeric_seirs_model_child(this)">\
<option>numeric_seirs_model-&gt;</option>\
<option>numeric_seirs_model_xam.py</option>\
</select>\
');
function numeric_seirs_model_child(item)
{	var child_list = [
		'numeric_seirs_model_xam.py.htm'
	];
	var index = item.selectedIndex;
	item.selectedIndex = 0;
	if(index > 0)
		document.location = child_list[index-1];
}
