<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Fullscreen YouTube Video</title>
  <link rel="stylesheet" href="index.css">
  <script src="index.js" defer></script>
 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script></head>

<body>
  <div class="Buttons">
  <button onclick="clickme()" style="position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px 20px;
  background-color: #ff0000;
  color: white;
  border:none;
  border-radius:4px;
  font-size: 16px;
  cursor: pointer;
  z-index: 9999; border: 2px solid white;">Comic<strong></strong></button>
<button onclick="gotoabout()" class="btn btn-success" style="position: fixed; bottom: 20px; background-color: #ff0000;
 color: white; z-index: 9999; border:2px solid white
 ; font-size: 16px;  transform: translate(50%); padding: 10px 20px; margin-left: 37rem; width:8rem; ">About </button>
 <button onclick="gotofeedback()" class=" btn btn-success" style= "position: fixed; border-radius: 4px; z-index: 9999; background-color: #ff0000; transform: translateX(50%); margin-top: 53rem; margin-left: 84rem; width: 10rem; height: 4.3rem; padding-bottom:1.6rem; margin-top:58.2rem; text-align: center; border:2px solid white; text-align: center; justify-content: center
 ; ">Feedback</button>
  </div>
  
  <div class="side-image1">
    <img src="hulk.jpg" alt="Hulk Image">
  </div>
  <br>
  <br>
  <div class="side-image2">
<img src="cp.jpg" alt="captain america">
 </div>
 <div class="side-image3">
<img src="spider.jpg" alt="spider man">
</div>
<div class="side-image4">
  <img src="panther.jpg" alt=" Black panther">
</div>
  <div class="video-container">
    <iframe 
      src="https://www.youtube.com/embed/XLuL_TXbK1g?autoplay=1&mute=1&controls=0&loop=1&playlist=XLuL_TXbK1g&modestbranding=1&showinfo=0" 
      allow="autoplay; fullscreen" 
      allowfullscreen>
    </iframe>
  </div>

</body>
</html>
