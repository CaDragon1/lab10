##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

# House walls
houseBody = drawpad.create_rectangle(250, 250, 550, 550)
# Roof
houseRoofOne = drawpad.create_line(150, 250, 400, 50)
houseRoofTwo = drawpad.create_line(400, 50, 650, 250)
houseRoofThree = drawpad.create_line(150, 250, 650, 250)
# Door
houseDoor = drawpad.create_rectangle(360, 400, 440, 550)
# Windows
windowOne = drawpad.create_rectangle(275, 410, 340, 475)
windowTwo = drawpad.create_rectangle(460, 410, 525, 475)

root.mainloop()
