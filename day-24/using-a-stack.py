#! /usr/bin/env python3

import math


PARAMETERS = [
    [11, 1, 6],    # 0  - a
    [11, 1, 12],
    [15, 1, 8],
    [-11, 26, 7],  # 3  - d
    [15, 1, 7],
    [15, 1, 12],
    [14, 1, 2],    # 6  - g
    [-7, 26, 15],
    [12, 1, 4],
    [-6, 26, 5],   # 9  - j
    [-10, 26, 12],
    [-15, 26, 11],
    [-9, 26, 13],  # 12
    [0, 26, 7],
]


model_number = 99999999999999
model_iter = (x for x in str(model_number))
z = 0

for ix in range(14):
    w = next(model_iter)
    x = z % 26

    z = math.trunc(z / PARAMETERS[ix][1])
    x += PARAMETERS[ix][0]

    if x != w:
        z *= 26
        y = w + PARAMETERS[ix][2]
        z += y



model_iter = (x for x in str(model_number))
stack = [0]

for ix in range(14):
    w = next(model_iter)
    x = stack[-1]

    if ix in [3, 7, 9, 10, 11, 12, 13]:
        stack.pop()
    x += PARAMETERS[ix][0]

    if x != w:
        y = w + PARAMETERS[ix][2]
        stack.push(y)


# Pop things off the stack in steps 3, 7, and 9-13
# Then, we push something back on the stack right afterwards
# But, that means that (in certain circumstances), the entries
# from steps 2, 6, 8, 9, 10, 11, and 12 are no longer on the stack







#    |    |  ||| || <-- pop
# abcd efgh ijkl mn

# ix = 0
stack == [0]
stack.push(a + 6)


# ix = 1
stack == [0, a+6] 
x = (a + 6) + 11
x = a + 17
stack.push(b + 12)


# ix = 2
stack == [0, a+6, b+12]
x = (b + 12) + 15
x = b + 27
stack.push(c + 8)


# ix = 3
stack == [0, a+6, b+12, c+8]
stack.pop()
stack == [0, a+6, b+12]
x = c + 8 + -11
x = c - 3

if d != c - 3:
    stack.push(d + 7)


# ix = 4
stack == [0, a+6, b+12, ???]

# Since both routes give x as being far more than a digit,
# it doesn't matter what happened in step 3 - we're pushing
# `d = 7` to the stack
    # if d != c - 3:
    #     x = (d + 7) + 15
    #     x = d + 22          # <-- different from w
    #     stack.push(e + 7)
    # else:
    #     x = (b + 12) + 15
    #     x = b + 27          # <-- different from w
    #     stack.push(e + 7)
stack.push(e + 7)


# ix = 5
stack == [0, a+6, b+12(, c+8), d+7, e+7]
x = (e+7) + 15
x = e + 22
stack.push(f + 12)


# ix = 6
stack == [0, a+6, b+12(, c+8), d+7, e+7, f+12]
x = (f+12) + 14
x = f + 26
stack.push(g + 2)


# ix = 7
stack == [0, a+6, b+12(, c+8), d+7, e+7, f+12, g+2]
stack.pop()
x = (g+2) - 7
x = g - 5

if h != g - 5:
    stack.push(h + 15)


# ix = 8
stack = [0, a+6, b+12(, c+8), d+7, e+7, f+12, g+2(, h+15)]

    # if g != f - 5:
    #     x = (g+15) + 12
    #     x = g + 27
    #     stack.push(h + 4)
    # else:
    #     x = (f+2) + 12
    #     x = f + 14
    #     stack.push(h+4)

    # Both are greater than a digit, so we're pushing `h+4`

stack.push(i + 4)


# ix = 9
stack = [0, a+6, b+12(, c+8), d+7, e+7, f+12, g+2(, h+15), i+4]
stack.pop()
x = (i+4) - 6
x = i - 2

if j != i - 2:
    push(j + 5)



# ix = 10
stack = [0, a+6, b+12(, c+8), d+7, e+7, f+12, g+2(, h+15), i+4(, j+5)]
stack.pop()

if j != i - 2:
    x = (j+5) - 10
    x = j - 5

if k != j - 5:




# ix = 11





# ix = 12





# ix = 13









