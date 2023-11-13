<?php
$folder = $_GET['type'] === 'photos' ? 'photos' : 'videos';
$files = scandir($folder);

foreach ($files as $file) {
    if ($file !== '.' && $file !== '..') {
        if ($_GET['type'] === 'videos') {
            // For videos, generate a video tag
            echo "<video controls width='640' height='360'><source src='$folder/$file' type='video/mp4'>Your browser does not support the video tag.</video>";
        } else {
            // For photos, generate an img tag
            echo "<img src='$folder/$file' style='max-width: 200px; margin: 10px;'>";
        }
    }
}
?>
