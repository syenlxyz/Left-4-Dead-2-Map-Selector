import numpy as np
import tkinter as tk

class MapSelector:
    def __init__(self):
        self.items = self.get_items()
    
    @staticmethod
    def get_items():
        items = [
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
        return items
    
    def select_item(self):
        if not self.items:
            self.items = self.get_items()
        
        items = self.items
        num_item = len(items)
        
        weights = np.random.poisson(size=num_item) + 1
        probs = weights / sum(weights)
        
        item = np.random.choice(items, p=probs)
        items.remove(item)
        return item
    
    def run(self):
        window = tk.Tk()
        window.title('Left 4 Dead 2 Map Selector')
        window.geometry('320x140')
        
        label = tk.Label(window, text='Select Map', font=('TkDefaultFont', 22))
        label.pack(pady=35)
        
        def select_map():
            item = self.select_item()
            label['text'] = item
        
        button = tk.Button(window, text='Select Map', command=select_map)
        button.pack()
        
        window.mainloop()

if __name__=='__main__':
    app = MapSelector()
    app.run()