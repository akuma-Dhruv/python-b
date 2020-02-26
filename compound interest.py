import os
print ('program for compound interest ')
p = input('\nenter principal amount ')
r= input('\nenter rate of interest')
n= input ('\nenter no of times interest charged in a year')
t= input('\nenter  time ')
rn =int(r)/int(n)
nt=int(n)*int(t)
inn= int(p)*pow(1+(float(rn)/100),int(nt))
print(inn)
#print
os.system('pause')

