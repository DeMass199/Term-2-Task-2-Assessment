import gooeypie as gp
#imports all the classes downloaded via the
# pip


def on_text_change(event):
    text = text_box.text
    print(text)


    if len(text) < 10:
        print("This code it strong")
    else:
        print("This password needs some strengthening")

app = gp.GooeyPieApp('Hello!, I am a password Checker')

text_box = gp.Textbox(app)
text_box.add_event_listener('change', on_text_change)

label = gp.Label(app, 'Type in your password to be checked')

app.width = 300
app.height = 200
app.title = "Password Checker"
# sets the width attributes to 1000

# set up Grid
app.set_grid(2, 1)
app.add(text_box,1,1, align='center')
app.add(label,2,1, align='center')
    

    

def toggle_mask(event):
    secret.toggle()
    text = text_box.text
    print(text)

    
    if len(text) < 10:
        print("This code it strong")
    else:
        print("This password needs some strengthening")

app = gp.GooeyPieApp('Password checker')

question = gp.Label(app, "What's your password?")

# This is where the users password is.
secret = gp.Secret(app)
secret.width = 50

# This makes the code visible
check = gp.Checkbox(app, '🪬 Show password')
check.add_event_listener('change', toggle_mask)

# setup of the grid
app.set_grid(3, 1)
app.add(question, 1, 1)
app.add(secret, 2, 1)
app.add(check, 3, 1)

app.run()

# Need to have a password checker that will read the passwords
# symbols and if it doesn't have enough figures (8-10) it is
# a weak password. Then provide a option to the slider for a 
# more secure password.

# put a slider in that will provide auto generated password 
# that is stronger or weaker passcode based on there choice.






# SCRAPPED CODE:
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