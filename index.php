<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" type="text/css" href="styles.css">
<title>Capteur de Distance</title>
</head>
<body>
<section class="container">
<h1>Capteur de Distance</h1>
<?php
// URL de l'API (endpoint : /distance)
$API_URL = "http://localhost:5000/distance";
// Récupération des données de l'API
$json = file_get_contents($API_URL);
$data = json_decode($json, true);
echo "<p><span>{$data['distance_cm']}</span> cm</p>";
echo "<p id='mesure'>Mesure n° <span>{$data['numero']}</span></p>";
?>
</section>
<button onclick="window.location.reload()">Rafraîchir</button>
</body>
</html>