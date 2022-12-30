from tkinter import *
from tkinter import ttk, messagebox
# use pip install googletrans==4.0.0-rc1 to install googletrans lib
import googletrans
from googletrans import Translator
from threading import *

root = Tk()
root.title("Translator V4.2.1")
root.geometry("1070x380")
root.resizable(False, False)
# root.configure(background="white")


# threading
def threading():
    # call the work function
    thread1 = Thread(target=translate_now)
    thread1.start()


# label update function
def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)


def translate_now():
    text_ = text1.get(1.0, END)
    t1 = Translator()

    try:
        trans_text = t1.translate(text=text_, src=combo1.get(), dest=combo2.get(), )
        trans_text = trans_text.text

        text2.delete(1.0, END)
        text2.insert(END, trans_text)

    except ValueError:
        messagebox.showwarning("Error", "Select a language")

    except IndexError:
        messagebox.showwarning("Error", "Empty Field")

    except TimeoutError:
        messagebox.showinfo("Connection lost", "Please try again!")


# icon
image_icon = PhotoImage(file="Translate.png")
root.iconphoto(False, image_icon)


# arrow
arrow_image = PhotoImage(file="arrow2.png")
image_label = Label(root, image=arrow_image, width=150, height=150)
image_label.place(x=460, y=50)


language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()


# first combobox
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=118, y=20)
combo1.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", width=18, bd=2, relief=GROOVE)
label1.place(x=10, y=50)

# second combobox
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="segoe 30 bold", width=18, bd=2, relief=GROOVE)
label2.place(x=620, y=50)

# first frame
f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Tobote 20", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


# Second frame
f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Tobote 20", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


# translate button
translate = Button(root, text="Translate", font=("Roboto", 15), cursor="hand2", bd=1,
                   width=10, height=2, bg="black", fg="white", command=threading)
translate.place(x=476, y=250)


# footer label
footerLabel = Label(root, text="Translator V4.2.1 Created by Maruf Ahmed © 2022", font="segoe 8 italic", fg="gray")
footerLabel.place(x=8, y=360)



# update label call
label_change()

root.mainloop()
