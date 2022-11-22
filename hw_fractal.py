#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle as tl

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string


def draw_l_system(instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            tl.forward(distance)
        elif cmd == '+':
            tl.right(angle)
        elif cmd == '-':
            tl.left(angle)


# In[ ]:


#scale = 400
tl.pensize(2)
#tl.penup()
#tl.goto(-scale, -scale/4)
#tl.pendown()

axiom = "FX+FX+FX"
rules = {"X":"X+YF+", "Y":"-FX-Y"}
iterations = 8
angle = 90
distance = 12
tl.color("purple")
tl.speed(100)

instructions = create_l_system(iterations, axiom, rules)
draw_l_system(instructions, angle, distance)

tl.done()


# In[ ]:




