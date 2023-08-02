# File: main.py
# Project of: CS 469
# Date Modified: August 2, 2023
# Description: Mantain the Signal Project

import tkinter as tk
from tkinter import filedialog
import numpy as np
import pandas as pd
from geopy.geocoders import Nominatim
import warnings


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
    print("\n")
    print("The Average Speed Will be Shown Within Radius of 1.15 Miles")
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
    arr_condition_carrier_tmobile = np.logical_or(arr_preprocessed[0:, 1][0:] == "T-Mobile LTE",
                                                  arr_preprocessed[0:, 1][0:] == "T-Mobile NRNSA",
                                                  arr_preprocessed[0:, 1][0:] == "T-Mobile NR")
    arr_condition_lat = np.logical_and(arr_preprocessed[0:, 2][0:] > location.latitude - 1,
                                       arr_preprocessed[0:, 2][0:] < location.latitude + 1)
    arr_condition_lon = np.logical_and(arr_preprocessed[0:, 3][0:] < location.longitude - -1,
                                       arr_preprocessed[0:, 3][0:] > location.longitude + -1)
    arr_condition_tmobile = np.logical_and(arr_condition_carrier_tmobile, arr_condition_lat, arr_condition_lon)
    return arr_condition_tmobile


def condition_data_verizon(arr_preprocessed, location):
    """
            Function: condition_data_verizon
            Parameters: arr_preproccesed, location
            Return: arr_condition_lat
            Description:
            Filtering Location & Verizon from the user input
        """
    arr_condition_carrier_verizon = np.logical_or(arr_preprocessed[0:, 1][0:] == "Verizon LTE",
                                                  arr_preprocessed[0:, 1][0:] == "Verizon NRNSA",
                                                  arr_preprocessed[0:, 1][0:] == "Verizon NR")
    arr_condition_lat = np.logical_and(arr_preprocessed[0:, 2][0:] > location.latitude - 1,
                                       arr_preprocessed[0:, 2][0:] < location.latitude + 1)
    arr_condition_lon = np.logical_and(arr_preprocessed[0:, 3][0:] < location.longitude - -1,
                                       arr_preprocessed[0:, 3][0:] > location.longitude + -1)
    arr_condition_verizon = np.logical_and(arr_condition_carrier_verizon, arr_condition_lat, arr_condition_lon)
    return arr_condition_verizon


def condition_data_att(arr_preprocessed, location):
    """
            Function: condition_data_att
            Parameters: arr_preproccesed, location
            Return: arr_condition_lat
            Description:
            Filtering Location & AT&T from the user input
        """
    arr_condition_carrier_att = np.logical_or(arr_preprocessed[0:, 1][0:] == "AT&T LTE",
                                              arr_preprocessed[0:, 1][0:] == "AT&T NRNSA",
                                              arr_preprocessed[0:, 1][0:] == "AT&T NR")
    arr_condition_lat = np.logical_and(arr_preprocessed[0:, 2][0:] > location.latitude - 1,
                                       arr_preprocessed[0:, 2][0:] < location.latitude + 1)
    arr_condition_lon = np.logical_and(arr_preprocessed[0:, 3][0:] < location.longitude - -1,
                                       arr_preprocessed[0:, 3][0:] > location.longitude + -1)
    arr_condition_att = np.logical_and(arr_condition_carrier_att, arr_condition_lat, arr_condition_lon)
    return arr_condition_att


def select_arr_download_tmobile(arr_condition_tmobile, arr_preprocessed_tmobile):
    """
            Function: arr_download_tmobile
            Parameters: arr_condition_lat, arr_condition_lon, arr_preprocessed
            Return: arr_download
            Description:
            Take the Download Speed from the user input
    """
    arr_download_tmobile = np.extract(arr_condition_tmobile, arr_preprocessed_tmobile[0:, 4])
    arr_download_tmobile = (np.mean(arr_download_tmobile) * 0.001)
    arr_download_tmobile = np.around(arr_download_tmobile, decimals=2)
    print("\n")
    print("T-Mobile Average Download Speed: ", arr_download_tmobile, " Mb/s")
    return arr_download_tmobile


def select_arr_upload_tmobile(arr_condition_tmobile, arr_preprocessed_tmobile):
    """
            Function: arr_upload
            Parameters: arr_condition_lat, arr_condition_lon, arr_preprocessed
            Return: arr_download
            Description:
            Take the Upload Speed from the user input
    """
    arr_upload_tmobile = np.extract(arr_condition_tmobile, arr_preprocessed_tmobile[0:, 5])
    arr_upload_tmobile = (np.mean(arr_upload_tmobile) * 0.001)
    arr_upload_tmobile = np.around(arr_upload_tmobile, decimals=2)
    print("T-Mobile Average Upload Speed: ", arr_upload_tmobile, " Mb/s")
    return arr_upload_tmobile


def select_arr_download_verizon(arr_condition_verizon, arr_preprocessed_verizon):
    """
            Function: arr_download_verizon
            Parameters: arr_condition_lat, arr_condition_lon, arr_preprocessed
            Return: arr_download
            Description:
            Take the Download Speed from the user input
    """
    arr_download_verizon = np.extract(arr_condition_verizon, arr_preprocessed_verizon[0:, 4])
    arr_download_verizon = (np.mean(arr_download_verizon) * 0.001)
    arr_download_verizon = np.around(arr_download_verizon, decimals=2)
    print("\n")
    print("Verizon Average Download Speed: ", arr_download_verizon, " Mb/s")
    return arr_download_verizon


def select_arr_upload_verizon(arr_condition_verizon, arr_preprocessed_verizon):
    """
            Function: arr_upload_verizon
            Parameters: arr_condition_lat, arr_condition_lon, arr_preprocessed
            Return: arr_download
            Description:
            Take the Upload Speed from the user input
    """
    arr_upload_verizon = np.extract(arr_condition_verizon, arr_preprocessed_verizon[0:, 5])
    arr_upload_verizon = (np.mean(arr_upload_verizon) * 0.001)
    arr_upload_verizon = np.around(arr_upload_verizon, decimals=2)
    print("Verizon Average Upload Speed: ", arr_upload_verizon, " Mb/s")
    return arr_upload_verizon


def select_arr_download_att(arr_condition_att, arr_preprocessed_att):
    """
            Function: arr_download_att
            Parameters: arr_condition_lat, arr_condition_lon, arr_preprocessed
            Return: arr_download
            Description:
            Take the Download Speed from the user input
    """
    arr_download_att = np.extract(arr_condition_att, arr_preprocessed_att[0:, 4])
    arr_download_att = (np.mean(arr_download_att) * 0.001)
    arr_download_att = np.around(arr_download_att, decimals=2)
    print("\n")
    print("AT&T Average Download Speed: ", arr_download_att, " Mb/s")
    return arr_download_att


def select_arr_upload_att(arr_condition_att, arr_preprocessed_att):
    """
            Function: arr_upload_att
            Parameters: arr_condition_lat, arr_condition_lon, arr_preprocessed
            Return: arr_download
            Description:
            Take the Upload Speed from the user input
    """
    arr_upload_att = np.extract(arr_condition_att, arr_preprocessed_att[0:, 5])
    arr_upload_att = (np.mean(arr_upload_att) * 0.001)
    arr_upload_att = np.around(arr_upload_att, decimals=2)
    print("AT&T Average Upload Speed: ", arr_upload_att, " Mb/s")
    return arr_upload_att


def find_fastest_carrier(arr_download_tmobile, arr_upload_tmobile, arr_download_verizon, arr_upload_verizon,
                         arr_download_att, arr_upload_att):
    """
            Function: find_fastest_carrier
            Parameters: arr_download_tmobile, arr_upload_tmobile, arr_download_verizon, arr_upload_verizon,
                         arr_download_att, arr_upload_att
            Return:
            Description:
           Data Storytelling and Find Average for Download and Upload Speed
    """
    fastest_carrier_table = (
        ("", "T-Mobile", "Verizon", "AT&T"), ("Download", arr_download_tmobile, arr_download_verizon, arr_download_att),
        ("Upload", arr_upload_tmobile, arr_upload_verizon, arr_upload_att))

    max_avg_download = max(fastest_carrier_table[1][1:])
    max_avg_download_index = fastest_carrier_table[1].index(max_avg_download)
    max_avg_download_carrier = fastest_carrier_table[0][max_avg_download_index]

    if max_avg_download > 15:
        download_avg_desc = "is Able to Stream 4K UHD Netflix Films"
    elif 5 < max_avg_download <= 15 :
        download_avg_desc = "is Able to Stream 1080 Full HD Netflix Films"
    elif 3 < max_avg_download <= 5:
        download_avg_desc = "is Able to Stream 720 HD Netflix Films"
    else:
        download_avg_desc = "is Not Recommended to Stream Netflix Films"

    max_avg_upload = max(fastest_carrier_table[2][1:])
    max_avg_upload_index = fastest_carrier_table[2].index(max_avg_upload)
    max_avg_upload_carrier = fastest_carrier_table[0][max_avg_upload_index]

    if max_avg_upload > 3.8:
        upload_avg_desc = "is Able to Host Group Zoom Calls in 1080p Full HD"
    elif 2.6 < max_avg_upload <= 3.8 :
        upload_avg_desc = "is Able to Host Group Zoom Calls in 720p HD"
    elif 1 < max_avg_upload <= 2.6:
        upload_avg_desc = "is Able to Host Group Zoom Calls in High Quality"
    else:
        upload_avg_desc = "is not Able to Host Group Zoom Calls"

    print("\n")
    print(f"{max_avg_download_carrier} Showed the Fastest Download Speed of {max_avg_download} Mb/s")
    print(f"{max_avg_download_carrier} {download_avg_desc}")
    print(f"{max_avg_upload_carrier} Showed the Fastest Upload Speed of {max_avg_upload} Mb/s")
    print(f"{max_avg_upload_carrier} {upload_avg_desc}")

def application_header():
    """
            Function: application_header
            Parameters:
            Return:
            Description:
           Header of the application
    """
    print("\n --------------------------------------------------------------------------------------------------------- \n")
    print("Maintain the Signal (iOS Speedtest Version)")
    print("\n")

def application_footer():
    """
            Function: application_footer
            Parameters:
            Return:
            Description:
           Footer of the application
    """
    print("\n")
    print("Sources: Ookla Speedtest, Netflix Help Center & Zoom Support \n")
    print("---------------------------------------------------------------------------------------------------------")


if __name__ == '__main__':
    # Application Header
    f_application_header = application_header()
    # Remove Runtime Warning for nan Data
    warnings.filterwarnings("ignore", category=RuntimeWarning)
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
    # Select Download & Upload based on Location & Show the Speed From Each Carrier
    f_select_arr_download_tmobile = select_arr_download_tmobile(f_condition_data_tmobile, f_parsed_arr)
    f_select_arr_upload_tmobile = select_arr_upload_tmobile(f_condition_data_tmobile, f_parsed_arr)
    f_select_arr_download_verizon = select_arr_download_verizon(f_condition_data_verizon, f_parsed_arr)
    f_select_arr_upload_verizon = select_arr_upload_verizon(f_condition_data_verizon, f_parsed_arr)
    f_select_arr_download_att = select_arr_download_att(f_condition_data_att, f_parsed_arr)
    f_select_arr_upload_att = select_arr_upload_att(f_condition_data_att, f_parsed_arr)
    # Find the fastest Download & Upload
    f_find_fastest_carrier = find_fastest_carrier(f_select_arr_download_tmobile, f_select_arr_upload_tmobile,
                                                  f_select_arr_download_verizon, f_select_arr_upload_verizon,
                                                  f_select_arr_download_att, f_select_arr_upload_att)
    # Application Footer
    f_application_footer = application_footer()
