import tkinter as tk 
import time, shutil

KB = 1024
MB = 1024 * KB
GB = 1024 * MB
FILESYS = "/media/jsmith/Vol250GB/" 

def label_update_loop():
  while True:
    # Update tk.StringVar with available disk space
    df = shutil.disk_usage(FILESYS).free / GB
    dftxt.set("%.2f"%df + " GB")
    wndMain.update()
    # Sleep until next update
    time.sleep(2)


# Create main window.
wndMain = tk.Tk()

# Set the size of the tkinter main window.
wndMain.geometry("180x50")

# Initialize a tkinter StringVar
dftxt = tk.StringVar()

# Create label widgets
label1 = tk.Label(wndMain, text=FILESYS, font='Arial 10')
label2 = tk.Label(wndMain, textvariable=dftxt, font='Arial 17 bold')
label1.pack(pady=0)
label2.pack(pady=2)

label_update_loop()
wndMain.mainloop()
