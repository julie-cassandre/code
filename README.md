<?php

$img=imagecreatetruecolor(70,40);

//定义三种随机颜色
 $black=imagecolorallocate($img,rand(0,255),rand(0,255),rand(0,255));
 $green=imagecolorallocate($img,rand(0,255),rand(0,255),rand(0,255));
 $pink=imagecolorallocate($img,rand(0,255),rand(0,255),rand(0,255));

//定义背景颜色：白色
  $white=imagecolorallocate($img,255,255,255);
   imagefill($img,0,0,$white);

//随机生成字母和数字
  $code="";
for($i=0;$i<4;$i++) 
{  
      $number=rand(1,3);
switch($number){
   case 1:$num = rand(65,90);
      $code .=chr($num);
   
         break;
    case 2:$num = rand(97,122);
     $code .=chr($num);
            break;
  case 3:$code .=rand(0,9);
  
        break; 
   default；break;
}
     
    };
   //随机生成模糊干扰点
  for($i=0;$i<100;$i++){
   imagesetpixel($img,rand(0,100),rand(5,100),$black);
   imagesetpixel($img,rand(0,100),rand(5,100),$green);
   imagesetpixel($img,rand(0,100),rand(5,100),$pink);
}
//随机生成三根线段
     imageline($img, rand(0,10),rand(0,10),rand(0,100),rand(0,100), $pink);
     imageline($img, rand(5,15),rand(5,15),rand(0,100),rand(0,100), $green);
     imageline($img, rand(10,20),rand(10,20),rand(0,100),rand(0,100), $black);
//生成验证码
 header("content-type: image/png");
imagestring($img,55,15,15,$code,$pink);

 imagepng($img);
   imagedestroy($img);
