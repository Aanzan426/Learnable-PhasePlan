const startDate = new Date("YYYY-MM-DD HH:MM:SS"); 
let forcedMode = false;


const text = "Hey... I made something for you (lots of kisses)";
let i = 0;
let attempts = 0;

// typing intro
function type(){
    if(i < text.length){
        document.getElementById("text").innerHTML += text.charAt(i);
        i++;
        setTimeout(type, 60);
    }
}
type();

function start(){
    document.getElementById("enterBtn").style.display="none";
    document.getElementById("question").classList.remove("hidden");
}

function correct(){
    document.getElementById("question").classList.add("hidden");
    document.getElementById("proposal").classList.remove("hidden");
    updateTimer();
    setInterval(updateTimer, 60000);
}

function wrong(){
    alert("Wrong answer 😤");
}

function updateTimer(){
    const now = new Date();
    let diff = Math.floor((now - startDate) / 1000);

    const days = Math.floor(diff / (3600 * 24));
    diff %= (3600 * 24);
    const hours = Math.floor(diff / 3600);
    diff %= 3600;
    const minutes = Math.floor(diff / 60);

    document.getElementById("timer").innerHTML =
        `We've been together for: <br>
         <strong>${days}</strong> days 
         <strong>${hours}</strong> hours 
         <strong>${minutes}</strong> minutes`;
}

// RUNNING NO BUTTON
document.addEventListener("mousemove", function(e){
    const no = document.getElementById("no");
    if(!no) return;

    const rect = no.getBoundingClientRect();
    const dist = Math.hypot(e.clientX - rect.x, e.clientY - rect.y);

    if(dist < 120){
        no.style.position = "absolute";
        no.style.left = Math.random() * (window.innerWidth - 100) + "px";
        no.style.top = Math.random() * (window.innerHeight - 50) + "px";

        attempts++;

        if(attempts === 5){
    		alert("Playing hard to get eh!... nice... I like that spirit 😏");
	}

	if(attempts === 10){
    		forcedMode = true;

    		document.body.innerHTML = `
        		<div id="forceScreen" style="
            			background:black;
            			color:white;
            			height:100vh;
            			display:flex;
            			align-items:center;
            			justify-content:center;
            			font-family:Arial;
            			text-align:center;
            			padding:20px;
        		">
           			 <h1>Do you even have a choice baby 😌❤️???<br><br><small>(tap anywhere)</small></h1>
        		</div>
    		`;
    		document.addEventListener("click", returnToQuestion, { once:true });
	}
    }
});

function yes(){
    window.location.href = "answer.php?response=yes";
}

function returnToQuestion(){
    document.body.innerHTML = `
    <div class="container">
        <h1>Ms. Sariah Fletcher... Will you be my Valentine?</h1>
        <button id="yes" onclick="yes()">YES ❤️</button>
    </div>
    `;
}
