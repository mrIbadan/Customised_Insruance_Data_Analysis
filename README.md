![](https://img.shields.io/static/v1?label=&message=александр-котенко&color=:#A7C7E7)

![](https://img.shields.io/static/v1?label=&message=Readme's_in_each_Folder&color=:#FAC898)

![](https://img.shields.io/badge/powered%20by%20JupyterLab-blue.svg?logo=jupyter&logoColor=white)
![](https://img.shields.io/badge/powered%20by%20Python-yellow.svg?logo=Python&logoColor=white)
![](https://img.shields.io/badge/powered%20by%20R-blue.svg?logo=R&logoColor=white)

<h2 style="color:#ff6961"> Works in Progress TEST </h2> <ol  style="color:#A7C7E7">
   
  <li>Stratify the data better (by LOB in particular) to better relect realistic scenarios</li>
  <li>Example - for commercial property setting the value of the individual site, use external data</li>

  <li>Not worthwhile spending time here Going between rpy2 (using Python in R, seperate notebooks for now) - Easier in Data bricks %R, %sql, %Python magic commands</li>
  <li>Include some outliers for testing (so can create a control table to flag or drop these fields)</li>
</ol> 

Exploring ways to share code & demos via new [code space feature](https://github.com/alexkotsscott/Random_Data_Exploration/blob/main/CodeSpace_Link.md)
Codespace is pretty basic - about 5gb RAM
Linux based
Can handle some of the smaller demos

Coding is primarly (at this point in time) written in both R & Python
Both R & Python scripts will have a dedicated Engine to power the behind the scenes stuff - install (if not installed) packages 
The engine also contains user defined functions that are used regularly & can likely to be required to run a particular project


# Last Update - 2023/02/24

# Random_Data_Exploration
[01_Create_Data](https://github.com/alexkotsscott/Customised_Insruance_Data_Analysis/blob/master/Generate%20Data%20Sets/01_Create_Data.ipynb)
Generate random data - EDA it, model it, map it. Continual work in progress

Some of the Scripts in this can be run in the new CodeSpace feature

Random data is consists of these fields - will likely evolve to enrich the data
Geographic data - for example Latidues & Longitudes are randomly generated
  - Then reverse geocoded to get the postcode
    - The open source version is new, very slow - many ways to break this down for example:
        - Break down the data set into seperate samples and run on different machines
          - Run time about 5 hours (average) for 10,000 random rows of lats & longs)
            - Currently just random, so good luck finding a postcode in the Adriatic
            
            
            
Another appproach for generating REAL Postcodes is via python [random addresses US](https://github.com/alexkotsscott/Random_Data_Exploration/blob/main/random_addresses.ipynb)
  - Currently only generates random postcodes for a few states in the US

Randomly Generated fields below

The link below creates random data based on criteria to generate random data, sample size is optional, simple logic for example you can't have a claim count where there was no conversion (sale) to begin with

The below is a generic random dataset for multiple lines of business 
  - work to be done here on the data sample - a claim for £200 for a phone is not the same as £2,000,000 for comercial property
   - Example creating a random data set purely for the motor market - so more sensible inputs in terms of premium claims etc (second hyperlink) 
  
[01_Create_Data](https://github.com/alexkotsscott/Customised_Insruance_Data_Analysis/blob/master/Generate%20Data%20Sets/01_Create_Data.ipynb)

[01_Create_Data_Motor](https://github.com/alexkotsscott/Customised_Insruance_Data_Analysis/blob/master/Generate%20Data%20Sets/01_Motor_Create_Data.ipynb)

"Customer_ID":          Cryptographically generated random identifiers
"Purchase_Date":        Dates are random within a given range, Purchase date must always be earlier or equal to - Cover_Start_Date
"Cover_Start_Date":     Date Cover Starts - Random
"LOB":                  Line Of Business
"Sale_Flag":            Binary - 0/1
"Purchase_Price":       Randomly generated - needs to be taylored for each LOB
"Claims_Count":         Number of claims in the customers history - currently just between 0/1 at random - only generated for sales (work to be done here)
"Convictions Count":    Number of historical convictions (regardless of sale 0/1 here), bound between 0 -> 5 at random
"Period_of_Cover":      12, 24, 36, 48 months randomly sampled
"Premium":              Is Premium, random, needs logic to keep it sensible by LOB etc
"Age":                  Between 18 & 80 random
"Broker":               Random between -> 'london_ins', 'some_syndicate', 'some_mga' # Could add in weights for balance 
