const form = document.getElementById("details");

form.addEventListener('submit', function(event)){
	const usern = document.getElementById("username").value.trim();
	const pass = document.getElementById("password").value.trim();

	if(usern === '' pass === ''){
		alert("Fields cannot be empty");
		event.preventDefault();
		return;
	}

	if (usern.length < 8 || password.length < 8){
		alert("Credentials should be min 8 digits");
		event.preventDefault();
		return;
	}
});
	

	