import tkinter as tk

size = 8
puzzle = list(range(0, size * size))


root = tk.Tk()
root.title(str(size * size - 1) + " Puzzle")

window = tk.Frame(root, padx=50, pady=50)
window.pack()

container = tk.Frame(window)
container.grid(row=0, column=0, columnspan=3)

board = tk.Frame(container, background='gray30', padx=5, pady=5)
board.pack()

def show_board(size, puzzle):
    piece_pixel = 300 / size - 10

    for i, val in enumerate(puzzle):
        if i == 0:
            continue
        r = int(i / size)
        c = i % size
        tk.Frame(board, background='grey80', width=piece_pixel, height=piece_pixel).grid(row=r, column=c, padx=5, pady=5)
        tk.Label(board, text=str(val), background='grey80').grid(row=r, column=c)

show_board(size, puzzle)

def prev(s=size, p=puzzle):
    for i, elem in enumerate(p):
        p[i] += 1
    show_board(s, p)
        

tk.Button(window, text="prev", command=prev, padx=20, pady=10).grid(row=2, column=0, sticky=tk.E)
tk.Label(window, text="1").grid(row=2, column=1)
tk.Button(window, text="next", padx=20, pady=10).grid(row=2, column=2, sticky=tk.W)

tk.Frame(window, height=20).grid(row=3, column=0, columnspan=3)

message = tk.Message(window, width=310, text="Complexity in time: 477\nComplexity in size: 962\nNumber of moves: 18")
message.grid(row=4, column=0, columnspan=3, sticky=tk.W)

root.mainloop()
