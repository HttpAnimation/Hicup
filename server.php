<?php
$folder = $_GET['type'] === 'photos' ? 'photos' : ($_GET['type'] === 'videos' ? 'videos' : 'music');
$files = scandir($folder);

foreach ($files as $file) {
    if ($file !== '.' && $file !== '..') {
        $filePath = "$folder/$file";
        if ($_GET['type'] === 'videos') {
            // For videos, generate a video tag
            echo "<video controls width='640' height='360'><source src='$filePath' type='video/mp4'>Your browser does not support the video tag.</video>";
        } else if ($_GET['type'] === 'music') {
            // For music, generate an audio tag
            echo "<audio controls><source src='$filePath' type='audio/mp3'>Your browser does not support the audio tag.</audio>";
        } else {
            // For photos, generate an img tag
            echo "<img src='$filePath' style='max-width: 200px; margin: 10px;'>";
        }
    }
}
?>
