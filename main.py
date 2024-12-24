from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from funcs import generatePassword  # Importing the function from funcs.py

root = Tk()
root.geometry('720x480')
root.resizable(False, False)
root.title('Passwords Generator')

bgColor = '#f0f0f0'  # Light background color
textColor = '#000000'  # Black text color
buttonBgColor = '#d3d3d3'  # Light gray color for buttons
frameBgColor = '#ffffff'  # Background color for the results frame

root.configure(bg=bgColor)
style = ttk.Style()

style.configure('TFrame', background=bgColor)
style.configure('TLabel', background=bgColor, foreground=textColor)
style.configure('TButton', background=buttonBgColor, foreground=textColor)

# Counter for password generations
generationCount = 0

def copyToClipboard(passwordToCopy):
    root.clipboard_clear()
    root.clipboard_append(passwordToCopy)
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard")

# Function to handle the "Generate" button
def generate():
    global generationCount
    try:
        inputValue = int(passwordLengthEntry.get())
        if 1 <= inputValue <= 25:
            newPassword = generatePassword(inputValue)

            # Move the interface to the right
            mainFrame.place(relx=0.7, rely=0.5, anchor="center")

            # Show the results window
            resultsCanvas.place(relx=0.1, rely=0.1, width=250, height=300)

            # Create a new label to display the result
            resultLabel = Label(resultsFrame, text=newPassword, font=("Arial", 10), bg=frameBgColor, fg=textColor, cursor="hand2", justify="left", bd=0, relief="flat")
            resultLabel.pack(anchor="w", pady=5)

            # Bind password copying on hover and click
            resultLabel.bind("<Button-1>", lambda e, pwd=newPassword: copyToClipboard(pwd))

            resultsList.append(resultLabel)

            # Increment the generation counter
            generationCount += 1

            # Check if we need to reset the field
            if generationCount >= 10:
                reset()
                generationCount = 0
        else:
            messagebox.showerror("Error", "Enter a number between 1 and 25")
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

# Function to reset the results
def reset():
    global generationCount
    for label in resultsList:
        label.destroy()
    resultsList.clear()
    resultsCanvas.place_forget()  # Hide the results window
    mainFrame.place(relx=0.5, rely=0.5, anchor="center")  # Return the interface to its original position
    generationCount = 0  # Reset the generation counter

# List to store references to the result labels
resultsList = []

# Create the main interface frame
mainFrame = ttk.Frame(root, padding=20)
mainFrame.grid()

# Create a window to display the results
resultsCanvas = Canvas(root, bg=bgColor, highlightthickness=0)

# Draw a rounded rectangle
def drawRoundedRect(canvas, x, y, width, height, radius, fillColor):
    canvas.create_arc((x, y, x + radius * 2, y + radius * 2), start=90, extent=90, fill=fillColor, outline=fillColor)
    canvas.create_arc((x + width - radius * 2, y, x + width, y + radius * 2), start=0, extent=90, fill=fillColor, outline=fillColor)
    canvas.create_arc((x, y + height - radius * 2, x + radius * 2, y + height), start=180, extent=90, fill=fillColor, outline=fillColor)
    canvas.create_arc((x + width - radius * 2, y + height - radius * 2, x + width, y + height), start=270, extent=90, fill=fillColor, outline=fillColor)
    canvas.create_rectangle((x + radius, y, x + width - radius, y + height), fill=fillColor, outline=fillColor)
    canvas.create_rectangle((x, y + radius, x + width, y + height - radius), fill=fillColor, outline=fillColor)

# Draw the background with rounded corners for the results
drawRoundedRect(resultsCanvas, 0, 0, 250, 300, 20, frameBgColor)

# Frame for text inside the results window
resultsFrame = Frame(resultsCanvas, bg=frameBgColor)
resultsFrame.place(relx=0.5, rely=0.5, anchor="center")
resultsFrame.config(width=200, height=300)
resultsFrame.pack_propagate(False)

# Title
ttk.Label(mainFrame, text="Passwords Generator", font=("Arial", 19)).grid(column=0, row=0, columnspan=2, pady=10, sticky="ew")

# Input field for the password length
passwordLengthEntry = ttk.Entry(mainFrame, font=("Arial", 12), width=5, justify="center")
passwordLengthEntry.grid(column=0, row=1, padx=10, pady=10, sticky="ew")

# Function to manage placeholder behavior
def addPlaceholder(event=None):
    if passwordLengthEntry.get() == "":
        passwordLengthEntry.insert(0, "Pass len")
        passwordLengthEntry.config(foreground="grey")

def removePlaceholder(event=None):
    if passwordLengthEntry.get() == "Pass len":
        passwordLengthEntry.delete(0, "end")
        passwordLengthEntry.config(foreground="black")

# Add placeholder
passwordLengthEntry.insert(0, "Pass len")
passwordLengthEntry.config(foreground="grey")

# Bind focus events for the placeholder
passwordLengthEntry.bind("<FocusIn>", removePlaceholder)
passwordLengthEntry.bind("<FocusOut>", addPlaceholder)

# "Generate" button
generateButton = ttk.Button(mainFrame, text="Generate", command=generate)
generateButton.grid(column=0, row=2, padx=5, pady=10, sticky="ew")

# "Reset" button
resetButton = ttk.Button(mainFrame, text="Reset", command=reset)
resetButton.grid(column=1, row=2, padx=5, pady=10, sticky="ew")

# "Exit" button
quitButton = ttk.Button(mainFrame, text="Exit", command=root.destroy)
quitButton.grid(column=0, row=3, columnspan=2, pady=10, sticky="ew")

# Center all elements within the window
mainFrame.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
