<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
  <head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <meta name="generator" content="PSPad editor, www.pspad.com">
  <title></title>
  </head>
  <body>
    <?php
      $conn = new mysqli("10.0.0.16", "TEST", "123456789", "Test_DB", "3308");
      if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
      }
      echo "Connected successfully";
    ?>
    <br><b>Start</b><br>
    <?php
      print_r($_POST);
      echo "<br>";
      $json = json_encode($_POST);
      echo $json;
      echo "<br>";
      echo $json["MYSQL"];
    ?>
    <br><b>End</b>
  </body>
</html>



<?php

///////////////////////////////////////////////////////////////// Time test only PHP (Yes, mysqli didn't work the first time)

/*echo "<br>";
$sql = "SELECT CURRENT_TIMESTAMP;";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
$row = $result->fetch_assoc();
  // output data of each row*/
  /*while($row = $result->fetch_assoc()) {
    echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
  }*/
  /*print_r($row["CURRENT_TIMESTAMP"]);
} else {
  echo "0 results";
}
$conn->close();*/
?>