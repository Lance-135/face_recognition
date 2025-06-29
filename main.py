import tkinter as tk
from encoder import encode_faces
from recognizer import FaceRecognizer
from test import capture_image

window = tk.Tk()

def take_image():
    capture_image(window)

def mtcnn_recog():
    encode_faces()
    recognizer = FaceRecognizer()
    recognizer.recognize_from_video(window, 1)

def yolov8_recog():
    encode_faces()
    recognizer = FaceRecognizer()
    recognizer.recognize_from_video(window, 2)

def main():
    window.title("Face Recognition System")
    window.geometry("500x800")
    window.configure(bg="#f0f0f0")

    # Heading Label
    title = tk.Label(
        window,
        text="Face Recognition App",
        font=("Helvetica", 20, "bold"),
        bg="#f0f0f0",
        pady=5
    )
    title.pack()

    # Frame to hold buttons
    button_frame = tk.Frame(window, bg="#f0f0f0")
    button_frame.pack(pady=10)

    # Button styling
    button_style = {
        "font": ("Helvetica", 12),
        "bg": "#4CAF50",
        "fg": "white",
        "padx": 20,
        "pady": 0,
        "bd": 0,
        "relief": "ridge",
        "width": 25
    }

    tk.Button(button_frame, text="➕ Add Image", command=take_image, **button_style).pack(pady=3)
    tk.Button(button_frame, text="📸 Start Detection (MTCNN)", command=mtcnn_recog, **button_style).pack(pady=3)
    tk.Button(button_frame, text="🤖 Start Detection (YOLOv8)", command=yolov8_recog, **button_style).pack(pady=3)
    tk.Button(button_frame, text="🚪 Quit App", command=exit, **button_style).pack(pady=3)

    window.protocol("WM_DELETE_WINDOW", exit)
    window.mainloop()

main()
