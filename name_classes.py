#Name Classes
#https://edabit.com/challenge/kbtju9wk5pjGYMmHF

class Name:
  def __init__(self, fname, lname):
    Name.fullname = fname.capitalize()  + " "+ lname.capitalize() 
    Name.fname = fname.capitalize() 
    Name.lname = lname.capitalize() 
    Name.initials = fname[0].upper() +"."+ lname[0]+"."
   

a1 = Name('john', 'SMITH')
print(a1.initials)
print(a1.fullname)
print(a1.fname)
print(a1.lname)
