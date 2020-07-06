function delNote(x){
	if(confirm("are you sure you want to delete this note")){
		location.href='/delete/'+x;
	}
}
$(document).ready(function(){
});