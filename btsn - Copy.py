# Welcome to Back to School Night!

# This is a comment and is ignored by the computer.  They are used to make a program
# easier to read by humans.  Comments always start with a "#" sign.
# Tonight you are going to create simple programs using Python and Turtle.

# The line below allows python to use turtle commands. Notice it does NOT have a "#" in front.  This means
# the computer will try to follow the instruction.

import turtle

# The turtle has many commands it can understand.  One of those is forward.  The line below tells the turtle to
# go forward 100 pixels.

turtle.forward(100)

# To see what this line does, go to the Run menu and choose Run.  Then choose btsn.  A new window should open
# and you should see a line with a triangle shape at the end.  That triangle is the turtle (you have to use
# your imagination a bit).

# Challenge 1 - Change the command in line 14 so that the turtle goes forward 200 pixels.  When finished, run
# the program again.

# The turtle can do other things as well.  For example, the turtle can turn left or right.  The command below causes
# the turtle to turn 90 degrees to the left.  Remove the "#" from the beginning of the line and run the program
# to see what happens.

#turtle.left(90)

# Notice that the turtle is now facing "up."  Remove the "#" from line 33 and run the program to see that the
# turtle goes forward in the direction it is facing.

#turtle.forward(200)

# Challenge 2 - In the space below, add lines that will complete the square that is already half-drawn.


# Challenge 3 - Use the turtle to draw a hexagon.  Hint/Reminder: A hexagon has 6 sides and the turtle will need
# to turn 60 degrees each time.  If you don't want to see the square again, put a "#" in front of all the commands
# except the import turtle line.  You can make the hexagon any size you want.




# Congratulations!  You are well on your way to becoming a Python programmer.  If, however, after writing line after
# after line of "turtle.forward and turtle.left" you thought, "There has got to be a better way." you would
# be right.

# There is a way in Python (and most other languages) to repeat steps.  These are called loops.  In Python, a loop is
# written as:
# for x in range(4):
#     turtle.forward(100)
#     turtle.left(90)
# The first line tells how many times to do something and the indented lines underneath describe WHAT to do that many
# times.  The loop above is a shorter way to make a square!

# Challenge 4 - Comment out (put a "#" in front of) all the lines except for import turtle.  Can you write a loop
# that will make a hexagon?



# Final Challenge - A dodecagon is a twelve-sided figure with exterior angles of 30 degrees.  Use a loop to create
# a dodecagon.




# This final line keeps the drawing window open until you click the red x to close it.  Try putting a "#" in front
# of the command to see what effect that has.  Don't forget to take the "#" away to keep the window open.
turtle.exitonclick()