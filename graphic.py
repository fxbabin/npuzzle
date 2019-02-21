import tkinter as tk

root = tk.Tk()
root.geometry("400x600")

frame = tk.Frame(root, background='gray80', padx=5, pady=5)
frame.place(x=50, y=50, width=310, height=310)

for i in range(0, 9):
    tk.Frame(frame, background='grey30', width=90, height=90).grid(row=int(i / 3), column=i % 3, padx=5, pady=5)

root.mainloop()