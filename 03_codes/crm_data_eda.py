# -----------------------------------------------------------------------------
# Author: Dhruv Panchal <dhruvpanchal1491@gmail.com>
# Project: UrbanPiper_Assignment
# Create Date: 2021-04-12
# Update Date:
# Contributors:
# Python Version: 3.8.3
# -----------------------------------------------------------------------------

# Import Packages
import pandas as pd
import os

# Change Directory
os.chdir(r'C:\Users\dhruv\Documents\UrbanPiper\02_data')
os.getcwd()

# Import Data
df = pd.read_csv("crm_data.csv")

# Continuous Variables
df.describe()
df.nunique()
df.count()

#### Would be better to get the sales cycle verified by Devarshi before making major progress and then having to rework
# Need to remap deal_stage unique values since there seem to be some duplicate entries

# Convert next_reachout_date to date format

# Data Type Conversion

# Missing Value Treatment

# Outlier Treatment

# Create New Features: Categorical and Continuous

# Univariate Report

# Bi-variate Report

#
