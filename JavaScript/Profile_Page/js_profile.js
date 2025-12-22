function addHobbyList() {
    const hobby_input = document.getElementById("hobby_id");
    const hobby_list = document.getElementById("hobby_list");

    const newItem = document.createElement("li");
    newItem.textContent = hobby_input.value;

    hobby_list.appendChild(newItem);

    hobby_input.value = "";
}

function updateCourse() {
    const course_update = document.getElementById("course");
    alert("Selected Course: " + course_update.value);
}

function changeColor() {
    const random_color = "#" + Math.floor(Math.random() * 16777215).toString(16);
    document.getElementById("profile_id").style.backgroundColor = random_color;
}
