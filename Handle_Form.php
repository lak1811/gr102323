<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>HandlingOfForm</title>

</head>
<body style="background: #fff7e6;">
	<h1>RESULT</h1>

	<?php
	$flag=True;
	$flag2=True;
	require("config.php");

	if(empty($_POST['name'])){
		$error="You have not entered your name";
		echo "<p style=\"color:red;\">".$error."</p>";				
			$flag = false; 
	}
	if(empty($_POST['email'])){
				$error = "Please enter your email address.";
				echo "<p style=\"color:red;\">".$error."</p>";				
				$flag = false; 
	}
	if(empty($_POST['description'])){
				$error = "Please enter a description for your inquiry";
				echo "<p style=\"color:red;\">".$error."</p>";				
				$flag = false; 
	}
	
	if(!isset($_POST['concern'])){
				$error = "Specify your concern?";
				echo "<p style=\"color:red;\">".$error."</p>";				
				$flag = false; 
			}


	if ($flag){
		if ($_POST['concern']=="feedback" ) {
		 	
		$concern="Feedback";
	}
}

	if ($flag){
		if ($_POST['concern']=="complaint" ) {
		 	
		$concern="Complaint";
	}
}


	if ($flag){
		if ($_POST['concern']=="other" ) {
		 	
		$concern="Other";
	}
}

	


	if($flag){
		$queryid="select max(id) as most from contactus";
		$resultt=mysqli_query($CONN,$queryid);
		$id=mysqli_fetch_assoc($resultt);
		$finali=$id['most'];
		$finalid=$finali+1;

		
		$name=$_POST['name'];
		$email=$_POST['email'];
		$description=$_POST['description'];
		$concern=$_POST['concern'];
		$todaydate = date('Y-m-d'); 


		$query="INSERT INTO contactus (Namee,Email,Concern,DESCR,dato,ID) VALUES ('$name','$email','$concern','$description','$todaydate','$finalid')";
    	$result = mysqli_query($CONN,$query);
    	if($result==''){
    		$flag2=False;
    		echo "<h1>This process was a Failure</h1>";

    	}

    	if ($flag2!=''){
    		echo "<br> ";
		echo "<p> This feedback has been registered. Thank you " .$_POST['name']." </p>";
		echo "Here is the information that we have recieved as a confirmation of your sent feedback";
		echo "<p>Name: " .$_POST['name']." </p>";

		echo "<p>Email: " .$_POST['email']." </p>";
		echo "<p>Description: " .$_POST['description']." </p>";
		echo "<p>Concern: " .$_POST['concern']." </p>";
		echo "<p>Id: $finalid </p>";

		echo "<h3>Thank you for your interaction. We will read this and get better!</h3>";

    	}
    	
}

mysqli_close($CONN)


?>
</body>
</html>
