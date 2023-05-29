CSIRO model CCAM (version r526M) - Near Surface Air Temperature
=============

The script ```add_metadata_CCAM_AirTemp.py``` aims to improve the data quality of the file ```tas_ccam_20150101_raw.nc``` by adding relevant metadata to the netCDF file. This activity is part of the Climate Data Analyst Interview exercise task.

The data is from the regional climate model CCAM and has the following characteristics:
* it was driven using data from the CSIRO-ARCCSS global climate model ACCESS-CM2 which performed the CMIP6 experiment SSP370
* the resolution is 12 km
* the data consists of hourly air temperature starting on the 1st Jan 2015

More info can be requested via the email ccam@csiro.au.

## About this task
The task description can be found in the file ```Documents/Task_description.docx``` found in this repository.

This script modifies the netCDF file by adding new attributes. These attributes are configurable through 
two config files ```global_attrs_config``` and ```var_attrs_config```.

The answer for Task 3 is in the Documents folder, as well as the processed file as a result of running the script.

## Location of Original Dataset

The original file can be found on:

https://drive.google.com/file/d/1nJTr6luWErpXFCqfptBSysIk7jW9ktoR

and there is also a copy of the file in this repository.

## Requirements
Please see ```requirements.txt``` file for required libraries.

To install packages use 
```bash
pip install -r requirements.txt
```

## Using the Script

```bash
usage: python add_metadata_CCAM_temp.py
```
Creates updated NetCDF file from CSIRO with added metadata.
```

## Contact Support
For support contact

email: berger.anap@gmail.com
