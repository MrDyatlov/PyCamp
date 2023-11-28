import tkinter.messagebox
from tkinter import *
from PIL import ImageTk, Image
import string
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import base64

# FONTs
FONT = ("Bahnschrift", 15, "normal")


# window
window = Tk()
window.title("Secret Notes")
window.minsize(300, 620)

# open int the middle | open little above-average
window.update()
width_s = window.winfo_screenwidth()
height_s = window.winfo_screenheight()
width_w = window.winfo_width()
height_w = window.winfo_height()
x = (width_s / 2) - (width_w / 2)
y = (height_s / 1.25) - (height_w)
window.geometry('%dx%d+%d+%d' % (width_w, height_w, x, y))

# space
space = Label()
# messagebox
message_box = tkinter.messagebox
# string DATA
printables = list(string.printable)
printables.remove(" ")
printables.remove("\n")

# encrypt func
def encrypt(key, secret, encode=True):
    key = SHA256.new(key).digest()
    IV = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(secret) % AES.block_size
    secret += bytes([padding]) * padding
    data = IV + encryptor.encrypt(secret)
    return base64.b64encode(data).decode("utf-8") if encode else data

# decrypt func
def decrypt(key, secret, decode=True):
    if decode:
        secret = base64.b64decode(secret.encode("utf-8"))
    key = SHA256.new(key).digest()
    IV = secret[:AES.block_size]
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(secret[AES.block_size:])
    padding = data[-1]
    if data[-padding:] != bytes([padding]) * padding:
        raise ValueError("Invalid padding...")
    return data[:-padding]

# save by encrypt func
def export_hash():
    title = title_entry.get()
    secret = secret_entry.get("1.0", END)
    key = key_entry.get()
    encrypted = encrypt(key=key.encode("utf-8"), secret=secret.encode("utf-8"))

    try:
        if title[0] in printables and key[0] in printables and secret[0] in printables:
            with open("secrets.txt", "a") as notes:
                notes.write(title + "\n")
                notes.write(encrypted + "\n\n")
                notes.close()
        elif secret[0] == " " or title[0] == " " or key[0] == " ":
            message_box.showwarning(title="Secret Warning", message="You can't start with 'space'.")
        else:
            message_box.showwarning(title="Warning", message="Please complete all form.")
    except:
        message_box.showwarning(title="Warning", message="Please complete all form.")

# decryption func
def import_hash():
    secret = secret_entry.get("1.0", END)
    key = key_entry.get()
    try:
        decryption = decrypt(key.encode("utf-8"), secret)
        #secret_entry.delete("1.0", END)
        #secret_entry.insert(INSERT, decryption.decode("latin-1"))
        message_box.showinfo(title="Secret", message=decryption.decode("utf-8"))
    except ValueError:
        message_box.showwarning(title="Key Warning", message="Incorrect password.")


# image
png = ImageTk.PhotoImage(Image.open("cia.png").resize(size=(200, 200)))
image_label = Label(image= png)
image_label.pack()

# title label
title_label = Label(text="Title of Secret", font=FONT)
title_label.pack()

# title entry
title_entry = Entry(width=30)
title_entry.focus()
title_entry.pack()

space.pack()

# secret label
secret_label = Label(text="Secret", font=FONT)
secret_label.pack()

# secret textbox
secret_entry = Text(width=30, height=10,  spacing1=1)
secret_entry.pack()


space.pack()


# key label
key_label = Label(text="Key of Secret", font=FONT)
key_label.config(pady=10)
key_label.pack()



# key entry
key_entry = Entry(width=30)
key_entry.pack()


# save by encrypt button
save_and_encrypt = Button(text="Save by Encrypt", command=export_hash)
save_and_encrypt.config(pady=15, border=0)
save_and_encrypt.pack()

# decrypt button
decrypt_butt = Button(text="Decrypt", command=import_hash)
decrypt_butt.config(pady=10, border=0)
decrypt_butt.pack()

window.mainloop()
