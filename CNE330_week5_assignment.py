# This is my last assignment for CNE330. It draws half of a triangle using * and for loops
# Author: Mason Jones, mcjones@student.rtc.edu
# Create Date: 10/15/2024


def draw_right_triangle(depth):
    triangle = ""                   # creates a string that we can add the triangle to
    for row in range(depth):
        for column in range(
                row + 1):           # add 1 to row because row starts at 0. Still 5 iterations
            triangle += "*"
        triangle += "\n"            # creates a newline after each star row
    return triangle

print(draw_right_triangle(5))       # height of 5, prints the returned triangle string
