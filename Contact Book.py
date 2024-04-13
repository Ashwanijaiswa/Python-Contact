import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Management System")

        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        self.label_name = tk.Label(self.master, text="Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_name = tk.Entry(self.master)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_phone = tk.Label(self.master, text="Phone:")
        self.label_phone.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_phone = tk.Entry(self.master)
        self.entry_phone.grid(row=1, column=1, padx=5, pady=5)

        self.label_email = tk.Label(self.master, text="Email:")
        self.label_email.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_email = tk.Entry(self.master)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        self.label_address = tk.Label(self.master, text="Address:")
        self.label_address.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_address = tk.Entry(self.master)
        self.entry_address.grid(row=3, column=1, padx=5, pady=5)

        self.button_add = tk.Button(self.master, text="Add Contact", command=self.add_contact)
        self.button_add.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.listbox_contacts = tk.Listbox(self.master, width=50)
        self.listbox_contacts.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.button_delete = tk.Button(self.master, text="Delete Contact", command=self.delete_contact)
        self.button_delete.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            contact = Contact(name, phone, email, address)
            self.contacts.append(contact)
            self.listbox_contacts.insert(tk.END, f"{contact.name}: {contact.phone_number}")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and Phone fields are required.")

    def delete_contact(self):
        selected_index = self.listbox_contacts.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.listbox_contacts.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
