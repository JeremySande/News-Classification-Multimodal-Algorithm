<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>News Classification</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        input[type="file"], input[type="text"], button {
            display: block;
            margin: 10px auto;
            padding: 10px;
            width: 80%;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
        button {
            background-color: #5cb85c;
            color: white;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>News Classification</h2>
        <form action="upload.php" method="POST" enctype="multipart/form-data">
            <input type="text" name="headline" placeholder="Enter news headline" required>
            <input type="file" name="image" accept="image/*" required>
            <button type="submit">Classify News</button>
        </form>
    </div>
</body>
</html>
