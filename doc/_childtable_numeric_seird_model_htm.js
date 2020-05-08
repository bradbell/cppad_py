// Child table for section numeric_seird_model
document.write('\
<select onchange="numeric_seird_model_child(this)">\
<option>numeric_seird_model-&gt;</option>\
<option>numeric_seird_model_xam.py</option>\
</select>\
');
function numeric_seird_model_child(item)
{	var child_list = [
		'numeric_seird_model_xam.py.htm'
	];
	var index = item.selectedIndex;
	item.selectedIndex = 0;
	if(index > 0)
		document.location = child_list[index-1];
}
