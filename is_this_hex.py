#Create a function that determines whether a string is a valid hex code.
#https://edabit.com/challenge/9p5tMqyYENTmD9Nh5

def is_this_hex(str):
  chars = ['A', 'B', 'C', 'D', 'E','a', 'b', 'c', 'd', 'e', '#', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  print(chars)
  if len(str)!=7:
    print('Not a Hex. \n Oops, the length of the number is incorrect')
    return False
  for i in range (7):
    if str[i] not in chars:
      print("Not a Hex. Oops, you've included characters that can't be in a hex number")
      return False
  else:
    print('Its a hex')
    return True

        

is_this_hex("#253de2")
