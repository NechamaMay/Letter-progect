import cv2
import numpy as np
from PIL import Image
import os
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
        # בודק גודל מינימלי
        if w < 10 or h < 10:
            continue
         # שינוי גודל התמונה לגודל מקסימלי של 224x224 תוך שמירה על יחס גובה-רוחב
        letter_pil = Image.fromarray(letter_crop)
        letter_pil.thumbnail((224, 224))
        #חותך את האות
        letter_img = Image.fromarray(letter_crop)
          # צור תמונה בגודל 224x224 עם רקע לבן
        letter_img = Image.new("L", (224, 224), 255)
        # מחשב את מיקום האות במרכז הרקע הלבן
        offset = ((224 - letter_pil.width) // 2, (224 - letter_pil.height) // 2)
        
        # הדבק את האות במרכז הרקע הלבן
        letter_img.paste(letter_pil, offset)
        letter_img.save(f"{output_dir}/letter_{i}.jpg")
import os

for i in range(1, 26):
    # בניית הנתיב של התיקיה שבה הקבצים נמצאים
    directory_path = r"C:\Users\necha\Desktop\LetterProject\dataset\train\{}".format(i)
    
    try:
        # קבלת רשימת כל הקבצים בתיקיה
        files = os.listdir(directory_path)
    except FileNotFoundError:
        print(f"Directory not found: {directory_path}")
        continue
    
    # הדפסת הנתיב של כל קובץ והפעלת הפונקציה split_handwritten_text
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        output_directory = r"C:\Users\necha\Desktop\LetterProject\dataset\train\{}.1".format(i)
        split_handwritten_text(file_path, output_directory)