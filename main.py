import gooeypie as gp
#imports all the classes downloaded via the
# pip

def on_text_change(event):
    text = text_box.text
    print(text)

    if text == "Gus":
        label.text = "🧱"
    elif text == "Jai":
        label.text = "🥷🏿"
    elif text == "Braxton":
        label = "🍕"
    elif text == "Fong":
        label = "👾💻🎮"
    elif text == "Mitchell":
        label = "🦏🦛"
    elif text == "Jacob G":
        label = "🙎🏿‍♂️"
    # elif text == "":
    #     label = ""
    # elif text == "":
    #     label = ""
    # elif text == "":
    #     label = ""
    # elif text == "":
    #     label = ""


app = gp.GooeyPieApp('Hello!, I am a password Checker')

text_box = gp.Textbox(app)
text_box.add_event_listener('change', on_text_change)

label = gp.Label(app, 'blank')

app.width = 600
app.height = 400
app.title = "Password Checker"
# sets the width attributes to 1000

# set up Grid
app.set_grid(2, 1)
app.add(text_box,1,1)
app.add(label,2,1)

# def submit(event):
#     lbl.text = "It works"

# #create some widget
# btn = gp.Button(app, "Submit", submit)
# lbl = gp.Label(app, '')
# # put stuff in Grid!!!
# app.add(btn,1,1, align='center')
# app.add(lbl,2,1, align='center')

app.run()

