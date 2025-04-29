import tkinter as tkinterlib

def create_date_selectors(self):
    
    days = [str(i) for i in range(1, 32)]
    months = [str(i) for i in range(1, 13)]

    self.start_day_var = tkinterlib.StringVar()
    self.start_month_var = tkinterlib.StringVar()
    self.start_day_var.set("1")
    self.start_month_var.set("1")

    self.end_day_var = tkinterlib.StringVar()
    self.end_month_var = tkinterlib.StringVar()
    self.end_day_var.set("31")
    self.end_month_var.set("12")

    start_label = tkinterlib.Label(self, text="Startdatum (Monat/Tag):")
    start_label.pack(padx=10, pady=5)

    end_label = tkinterlib.Label(self, text="Enddatum (Monat/Tag):")
    end_label.pack(padx=10, pady=5)

    start_day_menu = tkinterlib.OptionMenu(self, self.start_day_var, *days)
    start_month_menu = tkinterlib.OptionMenu(self, self.start_month_var, *months)
    end_day_menu = tkinterlib.OptionMenu(self, self.end_day_var, *days)
    end_month_menu = tkinterlib.OptionMenu(self, self.end_month_var, *months)

    start_day_menu.pack(padx=5, pady=5)
    start_month_menu.pack(padx=5, pady=5)
    end_day_menu.pack(padx=5, pady=5)
    end_month_menu.pack(padx=5, pady=5)

    self.start_day_var.trace_add("write", lambda *args: update_startdate(self))
    self.start_month_var.trace_add("write", lambda *args: update_startdate(self))
    self.end_day_var.trace_add("write", lambda *args: update_enddate(self))
    self.end_month_var.trace_add("write", lambda *args: update_enddate(self))

def update_startdate(self):
    month = self.start_month_var.get().zfill(2)
    day = self.start_day_var.get().zfill(2)
    self.default_startdate = f"{month}-{day}"  # Monat vor Tag

def update_enddate(self):
    month = self.end_month_var.get().zfill(2)
    day = self.end_day_var.get().zfill(2)
    self.default_enddate = f"{month}-{day}"  # Monat vor Tag
