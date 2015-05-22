<?php
 require_once '../db.php';
 if($_POST){
 $usernam=$_POST["username"];
 $firstname=$_POST["firstname"];
 $lastname=$_POST["lastname"];
 $email=$_POST["email"];
 $conn = new mysqli($servername, $username, $password, $dbname);
 if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
 } 
 $sql = "SELECT * FROM usertable WHERE username='$usernam'";
 $result = $conn->query($sql);
 if($result->num_rows==0)
  {
   $sql="INSERT INTO usertable(username,firstname,lastname,email) VALUES('$usernam','$firstname','$lastname','$email');";
   if($conn->query($sql)===TRUE)
    echo "success";
   else
    echo"Error".$conn->error;
  }
 else
  echo"success";
}
?>

