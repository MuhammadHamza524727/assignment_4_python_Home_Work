import tkinter as tk

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
CELL_SIZE = 40
ERASER_SIZE = 20

class EraseCanvasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Erase Canvas")
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
        self.canvas.pack()

        self.cells = [] 
        self.eraser = None

        self.draw_grid()
        self.canvas.bind("<Motion>", self.move_eraser)

  
        self.canvas.bind("<Button-1>", self.place_eraser)

    def draw_grid(self):
        num_rows = CANVAS_HEIGHT // CELL_SIZE
        num_cols = CANVAS_WIDTH // CELL_SIZE
        for row in range(num_rows):
            for col in range(num_cols):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='black')
                self.cells.append(cell)

    def place_eraser(self, event):
        x, y = event.x, event.y
        if self.eraser is None:
            self.eraser = self.canvas.create_rectangle(
                x, y, x + ERASER_SIZE, y + ERASER_SIZE, fill='pink', outline=''
            )

    def move_eraser(self, event):
        if self.eraser is not None:
            x, y = event.x, event.y
            self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
            self.erase_objects(x, y)

    def erase_objects(self, x, y):
        x1 = x
        y1 = y
        x2 = x1 + ERASER_SIZE
        y2 = y1 + ERASER_SIZE

        overlapping = self.canvas.find_overlapping(x1, y1, x2, y2)
        for item in overlapping:
            if item != self.eraser:
                self.canvas.itemconfig(item, fill='white')

if __name__ == '__main__':
    root = tk.Tk()
    app = EraseCanvasApp(root)
    root.mainloop()
