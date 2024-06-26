import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
from PIL import Image
def split_handwritten_text(image_path, output_dir):
 # קרא את התמונה
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # סף את התמונה כדי להפוך אותה לשחור-לבן
    _, thresh = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
    # מצא קונטורים (מתארים) של האותיות
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # סדר את הקונטורים משמאל לימין
    contours = sorted(contours, key=lambda ctr:
    cv2.boundingRect(ctr)[0])
 # עבור כל קונטור, חתוך את האזור הרלוונטי ושמור אותו כתמונה נפרדת
    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        letter_crop = img[y:y+h, x:x+w]
        letter_img = Image.fromarray(letter_crop)
        letter_img.save(f"{output_dir}/letter_{i}.png")
def upload_image():
    # Open a file dialog to select an image
    file_path = filedialog.askopenfilename()
    if file_path:
        # Load the image using PIL
        img = Image.open(file_path)
        img = ImageTk.PhotoImage(img)

        # Create a label to display the image

        split_handwritten_text(file_path,r"C:\Users\necha\Desktop\LetterProject\cut")

# Create the main window
root = tk.Tk()
root.title("Graphology project")
root.geometry("400x400")

# Create a label with central text
title_label = tk.Label(root, text="Upload an Image of your handwriting, lowercase only.", font=("Comic Sans MS", 12))
title_label.pack(pady=20)

# Create an upload button
upload_button = tk.Button(root, text="Upload Image", command=upload_image, font=("Comic Sans MS", 12), bg="blue")
upload_button.pack(pady=10)

# Run the main loop
root.mainloop()
