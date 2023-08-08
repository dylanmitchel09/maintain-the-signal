# Mantain the Signal (iOS Ookla Speedtest Version)

Maintain the Signal is an application that finds the fastest average download and upload speeds based on your location within the United States and compares them between T-Mobile, Verizon, and AT&T.
Note: This application only supports exported CSV files from the Ookla Speedtest iOS version.

## Features

- Data storytelling of internet speed tests
- Use your own data from Ookla Speedtest for analysis
- Find speeds based on location within a radius of 1.15 miles

## Installation

Mantain the Signal requires [Pyhton 3.9](https://www.python.org/downloads/release/python-3913/) to run.

Install Pyhton followed by pip

```sh
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python get-pip.py
```

Install the application dependencies

```sh
$ pip install -r requirements.txt
```

## Running

To run Maintain the Signal, use the following command:

```sh
$ python3 main.py
```

You will be prompted to open the Ookla Speedtest CSV file. For example, [SpeedTestExport_20230808.csv](https://github.com/dylanmitchel09/maintain-the-signal/blob/main/SpeedTestExport_20230808.csv) is an example Ookla Speedtest CSV file.

Followed by, you will be prompted to enter the location you want to analyze

```sh
Enter Location: Oregon State University
```

Once that is finished, you will have the average upload and download speeds from T-Mobile, AT&T, and Verizon, along with the overall fastest upload and download speeds.

## Sample Output

```sh
$ python3 main.py

 ---------------------------------------------------------------------------------------------------------

Maintain the Signal (iOS Speedtest Version)


Enter Location: Oregon State University


The Average Speed Will be Shown Within Radius of 1.15 Miles


T-Mobile Average Download Speed:  182.05  Mb/s
T-Mobile Average Upload Speed:  16.08  Mb/s


Verizon Average Download Speed:  607.27  Mb/s
Verizon Average Upload Speed:  38.17  Mb/s


AT&T Average Download Speed:  85.81  Mb/s
AT&T Average Upload Speed:  14.5  Mb/s


Verizon Showed the Fastest Download Speed of 607.27 Mb/s
Verizon is Able to Stream 4K UHD Netflix Films
Verizon Showed the Fastest Upload Speed of 38.17 Mb/s
Verizon is Able to Host Group Zoom Calls in 1080p Full HD


Sources: Ookla Speedtest, Netflix Help Center & Zoom Support

---------------------------------------------------------------------------------------------------------
```
