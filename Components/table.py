
from tkinter import *
from Components.scrollableframe import *

class SimpleTable(Frame):
    def __init__(self, parent, rows=10, columns=5,**kwargs):
        super().__init__(parent, background="#f2efe6",**kwargs)
        self.header_color="#a19e95"
        self.even_color="#c2bfb8"
        self.odd_color="#ebe6d8"
        self._widgets = []
        for row in range(rows):
            current_row = []
            if(row==0):
              bg=self.header_color
            elif(row%2==0):
                bg=self.even_color
            else:
                bg=self.odd_color
            for column in range(columns):
                label = Label(self, text="-",borderwidth=0, height=3,bg=bg,wraplength=400)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)


    def set(self, row, column, value,widget=None,**kwargs):
        widget_ref = self._widgets[row][column]
        if(widget is not None):
            if(row%2==0):
                widget.configure(bg=self.even_color)
            else:
                widget.configure(bg=self.odd_color)
            widget.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
            self._widgets[row][column]=widget
            widget_ref=widget
        widget_ref.configure(text=str(value),**kwargs)

if __name__ == "__main__":
    root = Tk()
    t = SimpleTable(root, 10, 2)
    t.pack(side="top", fill="x")
    t.set(0, 0, "Hello, world avc c sd ")
    root.mainloop()