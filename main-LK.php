<!DOCTYPE html>
<html>
<head>

	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>HomePage</title>
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
		table, th, td {
  		border: 1px solid black;
  		border-collapse: collapse;
  		width: 350px;
  		height: 60px;
  		
}
		th{
			font-size: 30px;
			color: black;
			


		}
		td{
			font-size: 15px;
			
		}



body{
	background: #fff7e6;
	overflow-x: hidden; /* Hide horizontal scrollbar */
}
html,body {
    margin:0;
    width: 100%;
   
    /*This is my attempt to remove the space under my page */
   
    height: 1100px;

}
.sticky {
  position: fixed;
  top: 0;
  width: 100%;
  }


#main1pic-lk{
  width: 1100px;
 height: 450px;
 position: relative; top: 70px; left: 200px;
 border-radius: 50px;
 border: 1px solid black;

	display: block;

  	
 	text-align: center;

}

#div1-lk{
  width: 200px;
  height: 25px;
  background-color: #4ef57b;
  position: relative;top: 24px; left: 250px;
  width: 300px;
  border-radius: 50px;
} 

#div2-lk{
  width: 500px;
  height: 50px;
    position: relative; left: 500px; bottom: 40px;
  text-align: center;
}

.topbuttons{
	position: relative; bottom: 40px; left: 100px;
  font-family: "Times New Roman", Times, serif;
  font-size: 25px;
  background-color: #4ef57b;

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
    position: fixed;
  background-color: #4ef57b;
  color: white;
  font-size: 30px;
  z-index: 99;
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


<img id="main1pic-lk" src="main-lk5.png">


<div id="div1-lk">
	<h2><strong>Vietnam needs your help!</strong> </h4>
</div>


<div style="width: 500px;
  height: 50px;
    position: relative; left: 500px; top: 20px;
  text-align: center;">
	<h2><strong>Who are we and what do we do?</strong> </h4>
</div>

<p style="width: 920px; position: relative; left: 280px; bottom: px; border: 1px solid black;">Welcome to our <strong>Thien dam charity group </strong>. We are an non-profit organization which is run by a small family in <strong>Norway</strong>. Thien dam charity group are funded through donations and purchases made from our business. Our business is based on <strong>selling foods</strong> at various festivals in Norway, and thereafter we donate the profits to various charities in Vietnam. 

<a href="Aboutus-SK.php">Read more >>></a> </p>





<?php
require_once("config.php");
$query1="SELECT title FROM news WHERE dato=(SELECT MIN(dato)) limit 1;";
    $result1 = mysqli_query($CONN,$query1);
    $row1 = $result1->fetch_assoc();
        
?>

<?php
require_once("config.php");
$query2="SELECT news FROM news WHERE dato=(SELECT MIN(dato)) limit 1;";
    $result2 = mysqli_query($CONN,$query2);
    $row2 = $result2->fetch_assoc();

        
?>

<div style="border: 2px solid black; width: 310px; position: relative; top: 40px; left: 550px; ">
<div style="width: 310px; ">
	<h1 style="font-size: 35px; position: relative; left: 20px; ">News of the week</h1>

	
</div>
<div style="width: 250px; font-size: 15px; position: relative; left: 20px; ">
	<?php
	echo "<h1>".$row1['title']."</h1>";
	echo "<p>".$row2['news']."</p>";

	?>

</div>
<img style="width: 250px; height: 250px; position: relative; top: 20px; left: 20px; " src="main-lk6.png">

<h1 style="position: relative; left: 35px; top: 5px; "><a href="news-LG.php">Read more >>></a></h1>

</div>





<?php
require_once("config.php");
$query1="SELECT namee FROM charity";
    $result1 = mysqli_query($CONN,$query1);
    $row1 = $result1->fetch_assoc();
        
?>

<?php
require_once("config.php");
$query2="SELECT descr, url FROM charity";
    $result2 = mysqli_query($CONN,$query2);
    $row2 = $result2->fetch_assoc();

$linken=$row2['url']
?>

<div style="border: 2px solid black;  width: 310px; position: relative; bottom: 600px; left: 50px; ">
<div style=" width: 310px;  ">
	<h1 style="font-size: 35px; width: 210px; position: relative; left: 30px; ">Charity of the week</h1>

	
</div>
<div style="width: 250px; font-size: 15px; position: relative; left: 30px; ">
	<?php
	echo "<h2>".$row1['namee']."</h2>";
	echo "<p>".$row2['descr']."</p>";

	?>

</div>
<img style="width: 250px; height: 250px; position: relative; top: 20px; left: 25px; " src="main-lk2.png">

<h1 style="position: relative; left: 45px; top: 10px; "><a href=<?php echo $linken; ?>>Read more >>></a></h1>








</div>
<div style="position: relative; left: 1100px; bottom: 1340px; ">
	<table style="height: 100%;">
<?php

require_once("config.php");


$query="SELECT location,date_format(dato,'%d-%m-%Y') as dato1 FROM Locations ORDER BY dato ASC";
    $result = mysqli_query($CONN,$query);
        
?>

	
		<th style="font-size: 37px;" colspan="2" >Upcoming events</th>
	
		<tr>
			<th>Location</th>
			<th>Date </th>
		</tr>
		<?php
		$count=0;
		
		while($res = mysqli_fetch_array($result)) {  
			   
            echo "<tr>";
            echo "<td>".$res['location']."</td>";
            echo "<td>".$res['dato1']."</td>";
            echo "<br>";
            $count+=1;
            if($count==7){
            	break;
            }         
        }
       
		?>
		<tr>
			<th  colspan="2"> <a href="Locations-MMA.php"> Read more >>></a></th>
		</tr>

		
	</table>





<div style="width: 150px; height: 150px; background-color: #4ef57b; position: relative;right: 970px; top: 150px;">

<a href="news-LG.php"> <img style="height: 100px; width: 100px; position: relative; top: 20px; left: 25px; " src="main-lk4.png"></a>
	<h1 style="position: relative; left: 30px; top: 27px;">News</h1>

 </div>


<div style="height: 150px; width: 150px; background-color: #4ef57b; position: relative; bottom: 10px; left: 100px;border: 1px solid black; "></div>
	<a href="contactus-LK.php"> <img style="height: 100px; width: 100px; position: relative; left: 125px;bottom: 135px; " src="main-lk3.png"></a>
	<h1 style="position: relative;left: 100px; bottom:130px; ">Contact us!</h1>
</div>






	<header style="  
	padding: 20px;
  align-content: center;
  height: 25px;
  width: 1495px;
 text-align: center;
  position: fixed; bottom: 0px;
  background: #4ef57b;
  color: white;
  font-size: 30px;">


  <footer style="position: relative; bottom: 5px; right: 30px; color: black;"><strong>© 2022 Thien dam charity group is a registered nonprofit organization</strong></footer>

</header>

</body>
</html>