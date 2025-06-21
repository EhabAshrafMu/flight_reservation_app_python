import tkinter as tk
from tkinter import ttk
import sqlite3
from home import HomePage
from edit_reservation import EditReservationPage

class ReservationsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="All Reservations", font=("Arial", 16)).pack(pady=10)

        # Table view
        self.tree = ttk.Treeview(self, columns=("Name", "Flight", "From", "To", "Date", "Seat"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Flight", text="Flight No.")
        self.tree.heading("From", text="Departure")
        self.tree.heading("To", text="Destination")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Seat", text="Seat No.")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Refresh and Back
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Refresh", command=self.load_data).pack(side="left", padx=10)
        ttk.Button(btn_frame, text="Back", command=lambda: controller.show_frame(HomePage)).pack(side="left", padx=10)
        ttk.Button(btn_frame, text="Delete Selected", command=self.delete_selected).pack(side="left", padx=10)
        ttk.Button(btn_frame, text="Edit Selected", command=self.edit_selected).pack(side="left", padx=10)


    def load_data(self):
        # Clear the table first
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Fetch from DB
        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, flight_number, departure, destination, date, seat_number FROM reservations")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            self.tree.insert("", "end", values=row)

    def edit_selected(self):
        selected = self.tree.selection()
        if not selected:
            print("No reservation selected.")
            return

        item = self.tree.item(selected[0])
        values = item["values"]

        # Fetch the actual reservation ID (optional — if you stored it in the table)
        # But assuming we use other unique data fields:

        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id FROM reservations WHERE
            name=? AND flight_number=? AND departure=? AND destination=? AND date=? AND seat_number=?
        ''', values)
        result = cursor.fetchone()
        conn.close()

        if not result:
            print("Reservation not found.")
            return

        reservation_id = result[0]

        data = {
            "id": reservation_id,
            "name": values[0],
            "flight_number": values[1],
            "departure": values[2],
            "destination": values[3],
            "date": values[4],
            "seat_number": values[5]
        }

        edit_page = self.controller.frames[EditReservationPage]
        edit_page.load_reservation(data)
        self.controller.show_frame(EditReservationPage)

    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            print("No reservation selected.")
            return

        values = self.tree.item(selected[0])["values"]
        name, flight, departure, destination, date, seat = values

        conn = sqlite3.connect("flights.db")
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM reservations
            WHERE name=? AND flight_number=? AND departure=? AND destination=? AND date=? AND seat_number=?
        ''', (name, flight, departure, destination, date, seat))
        conn.commit()
        conn.close()

        print("Reservation deleted.")
        self.load_data()  # Refresh table
