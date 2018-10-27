# Code for 2018 Research Project

This repo contains all the scripts used to determine the various parameters associated with the design of a **50x50** cross dipole antenna array to be used for the detection and tracking of space debris in Low Earth Orbit (LEO)

## Pertinant Files

1. `dataFitting.py` contains the code used generate the least square regression function used to fit the original data to a new dataset of arbitrary length.
2. `test.py` contains the code used to convert the 1D matrix from the newly fitted data into a 2D matrix, and plot the resultant distribution pattern.
3. `parameters.py` contains the code used to calculate the various paramters needed in determining the desired gain of the array

All associated graphs and data-filled CSV files are included in this repo, but will be repopulated when the code is rerun
