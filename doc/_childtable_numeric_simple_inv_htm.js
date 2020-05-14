// Child table for section numeric_simple_inv
document.write('\
<select onchange="numeric_simple_inv_child(this)">\
<option>numeric_simple_inv-&gt;</option>\
<option>numeric_simple_inv_xam.py</option>\
</select>\
');
function numeric_simple_inv_child(item)
{	var child_list = [
		'numeric_simple_inv_xam.py.htm'
	];
	var index = item.selectedIndex;
	item.selectedIndex = 0;
	if(index > 0)
		document.location = child_list[index-1];
}
