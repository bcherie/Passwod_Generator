import string
import secrets
import tkinter as tk
from tkinter import ttk

opt_list = ["только цифры", "цифры и буквы", "цифры, буквы и символы"]
def generate_password():
    length = int(passwd_len.get())
    comb = str(selected_opt.get())
    if comb == opt_list[0]:
        letters = string.digits
    elif comb == opt_list[1]:
        letters = string.ascii_letters + string.digits
    else:
        letters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(letters) for i in range(length))

    pass_str = tk.StringVar()
    pass_str.set(password)
    res = tk.Entry(window, textvariable=pass_str, state='readonly')
    res.place(x=10, y=200, width=200, height=20)

def check_len_password(*args):
    check_l = l.get()
    if 1 <= len(check_l) <= 2:
        gen_button.config(state='normal')
    else:
        gen_button.config(state='disabled')

#инициализация окна
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x500")
window.resizable(width=False, height=False)

#элементы окна
#запрос длины пароля
label = tk.Label(window, text="Введите длину пароля")
label.place(x=10, y=20)

l = tk.StringVar(window)
l.trace("w", check_len_password)
passwd_len = tk.Entry(window, textvariable=l)
passwd_len.place(x=10, y=40)

#выбор комбинации для пароля
label_1 = tk.Label(window, text="Выберите комбинации, которые может содержать пароль")
label_1.place(x=10, y=60)

#сохранение выбора и установка значения по умолчанию для опции выбора - только цифры
selected_opt = tk.StringVar(window, opt_list[0])
offset = 0
for lang in opt_list:
    lang_btn = ttk.Radiobutton(text=lang, value=lang, variable=selected_opt)
    lang_btn.place(x=10, y=80 + offset)
    offset += 20

#кнопка генерации пароля
gen_button = tk.Button(window, text="Сгенерировать", command=generate_password, state='disabled')
gen_button.place(x=10, y=160)
gen_button.place(x=10, y=160)

window.mainloop()