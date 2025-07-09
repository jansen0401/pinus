import cv2
import os
from datetime import datetime

def capture_image():
    cap = cv2.VideoCapture(0)  # Buka kamera laptop
    if not cap.isOpened():
        print("Kamera tidak tersedia")
        return

    ret, frame = cap.read()
    if ret:
        filename = f"vision/captured/pinus_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Berhasil menyimpan gambar: {filename}")
    else:
        print("Gagal menangkap gambar")

    cap.release()
