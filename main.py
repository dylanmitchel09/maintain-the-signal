# File: main.py
# Project of: CS 469
# Date Modified: July 10, 2023
# Description: Mantain the Signal Project

import tkinter as tk
from tkinter import filedialog
import pandas as pd


# Resources:

def read_filename():
    """
        Function: read_filename
        Parameters:
        Return: filename
        Description:
        Read the csv file
        File will read from filename
        Will have a dialog to choose the file
    """
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename()
    filename = open(filepath, 'r')
    return filename


def parse_arr_preprocesssed(filename):
    """
        Function: parse_file
        Parameters: filename
        Return: arr_file
        Description:
        Read Date, ConnType, Lat, Lon, Download Speed, Upload Speed from the CSV
    """
    arr_preprocessed = pd.read_csv(filepath_or_buffer=filename.name, sep=',', header=0,
                                   usecols=['Date', 'ConnType', 'Lat', 'Lon', 'Download Speed', 'Upload Speed'],
                                   index_col=False,
                                   dtype={'ConnType': 'string', 'Lat': 'f', 'Lon': 'f', 'Download Speed': 'f',
                                          'Upload Speed': 'f'},
                                   parse_dates=['Date'])
    arr_preprocessed = arr_preprocessed.to_numpy()
    return arr_preprocessed


if __name__ == '__main__':
    # Read CSV
    f_file = read_filename()
    # Parse Selected Cols
    f_parsed_arr = parse_arr_preprocesssed(f_file)
    # Print Parsed Array
    print(f_parsed_arr)
