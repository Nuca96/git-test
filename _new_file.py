import os
import blabla

print("this is just de begining")

os.chdir('/home/idumea/disk/tests/')
os.system('cd {}'.format(os.getcwd()))
os.system('ls')

print(blabla.polinom2(3, 1, 2, 3))
print("end")
