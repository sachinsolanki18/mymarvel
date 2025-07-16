<?php
$servername = "localhost";
$username = "root";
$password = ""; // Default for WAMP
$dbname = "registration_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

$conn = new mysqli("localhost", "root", "", "registration_db");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "✅ Connected successfully";

// Retrieve POST data
$name = $_POST['name'];
$email = $_POST['email'];
$pass = $_POST['password'];
$gender = $_POST['gender'];
$city = $_POST['city'];
$feedback = $_POST['feedback'];

// Prepare SQL statement
$sql = "INSERT INTO user_feedback (name, email, password, gender, city, feedback)
        VALUES (?, ?, ?, ?, ?, ?)";

$stmt = $conn->prepare($sql);
$stmt->bind_param("ssssss", $name, $email, $pass, $gender, $city, $feedback);

if ($stmt->execute()) {
    echo "<h2>✅ Registration and Feedback submitted successfully!</h2>";
} else {
    echo "❌ Error: " . $stmt->error;
}

$stmt->close();
$conn->close();
?>
