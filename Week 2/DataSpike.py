"""Max"""
a,b,c,d=int(input()),int(input()),int(input()),int(input())
e,f,g,h=int(input()),int(input()),int(input()),int(input())
value = a
value = b if b > value else value
value = c if c > value else value
value = d if d > value else value
value = e if e > value else value
value = f if f > value else value
value = g if g > value else value
value = h if h > value else value
print(value)
