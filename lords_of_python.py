# this is the first version of the math programming i did for the pattern I found that resuts in a serpinski triangle when plotted see details below at triangle section. This was created in 2021 in the 'Lords of Python' google collab space I have

# this is part of a transfer and refactor project.

# initial conditions 
sums_list = []
summed_ints = []
summed_ints2 = []

x = 1
s = 0


# create a list containing the 50 sums of the sums 
for number in range(50):
  x = number+number
  
  sums_list.append(x)


# show the sums list
# sums_list

# sum the digits of the integers, first run
def sum_integers(item):
    s = 0
    while item:
        s, item = s + item % 10, item // 10
          
    summed_ints.append(s)

# function for second run through. hmm wonder if I could do all this with a lambda
def sum_integers2(item):
    s = 0
    while item:
        s, item = s + item % 10, item // 10
    
#        s += item % 10
#        item //= 10

           
    summed_ints2.append(s)

# trying to iterate through the list  first time
for item in sums_list:
    sum_integers(item)

# display the summed integers
summed_ints

# second time
for item in summed_ints:
    sum_integers2(item)


# a list of sums of the sums
# which is also a list of the sums of the rows of pascal's triangle
sums_list


## the next portion was part of the original 'Lords of Python' google collab space where I had this. considering moving this to an independent file.
# draw some sierpinski becuase theres connections here somehow
# this only draws lines, not plot dots per the chaos game
# works very nicely in pycharm

import turtle
def draw_sierpinski(length,depth):
    if depth==0:
        for i in range(0,3):
            t.fd(length)
            t.left(120)
    else:
        draw_sierpinski(length/2,depth-1)
        t.fd(length/2)
        draw_sierpinski(length/2,depth-1)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        draw_sierpinski(length/2,depth-1)
        t.left(60)
        t.bk(length/2)
        t.right(60)

window = turtle.Screen()
t = turtle.Turtle()
draw_sierpinski(100,2)
window.exitonclick()
