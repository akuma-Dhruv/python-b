import os
print("program for armstrong number")

OR=int(input("\nenter original number"))
ln= int(input("enter last number"))
while OR<ln :

  a=OR//100;
  b=(OR//10)-int(a)*10;
  c=(OR)-((OR//10)*10);
  print("digits are ",a,"  ",b,' ',c)
  if ((a*a*a)+(b*b*b)+(c*c*c))== OR :
   print("\nYES, it is a armstrong number")
  else:
   print(" \nNO, it is not an armstrong number")
  OR+=1

os.system("pause")