import gooeypie as gp

app = gp.GooeyPieApp('Hello!')

app.width = 250
hello_btn = gp.Button(app, 'Say Hello', None)
hello_lbl = gp.Label(app, '')
app.set_grid(2, 1)
app.add(hello_btn, 1, 1, align='center')
app.add(hello_lbl, 2, 1, align='center')

app.run()

