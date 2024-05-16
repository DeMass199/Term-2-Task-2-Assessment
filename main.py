import gooeypie as gp
#imports all the classes downloaded via the
# pip

# def on_text_change(event):
#     text = text_box.text
#     print(text)

#     if text == "Gus":
#         label.text = "🧱"
#     elif text == "Jai":
#         label.text = "-->🥷🏿🥷🏿🥷🏿🥷🏿🥷🏿🥷🏿<--"
#     elif text == "Braxton":
#         label.text = "🍕"
#     elif text == "Fong":
#         label.text = "Teacher👾💻🎮"
#     elif text == "Mitchell":
#         label.text = "🦏🦛"
#     elif text == "Jacob G":
#         label.text = "🙎🏿‍♂️"
#     elif text == "Nathan":
#         label.text = "🎮 🚫 grass"
#     elif text == "Patrick":
#         label.text = "🏀⛹🏿"
#     elif text == "Lucas":
#         label.text = "The 🇮🇹 🐐"
# #     elif text == "":
# #         label.text = ""
# #     elif text == "":
# #          label.text = ""

# app = gp.GooeyPieApp('Hello!, I am a password Checker')

# text_box = gp.Textbox(app)
# text_box.add_event_listener('change', on_text_change)

# label = gp.Label(app, 'Type in your password to be checked')

# app.width = 300
# app.height = 200
# app.title = "Password Checker"
# # sets the width attributes to 1000

# # set up Grid
# app.set_grid(2, 1)
# app.add(text_box,1,1, align='center')
# app.add(label,2,1, align='center')

# def submit(event):
#     lbl.text = "It works"

# #create some widget
# btn = gp.Button(app, "Submit", submit)
# lbl = gp.Label(app, '')
# # put stuff in Grid!!!
# app.add(btn,1,1, align='center')
# app.add(lbl,2,1, align='center')

def toggle_mask(event):
    secret.toggle()

app = gp.GooeyPieApp('Secret')

question = gp.Label(app, "What's your password?")

secret = gp.Secret(app)
secret.width = 50

check = gp.Checkbox(app, 'Show password')
check.add_event_listener('change', toggle_mask)

# setup of the grid
app.set_grid(3, 1)
app.add(question, 1, 1)
app.add(secret, 2, 1)
app.add(check, 3, 1)

app.run()

