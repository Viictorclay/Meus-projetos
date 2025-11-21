document.getElementById("menuBtn").addEventListener("click", function() {
    document.getElementById("sideMenu").classList.add("open");
});

document.getElementById("claseMenu").addEventListener("click", function() {
    document.getElementById("sideMenu").classList.remove("open");
});

// Fecha ao clicar fora
document.addEventListener("click", function(e) {
    let menu = document.getElementById("sideMenu");
    let btn = document.getElementById("menuBtn");

    if (!menu.contains(e.target) && !btn.contains(e.target)) {
        menu.classList.remove("open");
    }
});