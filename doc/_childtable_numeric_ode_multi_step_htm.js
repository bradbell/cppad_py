// Child table for section numeric_ode_multi_step
document.write('\
<select onchange="numeric_ode_multi_step_child(this)">\
<option>numeric_ode_multi_step-&gt;</option>\
<option>numeric_ode_multi_step_xam.py</option>\
</select>\
');
function numeric_ode_multi_step_child(item)
{	var child_list = [
		'numeric_ode_multi_step_xam.py.htm'
	];
	var index = item.selectedIndex;
	item.selectedIndex = 0;
	if(index > 0)
		document.location = child_list[index-1];
}
