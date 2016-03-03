grownup=1
new=1
month=0
while month<=4: 
    print(str.format("Month {0}: {1} pair(s) of rabbits", month,grownup))
    pre_grownup=grownup
    grownup= pre_grownup+new
    new=pre_grownup
    month=month+1
