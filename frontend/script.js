const API = " http://127.0.0.1:5000";
let currentUser = "";

// Load movies
fetch(API + "/movies")
.then(res => res.json())
.then(data => {
    let select = document.getElementById("movieSelect");
    data.forEach(m => {
        let option = document.createElement("option");
        option.value = m;
        option.text = m;
        select.appendChild(option);
    });
});

function register() {
    fetch(API + "/register", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            username: username.value,
            password: password.value
        })
    }).then(res => res.json()).then(alert);
}

function login() {
    fetch(API + "/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            username: username.value,
            password: password.value
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message || data.error);
        if (data.message) {
            currentUser = username.value;
            loadHistory();
        }
    });
}

function recommend() {
    let movie = movieSelect.value;

    fetch(API + "/recommend", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            movie: movie,
            username: currentUser
        })
    })
    .then(res => res.json())
    .then(data => {
        results.innerHTML = "";
        data.recommendations.forEach(m => {
            results.innerHTML += `<div class="movie">${m}</div>`;
        });
    });
}

function loadHistory() {
    fetch(API + "/history/" + currentUser)
    .then(res => res.json())
    .then(data => {
        history.innerHTML = "";
        data.forEach(m => {
            history.innerHTML += `<div class="movie">${m}</div>`;
        });
    });
}