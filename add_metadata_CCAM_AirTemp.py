#!/usr/bin/env python

# Importing the required packages, as listed in the file requirements.txt, which need to be previously installed
import shutil
from datetime import datetime
from configparser import ConfigParser

import netCDF4 as nc
import xarray as xr

"""
This script creates a copy of the file to be processed. Then it extracts metadata to be added as attributes, from
the config files that can be edited to contain necessary information. Next, the attributes are added as global and
variable attributes. Finally, information that needs to be extracted from the data array such as variables min 
and max values, and the end of time coverage are also added in the attributes. The file is then saved 
"""

# Create a copy of the file, so we don't overwrite the original file
shutil.copy('./tas_ccam_20150101_raw.nc', './tas_ccam_20150101_processed.nc')

# Open the copy of the netCDF file that is in this same directory, now called "..._processed.nc"
f = nc.Dataset('./tas_ccam_20150101_processed.nc', "a", format="NETCDF4")

"""Create dictionary from the config file 'global_attrs_config.ini'. The file is in this same directory in the 
folder config_files & it contains the additional global attributes.
"""
config_obj = ConfigParser()
config_obj.read("./config_files/global_attrs_config.ini")
global_attrs = dict()
g_atts = config_obj.sections()

for gatt in g_atts:
    item = config_obj.items(gatt)
    global_attrs[gatt] = dict(item)

# Add global attributes
for name, value in global_attrs['global_attributes'].items():
    setattr(f, name, value)


""" Create dictionary from the config file 'var_attrs_config.ini'. The file is in this same directory in the 
folder config_files & it contains additional attributes for the variables.
"""
config_obj = ConfigParser()
config_obj.read("./config_files/var_attrs_config.ini")
vars_attrs = dict()
vatts = config_obj.sections()

for vatt in vatts:
    item = config_obj.items(vatt)
    vars_attrs[vatt] = dict(item)

# Add variable attributes
for var in vatts:
    for n, val in vars_attrs[var].items():
        setattr(f[var], n, val)


# Find min and max vars (for lat, lon and tas)
da = xr.open_dataset('./tas_ccam_20150101_raw.nc')
for v in vars_attrs:
    if v == 'time':
        time_end = da[v].data[-1]
        setattr(f, 'time_coverage_end', str(time_end))
    else:
        v_max = da[v].values.max()
        v_min = da[v].values.min()
        # valid_max and valid_min for variables
        setattr(f[v], 'valid_min', v_min)
        setattr(f[v], 'valid_max', v_max)

today = datetime.now()
dt_string = today.strftime("%Y-%m-%dT%H:%M:%SZ")

setattr(f, 'date_created', dt_string)

f.close()