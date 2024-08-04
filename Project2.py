def main():
   number = 0
   number= input("Please put a natural number that is between 1 and 6 digits in length (and not zero).");
   while (number<=0 or (number%1)!=0 or number>999999):
       number=input("Unable to process number, enter a natural number of the appropriate number of digits");
   if(number%2==0):
      print("The number is divisible by 2");
   else:
      print("The number is not divisible by 2");
   if(number%3==0):
      print("The number is divisible by 3");
   else:
      print("The number is not divisible by 3");
   if(number%4==0):
      print("The number is divisible by 4");
   else:
      print("The number is not divisible by 4");
   if(number%5==0):
      print("The number is divisible by 5");
   else:
      print("The number is not divisible by 5");
   if(number%6==0):
      print("The number is divisible by 6");
   else:
      print("The number is not divisible by 6");
   if(number%7==0):
      print("The number is divisible by 7");
   else:
      print("The number is not divisible by 7");
   if(number%8==0):
      print("The number is divisible by 8");
   else:
      print("The number is not divisible by 8");
   if(number%9==0):
      print("The number is divisible by 9");
   else:
      print("The number is not divisible by 9");
   if(number%10==0):
      print("The number is divisible by 10");
   else:
      print("The number is not divisible by 10");
   if(number%11==0):
      print("The number is divisible by 11");
   else:
      print("The number is not divisible by 11");


if __name__ == '__main__':
    main()
