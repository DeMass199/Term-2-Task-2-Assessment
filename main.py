import gooeypie as gp

def toggle(event):
    secret.toggle()

def on_text_change(event):
    text = secret.text

    # length check

    if len(text) < 10:
        Label_length.text = f'{checkbox_false} Password does not meet length requirements'
    else:
        Label_length.text = f'{checkbox_true} Password meets the requirement'


    # upper check
    found_upper = False
        
    for char in text:
        if char.isupper():
            found_upper = True
        
    
    if found_upper == False:
        Label_upper.text = f'{checkbox_false} Password needs to have an upper character'
    else:
        Label_upper.text = f'{checkbox_true} Password contains an upper characeter'

    found_num = False

    for char in text:
        if char.isnumeric():
            found_num = True
        

    if found_num == False:
        Label_num.text = f'{checkbox_false} Password needs to have at least one number'
    else:
        Label_num.text = f'{checkbox_true} Password meets this requirment'
       
    

    found_alpha = False # have a variable that starts as False, that can be changed to true later on...
    found_digit = False  
    symbol_detected = False 

    # check for symbols 
    # if its not a letter or a number, then it must be a symbol

    for char in text:
        if char.isalpha():
            found_alpha = True
        break

    for char in text:
        if char.isdigit():
            found_digit = True
        break



    if found_alpha == True:
        Label_symbol.text = f'{checkbox_false} Password need to have at least one Symbol'
    elif found_digit == True:
        Label_symbol.text = f'{checkbox_false} Password need to have at least one Symbol'
    else:
        symbol_detected == True 
        Label_symbol.text = f'{checkbox_true} Password meets this requirment '




        
        # if char.isalpha(): 
        #     Label_symbol.text = f'{checkbox_false} Password need to have at least one Symbol'
        # elif char.isdigit():
        #     Label_symbol.text = f'{checkbox_false} Password need to have at least one Symbol'
        # else:
        #     Label_symbol.text = f'{checkbox_true} Password meets this requirment '
        
# isdigit():
    
    # If it meet all the above requirment then it will say that the password is strong unless it has
    # been related to any data breach.


def submit(event):
    lbl.text = "It works"


# window properties     
app = gp.GooeyPieApp('SPC (Secure password Checker)')
app.width = 800
app.height = 280
app.title = "Password Checker"
app.set_grid(6, 2)

# instantiate widgets 
label = gp.Label(app, f'Please type in your password to be checked in the Box below')
Label_length = gp.Label(app, f'Password must have a Length greater then 10')
Label_upper = gp.Label(app, f'Password must contain at least on uppercase letter A-Z')
Label_num = gp.Label(app, f'Password must contain at least one number 0-9')
Label_symbol = gp.Label(app, f'Password must contain at least one symbol, ! @ # $ % ^ & * () ? <> : "" - + = _ [] ; , . / ')
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
app.add(Label_num,5,1, align='center')
app.add(Label_symbol,6,1, align='center')
# app.add(Label_symbol,6,1, align='center')
app.add(check, 2, 2, align='center')



# event listeners for each widget
check.add_event_listener('change', toggle)
secret.add_event_listener('change',on_text_change)

# run the app
app.run()




