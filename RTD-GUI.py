import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import customtkinter as ct
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Reading in the dataset
data = pd.read_csv("CSV_files/filtered_data_20230816_033.csv")
Processed_data = data.iloc[0:4199, 0:44]

root = ct.CTk()
root.title("Test Pandas data frames GUI")
root.geometry("500x400")

ct.set_appearance_mode("dark")
ct.set_default_color_theme("blue")

canvas_widget = None
toolbar = None

#####################################################################################################################
# Plot class
class Graph:
    def __init__(self, data, iterate):
        self.data = data
        self.iterate = iterate
        self.tseries = 43
        self.legend = None

    def plot_data(self):
        global canvas_widget, toolbar

        # Create the Matplotlib subplots
        fig, ax = plt.subplots()

        ax.plot(self.data.iloc[:, self.tseries], self.data.iloc[:, self.iterate], color='blue', label=Processed_data.columns[self.iterate])
        ax.set_xlabel("Timeseries")
        ax.set_ylabel(Processed_data.columns[self.iterate])
        ax.legend()
        ax.grid(True)

        # Destroy previous canvas and toolbar if they exist
        if canvas_widget:
            canvas_widget.get_tk_widget().destroy()
        if toolbar:
            toolbar.destroy()

        # Embed the Matplotlib figure in the Tkinter window using FigureCanvasTkAgg
        canvas_widget = FigureCanvasTkAgg(fig, master=root)
        canvas_widget.get_tk_widget().pack()

        # Append a toolbar at the bottom of the window
        toolbar = NavigationToolbar2Tk(canvas_widget, master = root)
        toolbar.update()
        toolbar.pack()

        # Update canvas
        canvas_widget.draw()

####################################################################################################################

# Graph clearing function:

def graph_clear():

    if canvas_widget:
            canvas_widget.get_tk_widget().destroy()
    if toolbar:
        toolbar.destroy()

    return None


####################################################################################################################
# Create a frame for your dropdown menu
frame = ct.CTkFrame(root)
frame.pack(side=ct.TOP, fill=ct.X)

# Utilizing a function to create a class instance
def instance(value):
    graph = Graph(Processed_data, int(clicked.get()))
    graph.plot_data()
    return None

#label for the dropdown menu
dropdown_label = ct.CTkLabel(frame, text="Choose a dataset:")
dropdown_label.pack(side=ct.LEFT, padx=2)

# Create Dropdown menu
clicked = ct.StringVar()

#there is no function call, but the command invokes the function. "()"
drop = ct.CTkOptionMenu(master=frame, variable=clicked, values=[str(i) for i in range(1, 43)], command=instance)
drop.pack( padx = 5 )


#Clearing button, this button clears the plot:

Clear = ct.CTkButton(master = root, text = "Clear", command = graph_clear)
Clear.pack(side = ct.BOTTOM, padx = 5, pady = 3)



# Function to handle window close event
def on_closing():
    root.destroy()
    root.quit()

# Set the protocol for window close event
root.protocol("WM_DELETE_WINDOW", on_closing)

# Display graphs
root.mainloop()







