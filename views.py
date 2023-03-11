from django.http import HttpResponse
from django.shortcuts import redirect
import mysql.connector as mysql
from django.shortcuts import render


def Home(req):
    return HttpResponse("""<h2 style'color:blue'>YOU ARE GREAT CHOICE</h2>
    <div class="main-header">
        <div class="header">
          <h1>HOTEL MANAGEMENT SYSTEM</h1>
          <div>
            <img src="https://www.shutterstock.com/image-photo/luxury-hotel-infinity-pool-palms-260nw-648165631.jpg" height="50%" width="100%">
          </div>
 
      
      <div id="headercontent"><h2 style="text-align:center;color:brown;padding:10px;font-style:italic;">Wel-Come To Radhika Hotel</h2></div>
    </div>
      
      <div class="container fluid dark bg-primary">
       <div id="menu">
        <ul>
            
            <a href="Home"><button class="btn">Home</button></a>
            <a href="Reception"><button class="btn">Reception</button></a>
            <a href="Booking"><button class="btn">Booking</button></a>
            <a href="Gallary"><button class="btn">Gallary</button></a>
            <a href="Login"><button class="btn">Login</button></a>
            <a href="signout"><button class="btn">signout</button></a>
            <a href="About.html"><button class="btn"></button></a>
            <a href="Help"><button class="btn">Help</button></a>
            
        </ul>
        </div>
    
        <div id="content"><h2 style="text-align:center;color:black;padding:50px;">YOU ARE GREAT CHOICE! </h2></div>
    </div>
      </div>  
      <div class="Gallary">
       <div class="img">
            <img src="https://thumbs.dreamstime.com/b/catering-10-8265000.jpg" height="50%" width="40%">
            <img src="https://thumbs.dreamstime.com/b/restaurant-20049791.jpg" height="50%" width="40%">
           
   
   </div>
 </div>
  """)
def Reception(req):
    return HttpResponse("""<h2>Reception</h2>
        <div class="main-header">
        <div class="header">
          <h1>HOTEL MANAGEMENT SYSTEM</h1>
          <div>
          <img src="https://www.shutterstock.com/image-photo/luxury-hotel-infinity-pool-palms-260nw-648165631.jpg" height="50%" width="100%">
          </div>
 
      
      <div id="headercontent"><h2 style="text-align:center;color:brown;padding:10px;font-style:italic;">Wel-Come To Radhika Hotel</h2></div>
    </div>
      

   <div class="container fluid dark bg-primary">
   
   <div id="menu">
        <ul>
            
            <a href="Home"><button class="btn">Home</button></a>
            <a href="Reception"><button class="btn">Reception</button></a>
            <a href="Booking"><button class="btn">Booking</button></a>
            <a href="Gallary"><button class="btn">Gallary</button></a>
            <a href="Login"><button class="btn">Login</button></a>
            <a href="signout"><button class="btn">signout</button></a>
            <a href="About"><button class="btn">About</button></a>
            <a href="Help"><button class="btn">Help</button></a>
            
        </ul>
     </div>
  
      
    <div id="content">
        <ul>
            <button type="button" class="btn btn-warning btn">HOME</button>   <br>
            <button type="button" class="btn btn-warning btn">ROOMS</button>   <br>
            <button type="button" class="btn btn-warning btn">CALL US</button>  <br>
            <button type="button" class="btn btn-warning btn">GALLARY</button> <br>
        </ul>
    </div>
    </div>
  <div class="Gallary">
       <div class="img">
            <img src="https://thumbs.dreamstime.com/b/catering-10-8265000.jpg" height="50%" width="40%">
            <img src="https://thumbs.dreamstime.com/b/restaurant-20049791.jpg" height="50%" width="40%">
           
   
   </div>
  </div>
 </div>     
                    
     """)    
def Booking(req):
    return HttpResponse("""<h2>Booking</h2>
     <div class="main-header">
        <div class="header">
          <h1>HOTEL MANAGEMENT SYSTEM</h1>
          <div>
          <img src="https://www.shutterstock.com/image-photo/luxury-hotel-infinity-pool-palms-260nw-648165631.jpg" height="50%" width="100%">
          </div>
 
      
      <div id="headercontent"><h2 style="text-align:center;color:brown;padding:10px;font-style:italic;">Wel-Come To Radhika Hotel</h2></div>
    </div>
      
      <div class="container fluid dark bg-primary">
       <div id="menu">
        <ul>
            
            <a href="Home"><button class="btn">Home</button></a>
            <a href="Reception"><button class="btn">Reception</button></a>
            <a href="Booking"><button class="btn">Booking</button></a>
            <a href="Gallary"><button class="btn">Gallary</button></a>
            <a href="Login"><button class="btn">Login</button></a>
            <a href="signout"><button class="btn">signout</button></a>
            <a href="About"><button class="btn">About</button></a>
            <a href="Help"><button class="btn">Help</button></a>
            
        </ul>
    </div>
    
   <div id="content">
      <ul>
       <button type="button" class="btn btn-warning btn"> BOOK NOW</button>    <br>
       <button type="button" class="btn btn-warning btn">GUEST ROOMS</button>    <br>
       <button type="button" class="btn btn-warning btn">POOL</button>    <br>
       <button type="button" class="btn btn-warning btn">PARTY HALL</button>    <br>
       <button type="button" class="btn btn-warning btn">WEDDING HALL</button>    <br>
       <button type="button" class="btn btn-warning btn"> MEETING HALL</button>    <br>
      </ul>
    </div> 
     </div>
  <div class="Gallary">
       <div class="img">
            <img src="https://thumbs.dreamstime.com/b/catering-10-8265000.jpg" height="50%" width="40%">
            <img src="https://thumbs.dreamstime.com/b/restaurant-20049791.jpg" height="50%" width="40%">
           
   
    </div>
   </div>   
  </div>

    """)    
def Gallary(req):
     return HttpResponse("""<h2>Gallary</h2>
    <div class="main-header">
        <div class="header">
          <h1>HOTEL MANAGEMENT SYSTEM</h1>
          <div>
            <img src="https://www.shutterstock.com/image-photo/luxury-hotel-infinity-pool-palms-260nw-648165631.jpg" height="50%" width="100%">
          </div>
 
      
      <div id="headercontent"><h2 style="text-align:center;color:brown;padding:10px;font-style:italic;">Wel-Come To Radhika Hotel</h2></div>
    </div>
      
      <div class="container fluid dark bg-primary">
       <div id="menu">
        <ul>
            
            <a href="Home"><button class="btn">Home</button></a>
            <a href="Reception"><button class="btn">Reception</button></a>
            <a href="Booking"><button class="btn">Booking</button></a>
            <a href="Gallary"><button class="btn">Gallary</button></a>
            <a href="Login"><button class="btn">Login</button></a>
            <a href="signout"><button class="btn">signout</button></a>
            <a href="About"><button class="btn">About</button></a>
            <a href="Help"><button class="btn">Help</button></a>
            
        </ul>
        </div>
    
        <div class="Gallary">
       <div class="img">
            <img src="https://media-cdn.tripadvisor.com/media/photo-s/11/13/e6/4e/still-room-view-to-cocktail.jpg" height="100" width="100">
            <img src="data:image/jpeg;base64,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" height="100" width="100">
            <img src="data:image/jpeg;base64,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" height="100" width="100">
            <img src="https://thumbs.dreamstime.com/z/buffet-dinner-restaurant-catering-food-concept-66884106.jpg" height="100" width="100">
            <img src="data:image/jpeg;base64,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" height="100" width="100">
    </div>
      </div>  
      <div class="Gallary">
       <div class="img">
            <img src="https://thumbs.dreamstime.com/b/catering-10-8265000.jpg" height="50%" width="40%">
            <img src="https://thumbs.dreamstime.com/b/restaurant-20049791.jpg" height="50%" width="40%">
           
   
   </div>
 </div>
 </div>
 </div>
    """)   
 
def Login(req):
	return HttpResponse("""<center><h2>Login Page!</h2>
    	<div>    
     <img src="https://www.shutterstock.com/image-photo/luxury-hotel-infinity-pool-palms-260nw-648165631.jpg" height="50%" width="100%">
          </div>
	<form action="/logintask">
	<table>
		<tr>
			<td>User:</td>
			<td><input type="email" name="Email"> </td>
		</tr>
		<tr>
			<td>Password:</td>
			<td><input type="password" name="Pass"></td>
		</tr>
		<tr>
			<td></td>
			<td><input type="submit" value="Login"></td>
		</tr>
		<tr>
			<td></td>
			<td><a href="/register">NewUser!</a></td>
		</tr>
	</table>	
	</form> 
        </center>
""")
      
 
def register(req):
	return HttpResponse("""<center><h2>Register Page!</h2>
	<form action="/insert">
	<table>
		<tr>
			<td>Name:</td>
			<td><input type="text" name="Name" </td>
		</tr>
		<tr>
			<td>Email:</td>
			<td><input type="email" name="Email"></td>
		</tr>
		<tr>
			<td>Password:</td>
			<td><input type="password" name="Pass"></td>
		</tr>
		<tr>
			<td>Enter MoNo:</td>
			<td><input type="number" name="Mob"></td>
		</tr>
		
		<tr>
			<td></td>
			<td><input type="submit" value="Registerme!"></td>
		</tr>		
	</table>	
	</form>
	</center>
	""")
 

def insert(req):
    Name=req.GET.get("Name")
    Email=req.GET.get("Email")
    Pwd=req.GET.get("Pass")
    Mob=req.GET.get("Mob")

    conn = mysql.connect(host="localhost",user="root",password="vedika@123",database="vdb7653")

    cr = conn.cursor()

    query = "insert into usertb  values('{0}','{1}','{2}',{3})".format(Name,Email,Pwd,Mob)

    cr.execute(query)

    conn.commit()
    conn.close()    
    return redirect('/Login')

def logintask(req):
  Email=req.GET.get("Email")
  Pwd=req.GET.get("Pass")
  
  conn = mysql.connect(host="localhost",user="root",password="vedika@123",database="vdb7653")

  cr = conn.cursor()
  cr.execute("select * from usertb")
  
  while True:
       row=cr.fetchone()
       #print(row)
       if row is None:
         break;
       elif row[1]==Email and row[2]==Pwd:
         return redirect('/Home')
  return redirect('/Login')     


def signout(req):
    return HttpResponse("""<h2>signout<\h2>

     <div class="main-header">
        <div class="header">
          <h1>HOTEL MANAGEMENT SYSTEM</h1>
          <div>
            <img src="https://www.shutterstock.com/image-photo/luxury-hotel-infinity-pool-palms-260nw-648165631.jpg" height="50%" width="100%">
          </div>
 
      
      <div id="headercontent"><h2 style="text-align:center;color:brown;padding:10px;font-style:italic;">Wel-Come To Radhika Hotel</h2></div>
    </div>
      
      <div class="container fluid dark bg-primary">
       <div id="menu">
        <ul>
            
            <a href="Home"><button class="btn">Home</button></a>
            <a href="Reception"><button class="btn">Reception</button></a>
            <a href="Booking"><button class="btn">Booking</button></a>
            <a href="Gallary"><button class="btn">Gallary</button></a>
            <a href="Login"><button class="btn">Login</button></a>
            <a href="signout"><button class="btn">signout</button></a>
            <a href="About"><button class="btn">About</button></a>
            <a href="Help"><button class="btn">Help</button></a>
            
        </ul>
        </div><from action="">
<table>
  <tr>
    <td>name:</td>
    <td><input type="text" name="Name"></td>
   </tr>
   <tr>
       <td>Email:</td>
       <td><input type="Email" name="Email"></td>
    </tr>
    <tr>
        <td>password:</td>
        <td><input type="password" name="pass"></td>
    </tr>
    <tr>
      <td>mobile NO:</td>
      <td><input type="number" name="mob"></td>       
    </tr>
    
    <tr>
      <td></td>
      <td><input type="submit" value="registerme"></td>         
    </tr>
</table>
</from>

      </div>  
      <div class="Gallary">
       <div class="img">
            <img src="https://thumbs.dreamstime.com/b/catering-10-8265000.jpg" height="50%" width="40%">
            <img src="https://thumbs.dreamstime.com/b/restaurant-20049791.jpg" height="50%" width="40%">
           
   
   </div>
 </div>
 </div>
 """) 
def About(req):
    return HttpResponse("""<h2>About</h2>
           <div class="main-header">
        <div class="header">
          <h1>HOTEL MANAGEMENT SYSTEM</h1>
          <div>
            <img src="https://www.shutterstock.com/image-photo/luxury-hotel-infinity-pool-palms-260nw-648165631.jpg" height="50%" width="100%">
          </div>
 
      
      <div id="headercontent"><h2 style="text-align:center;color:brown;padding:10px;font-style:italic;">Wel-Come To Radhika Hotel</h2></div>
    </div>
      
      <div class="container fluid dark bg-primary">
       <div id="menu">
        <ul>
            
            <a href="index"><button class="btn">Home</button></a>
            <a href="Reception"><button class="btn">Reception</button></a>
            <a href="Booking"><button class="btn">Booking</button></a>
            <a href="Gallary"><button class="btn">Gallary</button></a>
            <a href="Login"><button class="btn">Login</button></a>
            <a href="signout"><button class="btn">signout</button></a>
            <a href="About"><button class="btn">About</button></a>
            <a href="Help"><button class="btn">Help</button></a>
            
        </ul>
        </div>
        <h1>Email:Radhikahotel@gmail.com</h1>
        <h2>call:12345755</h2>
        <h3>we are here for 24*7 at your service</h3>
    
        </DIV>
      </div>  
      <div class="Gallary">
       <div class="img">
            <img src="https://thumbs.dreamstime.com/b/catering-10-8265000.jpg" height="50%" width="40%">
            <img src="https://thumbs.dreamstime.com/b/restaurant-20049791.jpg" height="50%" width="40%">
           
   
   </div>
 </div>
                   
    """)
def Help(req):
    return HttpResponse("""<h2>HELP</h2>
 
     <div class="main-header">
        <div class="header">
          <h1>HOTEL MANAGEMENT SYSTEM</h1>
          <div>
            <img src="https://www.shutterstock.com/image-photo/luxury-hotel-infinity-pool-palms-260nw-648165631.jpg" height="50%" width="100%">
          </div>
 
      
      <div id="headercontent"><h2 style="text-align:center;color:brown;padding:10px;font-style:italic;">Wel-Come To Radhika Hotel</h2></div>
    </div>
      
      <div class="container fluid dark bg-primary">
       <div id="menu">
        <ul>
            
            <a href="Home"><button class="btn">Home</button></a>
            <a href="Reception"><button class="btn">Reception</button></a>
            <a href="Booking"><button class="btn">Booking</button></a>
            <a href="Gallary"><button class="btn">Gallary</button></a>
            <a href="Login"><button class="btn">Login</button></a>
            <a href="signout"><button class="btn">signout</button></a>
            <a href="About"><button class="btn">About</button></a>
            <a href="Help"><button class="btn">Help</button></a>
            
        </ul>
        </div>
    
        <div id="content"><h2 style="text-align:center;color:black;padding:50px;">How can we help you! </h2></div>
    </div>
      </div>  
      <div class="Gallary">
       <div class="img">
            <img src="https://thumbs.dreamstime.com/b/catering-10-8265000.jpg" height="50%" width="40%">
            <img src="https://thumbs.dreamstime.com/b/restaurant-20049791.jpg" height="50%" width="40%">
           
   
   </div>
 </div>
 
 """)