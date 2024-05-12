import gooeypie as gp
#imports all the classes downloaded via the
# pip

app = gp.GooeyPieApp('Hello!')

app.width = 600
app.height = 400
app.title = "Password Checker"
# sets the width attributes to 1000

# set up Grid
app.set_grid(2, 1)

def submit(event):
    lbl.text = "It works"

#create some widget
btn = gp.Button(app, "Submit", submit)
lbl = gp.Label(app, '')
# put stuff in Grid!!!
app.add(btn,1,1, align='center')
app.add(lbl,2,1, align='center')

app.run()

