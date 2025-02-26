<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $videoUrl = $_POST['videoUrl'];
    $output = downloadVideo($videoUrl);
    echo $output;
}

function downloadVideo($videoUrl) {
    // Escape the video URL for safety in shell command
    $escapedVideoUrl = escapeshellarg($videoUrl);

    // Set the command to download video using youtube-dl
    $command = "youtube-dl {$escapedVideoUrl}";

    // Execute the command and capture output
    exec($command, $output, $returnCode);

    // Print output and return code for debugging
    var_dump($output);
    var_dump($returnCode);

    // Check if download was successful
    if ($returnCode === 0) {
        return "Video downloaded successfully.";
    } else {
        return "Error downloading video.";
    }
}
?>
