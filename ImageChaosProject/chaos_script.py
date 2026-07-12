import tkinter as tk
from PIL import Image, ImageTk
import random
import time
import sys
import os

# Set the image path as a global variable for easier maintenance
IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'images(2).jpg')

def start_chaos():
    root = tk.Tk()
    root.withdraw()

    try:
        original_img = Image.open(IMAGE_PATH)
    except Exception as e:
        log(f"Error opening image: {e}")
        return

    start_time = time.time()
    gen_duration = 10
    wait_duration = 5

    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    img_refs = []

    while time.time() - start_time < gen_duration:
        win = tk.Toplevel(root)
        win.attributes("-topmost", True)
        win.overrideredirect(True)

        w = random.randint(100, 300)
        aspect_ratio = original_img.height / original_img.width
        h = int(w * aspect_ratio)

        resized_img = original_img.resize((w, h), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(resized_img)

        x = random.randint(0, sw - w)
        y = random.randint(0, sh - h)
        win.geometry(f"{w}x{h}+{x}+{y}")

        label = tk.Label(win, image=img_tk, bd=0)
        label.image = img_tk
        label.pack()

        img_refs.append(img_tk)
        root.update()
        time.sleep(0.1)

    time.sleep(wait_duration)
    root.destroy()

def log(message):
    log_path = os.path.join(os.path.dirname(__file__), 'chaos_log.txt')
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"{time.ctime()} - {message}\n")

if __name__ == "__main__":
    try:
        log("Chaos script started.")
        start_chaos()
        log("Chaos script finished.")
    except Exception as e:
        log(f"Unexpected error: {e}")
        sys.exit(1)
