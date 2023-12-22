

# take inputs
num = input('Enter the number: ')

# check number is palindrome or not
i = 0
length = len(num)
if(len(num) % 2 == 0):
    length = len(num) + 1
    
for i in range(length):
   if num[i] != num[-1-i]:
      print(num,'is not a Palindrome')
      break
else:
   print(num,'is a Palindrome')