from ast import Lambda
import tkinter as tk

window = tk.Tk()
window.title('калькулятор')
window.geometry('500x550')
window.resizable(False, False)
window.configure(bg = 'brown')

def calculate(operation): #функция вычисления
    global formula

    if operation == 'C':
        formula = '0'
    elif operation == 'del':
        formula = formula[:-1]
    elif operation == 'X^2':
        formula = str(eval(formula) ** 2) 
    elif operation == '=':
        formula = str(eval(formula)) 
    else:
        if formula == '0':
            formula = ''
        formula += operation
    text_lbl.configure(text=formula)


formula = '0'
text_lbl = tk.Label(text = formula, font = ('Arial', 34, 'bold'), bg = 'Brown', fg = 'White')
text_lbl.place(x = 11, y = 55)


#создам кнопки
buttons = ['C', 'del', 'x^2', '*', '1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '/', '%', '0', '.', '=']
x = 18  #длина кнопки
y = 140 #ширина кнопки

for i in buttons:
    get_lbl = lambda x = i: calculate(x)
    tk.Button(text = i, bg = 'gray', font = ('Arial', 23), command = get_lbl).place(x = x, y = y, width = 110, height = 75)
    x += 115
    if x > 400 :
        x = 18
        y += 78


window.mainloop()