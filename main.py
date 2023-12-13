# Miles to Kilometer Converter

from tkinter import *

# Function to convert miles to kilometers
def convert():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    # Update the result label with the calculated kilometers
    result.config(text=f"{km}")

# Create the main window
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Entry widget for user to input miles
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Label indicating "Miles"
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label indicating "is equal to"
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# Result label to display the converted kilometers
result = Label(text="0")
result.grid(column=1, row=1)

# Label indicating "km"
kilo = Label(text="km")
kilo.grid(column=2, row=1)

# Button to trigger the conversion
calc = Button(text="Convert", command=convert)
calc.grid(column=1, row=2)

# Start the Tkinter event loop
window.mainloop()

# END OF CODE
