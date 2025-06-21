from database import init_db
import tkinter as tk
from tkinter import ttk
from reservations import ReservationsPage
from home import HomePage
from edit_reservation import EditReservationPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flight Reservation System")
        self.geometry("600x400")
        self.resizable(True, True)

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        from booking import BookingPage
        for F in (HomePage, BookingPage, ReservationsPage, EditReservationPage): 
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ttk.Label(self, text="Flight Booking Page (Coming Soon)", font=("Arial", 14))
        label.pack(pady=20)

        back_btn = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage))
        back_btn.pack(pady=10)

if __name__ == "__main__":
    from database import init_db
    init_db()

    app = App()
    app.mainloop()