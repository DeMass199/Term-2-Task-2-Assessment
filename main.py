import gooeypie as gp

def toggle(event):
    question.toggle()

def on_text_change(event):
    text = secret.text

    if len(text) < 10:
        Label_length.text = f'{checkbox_false} Password does not meet length requirements'
    else:
        Label_length.text = f'{checkbox_true} Password meets length requirements'

    # elif gp.search("[A-Z]", text):
    #     print("Password must contain at least on uppercase letter.")

    # elif gp.search("[a-z]", text):
    #     print("Password must contain at least on lowercase letter.")

    # elif gp.search("[0-9]", text):
    #     print("Password must contain at least one number.")   
    # else:
    #     print("password is strong")
  
def submit(event):
    lbl.text = "It works"


# window properties     
app = gp.GooeyPieApp('SPC (Secure password Checker)')
app.width = 700
app.height = 280
app.title = "Password Checker"
app.set_grid(6, 2)

# instantiate widgets 
label = gp.Label(app, f'Please type in your password to be checked in the Box below')
Label_length = gp.Label(app, f'Password must have a Length greater then 10')
Label_upper = gp.Label(app, f'Password must contain at least on uppercase letter A-Z')
Label_lower = gp.Label(app, f'Password must contain at least on lowercase letter a-z')
Label_num = gp.Label(app, f'Password must contain at least one number 0-9')
secret = gp.Secret(app)
secret.width = 50
checkbox_true = "✅"
checkbox_false = "❌"
check = gp.Checkbox(app, '🪬 Show password')
btn = gp.Button(app, "Submit", submit)
lbl = gp.Label(app, '')

# place / add widgets in window
app.add(label,1,1, align='center')
app.add(secret,2,1, align='center')
app.add(Label_length,3,1, align='center')
app.add(Label_upper,4,1, align='center')
app.add(Label_lower,5,1, align='center')
app.add(check, 2, 2, align='center')
# app.add(btn,1,1, align='center')
# app.add(lbl,2,1, align='center')


# event listeners for each widget
check.add_event_listener('change', toggle)
secret.add_event_listener('change',on_text_change)

# run the app
app.run()











#create some widget


# put




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

# This Code is for Strong or not strong enough passwords: 
# import gooeypie as gp

# def login(event):
#     if pass_inp.text == 'bestpassword':
#         status_lbl.text = '✔ Access granted!'
#     else:
#         status_lbl.text = '❌ Access denied!'

# app = gp.GooeyPieApp('Login')

# user_lbl = gp.Label(app, "Username")
# user_inp = gp.Input(app)
# pass_lbl = gp.Label(app, "Password")
# pass_inp = gp.Secret(app)
# login_btn = gp.Button(app, 'Login', login)
# status_lbl = gp.Label(app, '')

# app.set_grid(4, 2)
# app.add(user_lbl, 1, 1)
# app.add(user_inp, 1, 2)
# app.add(pass_lbl, 2, 1)
# app.add(pass_inp, 2, 2)
# app.add(login_btn, 3, 2)
# app.add(status_lbl, 4, 2)

# app.run()