# File: main.py
# Project of: CS 469
# Date Modified: July 23, 2023
# Description: Mantain the Signal Project
import sys
import tkinter as tk
from tkinter import filedialog

import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim

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

def find_location():
    """
        Function: find_location
        Parameters:
        Return: location
        Description:
        Get Lat Lon from user input
    """
    geolocator = Nominatim(user_agent="maintain-the-signal")
    user_location = input("Enter Location: ")
    location = geolocator.geocode(user_location)
    return location

def condition_data_lat(arr_preprocessed, location):
    """
            Function: condition_data_lat
            Parameters: arr_preproccesed, location
            Return: arr_condition_lat
            Description:
            Filtering Latitude from the user input
        """
    arr_condition_lat = np.logical_and(arr_preprocessed[0:,2][0:] > location.latitude - 1, arr_preprocessed[0:,2][0:] < location.latitude + 1)
    return arr_condition_lat

def condition_data_lon(arr_preprocessed, location):
    """
            Function: condition_data_lon
            Parameters: arr_preproccesed, location
            Return: arr_condition_lat
            Description:
            Filtering Longitude from the user input
        """
    arr_condition_lon = np.logical_and(arr_preprocessed[0:,3][0:] < location.longitude - -1, arr_preprocessed[0:,3][0:] > location.longitude + -1)
    return arr_condition_lon

def select_arr_download(arr_condition_lat, arr_preprocessed):
    """
            Function: arr_download
            Parameters: arr_condition_lat, arr_condition_lon, arr_preprocessed
            Return: arr_download
            Description:
            Take the Download Speed from the user input
    """
    arr_download = np.extract(arr_condition_lat, arr_preprocessed[0:,4])
    print(arr_download)
    return arr_download

def select_arr_upload(arr_condition_lat, arr_preprocessed):
    """
            Function: arr_download
            Parameters: arr_condition_lat, arr_condition_lon, arr_preprocessed
            Return: arr_download
            Description:
            Take the Upload Speed from the user input
    """
    arr_upload = np.extract(arr_condition_lat, arr_preprocessed[0:,5])
    print(arr_upload)
    return arr_upload

def select_arr_

if __name__ == '__main__':
    # Read CSV
    f_file = read_filename()
    # Parse Selected Cols
    f_parsed_arr = parse_arr_preprocesssed(f_file)
    # Filter based on location
    f_location = find_location()
    # Condition for the filtering
    f_condition_data_lat = condition_data_lat(f_parsed_arr, f_location)
    f_condition_data_lon = condition_data_lon(f_parsed_arr, f_location)
    # Select Download & Upload based on Location
    f_select_arr_download = select_arr_download(f_condition_data_lat, f_parsed_arr)
    f_select_arr_upload = select_arr_upload(f_condition_data_lat, f_parsed_arr)
