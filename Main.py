import tkinter as tk 

import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS   # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = tk.Tk() # Create the main application window
SWIDTH = root.winfo_screenwidth()   # Get the screen width
SHEIGHT = root.winfo_screenheight() # Get the screen height
root.title("Where the image will form") # Set the title of the window
root.geometry(f"{SWIDTH}x{SHEIGHT}") # Set the size of the window to match the screen size

WIT = tk.Label(root, text="Where the image will form?", font=("Arial", 60)) # Create a label for the title of the application
WIT.pack(pady=45) # Pack the label into the window

FL = tk.Label(root, text="Enter the focal length (in cm) [f] :\n(Enter the value with sign convention)", font=("Arial", 20)) # Create a label for telling the user to enter the focal length in CMs
FL.pack(pady=35) # Pack the label into the window
FI = tk.Entry(root, font= "Arial 16") # Create an entry widget for user input
FI.pack() # Pack the entry widget into the window, making it visible


OL = tk.Label(root, text="Enter the object distance from pole (in cm) [u] :\n(Enter the value with sign convention)", font=("Arial", 20)) # Create a label for telling the user to enter the object length in CMs
OL.pack(pady=35) # Pack the label into the window
OI = tk.Entry(root, font= "Arial 16") # Create an entry widget for user input
OI.pack() # Pack the entry widget into the window, making it visible


BTTN = tk.Button(root, text="Calculate", font=("Arial", 20), command=lambda: calculate()) # Create a button that will call the calculate function when clicked
BTTN.pack(pady=35) # Pack the button into the window

NOI = tk.Label(root, text="The nature of the image will be:", font=("Arial", 20)) # Create a label for displaying the nature of the image
NOI.pack(padx=30,side="left") # Pack the label into the window

DOI = tk.Label(root, text= "The distance of the image from the pole will be:", font=("Arial", 20)) # Create a label for displaying the distance of the image from the pole
DOI.pack(padx=30,side="right") # Pack the label into the window

canvas = tk.Canvas(root, width=550, height=300,) # Create a canvas widget for adding images
canvas.pack(padx=10) # Pack the canvas into the window

OBC_path = resource_path("images/Object_beyond_c_case.png") # Get the path to the object image
OBC = tk.PhotoImage(file=OBC_path) # Load the object image
OAC_path = resource_path("images/Object_at_C.png") # Get the path to the object image
OAC = tk.PhotoImage(file=OAC_path) # Load the object image
OBFC_path = resource_path("images/Object_btw_F_C.png") # Get the path to the object image
OBFC = tk.PhotoImage(file=OBFC_path) # Load the object image
OAF_path = resource_path("images/Object_at_F.png") # Get the path to the object image
OAF = tk.PhotoImage(file=OAF_path) # Load the object image
OBFP_path = resource_path("images/Object_btw_F_P.png") # Get the path to the object image
OBFP = tk.PhotoImage(file=OBFP_path) # Load the object image
OAD_path = resource_path("images/Object_at_dis.png") # Get the path to the object image
OAD = tk.PhotoImage(file=OAD_path) # Load the object image

def calculate():
    f = float(FI.get()) # Get the focal length from the user input and convert it to a float
    u = float(OI.get()) # Get the object distance from the user input and convert it to a float
    v = (u*f)/(u-f) # Calculate the image distance using the lens formula
    canvas.delete("all") # Clear the canvas of any previous images
    if 2*f > u and f < 0 : 
        NOI.config(text="The nature of the image will be:\n1)Image will form between C and F\n2) The image will be Diminished\n3) The image will be real and inverted") # Update the nature of the image label with the appropriate text
        DOI.config(text=f"The distance of the image from the pole will be:\n{v} cm") # Update the distance of the image label with the calculated value
        canvas.create_image(275, 150, image=OBC) # Add the object image to the canvas
    elif 2*f == u and f<0 :
        NOI.config(text="The nature of the image will be:\n1)Image will form at C\n2) The image will be the same size of the object\n3) The image will be Real and Inverted") # Update the nature of the image label with the appropriate text
        DOI.config(text=f"The distance of the image from the pole will be:\n{v} cm") # Update the distance of the image label with the calculated value
        canvas.create_image(275, 150, image=OAC) # Add the object image to the canvas
    elif 2*f < u < f :
        NOI.config(text="The nature of the image will be:\n1)The image will form beyond the center of curvature\n2) The image will be magnified/enlarged\n3) The image will be real and inverted") # Update the nature of the image label with the appropriate text
        DOI.config(text=f"The distance of the image from the pole will be:\n{v} cm") # Update the distance of the image label with the calculated value
        canvas.create_image(275, 150, image=OBFC) # Add the object image to the canvas
    elif f == u:
        NOI.config(text="The nature of the image will be:\n1) The image will form at infinity\n2) The image will be highly enlarged\n3) The image will be real and inverted") # Update the nature of the image label with the appropriate text
        DOI.config(text=f"The distance of the image from the pole will be:\n{v} cm") # Update the distance of the image label with the calculated value
        canvas.create_image(275, 150, image=OAF) # Add the object image to the canvas
    elif f < u and f<0 :
        NOI.config(text="The nature of the image will be:\n1) The image will form behind the mirror\n2) The image will be magnified/enlarged\n3)The image formed will be virtual and erect") # Update the nature of the image label with the appropriate text
        DOI.config(text=f"The distance of the image from the pole will be:\n{v} cm") # Update the distance of the image label with the calculated value
        canvas.create_image(275, 150, image=OBFP) # Add the object image to the canvas
    elif f > u and f>0 :
        NOI.config(text="The nature of the image will be:\n1) The image will form behind the mirror\n2) The image will be diminished\n3)The image formed will be virtual and erect") # Update the nature of the image label with the appropriate text
        DOI.config(text=f"The distance of the image from the pole will be:\n{v} cm") # Update the distance of the image label with the calculated value
        canvas.create_image(275, 150, image=OAD) # Add the object image to the canvas

root.mainloop()