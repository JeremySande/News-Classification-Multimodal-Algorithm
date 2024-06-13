<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $headline = $_POST["headline"];
    $image = $_FILES["image"];

    // Directory to upload images
    $uploadDirectory = "uploads/";
    // Create directory if it doesn't exist
    if (!is_dir($uploadDirectory)) {
        mkdir($uploadDirectory, 0777, true);
    }
    $imagePath = $uploadDirectory . basename($image["name"]);

    // Move uploaded file to the server
    if (move_uploaded_file($image["tmp_name"], $imagePath)) {
        // Call Python script for classification
        $command = escapeshellcmd("python3 classify_news.py " . escapeshellarg($headline) . " " . escapeshellarg($imagePath));
        $output = shell_exec($command);

        // Display result
        echo "<h2>Classification Result:</h2>";
        echo "<pre>$output</pre>";
    } else {
        echo "Failed to upload image.";
    }
}
?>
