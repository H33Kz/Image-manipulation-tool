from tkinter import *
import layouts

def main():
    second = False
    root = Tk()
    root.title('Image processing tool')
    
    m = layouts.MainMenu(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()