# Import the required modules
from tkinter import Tk, Button, Label, Text, filedialog, messagebox, StringVar
from stegano import lsb

# Function to hide text in an image
def hide_text_in_image(image_path, secret_text, output_path):
    try:
        # Encode the secret text to UTF-8
        secret_text = secret_text.encode('utf-8')
        # Decode any unicode escape characters
        secret_text = secret_text.decode('unicode-escape')

        # Hide the secret text in the image using LSB steganography
        secret_image = lsb.hide(image_path, secret_text)
        secret_image.save(output_path)

        print("Steganography completed!")
    except Exception as e:
        raise ValueError("Failed to hide message: " + str(e))

# Function to reveal text from an image
def reveal_text_in_image(image_path):
    try:
        # Reveal the secret text from the image
        secret_text = lsb.reveal(image_path)
        # Encode the secret text to unicode-escape
        secret_text = secret_text.encode('unicode-escape')
        # Decode the secret text to UTF-8
        secret_text = secret_text.decode('utf-8')

        return secret_text
    except Exception as e:
        raise ValueError("Failed to extract message: " + str(e))

# Function to handle the image selection
def select_image():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=(("Image files", "*.png *.jpg *.jpeg"), ("All files", "*.*"))
    )
    if file_path:
        image_path.set(file_path)
        selected_image_label.config(text="Selected Image: " + file_path)

# Function to handle hiding the message in the image
def hide_message():
    image_file = image_path.get()
    secret_message = secret_text.get("1.0", "end-1c")
    output_file = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=(("PNG files", "*.png"), ("All files", "*.*"))
    )

    if image_file and secret_message and output_file:
        try:
            hide_text_in_image(image_file, secret_message, output_file)
            messagebox.showinfo("Steganography", "Message hidden successfully!")
        except Exception as e:
            messagebox.showerror("Steganography", str(e))
    else:
        messagebox.showwarning("Steganography", "Please select an image, enter a secret message, and choose an output file.")

# Function to handle extracting the message from the image
def extract_message():
    image_file = image_path.get()

    if image_file:
        try:
            secret_message = reveal_text_in_image(image_file)
            secret_text.delete("1.0", "end")
            secret_text.insert("1.0", secret_message)
        except Exception as e:
            messagebox.showerror("Steganography", str(e))
    else:
        messagebox.showwarning("Steganography", "Please select an image.")

# Create the main window
window = Tk()
window.title("Steganography Tool By N404R")
window.geometry("800x650") 
window.configure(bg="#f5f4e8")

# Create a StringVar to store the selected image path
image_path = StringVar()

# Create the title label
title_text = Label(window, text="Steganography Tool By N404R", font=("Arial", 15, "bold"), bg="#f5f4e8")
title_text.pack(pady=10, side="top")

# Create the 'Select Image' button
select_button = Button(window, text="Select Image", command=select_image, bg="#4287f5", fg="white")
select_button.pack(pady=10)

# Create the label to display the selected image path
selected_image_label = Label(window, text="Selected Image: None", bg="#f5f4e8")
selected_image_label.pack(pady=10)

# Create the label and text box for entering the secret text
secret_text_label = Label(window, text="Secret Text:", bg="#f5f4e8")
secret_text_label.pack()
secret_text = Text(window, height=8, width=40, font=("Arial", 12), wrap="word", relief="solid", bd=1)
secret_text.pack()

# Create the 'Hide Message' button
hide_button = Button(window, text="Hide Message", command=hide_message, bg="#4287f5", fg="white")
hide_button.pack(pady=10)

# Create the 'Extract Message' button
extract_button = Button(window, text="Extract Message", command=extract_message, bg="#4287f5", fg="white")
extract_button.pack(pady=10)

# Create the disclaimer and copyright texts
disclaimer_text = '''Disclaimer:

This project is created solely for educational purposes as part of a college assignment. The purpose of this project is to demonstrate the concept of steganography and its implementation using Python and the Stegano library. The project does not promote or endorse any illegal or unethical use of steganography techniques.

The project and its creators do not take any responsibility for the misuse of this tool or any consequences arising from its usage. Any unauthorized use or dissemination of hidden information in images is strictly prohibited.

Users are advised to use this tool responsibly and within legal and ethical boundaries. The creators of this project shall not be held liable for any damages, losses, or legal implications resulting from the misuse or improper use of this tool.

By using this project, you agree to the terms and conditions mentioned above.
'''

copyright_text = '''Copyright (c) 2023 N404R
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
'''

# Function to display the disclaimer message
def show_disclaimer():
    messagebox.showinfo("Disclaimer", disclaimer_text)

# Function to display the copyright message
def show_copyright():
    messagebox.showinfo("Copyright", copyright_text)

# Create the 'Disclaimer' button
disclaimer_button = Button(window, text="Disclaimer", command=show_disclaimer, bg="#ffb677", fg="black")
disclaimer_button.pack(side="left", padx=10)

# Create the 'Copyright' button
copyright_button = Button(window, text="Copyright", command=show_copyright, bg="#ffb677", fg="black")
copyright_button.pack(side="right", padx=10)

# Create the labels for the steps
steps_label = Label(window, text="How to Use:", font=("Arial", 12, "bold"), bg="#f5f4e8")
steps_label.pack(pady=10)

step1_label = Label(window, text="1. Click 'Select Image' to choose an image file.", bg="#f5f4e8", wraplength=400)
step1_label.pack()
step2_label = Label(window, text="2. Enter your secret message in the 'Secret Text' field.", bg="#f5f4e8", wraplength=400)
step2_label.pack()
step3_label = Label(window, text="3. Click 'Hide Message' to hide the secret message in the selected image.", bg="#f5f4e8", wraplength=400)
step3_label.pack()
step4_label = Label(window, text="4. To extract the hidden message, click 'Extract Message'.", bg="#f5f4e8", wraplength=400)
step4_label.pack(pady=10)

# Start the main window's event loop
window.mainloop()