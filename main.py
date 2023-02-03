import tkinter as Tk


app = Tk.Tk()
app.geometry("440x580")  # Размеры окна
app.title("Calculator")  # Название программы
app.resizable(False, False)  # Запрет на изменение размера в ручную
app.configure(bg="black")

#функциональность калькулятора
def calc(operation):
    global window

    if operation == "C":
        window = ""
    elif operation == "del":
        window = window[0:-1] #удаление одного значения
    elif operation == "=":
        window = str(eval(window))
    elif operation == "x²":
        window = str((eval(window) **2))
    else:
        if window == "0":
            window = ""
        window += operation
    label_text.configure(text=window)

#поле вывода
window = "0"
label_text = Tk.Label(text=window, font=("None", 30, "bold"), bg="black", fg="white")
label_text.place(x=20, y=50)

#создание кнопок
btns = ["%", "C", "del", "+",
        "7", "8", "9", "/",
        "4", "5", "6", "*",
        "1", "2", "3", "-",
        "x²", "0", ".", "="]
x = 18
y = 150 #отступы кнопок
for btn in btns:
    get_lbl = lambda x = btn: calc(x)
    Tk.Button(text=btn, bg="red", font=("None", 20),
              command=get_lbl).place(x=x, y=y, width=100, height=80)
    x += 102
    if x > 400:
        x = 18
        y += 81


if __name__ == "__main__":
    app.mainloop()