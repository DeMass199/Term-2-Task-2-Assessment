import gooeypie as gp
from word_checker import check_if_contained_in_txt

def toggle(event):
    secret.toggle()

def on_text_change(event):
    progress_score = 100
    negative = 20
    text = secret.text
    
    if checkbox_false == False:
        print(progress_score)
        progress_score -=20
    else: 
        checkbox_true == True

    # length check
    if len(text) < 10:
        Label_length.text = f'{checkbox_false} Password does not meet length requirements'
        progress_score -= negative
       
    else:
        Label_length.text = f'{checkbox_true} Password meets the length requirement'

    # upper check
    found_upper = False
        
    for char in text:
        if char.isupper():
            found_upper = True
        
    
    if found_upper == False:
        Label_upper.text = f'{checkbox_false} Password needs to have an upper character'
        progress_score -= negative
    else:
        Label_upper.text = f'{checkbox_true} Password contains an upper characeter'

    found_num = False

    for char in text:
        if char.isnumeric():
            found_num = True
        

    if found_num == False:
        Label_num.text = f'{checkbox_false} Password needs to have at least one number'
        progress_score -= negative
    else:
        Label_num.text = f'{checkbox_true} Password meets the at least one number requirment'
       


    symbol_checker = False

    for char in text:
        if not char.isalnum():
            symbol_checker = True
            
     
    if symbol_checker == False:
        Label_symbol.text = f'{checkbox_false} Password need to have at least one Symbol'
        progress_score -= negative
    else:
        Label_symbol.text = f'{checkbox_true} Password meets the symbol requirment'

    label_common.text = " "
    if check_if_contained_in_txt(text):
        label_common.text = f'{checkbox_false} Password contains a common text'
        progress_score -= negative
        # print("ALERT")
    else:
        label_common.text = f'{checkbox_true} Password does not contain any common text'

    if progress_score == 100:
        progress.text = "⭐️⭐️⭐️⭐️⭐️"
        print("⭐️⭐️⭐️⭐️⭐️")
    elif progress_score == 80:
        progress.text = "⭐️⭐️⭐️⭐️"
        print("⭐️⭐️⭐️⭐️")
    elif progress_score == 60:
        progress.text = "⭐️⭐️⭐️"
        print("⭐️⭐️⭐️")
    elif progress_score == 40:
        progress.text = "⭐️⭐️"
        print("⭐️⭐️")
    elif progress_score == 20:
        progress.text = "⭐️"
        print("⭐️")
    else:
        progress.text = "Password is very weak"
        print("Password is very weak")

    
    # If it meet all the above requirment then it will say that the password is strong.
    # Then it will check if it has been related to any data breach.

def submit(event):
    lbl.text = "It works"

# window properties     
app = gp.GooeyPieApp('SPC (Secure password Checker)')
app.width = 800
app.height = 280
app.title = "Password Checker"
app.set_grid(7, 3)

# instantiate widgets 
label = gp.Label(app, f'Please type in your password to be checked in the Box below')
Label_length = gp.Label(app, f'Password must have a Length greater then 10')
Label_upper = gp.Label(app, f'Password must contain at least on uppercase letter A-Z')
Label_num = gp.Label(app, f'Password must contain at least one number 0-9')
Label_symbol = gp.Label(app, f'Password must contain at least one symbol, ! @ # $ % ^ & * () ? <> : "" - + = _ [] ; , . / ')
secret = gp.Secret(app)
label_common = gp.Label(app, f'Password must not contain a common password' )
progress = gp.StyleLabel(app, '')
secret.width = 50
checkbox_true = "✅"
checkbox_false = "❌"
check = gp.Checkbox(app, '🪬 Show password')
btn = gp.Button(app, "Submit", submit)
lbl = gp.Label(app, '')

# place / add widgets in window
app.add(label,1,1, align='center')
app.add(secret,2,1, align='center', column_span = 2)
app.add(Label_length,3,1, valign='middle')
app.add(Label_num,4,1, valign='middle')
app.add(Label_upper,5,1, valign='middle')
app.add(Label_symbol,6,1, valign='middle')
app.add(label_common,7,1, valign='middle')
app.add(check, 2, 3, valign='middle')
app.add(progress,4,2, align='center')


# event listeners for each widget
check.add_event_listener('change', toggle)
secret.add_event_listener('change',on_text_change)
# progress.add_event_listener('change',password_progressbar)
# run the app
app.run()
