# ATGS User Interface GUI


import tkinter as tk
from tkinter import ttk
import os
import subprocess

class ServerDroneControlApp:
    def __init__(self, root):
        """
        Initialize the Server and Drone Control Panel application.

        Args:
            root (tkinter.Tk): The main application window.
        """
        self.root = root
        self.root.title("Server and Drone Control Panel")

        # Increase the window size
        self.root.geometry("700x350")

        # Create a custom style for buttons
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 15), background="white")

        # Create a frame to hold buttons and labels
        self.frame = ttk.Frame(root)
        self.frame.pack(expand=True, fill="both")

        self.server_process = None
        self.drone_process = None

        # Get the parent directory of the current script
        parent_directory = os.path.dirname(os.path.abspath(__file__))

        # Create Start and Stop buttons for the server and drone
        self.start_server_button = ttk.Button(self.frame, text="Start Server", command=self.start_server)
        self.stop_server_button = ttk.Button(self.frame, text="Stop Server", command=self.stop_server, state=tk.DISABLED)
        self.start_drone_button = ttk.Button(self.frame, text="Start Drone", command=self.start_drone)
        self.stop_drone_button = ttk.Button(self.frame, text="Stop Drone", command=self.stop_drone, state=tk.DISABLED)

        # Place buttons on the GUI
        self.start_server_button.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        self.stop_server_button.grid(row=0, column=1, padx=20, pady=10, sticky="w")
        self.start_drone_button.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.stop_drone_button.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        # Set the parent directory for server and drone scripts
        self.server_script_path = os.path.join(parent_directory, "Server.py")
        self.drone_script_path = os.path.join(parent_directory, "Drone.py")

        # Create labels for server and drone status
        self.server_status_label = ttk.Label(self.frame, text="Server Status: Not Running", font=("Helvetica", 20), foreground="red")
        self.drone_status_label = ttk.Label(self.frame, text="Drone Status: Not Running", font=("Helvetica", 20), foreground="red")

        # Place status labels on the GUI
        self.server_status_label.grid(row=2, column=0, padx=20, pady=5, sticky="w")
        self.drone_status_label.grid(row=3, column=0, padx=20, pady=5, sticky="w")

        # Center the frame in the window
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

    def update_server_status(self, running):
        """
        Update the server status label.

        Args:
            running (bool): True if the server is running, False otherwise.
        """
        if running:
            self.server_status_label.config(text="Server Status: Running", foreground="green")
        else:
            self.server_status_label.config(text="Server Status: Not Running", foreground="red")

    def update_drone_status(self, running):
        """
        Update the drone status label.

        Args:
            running (bool): True if the drone is running, False otherwise.
        """
        if running:
            self.drone_status_label.config(text="Drone Status: Running", foreground="green")
        else:
            self.drone_status_label.config(text="Drone Status: Not Running", foreground="red")

    def start_server(self):
        """Start the server process."""
        if not self.server_process:
            self.server_process = subprocess.Popen(["python3", self.server_script_path])
            self.start_server_button.config(state=tk.DISABLED)
            self.stop_server_button.config(state=tk.NORMAL)
            self.update_server_status(True)

    def stop_server(self):
        """Stop the server process."""
        if self.server_process:
            self.server_process.terminate()
            self.server_process = None
            self.start_server_button.config(state=tk.NORMAL)
            self.stop_server_button.config(state=tk.DISABLED)
            self.update_server_status(False)

    def start_drone(self):
        """Start the drone process."""
        if not self.drone_process:
            self.drone_process = subprocess.Popen(["python3", self.drone_script_path])
            self.start_drone_button.config(state=tk.DISABLED)
            self.stop_drone_button.config(state=tk.NORMAL)
            self.update_drone_status(True)

    def stop_drone(self):
        """Stop the drone process."""
        if self.drone_process:
            self.drone_process.terminate()
            self.drone_process = None
            self.start_drone_button.config(state=tk.NORMAL)
            self.stop_drone_button.config(state=tk.DISABLED)
            self.update_drone_status(False)

if __name__ == "__main__":
    root = tk.Tk()
    app = ServerDroneControlApp(root)
    root.mainloop()