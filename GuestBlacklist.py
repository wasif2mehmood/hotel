import tkinter as tk
from HotelClass import Hotel
from BookingClass import *
import date_validator

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("SAMI Blacklist GUI-done by XXXX")

        self.myHotel = Hotel("SAMI", "availablerooms.txt")

        # Create the labels and their text fields
        self.passport_label = tk.Label(master, text="Passport:")
        self.passportentry = tk.Entry(master)

        self.date_label = tk.Label(master, text="Date Reported:")
        self.date_entry = tk.Entry(master)
        self.date_entry.config(state='disabled')

        self.reason_laebel = tk.Label(master, text="Reason(s):")
        self.reason_entry = tk.Entry(master)
        # disable entry3
        self.reason_entry.config(state='disabled')
        # date format
        self.label4 = tk.Label(master, text="(dd-mon-yyyy)")

        # Create the buttons
        self.search = tk.Button(master, text="Search", command=self.search_)
        self.blacklist = tk.Button(
            master, text="Blacklist", command=self.blacklist_)
        # disable button2
        self.blacklist.config(state='disabled')
        self.reset = tk.Button(master, text="Reset", command=self.reset_)

        # Create the large text field
        self.text = tk.Text(master)

        # Arrange the widgets in the grid
        self.passport_label.grid(row=0, column=0, padx=5, pady=5)
        self.passportentry.grid(row=0, column=1, padx=5, pady=5)
        self.date_label.grid(row=1, column=0, padx=5, pady=5)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)
        self.reason_laebel.grid(row=2, column=0, padx=5, pady=5)
        self.reason_entry.grid(row=2, column=1, padx=5, pady=5)
        self.label4.grid(row=1, column=2, padx=5, pady=5)
        self.search.grid(row=3, column=0, padx=5, pady=5)
        self.blacklist.grid(row=3, column=1, padx=5, pady=5)
        self.reset.grid(row=3, column=2, padx=5, pady=5)
        self.text.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    def search_(self):
        # enable entry2
        self.date_entry.config(state='normal')
        # enable entry3
        self.reason_entry.config(state='normal')
        # enable button2
        self.blacklist.config(state='normal')
        # disable button 1
        self.search.config(state='disabled')
        # disable entry1
        self.passportentry.config(state='disabled')
        # get the passport number
        self.passport = self.passportentry.get()
        # search for the guest
        try:
            self.guest = self.myHotel.searchGuest(self.passport)
            # check if guest is blacklisted
            if self.guest.isBlacklisted():
                # if guest is blacklisted
                # display the guest's details
                self.text.insert(tk.END, str(self.guest))
                self.text.insert(tk.END, "\nGuest is already blacklisted")
                # disable blackilst button,reason and date
                self.blacklist.config(state='disabled')
                self.date_entry.config(state='disabled')
                self.reason_entry.config(state='disabled')

            else:
                # if guest is not blacklisted
                # display the guest's details
                self.text.insert(tk.END, str(self.guest))
                # display the date and reason fields
                self.text.insert(
                    tk.END, "\nEnter date and reason to blacklist: \n")
        except:
            self.text.insert(tk.END, "\nGuest not found!")

    def blacklist_(self):

        # get date
        self.date = self.date_entry.get()
        # get reason
        self.reason = self.reason_entry.get()
        # check if date is valid and also error message if reason is not entered
        if date_validator.validate_date(self.date) and self.reason != "":
            # blacklist the guest
            self.guest.blacklist(self.date, self.reason)
            # display the guest's details
            self.text.insert(tk.END, str(self.guest))
            # disable blackilst button,reason and date
            self.blacklist.config(state='disabled')
            self.date_entry.config(state='disabled')
            self.reason_entry.config(state='disabled')
            # open Blacklist.txt for appending
            self.file = open("Blacklist.txt", "a")
            # write the guest's details to the file PA0010023, 12-Mar-2023, Causes damage to facilities in this format
            self.file.write("\n"+self.passportentry.get() +
                            ", " + self.date + ", " + self.reason+"\n")

            self.file.close()

            # display message that guest is blacklisted on date due to

            self.text.insert(tk.END, "\n<<blacklisted on date, due to>> ")
            # display date,reason
            self.text.insert(tk.END, "\n"+self.date + ", " + self.reason)

        else:
            # if date is not valid
            if date_validator.validate_date(self.date) == False:
                self.text.insert(tk.END, "\nInvalid date format!")
            # if reason is not entered
            if self.reason == "":
                self.text.insert(tk.END, "\nReason not entered!")
            # if date is empty
            if self.date == "":
                self.text.insert(tk.END, "\nDate not entered!")

    def reset_(self):

        # enable all entries
        self.passportentry.config(state='normal')
        self.date_entry.config(state='normal')
        self.reason_entry.config(state='normal')
        
        # empty al text fields
        self.passportentry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.reason_entry.delete(0, tk.END)
        self.text.delete(1.0, tk.END)
        # enable entry1
        self.passportentry.config(state='normal')
        # disable entry2
        self.date_entry.config(state='disabled')
        # disable entry3
        self.reason_entry.config(state='disabled')
        # enable button1
        self.search.config(state='normal')
        # disable button2
        self.blacklist.config(state='disabled')
        


root = tk.Tk()
my_gui = MyGUI(root)
root.mainloop()
