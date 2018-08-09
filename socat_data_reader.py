#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Simple tool for reading SOCAT datasets using pandas. Contains two functions:
    get_socat_preamble_size - returns the number of lines in the the preamble (i.e. before the main data table)
    read_socat_file - returns a pandas DataFrame containing the preamble.

Created on Thu Aug  9 09:25:38 2018
@author: Tom Holding
"""

import pandas as pd;

#Returns the size of the preamble portion of a socat ascii file. This included everything before the individual data points:
#   The preamble/description.
#   The expedition table.
#   Post expedition table description.
#   Does not include the header of the individual data points table.
def get_socat_preamble_size(filepath):
    headerSize = 0;
    with open(filepath) as SOCAT:
      for preline in SOCAT:
         if 'Expocode' not in preline or 'yr' not in preline:
            headerSize += 1;
         else:
            break;
    return headerSize;

#Reads socat file by skipping the expedition table and description.
def read_socat_file(filepath):
    headerSize = get_socat_preamble_size(filepath);
    return pd.read_table(filepath, sep='\t', skiprows=headerSize);

