//site.stateCd
//userCompany.stateCd

$(document).ready(function(){


  	$("#countryCd").change(function(){searchStates()});

});
function searchStates(state){
	var country = document.getElementById("countryCd");
	var temp = country.options[country.selectedIndex].value;
	var param = 'company.country_cd=' + temp+"&random="+Math.random();
	$.ajax({
		type:"post",
		url:"accountAction_searchStates_User.action",
		data:param,
	    dataType:"json",
		success: function(data) {
			if(data!=null && data.length>0){
				var isSelected="";
				var stateCd = "<select id=stateCd name=company.state_cd >";
				for (i=0; i< data.length;i++) {
					if(data[i].cd==state){
							isSelected="selected";
					}
					stateCd  = stateCd+"<option id='"+data[i].cd+"' value='"+data[i].cd+"' "+isSelected;
					stateCd +=" >"+data[i].name;
					stateCd +="</option>\n";
					isSelected="";
				}
				stateCd = stateCd + "</select>";
				document.getElementById("search").innerHTML = stateCd;
			}else{
				alert('<s:text name="PRF_NO_STATES_FOR_YOUR_CHOICE"/>');
				var stateCd = "<select id=stateCd name=company.state_cd >";
				stateCd +="</option>\n";
				document.getElementById("search").innerHTML = stateCd;
			}
		},
		error: function(data) {
		}
	});
}