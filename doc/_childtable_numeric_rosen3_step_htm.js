// Child table for section numeric_rosen3_step
document.write('\
<select onchange="numeric_rosen3_step_child(this)">\
<option>numeric_rosen3_step-&gt;</option>\
<option>numeric_rosen3_step_xam.py</option>\
</select>\
');
function numeric_rosen3_step_child(item)
{	var child_list = [
		'numeric_rosen3_step_xam.py.htm'
	];
	var index = item.selectedIndex;
	item.selectedIndex = 0;
	if(index > 0)
		document.location = child_list[index-1];
}
