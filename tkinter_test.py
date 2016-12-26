import tkinter as tk


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__create_frame()
        self.__create_button()
        self.__create_menu()

    def __create_frame(self):
        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=1)

    def __create_button(self):
        resource_button = tk.Button(self.frame, text="资源", 
                                    command=self.__fake,
                                    bg="#292929", fg="white", bd=0)
        resource_button.pack(side=tk.TOP, anchor=tk.NW)
        search_button = tk.Button(self.frame, text="搜索", command=self.__fake,
                                  bg="#292929", fg="white", bd=0)
        search_button.pack(side=tk.TOP, anchor=tk.NW)

    def __create_menu(self):
        menubar = tk.Menu(self.frame)
        # 创建 File 下拉菜单
        menu_file = tk.Menu(menubar, tearoff=0)
        menu_file.add_command(label="New File", command=self.__fake)
        menu_file.add_command(label="New Window", command=self.__fake)
        menubar.add_cascade(label="File", menu=menu_file)
        # 创建 Edit 下拉菜单
        menu_edit = tk.Menu(menubar, tearoff=0)
        menu_edit.add_command(label="Cut", command=self.__fake)
        menu_edit.add_command(label="Copy", command=self.__fake)
        menu_edit.add_command(label="Paste", command=self.__fake)
        menubar.add_cascade(label="Edit", menu=menu_edit)

        # 显示菜单
        self.config(menu=menubar)

    def __fake(self):
        print("Pretending to be doing some real thing...")

myapp = App()
myapp.title("A Progressive Trainning of Tkinter")
myapp.minsize(800, 500)
myapp.maxsize(1200, 700)

myapp.mainloop()
