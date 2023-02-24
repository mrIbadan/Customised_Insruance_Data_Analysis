# pip install random-address
# pip install pandas

import os
import pandas as pd
import random_address

#from random_address import real_random_address

import argparse
parser = argparse.ArgumentParser(description='Script so useful.')
parser.add_argument("--opt1")

#add_dict = real_random_address()
add_dict = random_address.real_random_address()
pd.json_normalize(add_dict) # create data frame from .json format

def create_random_address_us():
    
    add_dict =random_address.real_random_address()
    add_df = pd.json_normalize(add_dict)
    
    return (add_df)

appended_data = []
for i in range(5):
    data = create_random_address_us()
    # store DataFrame in list
    appended_data.append(data)


filename = "random_us_addresses.csv"
if not os.path.isfile(filename):
    df.to_csv(filename, header='column_names', index=False)
else:  # else it exists so append without writing the header
    df.to_csv(filename, mode='a', header=False, index=False)

for i in range(sample_size):
    address_data = create_random_address_us()
    # store DataFrame in list
    address_data.to_csv(filename, mode='a', header=False, index=False)    