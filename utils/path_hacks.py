import os

def get_data_path(filepath: str, datafile: str) -> str:

    """Returns path to data files in directory to deal with relative imports

    Args:
        filepath: path of the current file accessed by __file__ variable
        datafile: path of the file containing data usually train/test.csv

    Returns:
        absolute path to the datafile
    """
    current_dir = os.path.dirname(filepath)
    data_path = os.path.join(current_dir, datafile)
    return data_path
    
