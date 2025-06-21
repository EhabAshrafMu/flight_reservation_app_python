import tkinter as tk
from tkinter import ttk
import sqlite3

class EditReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.selected_id = None

        ttk.Label(self, text="Edit Reservation", font=("Arial", 16)).pack(pady=10)

        # Input Fields
        self.entries = {}
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        for field in fields:
            frame = ttk.Frame(self)
            frame.pack(pady=5)
            ttk.Label(frame, text=field).pack(side="left", padx=5)
            entry = ttk.Entry(frame)
            entry.pack(side="left", padx=5)
            self.entries[field] = entry

        # Save Button
        ttk.Button(self, text="Save Changes", command=self.save_changes).pack(pady=10)
        from reservations import ReservationsPage
        ttk.Button(self, text="Back", command=lambda: controller.show_frame(controller.frames["ReservationsPage"].__class__)).pack()

    def load_reservation(self, values):
        self.selected_id = values["id"]  # id passed separately
        self.entries["Name"].delete(0, tk.END)
        self.entries["Name"].insert(0, values["name"])
        self.entries["Flight Number"].delete(0, tk.END)
        self.entries["Flight Number"].insert(0, values["flight_number"])
        self.entries["Departure"].delete(0, tk.END)
        self.entries["Departure"].insert(0, values["departure"])
        self.entries["Destination"].delete(0, tk.END)
        self.entries["Destination"].insert(0, values["destination"])
        self.entries["Date"].delete(0, tk.END)
        self.entries["Date"].insert(0, values["date"])
        self.entries["Seat Number"].delete(0, tk.END)
        self.entries["Seat Number"].insert(0, values["seat_number"])

    def save_changes(self):
        data = {
            "name": self.entries["Name"].get(),
            "flight_number": self.entries["Flight Number"].get(),
            "departure": self.entries["Departure"].get(),
            "destination": self.entries["Destination"].get(),
            "date": self.entries["Date"].get(),
            "seat_number": self.entries["Seat Number"].get()
        }

        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE reservations
            SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
            WHERE id=?
        """, (data["name"], data["flight_number"], data["departure"], data["destination"], data["date"], data["seat_number"], self.selected_id))
        conn.commit()
        conn.close()

        print("Reservation updated.")
        from reservations import ReservationsPage
        self.controller.show_frame(ReservationsPage)
