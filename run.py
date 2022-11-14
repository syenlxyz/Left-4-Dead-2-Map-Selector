# Import python packages
import numpy as np
import tkinter as tk
from tkinter.font import Font

# Draw sample from list of maps
def get_sample():
    # Set up list of maps
    maps = get_sample.items
    if not maps:
        maps = default.copy()
    num_map = len(maps)
    
    # Draw sample using random weights
    weights = np.random.poisson(size=num_map) + 1
    probs = weights / sum(weights)
    sample = np.random.choice(maps, p=probs)
    
    # Draw sample without replacement
    maps.remove(sample)
    get_sample.items = maps
    return sample

# Run tk interface
def run():
    # Set up tkinter window 
    window = tk.Tk()
    window.title('L4D2 Map Selector')
    window.geometry('300x120')

    # Create placeholder for selected map
    font = Font(family='TkDefaultFont', size=15)
    label = tk.Label(window, text='', font=font)
    label.pack(pady=30)
    
    # Create button to select map
    def generate():
        sample = get_sample()
        label['text'] = sample
    select_btn = tk.Button(window, text='Generate', command=generate)
    select_btn.pack()

    # Launch tkinter window
    window.mainloop()

# Run the main program
if __name__ == '__main__':
    # Define a list of l4d2 maps
    global default
    default = [
        'Dead Center',
        'The Passing',
        'Dark Carnival',
        'Swamp Fever',
        'Hard Rain',
        'The Parish',
        'The Sacrifice',
        'No Mercy',
        'Crash Course',
        'Death Toll',
        'Dead Air',
        'Blood Harvest',
        'Cold Stream',
        'The Last Stand'
    ]

    # Initialize list of maps
    get_sample.items = default.copy()
    run()