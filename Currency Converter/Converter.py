from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from currency_converter import CurrencyConverter

root = Tk()
root.geometry("750x500")
# root.resizable(True, True)
root.title("Currency Converter")
root.config(bg="steel blue", cursor="arrow")
# root.state("zoomed")
from_num = DoubleVar()
to_num = DoubleVar()
from_country = StringVar()
from_country.set("Indian Rupee")
to_country = StringVar()
to_country.set("United State Dollar")
from_num.set(1)
to_num.set(None)
result = StringVar()
result.set("")

currency_country_dict = {
    "SEK": "Swedish Krona",
    "PHP": "Philippine Peso",
    "HKD": "Hong Kong Dollar",
    "HUF": "Hungarian Forint",
    "CHF": "Swiss Franc",
    "GBP": "British Pound",
    "CZK": "Czech Koruna",
    "MXN": "Mexican Peso",
    "BRL": "Brazilian Real",
    "HRK": "Croatian Kuna",
    "SGD": "Singapore Dollar",
    "EEK": "Estonian Kroon",
    "INR": "Indian Rupee",
    "JPY": "Japanese Yen",
    "MYR": "Malaysian Ringgit",
    "TRL": "Turkish Lira",
    "RUB": "Russian Ruble",
    "LTL": "Lithuanian Litas",
    "MTL": "Maltese Lira",
    "EUR": "Euro",
    "PLN": "Polish Zloty",
    "RON": "Romanian Leu",
    "THB": "Thai Baht",
    "ILS": "Israeli New Shekel",
    "CYP": "Cypriot Pound",
    "KRW": "South Korean Won",
    "SIT": "Slovenian Tolar",
    "ISK": "Icelandic Krona",
    "AUD": "Australian Dollar",
    "ZAR": "South African Rand",
    "NOK": "Norwegian Krone",
    "DKK": "Danish Krone",
    "BGN": "Bulgarian Lev",
    "SKK": "Slovak Koruna",
    "NZD": "New Zealand Dollar",
    "CNY": "Chinese Yuan",
    "USD": "United States Dollar",
    "CAD": "Canadian Dollar",
    "LVL": "Latvian Lats",
    "IDR": "Indonesian Rupiah",
}

def set_from_country(event):
    name = currency_country_dict.get(get_from_currency.get())
    from_country.set(name)

def set_to_country(event):
    name = currency_country_dict.get(get_to_currency.get())
    to_country.set(name)

def currency_convert():
    try:
        float(from_num.get())
    except:
        messagebox.showerror("Error", "please give valid amount to make convertion!")
    else:
        converter = CurrencyConverter()
        print("Converting...")
        converted_value = converter.convert(from_num.get(), get_from_currency.get(), get_to_currency.get())
        print(converted_value, "is converted value")
        to_num.set(converted_value)

        text = "{}  {} equals to {:.8f} {}".format(from_num.get(), from_country.get(), to_num.get(), to_country.get())
        result_label = Label(root, text=text,bg="steel blue", font=("Calibri 14 bold"))
        result_label.place(x=140,y=150)


icon_photo = PhotoImage(file="icon.png")
root.iconphoto(False, icon_photo)
header_label = Label(root, text="Currency Converter",borderwidth=1, relief="groove",bg="steel blue", font=("arial 16 bold"), pady=8)
header_label.pack(fill=BOTH)

operational_frame = Frame(root, background="light blue",pady=50, padx=50)
operational_frame.place(x=70,y=200)

#----------------------------------------------------------
convert_from_entry = Entry(operational_frame, font=("calibri 12 bold"), textvariable=from_num)
convert_from_entry.grid(row=0,column=0)

countries = [c for c in currency_country_dict.keys()]
get_from_currency = ttk.Combobox(operational_frame, font=("calibri 12 bold"), values=countries)
get_from_currency.set("INR")
get_from_currency.grid(row=0,column=1, padx=20)

set_from_country_label = Label(operational_frame, font=("calibri 12 bold"), textvariable=from_country)
set_from_country_label.grid(row=0,column=2)
get_from_currency.bind("<FocusIn>", set_from_country)

#------------------------------------------------------
convert_button = Button(operational_frame, font=("calibri 12 bold"), text="Convert", command=currency_convert)
convert_button.grid(row=1,column=0,columnspan=3, pady=30)
#------------------------------------------------------

convert_to_entry = Entry(operational_frame, font=("calibri 12 bold"), textvariable=to_num)
convert_to_entry.grid(row=2,column=0)

get_to_currency = ttk.Combobox(operational_frame, font=("calibri 12 bold"), values=countries)
get_to_currency.set("USD")
get_to_currency.grid(row=2,column=1, padx=20)

set_to_country_label = Label(operational_frame, font=("calibri 12 bold"), textvariable=to_country)
set_to_country_label.grid(row=2,column=2)
get_to_currency.bind("<FocusIn>", set_to_country)

root.mainloop()
