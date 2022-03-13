import os
import time
import sys

# Argument to select file
namefile = str(sys.argv[1])
linuxnamefile = namefile + "| wc -l"

# Time count start
starttime = time.time()
os.system("clear")

# Baner
print('---------------------------------------------------------------')
print('>====>     >=>>=>          >>       >==>    >=>       >>       ')
print('>=>   >=>  >>   >=>       >>=>      >> >=>  >=>      >>=>      ')
print('>=>    >=> >>    >=>     >> >=>     >=> >=> >=>     >> >=>     ')
print('>=>    >=> >==>>=>      >=>  >=>    >=>  >=>>=>    >=>  >=>    ')
print('>=>    >=> >>    >=>   >=====>>=>   >=>   > >=>   >=====>>=>   ')
print('>=>   >=>  >>     >>  >=>      >=>  >=>    >>=>  >=>      >=>  ')
print('>====>     >===>>=>  >=>        >=> >=>     >=> >=>        >=> ')
print('Analysis of : ' + namefile, "launched...")
print('---------------------------------------------------------------')

# Number of lines
print('Number of lines :')
os.system("wc -l < " + namefile)  

# Passwords in the default browsers generation parameters
print('---------------------------------------------------------------')
print('Number of generated passwords :')
stpass = os.system("grep -E ':[a-f0-9]{8}$' " + linuxnamefile)
ndpass = os.system("grep -oP '^\d.*?\d(?=,)' " + linuxnamefile)
if stpass == 0 == ndpass:
    print('Passwords are likelly hashed, cant proceed this analysis.')
else:
    print('Passwords without special characters :')

# Most used emails count
print('---------------------------------------------------------------')
print('Most used emails count :')
print('Gmail :')
os.system("grep -E '{30}@gmail.com' " + linuxnamefile)
print('Hotmail :')
os.system("grep -E '{30}@hotmail.fr' " + linuxnamefile)
print('Yahoo :')
os.system("grep -E '{30}@yahoo.com' " + linuxnamefile)
print('Protonmail :')
os.system("grep -E '{30}@protonmail.com' " + linuxnamefile)
print('Riseup :')
os.system("grep -E '{30}@riseup.net' " + linuxnamefile)

# Admin account informations
print('---------------------------------------------------------------')
print('Admins account informations :')
os.system("grep -i Admin " + namefile)

# Time count stop
endtime = time.time()
print('---------------------------------------------------------------')
print("The execution took :")
print(format(endtime - starttime,".2f"), 'sec')
