// Code volontairement mauvais pour test SonarQube

function add(a, b) {
    return a + b
}

// Fonction inutile jamais utilisée
function unusedFunction() {
    let x = 10;
    let y = 20;
    return x * y;
}

// Mot de passe en clair (grosse vulnérabilité)
let password = "123456";

// Comparaison toujours vraie (bug logique)
if (true == "true") {
    console.log("Bad logic here!");
}

// Code dupliqué
function duplicate1() {
    return add(1, 2);
}

function duplicate2() {
    return add(1, 2);
}
