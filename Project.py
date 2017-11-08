# import the library
from appJar import gui

# handle button events
def press(button):
    if button == "Sum" or button =="Difference":

        app.showSubWindow("Frist Equation")
        Frist_Equation = app.getEntry("Equation one")
        print("Frist_Equation=",Frist_Equation)
        app.showSubWindow("Second Equation")
        Second_Equation = app.getEntry("Equation two")
        print("Second_Equation=", Second_Equation)



# create a GUI variable called app
app = gui("Login Window", "600x600")
app.setBg("white")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to Pynomail Caculator")
app.setLabelBg("title", "yellow")
app.setLabelFg("title", "purple")

app.addLabel("Choice","Chosse the opperation")
app.setLabelFg("Choice", "purple")
# link the buttons to the function called press


app.addButton("Sum", press)
app.addButton("Difference", press)


#pop window for the frist equation
app.startSubWindow("Frist Equation")
app.addLabel("l1", "add Frist Equation to this window")
# set the button's name to match the SubWindow's name
app.addEntry("Equation one")
app.setFocus("Equation one")

app.addNamedButton("Submit", "Frist Equation", app.hideSubWindow)
app.stopSubWindow()
#pop window for the Second equation
app.startSubWindow("Second Equation")
app.addLabel("l5", "add Second Equation to this window")
app.addEntry("Equation two")
app.setFocus("Equation two")
# set the button's name to match the SubWindow's name

app.addNamedButton("Submit", "Second Equation", app.hideSubWindow)
app.stopSubWindow()


# start the GUI/
app.go()
