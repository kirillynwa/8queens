from tkinter import *
from PIL import Image
import time
def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

def del_widget(wid):
    wid.delete(wid.find_all()[0])

def add_widget(wid):
    wid.create_image(size / 2, size / 2, anchor=CENTER, image=queen_img)

root = Tk()
root.title("8Queens")
center_window(800, 800)
size = 100
queen_img = PhotoImage(file="2.png")
even = True
counter = 0

# for row in range(8):
#     root.rowconfigure(index=row, weight=1)
#     for column in range(8):
#         root.columnconfigure(index=column, weight=1)
#         bg = "#fccea4" if even else "#d08845"
#         canvas = Canvas(bg=bg, borderwidth=0, width=size, height=size)
#         canvas.grid(row=row, column=column, padx=0, pady=0,  sticky="nsew")
#         even = not even
#     even = not even

class Queen:
    def __init__(self, column, neighbor):
        self.__column = column
        self.__neighbor = neighbor
        self.__row = 1
        widget = root.grid_slaves(row=self.__row - 1, column=self.__column - 1)[0]
        widget.create_image(size / 2, size / 2, anchor=CENTER, image=queen_img)

    def can_attack(self, test_row, test_column):
        if self.__row == test_row:
            return True
        column_difference = test_column - self.__column
        if (self.__row + column_difference == test_row) or (self.__row - column_difference == test_row):
            return True
        return self.__neighbor and self.__neighbor.can_attack(test_row, test_column)

    def find_solution(self):
        while self.__neighbor and self.__neighbor.can_attack(self.__row, self.__column):
            if not self.advance():
                return False
        return True

    def advance(self):
        global counter
        counter += 1
        if self.__row < 8:
            self.__row += 1
            widget = root.grid_slaves(row=self.__row-2, column=self.__column - 1)[0]
            widget.after(counter*500, del_widget, widget)
            widget1 = root.grid_slaves(row=self.__row - 1, column=self.__column - 1)[0]
            widget1.after(counter*500, add_widget, widget1)
            return self.find_solution()
        if self.__neighbor and not self.__neighbor.advance():
            return False
        self.__row = 1
        widget = root.grid_slaves(row=7, column=self.__column - 1)[0]
        widget.after(counter * 500, del_widget, widget)
        widget2 = root.grid_slaves(row=self.__row - 1, column=self.__column - 1)[0]
        widget2.after(counter * 500, add_widget, widget2)
        return self.find_solution()

    def print_columns(self):
        if self.__neighbor:
            self.__neighbor.print_columns()
        print("column " + str(self.__column) + " row " + str(self.__row))
        widget = root.grid_slaves(row=self.__row-1, column=self.__column-1)[0]
        widget.create_image(size / 2, size / 2, anchor=CENTER, image=queen_img)

def click_button():
    global even
    for row in range(8):
        root.rowconfigure(index=row, weight=1)
        for column in range(8):
            root.columnconfigure(index=column, weight=1)
            bg = "#fccea4" if even else "#d08845"
            canvas = Canvas(bg=bg, borderwidth=0, width=size, height=size)
            canvas.grid(row=row, column=column, padx=0, pady=0, sticky="nsew")
            even = not even
        even = not even
    lastQueen = 0
    for i in range(1, 9):
        lastQueen = Queen(i, lastQueen)
        if not lastQueen.find_solution():
            print("no solution")
    # lastQueen.print_columns()

btn = Button(text="Начать", command=click_button)
btn.grid(row=10, column=4, padx=0, pady=0,  sticky="nsew")


# widget = root.grid_slaves(row=0, column=0)[0]
# print(widget)
# print(widget.find_all()[0])
root.mainloop()
