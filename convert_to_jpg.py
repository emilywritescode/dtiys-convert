from PIL import Image
import os
import sys
import tkinter as tk
from tkinter import font, filedialog
from tkmacosx import Button


def convert_to_jpg(image_file):
    # Open file with Pillow
    im = Image.open(image_file)
    # Get file extension
    file_ext = os.path.splitext(image_file)[1]
    # Convert to JPG
    im.convert("RGB").save(image_file.replace(file_ext, ".JPG"), quality=100, subsampling=0)
    print(f"successfully converted {image_file} to jpg")
    # Delete original file
    os.remove(image_file)


def get_image_files(input):
    # Valid extensions of image files from iPhone
    valid_extensions = [".heic", ".png"]
    image_files = []
    # Return only the files that have valid extension
    for f in input:
        if os.path.splitext(f)[1].lower() in valid_extensions:
            image_files.append(f)

    return image_files


def select_images():
     # Ask user for image(s) to convert to JPG
     image_files = filedialog.askopenfilenames(initialdir="~/Downloads", title="Select file(s)")
     # Get valid image files to convert
     global valid_image_files
     valid_image_files = get_image_files(image_files)
     if valid_image_files:
         submit_button.config(state="normal", bg="#27AE60", activebackground="#27AE60")


def submit_to_convert():
    # Convert image(s) to JPG
    for image_file in valid_image_files:
        convert_to_jpg(image_file)
    submit_button.config(state="disabled", bg="silver", activebackground="silver")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Convert images to JPG")
    root.geometry("500x300")
    root.resizable(0, 0)

    deffont = tk.font.Font(family="PT Sans", size=16)

    select_button = Button(
        root,
        text="Select file(s) to convert",
        bg="#6FCF97",
        activebackground="#6FCF97",
        borderless=1,
        width=300,
        height=60,
        font=deffont,
        command=select_images
    )
    select_button.place(rely=0.3, relx=0.5, anchor=tk.CENTER)

    global submit_button
    submit_button = Button(
        root,
        text="Convert image(s)",
        bg="silver",
        activebackground="silver",
        borderless=1,
        width=300,
        height=60,
        font=deffont,
        state=tk.DISABLED,
        command=submit_to_convert
    )
    submit_button.place(rely=0.6, relx=0.5, anchor=tk.CENTER)


    root.mainloop()
