import time, shutil
import tkinter as tk # Use the tkinter GUI

KB = 1024
MB = 1024 * KB
GB = 1024 * MB
FSPATH = "/media/jsmith/Vol250GB/" 

def label_update():
  while True:
    # Update tk.StringVar with the available disk space
    df = shutil.disk_usage(FSPATH).free / GB
    dftxt.set("%.2f GB" % df)
    wndMain.update()
    # Relinquish the CPU for some seconds.
    time.sleep(2)


# Create the main window.
wndMain = tk.Tk()

# Set title and size of the main window.
wndMain.title("df") 
wndMain.geometry("180x50")

# Define a tkinter StringVar to use in a label.
dftxt = tk.StringVar()

# Create the text labels.
label1 = tk.Label(wndMain, text=FSPATH, font="Arial 10")
label2 = tk.Label(wndMain, textvariable=dftxt, font="Arial 17 bold")
label1.pack(pady=0)
label2.pack(pady=2)

label_update()
wndMain.mainloop() 
