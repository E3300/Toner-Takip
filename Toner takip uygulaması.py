import tkinter as tk
from datetime import date
import mysql.connector
from mysql.connector import Error
# Function to insert the name and current date into the MySQL table
def insert_name(entry,entry1,entry2):
    input_alan = entry.get()
    input_veren = entry1.get()
    input_marka = entry2.get()

    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='tonerdb',
                                             user='root',
                                             password='eylul')
        if connection.is_connected():
            cursor = connection.cursor()

            # Get the current date
            current_date = date.today()

            # Modify the INSERT query to include the current date
            insert_query = "INSERT INTO tonertable (alanName, verenName, markaName, dateTime) VALUES (%s, %s, %s,%s)"
            cursor.execute(insert_query, (input_alan, input_veren, input_marka, current_date))
            connection.commit()
            print("Toner inserted successfully into 'tonerdb' table!")

    except Error as e:
        print("Error while connecting to MySQL or inserting data:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def delete_all_records():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='tonerdb',
                                             user='root',
                                             password='eylul')
        if connection.is_connected():
            cursor = connection.cursor()
            delete_query = "DELETE FROM tonertable"
            cursor.execute(delete_query)
            connection.commit()
            print("All records deleted from 'tonerdb' table!")

    except Error as e:
        print("Error while connecting to MySQL or deleting records:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def open_display_users_menu():
    # Create a new window for the "Display Users" menu
    display_users_window = tk.Tk()
    display_users_window.geometry('400x700')
    display_users_window.title("Display Users Menu")

    # Create a Listbox to display the data
    # listbox_display_users = tk.Listbox(display_users_window, width=40, height=10)
    # listbox_display_users.pack(pady=10)

    # Create a function to display names in the new window
    def display_users_in_new_window():
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='tonerdb',
                                                 user='root',
                                                 password='eylul')
            if connection.is_connected():
                cursor = connection.cursor()
                select_query = "SELECT alanName, verenName , markaName,dateTime FROM tonertable"
                cursor.execute(select_query)
                data = cursor.fetchall()

                # Clear the current data in the Listbox
                # listbox_display_users.delete(0, tk.END)

                # Add the retrieved data to the Listbox
                for row in data:
                    row = tk.Label(display_users_window, text=f"Given Name: {row[0]}, Taken Name: {row[1]},Taken Name: {row[2]},Date : {row[3]}")
                    row.pack(pady=10)
                    # listbox_display_users.insert(tk.END, f"Given Name: {row[0]}, Taken Name: {row[1]},Taken Name: {row[2]},Date : {row[3]}")

        except Error as e:
            print("Error while connecting to MySQL or retrieving data:", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    # Call the function to display names in the new window
    display_users_in_new_window()

def open_insert_name_menu():
    # Create a new window for the "Insert Name" menu
    insert_name_window = tk.Tk()
    insert_name_window.geometry('400x700')
    insert_name_window.title("Insert Name Menu")

    # Create labels and input spaces for "Insert Name" menu
    label_insert_alan = tk.Label(insert_name_window, text="Enter given person name:")
    label_insert_alan.pack(pady=10)

    entry_insert_alan = tk.Entry(insert_name_window)
    entry_insert_alan.pack(pady=5)

    label_insert_veren = tk.Label(insert_name_window, text="Enter taken person name:")
    label_insert_veren.pack(pady=10)

    entry_insert_veren = tk.Entry(insert_name_window)
    entry_insert_veren.pack(pady=5)

    label_insert_marka = tk.Label(insert_name_window, text="Enter title name:")
    label_insert_marka.pack(pady=10)

    entry_insert_marka = tk.Entry(insert_name_window)
    entry_insert_marka.pack(pady=5)

    # Create a function to handle the "Submit" button click event in the new window
    def submit_button_click_in_new_window():
        input_alan = entry_insert_alan.get()
        input_veren = entry_insert_veren.get()
        input_marka = entry_insert_marka.get()

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='tonerdb',
                                                 user='root',
                                                 password='eylul')
            if connection.is_connected():
                cursor = connection.cursor()

                # Get the current date
                current_date = date.today()

                # Modify the INSERT query to include the current date
                insert_query = "INSERT INTO tonertable (alanName, verenName, markaName, dateTime) VALUES (%s, %s, %s,%s)"
                cursor.execute(insert_query, (input_alan, input_veren, input_marka, current_date))
                connection.commit()
                print("Toner inserted successfully into 'tonerdb' table!")
                # Close the window after the database operations are completed
                insert_name_window.destroy()
                

        except Error as e:
            print("Error while connecting to MySQL or inserting data:", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    # Create a "Submit" button in the new window
    submit_button_in_new_window = tk.Button(insert_name_window, text="Submit", command=submit_button_click_in_new_window)
    submit_button_in_new_window.pack()
    # delete_button_in_new_window = tk.Button(insert_name_window, text="Delete All", command=delete_all_records)
    # delete_button_in_new_window.pack()

# Create the main application window


def open_main_menu():
    # Create a new window for the main menu
    buttons_window = tk.Tk()
    buttons_window.title("Main Menu")
    buttons_window.geometry('400x700')
    # Create a button to open the "Insert Name Menu" window
    insert_name_button = tk.Button(buttons_window, text="Insert Name", command=open_insert_name_menu)
    display_name_button = tk.Button(buttons_window, text="Display Database", command=open_display_users_menu)
    insert_name_button.pack(pady=10)
    display_name_button.pack(pady=10)

# Create the main application window
root = tk.Tk()
root.title("Tkinter Example")

insert_name_button = tk.Button(root, text="Insert Name", command=open_insert_name_menu)
display_name_button = tk.Button(root, text="Display Database", command=open_display_users_menu)
insert_name_button.pack(pady=10)
display_name_button.pack(pady=10)
# Run the main event loop
root.geometry('400x700')
root.mainloop()
