from tkinter.filedialog import askopenfilename
from tkinter import Tk, Label, Button, Entry, END, Text, OptionMenu, StringVar, END, Listbox
import subprocess
import xlrd
import datetime

import constants
import read
import write
import calc

class CurrentOrderGui:
    def __init__(self, master):
        self.bg = "#35323b"
        self.black = "#201e24"
        self.light_green = "#00b986"
        self.black_green = "#008562"
        self.title_text = "#dddddd"
        self.button_text = "#eeeeee"

        self.incomplete_orders = []
        self.orders_to_display = []

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
        self.lbl_generator = Label(master, text="MANAGER", font=("Fixedsys", 18, "bold"), bg=self.black, fg=self.light_green)
        self.lbl_generator.place(x=185, y=5)

        ###ORDERS###
        self.orders_var = StringVar(master)
        self.orders_var.set(["#99999 - Shark (1115:1129)[14] x 10k units", "15"])
        self.lb_orders = Listbox(master, listvariable=self.orders_var, width=146, height=11)
        self.lb_orders.place(x=10, y=50)
        self.lb_orders.after(500, self.show_stats)

        #Can be deleted, commented out for now in case manual testing on show_stats() needs to be done
        #self.btn_test = Button(master, text="Update Stats", command=self.show_stats)
        #self.btn_test.place(x=600, y=350)

        #Can be deleted, commented out for now in case manual testing on import_orders() needs to be done
        #self.btn_update = Button(master, text="Pull Orders", command=self.import_orders)
        #self.btn_update.place(x=700, y=350)

        ###STATS###
        column_spacer = 240
        unit_spacer = 20
        self.lbl_last_bought_at = Label(master, text=self.last_bought_at_default_text, fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_last_bought_at.place(x=10, y=column_spacer)

        self.lbl_margin = Label(master, text=self.margin_default_text, fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_margin.place(x=10, y=column_spacer+unit_spacer)

        self.lbl_invested = Label(master, text=self.invested_default_text, fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_invested.place(x=10, y=column_spacer+unit_spacer*2)

        self.lbl_profit = Label(master, text=self.profit_default_text, fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_profit.place(x=10, y=column_spacer+unit_spacer*3)

        self.lbl_roi = Label(master, text=self.roi_default_text, fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_roi.place(x=10, y=column_spacer+unit_spacer*4)



        ###NOTES###
        self.txt_notes = Text(master, height=7, width=41, bg=self.black, fg=self.button_text, relief="flat")
        self.txt_notes.place(x=250, y=column_spacer)



        ###Speed Buttons###
        self.lbl_speed = Label(master, text="Speed of Completion", fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_speed.place(x=700, y=column_spacer)

        self.btn_speed_1 = Button(master, text="  1  ", command=self.complete_order_1)
        self.btn_speed_1.place(x=690, y=270)

        self.btn_speed_2 = Button(master, text="  2  ", command=self.complete_order_2)
        self.btn_speed_2.place(x=752, y=270)

        self.btn_speed_3 = Button(master, text="  3  ", command=self.complete_order_3)
        self.btn_speed_3.place(x=810, y=270)

        self.btn_speed_overnight = Button(master, text="Overnight", command=self.complete_order_overnight)
        self.btn_speed_overnight.place(x=695, y=300)

        self.btn_speed_aborted = Button(master, text=" Aborted ", command=self.complete_order_aborted)
        self.btn_speed_aborted.place(x=775, y=300)

        self.import_orders()

    def show_stats(self):
        if len(self.incomplete_orders) != 0:
            curr_trans = self.incomplete_orders[self.lb_orders.curselection()[0]]
            self.lbl_last_bought_at['text'] = self.last_bought_at_default_text
            self.lbl_margin['text'] = self.margin_default_text + str(calc.margin(curr_trans.unit_price, curr_trans.unit_intended_sell_price))
            self.lbl_invested['text'] = self.invested_default_text + str(calc.invested(curr_trans.unit_price, curr_trans.quantity)/1000) + "k"
            self.lbl_profit['text'] = self.profit_default_text + str(calc.profit(curr_trans.unit_price, curr_trans.unit_intended_sell_price, curr_trans.quantity)/1000) + "k"
            self.lbl_roi['text'] = self.roi_default_text + str(calc.roi(curr_trans.unit_price, curr_trans.unit_intended_sell_price, curr_trans.quantity)) + "%"

        self.lb_orders.after(500, self.show_stats)

    def import_orders(self):
        all_transactions = read.read_database(constants.PATH_TO_DATABASE)

        #clear Listbox and reset
        self.lb_orders.delete(0, 'end')
        self.incomplete_orders = []
        self.orders_to_display = []

        #Pull incomplete orders and format them for display in the Listbox
        for trans in all_transactions:
            if trans.completed == "None":
                self.incomplete_orders.append(trans)
                self.orders_to_display.append(trans.item_name + " x " + str(trans.quantity) + "k units (" 
                    + str(trans.unit_price) + ":" + str(trans.unit_intended_sell_price) + ") [" + str(calc.margin(trans.unit_price, trans.unit_intended_sell_price)) + "]")
        
        #Display orders
        if len(self.orders_to_display) == 0:
            self.orders_var.set(["All transactions are complete"])
        else:
            self.orders_var.set(self.orders_to_display)
        
        #set default selected value in Listbox (first item)
        if len(self.orders_to_display) != 0:
            self.lb_orders.select_set(0)

    def complete_order_1(self):
        self.complete_order(constants.COMPLETION_SPEEDS[0])

    def complete_order_2(self):
        self.complete_order(constants.COMPLETION_SPEEDS[1])

    def complete_order_3(self):
        self.complete_order(constants.COMPLETION_SPEEDS[2])

    def complete_order_overnight(self):
        self.complete_order(constants.COMPLETION_SPEEDS[3])

    def complete_order_aborted(self):
        self.complete_order(constants.COMPLETION_SPEEDS[4])

    def complete_order(self, completion_code):
        completed_id = self.incomplete_orders[self.lb_orders.curselection()[0]].transaction_id
        all_transactions = read.read_database(constants.PATH_TO_DATABASE)

        for trans in all_transactions:
            if trans.transaction_id == completed_id:
                curr_time = datetime.datetime.now()
                trans.end_year = curr_time.year
                trans.end_month = curr_time.month
                trans.end_day = curr_time.day
                trans.end_hour = curr_time.hour
                trans.end_minute = curr_time.minute
                trans.completed = completion_code
        write.write_to_database(constants.PATH_TO_DATABASE, all_transactions)
        self.import_orders() #update listbox


root = Tk()
my_gui = CurrentOrderGui(root)
root.mainloop()
