// Child table for section numeric_runge4_step
document.write('\
<select onchange="numeric_runge4_step_child(this)">\
<option>numeric_runge4_step-&gt;</option>\
<option>numeric_runge4_step_xam.py</option>\
</select>\
');
function numeric_runge4_step_child(item)
{	var child_list = [
		'numeric_runge4_step_xam.py.htm'
	];
	var index = item.selectedIndex;
	item.selectedIndex = 0;
	if(index > 0)
		document.location = child_list[index-1];
}
