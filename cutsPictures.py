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
        # בודק גודל מינימלי
      #   if w < 10 or h < 30:
      #       continue
      #    # שינוי גודל התמונה לגודל מקסימלי של 224x224 תוך שמירה על יחס גובה-רוחב
      #   letter_pil = Image.fromarray(letter_crop)
      #   letter_pil.thumbnail((224, 224))
      #   #חותך את האות
      #   letter_img = Image.fromarray(letter_crop)
      #     # צור תמונה בגודל 224x224 עם רקע לבן
      #   letter_img = Image.new("L", (224, 224), 255)
      #   # מחשב את מיקום האות במרכז הרקע הלבן
      #   offset = ((224 - letter_pil.width) // 2, (224 - letter_pil.height) // 2)
        
      # #   # הדבק את האות במרכז הרקע הלבן
      # #   letter_img.paste(letter_pil, offset)
        letter_crop.ravel(f"{output_dir}/letter_{i}.png")
split_handwritten_text(r"C:\Users\necha\Desktop\LetterProject\Libby.jpg", r"C:\Users\necha\Desktop\LetterProject\cuts")

