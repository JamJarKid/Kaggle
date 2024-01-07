import os

def add_data_path(filepath: str, datafile: str) -> str:
    #TODO: Add Docstring after adding docstring snip to luasnips 
    current_dir = os.path.dirname(filepath)
    data_path = os.path.join(current_dir, datafile)
    return data_path
    
