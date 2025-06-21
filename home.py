import tkinter as tk
from tkinter import ttk
from booking import BookingPage

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        from reservations import ReservationsPage
        # Wrapper frame placed in the center of the page
        wrapper = ttk.Frame(self)
        wrapper.place(relx=0.5, rely=0.5, anchor="center")  # ⬅️ this centers the content

        # Title Label
        label = ttk.Label(wrapper, text="Welcome to Flight Reservation System", font=("Arial", 16))
        label.pack(pady=20)

        # Book Button
        book_btn = ttk.Button(wrapper, text="Book Flight", command=lambda: controller.show_frame(BookingPage))
        book_btn.pack(pady=10, ipadx=10)

        # View Reservations Button
        view_btn = ttk.Button(wrapper, text="View Reservations", command=lambda: controller.show_frame(ReservationsPage))
        view_btn.pack(pady=10, ipadx=10)
