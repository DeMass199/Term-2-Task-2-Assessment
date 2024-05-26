import gooeypie as gp
#imports all the classes downloaded via the
# pip

def toggle(event):
    question.toggle()

def on_text_change(event):
    text = text_box.text
    print(text)
 
    # if len(text) < 10:
    #     print("Your password must be at least 10 characters long.")

    # elif gp.search("[A-Z]", text):
    #     print("Password must contain at least on uppercase letter.")

    # elif gp.search("[a-z]", text):
    #     print("Password must contain at least on lowercase letter.")

    # elif gp.search("[0-9]", text):
    #     print("Password must contain at least one number.")   
    # else:
    #     print("password is strong")
        
app = gp.GooeyPieApp('Hello!, I am a password Checker')

question = gp.Secret(app)
label = gp.Label(app, 'Please type in your password in the Box below')
label_2 = gp.Label(app, 'Password must contain at least on uppercase letter')
label_3 = gp.Label(app, 'Password must contain at least on lowercase letter')
label_4 = gp.Label(app, 'Password must contain at least one number')
# This is where the users password is.

secret = gp.Secret(app)
secret.width = 50
app.width = 600
app.height = 300
app.title = "Password Checker"
# sets the width attributes to 500

text_box = gp.Textbox(app)
text_box.add_event_listener('change', on_text_change)
check = gp.Checkbox(app, '🪬 Show password')
check.add_event_listener('change', toggle)

# app.set_column_weights(column1_weight, column2_weight)
# app.set_row_weights(row1_weight, row2_weight)

# set up Grid
app.set_grid(5, 2)
# app.set_column_weights(0, 1)

# # The second row will grow twice as much as the first row
# app.set_row_weights(1, 2)
app.add(label,1,1, align='center')
app.add(question,2,1, align='center')
app.add(label_2,3,1, align='center')
app.add(label_3,4,1, align='center')
app.add(label_4,5,1, align='center')
app.add(check, 2, 2, align='center')


app.run()


def submit(event):
    lbl.text = "It works"

#create some widget
btn = gp.Button(app, "Submit", submit)
lbl = gp.Label(app, '')

# put stuff in Grid!!!
app.add(btn,1,1, align='center')
app.add(lbl,2,1, align='center')




# Need to have a password checker that will read the passwords
# symbols and if it doesn't have enough figures (8-10) it is
# a weak password. Then provide a option to the slider for a 
# more secure password.

# put a slider in that will provide auto generated password 
# that is stronger or weaker passcode based on there choice.



# SCRAPPED CODE:
# def toggle_mask(event):
#     secret.toggle()

# app = gp.GooeyPieApp('Password checker')

# question = gp.Label(app, "What's your password?")

# # This is where the users password is.
# secret = gp.Secret(app)
# secret.width = 50

# # This makes the code visible
# check = gp.Checkbox(app, '🪬 Show password')
# check.add_event_listener('change', toggle_mask)

# # setup of the grid
# app.set_grid(3, 1)
# app.add(question, 1, 1)
# app.add(secret, 2, 1)
# app.add(check, 3, 1)

# app.run()

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