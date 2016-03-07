while True:
   num = int(input("Enter a number: "))
   i=2
   if num >= 1:
      while i< (num-1):
          if (num % i) == 0:
              print(num,"is not a prime number")
              print(i,"times",num//i,"is",num)
              break
          i=i+1
      else:
          print(num,"is a prime number")
   else:
       print(num,"is not a prime number")
