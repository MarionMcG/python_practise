## How Many Solutions Does This Quadratic Have?
## https://edabit.com/challenge/o2AKq4xy3nfZabKXL

def solutions(a, b, c):
  discrim = b**2 - 4*a*c
  if discrim == 0:
    print("One Real Root")
  if discrim <0:
    print("No Real Roots")
  if discrim >0:
    print('Two Real Roots')



a = 1
b = 0
c = -1
solutions(a, b, c)
