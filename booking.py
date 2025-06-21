import tkinter as tk
from tkinter import ttk
from database import sqlite3  

class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # Title
        ttk.Label(self, text="Book a Flight", font=("Arial", 16)).pack(pady=10)

        # Form fields
        self.entries = {}
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        for field in fields:
            frame = ttk.Frame(self)
            frame.pack(pady=5, padx=20, fill="x")
            ttk.Label(frame, text=field + ":").pack(side="left", padx=5)
            entry = ttk.Entry(frame)
            entry.pack(side="left", fill="x", expand=True)
            self.entries[field.lower().replace(" ", "_")] = entry

        # Submit button
        ttk.Button(self, text="Submit", command=self.submit_reservation).pack(pady=15)

        # Back button
        from home import HomePage

        ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage)).pack()

    def submit_reservation(self):
        data = {key: entry.get() for key, entry in self.entries.items()}
        if any(value.strip() == "" for value in data.values()):
            print("All fields are required.")
            return

        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', tuple(data.values()))
        conn.commit()
        conn.close()
        print("Reservation saved!")

        for entry in self.entries.values():
            entry.delete(0, tk.END)
