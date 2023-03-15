<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Contact us!</title>
	<link rel="stylesheet" type="text/css" href="app.css">
	<!-- Button based on the picture top left on website -->
<header id="myHeader">
 <a href="main-LK.php"><img src="logo.png" style="
  width: 100px; height: 65px; 
  position: relative;bottom: 20px; right: 70px;"></a>


<!-- ALL BUTTONS   -->
<a class="buttoncolor" href="aboutus-SK.php">About us</a>
&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 
&nbsp &nbsp 

<a class="buttoncolor"href="locations-MMA.php">Locations</a>
&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 
<a class="buttoncolor"href="news-LG.php">News</a>
&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 
<a class="buttoncolor"href="contactus-LK.php">Contact us</a>
&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp 




<!-- set default table settings on table, table head and table data  -->
<style type="text/css">
.sticky {
  position: fixed;
  top: 0;
  width: 100%;
}

body{
	background: #fff7e6;
}
html,body {
    margin:0;
    width: 100%;
   
    /*This is my attempt to remove the space under my page */
   
    height: 600px;

}
body{
	background: #fff7e6;
	overflow-x: hidden; /* Hide horizontal scrollbar */
}

.buttoncolor{
  color: black;	position: relative; bottom: 40px; left: 100px;
  font-family: "Times New Roman", Times, serif;
  font-size: 25px;
  background-color: #4ef57b;
  position: relative; left: 20px;
/*The picture in the profilebar of a user*/
}



#myHeader{
	padding: 20px;
  align-content: center;
  height: 25px;
  width: 1555px;
 text-align: center;
 z-index: 99;
  background-color: #4ef57b;
  color: white;
  font-size: 30px;
}
#myHeader1{
	padding: 20px;
  align-content: center;
  height: 25px;
  width: 1495px;
 text-align: center;
 position: fixed; bottom: 1px;
  background: #4ef57b;
  color: white;
  font-size: 30px;

}
a:link {
  color: black;
  background-color: transparent;
  text-decoration: none;
}
a:visited {
  color: black;
  background-color: transparent;
  text-decoration: none;
}


</style>
</header>
<script>
window.onscroll = function() {myFunction()};

var header = document.getElementById("myHeader");
var sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}
</script>
</head>
<body>



<div style="width: 500px; height: 50px; position: relative; left: 550px; bottom: 20px; ">
	<div style="width: 200px; height: 70px; text-align: center; position: relative; left: 150px; ">
	<h1 style="position: relative; top: 10px; right: 40px; ">Contact us!</h1>
	</div>
	<p style="font-size: 20px; width: 1050px; position: relative; right: 300px; bottom: 20px; ">Our team would love to get feedback from our users. Please fill out the form below and inform us on how we could be better!</p>
</div>

<div style="position: relative; right: 100px; ">
<div style="background-color: #4ef57b ; width: 660px; height: 380px; position: relative; left: 550px; top:70px; border-radius: 50px;
 border: 1px solid black;
	display: block;
 	text-align: center; "></div>

<div style="height: 70px; width: 300px; position: relative; left: 580px ; bottom: 480px; text-align: ">
	<h1 style="position: relative; top: 165px; left: 5px; ">Contact Form</h1> 

	
	<form action="http://localhost/Appen/Handle_Form.php" method="post">

			<div style="position: relative; left: 440px; top: 150px; ">
				<p><strong>Concern:</strong>
				<br>
				<br>
				<input type="radio" name="concern" value="feedback">Feedback
				<br>
				<input type="radio" name="concern" value="complaint">Complaint
				<br>
				<input type="radio" name="concern" value="other">Other
				</p>
			</div>
		<div style="position: relative; top: 40px; left: 10px; ">	
		<p style="text-align: left;  ">Name: <input style="font-size: 20px;  "type="text" name="name" size="20"> </p>
		
	
			
		
		<p style="text-align: left; ">Email: <input style="font-size: 20px; " type="text" name="email" size="20"></p>
		<p style="text-align: left; ">Description: <textarea style="font-size: 20px;" type="text" name="description" rows="6" cols="30" ></textarea></p>
		<button style="position: relative; left: 535px; bottom: 40px; background-color: #fff7e6; width: 60px; height: 37px; " type="submit" name="submit" value="Register">Submit</button>	
		</div>
	</form>
</div>
</div>



<header id="myHeader1">

  <footer style="position: relative; bottom: 5px; right: 30px; color: black;"><strong>© 2022 Thien dam charity group is a registered nonprofit organization</strong></footer>

</header>




</body>
</html>