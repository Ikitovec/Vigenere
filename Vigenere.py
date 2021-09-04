from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter import messagebox


def clicked():
    if ((combo2.get() == 'Зашифровать') | (combo2.get() == 'Расшифровать')):
        txt_original = txt.get("1.0", 'end-1c').lower()
        key1=txt2.get("1.0", 'end-1c').lower()

        txt4.delete(1.0, END)
        flag=0
        eng_low_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        rus_low_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        alphabet=''

        for i in txt_original:
            if eng_low_alphabet.find(i,0)!=-1:
                alphabet=eng_low_alphabet
                break
            elif rus_low_alphabet.find(i,0)!=-1:
                alphabet=rus_low_alphabet
                break
        if alphabet=='':
            flag=1
            messagebox.showinfo('Ошибка!', f'Не удалось определить алфавит!')

        for i in key1:
            if alphabet.find(i)==-1:
                flag=1
                messagebox.showinfo('Ошибка!', f'В ключе должны быть только буквы!')
                break

        if flag==0:
            temp=0
            for i in txt_original:
                if (alphabet.find(i,0)!=-1):


                    if combo2.get() == "Зашифровать":
                        index = alphabet.find(f'{i}', 0)
                        step = alphabet.find(f'{key1[temp % len(key1)]}', 0)
                        txt4.insert(INSERT,alphabet[(index+step) % len(alphabet)])

                    elif combo2.get() == "Расшифровать":
                        index = alphabet.find(f'{i}', 0)

                        step = alphabet.find(f'{key1[temp % len(key1)]}', 0)

                        txt4.insert(INSERT, alphabet[(index - step) % len(alphabet)])

                    temp += 1
                else:
                    txt4.insert(INSERT, i)


    else:
        messagebox.showinfo('Ошибка!', f'Вы неверно ввели действие! (Зашифровать или Расшифровать)')

def swap():
    temporary=txt4.get("1.0", 'end-1c')
    txt.delete(1.0, END)
    txt.insert(INSERT, temporary)
    txt4.delete(1.0, END)


window = Tk()
window.title("Шифр Вижинера")
window.geometry('500x600')

lbl = Label(window, text="Ваше сообщение:")
lbl.grid(column=0, row=0)


lbl = Label(window, text="Действие:")
lbl.grid(column=0, row=5)


combo2 = Combobox(window)
combo2['values'] = ("Зашифровать", "Расшифровать")
combo2.current(0)
combo2.grid(column=2, row=5)



btn = Button(window, text="Получить ответ", command=clicked)
btn.grid(column=0, row=16)
lbl = Label(window)

btn = Button(window, text="Перенести результат в исходное сообщение", command=swap)
btn.grid(column=2, row=16)
lbl = Label(window)




txt = scrolledtext.ScrolledText(window, width=40, height=1)
txt.grid(column=2, row=0)

lbl = Label(window, text="Первый ключ:")
lbl.grid(column=0, row=9)
txt2 = scrolledtext.ScrolledText(window, width=40, height=1)
txt2.grid(column=2, row=9)



lbl = Label(window, text="Результат:")
lbl.grid(column=0, row=13)
txt4 = scrolledtext.ScrolledText(window, width=40, height=1)
txt4.grid(column=2, row=13)


window.mainloop()

