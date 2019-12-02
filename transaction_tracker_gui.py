from tkinter.filedialog import askopenfilename
from tkinter import Tk, Label, Button, Entry, END, Text, OptionMenu, StringVar, END
import subprocess
import constants
import datetime
import read
import write

class TransactionTrackerGui:
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
        self.master.geometry("735x270")
        self.master.configure(bg=self.bg)
        self.master.resizable(False, False)
        master.title("Transaction Tracker - Flip")

        self.lbl_blank_header = Label(master, text=(" "*100), font=("Arial", 36), bg=self.black)
        self.lbl_blank_header.place(x=0,y=0)

        #Generator
        self.lbl_generator = Label(master, text="FLIP TRACKER", font=("Fixedsys", 18, "bold"), bg=self.black, fg=self.light_green)
        self.lbl_generator.place(x=5, y=24)

        #Version Num
        self.lbl_version = Label(master, text="v" + constants.VERSION, font=("Fixedsys", 16), bg=self.black, fg=self.title_text)
        self.lbl_version.place(x=660, y=32)


        ###DATA COLLECTION COLUMN"
        #Label Item Name
        self.lbl_item_name = Label(master, text="Item Name", fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_item_name.place(x=5, y=70)

        #Item Name
        self.txt_item_name = Entry(master, width=23, bg=self.black, fg=self.button_text, relief="flat")
        self.txt_item_name.place(x=5, y=90)


        #Label Buy Price
        self.lbl_buy_price = Label(master, text="Buy Price", fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_buy_price.place(x=5, y=115)

        #Buy Price
        self.txt_buy_price = Entry(master, width=9, bg=self.black, fg=self.button_text, relief="flat")
        self.txt_buy_price.insert(END, "0")
        self.txt_buy_price.place(x=5, y=135)


        #Label Intended Sell
        self.lbl_intended_sell = Label(master, text="Intended Selling Price", fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_intended_sell.place(x=5, y=160)

        #Intended Sell
        self.txt_intended_sell = Entry(master, width=9, bg=self.black, fg=self.button_text, relief="flat")
        self.txt_intended_sell.insert(END, "0")
        self.txt_intended_sell.place(x=5, y=180)


        #Label Quantity
        self.lbl_quantity = Label(master, text="Quantity (k)", fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_quantity.place(x=5, y=205)

        #Quantity
        self.txt_quantity = Entry(master, width=9, bg=self.black, fg=self.button_text, relief="flat")
        self.txt_quantity.insert(END, "0")
        self.txt_quantity.place(x=5, y=225)



        ###STATS COLUMN###
        #Label Margin
        self.lbl_last_bought_at = Label(master, text=self.last_bought_at_default_text, fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_last_bought_at.place(x=200, y=70)
        self.lbl_last_bought_at.after(1000, self.refresh_stats_column)

        #Label Margin
        self.lbl_margin = Label(master, text=self.margin_default_text + "0", fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_margin.place(x=200, y=90)

        #Label Invested
        self.lbl_invested = Label(master, text=self.invested_default_text + "0", fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_invested.place(x=200, y=110)

        #Label Profit
        self.lbl_profit = Label(master, text=self.profit_default_text + "0", fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_profit.place(x=200, y=130)

        #Label Roi
        self.lbl_roi = Label(master, text=self.roi_default_text + "0", fg=self.title_text, bg=self.bg, font=("Arial", 9))
        self.lbl_roi.place(x=200, y=150)


        ###NOTES COLUMN###
        #Notes
        self.txt_notes = Text(master, height=7, width=41, bg=self.black, fg=self.button_text, relief="flat")
        self.txt_notes.place(x=395, y=70)


        #Button Submit
        self.btn_submit = Button(master, text="Submit", command=self.submit, fg=self.button_text,
                                        bg=self.black_green, relief="flat", activeforeground=self.button_text,
                                        activebackground=self.black_green)
        self.btn_submit.place(x=395, y=198)

        #Button Reset
        self.btn_submit = Button(master, text="Reset", command=self.reset, fg=self.button_text,
                                        bg=self.black_green, relief="flat", activeforeground=self.button_text,
                                        activebackground=self.black_green)
        self.btn_submit.place(x=475, y=198)

    def refresh_stats_column(self):
        try:
            buy = int(self.txt_buy_price.get())
        except:
            buy = 0

        try:
            sell = int(self.txt_intended_sell.get())
        except:
            sell = 0

        try:
            quantity = float(self.txt_quantity.get())
        except:
            quantity = 0            

        #Margin
        if buy != 0 and sell != 0:
            margin = sell - buy
            self.lbl_margin['text'] = self.margin_default_text + " " + str(margin)
        else:
            self.lbl_margin['text'] = self.margin_default_text

        #Invested
        if buy != 0 and quantity != 0:
            invested = buy * quantity * 1000
            self.lbl_invested['text'] = self.invested_default_text + " " + str(invested/1000) + "k"
        else:
            self.lbl_invested['text'] = self.invested_default_text

        #Profit
        if buy != 0 and sell != 0 and quantity != 0:
            profit = quantity * 1000 * margin
            self.lbl_profit['text'] = self.profit_default_text + " " + str(profit/1000) + "k"
        else:
            self.lbl_profit['text'] = self.profit_default_text


        #ROI
        if buy != 0 and sell != 0 and quantity != 0:
            roi = profit / invested * 100
            self.lbl_roi['text'] = self.roi_default_text + " " + str(round(roi,1)) + "%"
        else:
            self.lbl_roi['text'] = self.roi_default_text

    
        self.lbl_last_bought_at.after(1000, self.refresh_stats_column)

    def submit(self):
        path = constants.PATH_TO_DATABASE

        #read old values
        all_rows = read.read_database(path)

        #add new value to all_rows
        gui_row = []
        gui_row.append(self.txt_item_name.get())
        gui_row.append(self.txt_buy_price.get())
        gui_row.append(self.txt_intended_sell.get())
        gui_row.append(self.txt_quantity.get())
        #Start Time
        gui_row.append(datetime.datetime.now().year)
        gui_row.append(datetime.datetime.now().month)
        gui_row.append(datetime.datetime.now().day)
        gui_row.append(datetime.datetime.now().hour)
        gui_row.append(datetime.datetime.now().minute)
        #End Time
        gui_row.append("None")
        gui_row.append("None")
        gui_row.append("None")
        gui_row.append("None")
        gui_row.append("None")
        #Notes
        gui_row.append(self.txt_notes.get('1.0', END))
        #Completed
        gui_row.append("None")

        if len(gui_row) != len(constants.TRANSACTION_HEADERS):
            raise Exception("New transaction data does not have the same number of properties as the database.")
        all_rows.append(gui_row)

        #write headers
        headers = constants.TRANSACTION_HEADERS
        all_rows.insert(0, headers)
        
        #write output
        write.write_to_database(path, all_rows)
        

    def reset(self):
        self.txt_item_name.delete(0, 'end')
        self.txt_buy_price.delete(0, 'end')
        self.txt_intended_sell.delete(0, 'end')
        self.txt_quantity.delete(0, 'end')
        self.txt_notes.delete('1.0', END)

        self.lbl_last_bought_at['text'] = self.last_bought_at_default_text
        self.lbl_margin['text'] = self.margin_default_text
        self.lbl_invested['text'] = self.invested_default_text
        self.lbl_profit['text'] = self.profit_default_text 
        self.lbl_roi['text'] = self.roi_default_text

if __name__ == "__main__":
    root = Tk()
    my_gui = TransactionTrackerGui(root)
    root.mainloop()