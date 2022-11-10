import numpy as np
import tkinter as tk
from tkinter.font import Font

def get_sample():
    maps = get_sample.items
    if not maps:
        maps = default.copy()
    num_map = len(maps)
    
    weights = np.random.poisson(size=num_map) + 1
    probs = weights / sum(weights)
    sample = np.random.choice(maps, p=probs)
    
    maps.remove(sample)
    get_sample.items = maps
    return sample

def run():
    window = tk.Tk()
    window.title('L4D2 Map Selector')
    window.geometry('300x120')

    font = Font(family='TkDefaultFont', size=15)
    label = tk.Label(window, text='', font=font)
    label.pack(pady=30)
    
    def generate():
        sample = get_sample()
        label['text'] = sample
    select_btn = tk.Button(window, text='Generate', command=generate)
    select_btn.pack()

    window.mainloop()

if __name__ == '__main__':
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

    get_sample.items = default.copy()
    run()