flock_sheep=[5,7,300,90,24,50,75]
print("Hello, my name is nim and these are my ship sizes","\n",flock_sheep)    
n=max(flock_sheep)
print("\n","Now my biggest sheep has size",n,"let's shear it")
p=flock_sheep.index(n)
m=flock_sheep.insert(p,8)
flock_sheep.remove(n)
print("\n","After shearing, here is nim's flock","\n",flock_sheep)

##print('\n',"One month has passed, now here is nim's flock",x)
    
