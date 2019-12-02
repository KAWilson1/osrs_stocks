from tkinter.filedialog import askopenfilename
from tkinter import Tk, Label, Button, Entry, END, Text, OptionMenu, StringVar, END, Listbox
import subprocess
import constants
import xlrd
import read

class CurrentOrderGui:
    def __init__(self, master):
        self.bg = "#35323b"
        self.black = "#201e24"
        self.light_green = "#00b986"
        self.black_green = "#008562"
        self.title_text = "#dddddd"
        self.button_text = "#eeeeee"

        self.margin_default_text = "Margin: "
        self.invested_default_text = "Invested: "
        self.profit_default_text = "Profit: "
        self.roi_default_text = "ROI: "
        self.last_bought_at_default_text = "Last Buy Order: "

        self.master = master
        self.master.geometry("900x400")
        self.master.configure(bg=self.bg)
        self.master.resizable(False, False)
        master.title("TT v" + constants.VERSION)

        self.lbl_blank_header = Label(master, text="                                                ", font=("Arial", 24), bg=self.black)
        self.lbl_blank_header.place(x=0,y=0)

        #Title
        self.lbl_title = Label(master, text="TT", font=("Fixedsys", 24, "bold"), bg=self.black, fg=self.title_text)
        self.lbl_title.place(x=5, y=5)

        #Version Num
        self.lbl_version = Label(master, text="v" + constants.VERSION, font=("Fixedsys", 16), bg=self.black, fg=self.title_text)
        self.lbl_version.place(x=90, y=17)

        #Generator
        self.lbl_generator = Label(master, text="FINDER", font=("Fixedsys", 18, "bold"), bg=self.black, fg=self.light_green)
        self.lbl_generator.place(x=185, y=5)


        ###Column 0###
        self.lbl_item_name = Label(master, text=self.last_bought_at_default_text, fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_item_name.place(x=200, y=70)

        self.lbl_buy = Label(master, text=self.margin_default_text, fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_buy.place(x=200, y=90)

        self.lbl_sell = Label(master, text=self.margin_default_text, fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_sell.place(x=200, y=90)

        self.lbl_margin = Label(master, text=self.margin_default_text, fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_margin.place(x=200, y=90)

        self.lbl_invested = Label(master, text=self.invested_default_text, fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_invested.place(x=200, y=110)

        self.lbl_profit = Label(master, text=self.profit_default_text, fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_profit.place(x=200, y=130)

        self.lbl_roi = Label(master, text=self.roi_default_text, fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_roi.place(x=200, y=150)

        self.lbl_place_at = Label(master, text=self.roi_default_text, fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_place_at.place(x=200, y=150)

        #LB of orders
        self.orders_var = StringVar(master)
        self.orders_var.set(["#99999 - Shark (1115:1129 [14]) x 10k units", "15"])
        self.lb_orders = Listbox(master, listvariable=self.orders_var)
        self.lb_orders.place(x=445, y=198)

        self.btn_test = Button(master, text="Test", command=self.print_lb_index)
        self.btn_test.place(x=800, y=220)

        self.btn_update = Button(master, text="Update", command=self.import_orders)
        self.btn_update.place(x=800, y=320)

    def print_lb_index(self):
        print(self.lb_orders.curselection())

    def import_orders(self):
        all_orders = read.read_database(constants.PATH_TO_DATABASE)
        self.orders_var.set(["1", "2", "3"])

root = Tk()
my_gui = CurrentOrderGui(root)
root.mainloop()
