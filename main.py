# File: main.py
# Project of: CS 469
# Date Modified: July 29, 2023
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
                                   usecols=['Date', 'ConnDetails', 'Lat', 'Lon', 'Download', 'Upload'],
                                   index_col=False,
                                   dtype={'ConnDetails': 'str', 'Lat': 'f', 'Lon': 'f', 'Download': 'f',
                                          'Upload': 'f'},
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


# Finding Data

def condition_data_tmobile(arr_preprocessed, location):
    """
            Function: condition_data_tmobile
            Parameters: arr_preproccesed, location
            Return: arr_condition_lat
            Description:
            Filtering Location & T-Mobile from the user input
        """
    arr_condition_lat = np.logical_and(arr_preprocessed[0:,2][0:] > location.latitude - 1, arr_preprocessed[0:,2][0:] < location.latitude + 1)
    arr_condition_lon = np.logical_and(arr_preprocessed[0:,3][0:] < location.longitude - -1, arr_preprocessed[0:,3][0:] > location.longitude + -1)
    arr_condition_carrier = np.logical_or(arr_preprocessed[0:,1][0:] == "T-Mobile LTE", arr_preprocessed[0:,1][0:] == "T-Mobile NRNSA", arr_preprocessed[0:,1][0:] == "T-Mobile NR")
    arr_condition_tmobile = np.logical_and(arr_condition_lat, arr_condition_lon, arr_condition_carrier)
    return arr_condition_tmobile

def condition_data_verizon(arr_preprocessed, location):
    """
            Function: condition_data_verizon
            Parameters: arr_preproccesed, location
            Return: arr_condition_lat
            Description:
            Filtering Location & Verizon from the user input
        """
    arr_condition_lat = np.logical_and(arr_preprocessed[0:,2][0:] > location.latitude - 1, arr_preprocessed[0:,2][0:] < location.latitude + 1)
    arr_condition_lon = np.logical_and(arr_preprocessed[0:,3][0:] < location.longitude - -1, arr_preprocessed[0:,3][0:] > location.longitude + -1)
    arr_condition_carrier = np.logical_or(arr_preprocessed[0:,1][0:] == "Verizon LTE", arr_preprocessed[0:,1][0:] == "Verizon NRNSA", arr_preprocessed[0:,1][0:] == "Verizon NR")
    arr_condition_verizon = np.logical_and(arr_condition_lat, arr_condition_lon, arr_condition_carrier)
    return arr_condition_verizon

def condition_data_att(arr_preprocessed, location):
    """
            Function: condition_data_att
            Parameters: arr_preproccesed, location
            Return: arr_condition_lat
            Description:
            Filtering Location & AT&T from the user input
        """
    arr_condition_lat = np.logical_and(arr_preprocessed[0:,2][0:] > location.latitude - 1, arr_preprocessed[0:,2][0:] < location.latitude + 1)
    arr_condition_lon = np.logical_and(arr_preprocessed[0:,3][0:] < location.longitude - -1, arr_preprocessed[0:,3][0:] > location.longitude + -1)
    arr_condition_carrier = np.logical_or(arr_preprocessed[0:,1][0:] == "AT&T LTE", arr_preprocessed[0:,1][0:] == "AT&T NRNSA", arr_preprocessed[0:,1][0:] == "AT&T NR")
    arr_condition_att = np.logical_and(arr_condition_lat, arr_condition_lon, arr_condition_carrier)
    return arr_condition_att

def select_arr_download(arr_condition_tmobile, arr_condition_verizon, arr_condition_att, arr_preprocessed):
    """
            Function: arr_download
            Parameters: arr_condition_lat, arr_condition_lon, arr_preprocessed
            Return: arr_download
            Description:
            Take the Download Speed from the user input
    """
    arr_download_tmobile = np.extract(arr_condition_tmobile, arr_preprocessed[0:,4])
    arr_download_verizon = np.extract(arr_condition_verizon, arr_preprocessed[0:,4])
    arr_download_att = np.extract(arr_condition_att, arr_preprocessed[0:,4])
    print("\n")
    print("T-Mobile Average Download Speed: ", (np.mean(arr_download_tmobile) * 0.001), " Mb/s")
    print("Verizon Average Download Speed: ", (np.mean(arr_download_verizon) * 0.001), " Mb/s")
    print("AT&T Average Download Speed: ", (np.mean(arr_download_att) * 0.001), " Mb/s")

def select_arr_upload(arr_condition_tmobile, arr_condition_verizon, arr_condition_att, arr_preprocessed):
    """
            Function: arr_upload
            Parameters: arr_condition_lat, arr_condition_lon, arr_preprocessed
            Return: arr_download
            Description:
            Take the Upload Speed from the user input
    """
    arr_upload_tmobile = np.extract(arr_condition_tmobile, arr_preprocessed[0:,5])
    arr_upload_verizon = np.extract(arr_condition_verizon, arr_preprocessed[0:, 5])
    arr_upload_att = np.extract(arr_condition_att, arr_preprocessed[0:, 5])
    print("\n")
    print("T-Mobile Average Upload Speed: ", (np.mean(arr_upload_tmobile) * 0.001), " Mb/s")
    print("Verizon Average Upload Speed: ", (np.mean(arr_upload_verizon) * 0.001), " Mb/s")
    print("AT&T Average Upload Speed: ", (np.mean(arr_upload_att) * 0.001), " Mb/s")


if __name__ == '__main__':
    # Read CSV
    f_file = read_filename()
    # Parse Selected Cols
    f_parsed_arr = parse_arr_preprocesssed(f_file)
    # Filter based on location
    f_location = find_location()
    # Condition for the filtering
    f_condition_data_tmobile = condition_data_tmobile(f_parsed_arr, f_location)
    f_condition_data_verizon = condition_data_verizon(f_parsed_arr, f_location)
    f_condition_data_att = condition_data_att(f_parsed_arr, f_location)
    # Select Download & Upload based on Location
    f_select_arr_download = select_arr_download(f_condition_data_tmobile, f_condition_data_verizon, f_condition_data_att, f_parsed_arr)
    f_select_arr_upload = select_arr_upload(f_condition_data_tmobile, f_condition_data_verizon, f_condition_data_att, f_parsed_arr)
