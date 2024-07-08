import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
from PIL import Image
import cutsPictures
import numpy as np
import pandas as pd
from keras.preprocessing import image
from keras.models import load_model

#calls model
# saved_model = load_model("vgg16_1.h5")
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img = np.asarray(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0 
    return img

def upload_image():
    # select image
    file_path = filedialog.askopenfilename()
    if file_path:
        # Load the image
        img = Image.open(file_path)
        img = ImageTk.PhotoImage(img)
        
        # Display the image in a label
        # img_label.config(image=img)
        # img_label.image = img

        # Cuts the image
        # cuts_output_dir = r"C:\Users\necha\Desktop\LetterProject\cuts"
        # cutsPictures.split_handwritten_text(file_path, cuts_output_dir)

        # results = []
        # for file in cuts_output_dir:
        #     img_path = file.path
        #     img_array = preprocess_image(img_path)
        #     output = saved_model.predict(img_array)
            
        #     # List of categories
        #     categories = [str(i) for i in range(1, 26)]
            
        #     # Predictions
        #     predicted_index = np.argmax(output)
        #     predicted_category = categories[predicted_index]
        #     predicted_probability = np.max(output)
        #     results.append((predicted_category, predicted_probability))
        
        # # top 2 predictions
        # top_2_results = sorted(results, key=lambda x: x[1], reverse=True)[:2]
        # top_2_categories = [result[0] for result in top_2_results]

        # # Load explanations
        # excel_path = r"C:\Users\necha\Desktop\LetterProject\letterExplanation.xlsx"  # Update with your actual path
        # df = pd.read_excel(excel_path)
        
        # explanations = []
        # for category in top_2_categories:
        #     row_index = int(category) - 1  
        #     explanation = df.iloc[row_index, 2]  
        #     explanations.append(explanation)
        
        # messagebox.showinfo("Predictions:", f" {top_2_categories} and {explanations}")
#main window
root = tk.Tk()
root.title("Graphology project")
root.geometry("400x400")

#label with central text
title_label = tk.Label(root, text="Upload an Image of your handwriting, lowercase only.", font=("Comic Sans MS", 12))
title_label.pack(pady=20)

#upload button
upload_button = tk.Button(root, text="Upload Image", command=upload_image, font=("Comic Sans MS", 12), bg="blue")
upload_button.pack(pady=10)

# main loop
root.mainloop()
