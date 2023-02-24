{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4dcf6f80",
   "metadata": {},
   "source": [
    "<h2 style=\"color:#ff6961\"> Works in Progress </h2> <ol  style=\"color:#A7C7E7\">\n",
    "   \n",
    "  <li>Stratify the data better (by LOB in particular) to better relect realistic scenarios</li>\n",
    "  <li>Example - for commercial property setting the value of the individual site, use external data</li>\n",
    "\n",
    "  <li>Not worthwhile spending time here Going between rpy2 (using Python in R, seperate notebooks for now) - Easier in Data bricks %R, %sql, %Python magic commands</li>\n",
    "  <li>Include some outliers for testing (so can create a control table to flag or drop these fields)</li>\n",
    "\n",
    "\n",
    "</ol> "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "98d75210",
   "metadata": {},
   "source": [
    "<h2 style=\"color:#D198B7\">Set Seed for reproducible code</h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fd5266ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "set.seed(080545)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f4f71707",
   "metadata": {},
   "source": [
    "<h2 style=\"color:#D198B7\">Read in Engine to support custom made packages </h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d20c3b26",
   "metadata": {},
   "outputs": [],
   "source": [
    "source(\"C:/Users/alexz/OneDrive/Documents/Git/Engine/Engine.R\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ed1c304c",
   "metadata": {},
   "source": [
    "<h3 style=\"color:#98D1B2 \">Load in required libraries</h3>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "13c859f7",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# List of packages required for the project\n",
    "packs <- c('dplyr', 'tidyr', 'data.table', 'lubridate', 'ids', 'randgeo', 'tidygeocoder', 'reticulate')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "60b405bc",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "Attaching package: 'dplyr'\n",
      "\n",
      "\n",
      "The following objects are masked from 'package:stats':\n",
      "\n",
      "    filter, lag\n",
      "\n",
      "\n",
      "The following objects are masked from 'package:base':\n",
      "\n",
      "    intersect, setdiff, setequal, union\n",
      "\n",
      "\n",
      "\n",
      "Attaching package: 'data.table'\n",
      "\n",
      "\n",
      "The following objects are masked from 'package:dplyr':\n",
      "\n",
      "    between, first, last\n",
      "\n",
      "\n",
      "\n",
      "Attaching package: 'lubridate'\n",
      "\n",
      "\n",
      "The following objects are masked from 'package:data.table':\n",
      "\n",
      "    hour, isoweek, mday, minute, month, quarter, second, wday, week,\n",
      "    yday, year\n",
      "\n",
      "\n",
      "The following objects are masked from 'package:base':\n",
      "\n",
      "    date, intersect, setdiff, union\n",
      "\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<dl>\n",
       "\t<dt>$dplyr</dt>\n",
       "\t\t<dd><style>\n",
       ".list-inline {list-style: none; margin:0; padding: 0}\n",
       ".list-inline>li {display: inline-block}\n",
       ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
       "</style>\n",
       "<ol class=list-inline><li>'dplyr'</li><li>'stats'</li><li>'graphics'</li><li>'grDevices'</li><li>'utils'</li><li>'datasets'</li><li>'methods'</li><li>'base'</li></ol>\n",
       "</dd>\n",
       "\t<dt>$tidyr</dt>\n",
       "\t\t<dd><style>\n",
       ".list-inline {list-style: none; margin:0; padding: 0}\n",
       ".list-inline>li {display: inline-block}\n",
       ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
       "</style>\n",
       "<ol class=list-inline><li>'tidyr'</li><li>'dplyr'</li><li>'stats'</li><li>'graphics'</li><li>'grDevices'</li><li>'utils'</li><li>'datasets'</li><li>'methods'</li><li>'base'</li></ol>\n",
       "</dd>\n",
       "\t<dt>$data.table</dt>\n",
       "\t\t<dd><style>\n",
       ".list-inline {list-style: none; margin:0; padding: 0}\n",
       ".list-inline>li {display: inline-block}\n",
       ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
       "</style>\n",
       "<ol class=list-inline><li>'data.table'</li><li>'tidyr'</li><li>'dplyr'</li><li>'stats'</li><li>'graphics'</li><li>'grDevices'</li><li>'utils'</li><li>'datasets'</li><li>'methods'</li><li>'base'</li></ol>\n",
       "</dd>\n",
       "\t<dt>$lubridate</dt>\n",
       "\t\t<dd><style>\n",
       ".list-inline {list-style: none; margin:0; padding: 0}\n",
       ".list-inline>li {display: inline-block}\n",
       ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
       "</style>\n",
       "<ol class=list-inline><li>'lubridate'</li><li>'data.table'</li><li>'tidyr'</li><li>'dplyr'</li><li>'stats'</li><li>'graphics'</li><li>'grDevices'</li><li>'utils'</li><li>'datasets'</li><li>'methods'</li><li>'base'</li></ol>\n",
       "</dd>\n",
       "\t<dt>$ids</dt>\n",
       "\t\t<dd><style>\n",
       ".list-inline {list-style: none; margin:0; padding: 0}\n",
       ".list-inline>li {display: inline-block}\n",
       ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
       "</style>\n",
       "<ol class=list-inline><li>'ids'</li><li>'lubridate'</li><li>'data.table'</li><li>'tidyr'</li><li>'dplyr'</li><li>'stats'</li><li>'graphics'</li><li>'grDevices'</li><li>'utils'</li><li>'datasets'</li><li>'methods'</li><li>'base'</li></ol>\n",
       "</dd>\n",
       "\t<dt>$randgeo</dt>\n",
       "\t\t<dd><style>\n",
       ".list-inline {list-style: none; margin:0; padding: 0}\n",
       ".list-inline>li {display: inline-block}\n",
       ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
       "</style>\n",
       "<ol class=list-inline><li>'randgeo'</li><li>'ids'</li><li>'lubridate'</li><li>'data.table'</li><li>'tidyr'</li><li>'dplyr'</li><li>'stats'</li><li>'graphics'</li><li>'grDevices'</li><li>'utils'</li><li>'datasets'</li><li>'methods'</li><li>'base'</li></ol>\n",
       "</dd>\n",
       "\t<dt>$tidygeocoder</dt>\n",
       "\t\t<dd><style>\n",
       ".list-inline {list-style: none; margin:0; padding: 0}\n",
       ".list-inline>li {display: inline-block}\n",
       ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
       "</style>\n",
       "<ol class=list-inline><li>'tidygeocoder'</li><li>'randgeo'</li><li>'ids'</li><li>'lubridate'</li><li>'data.table'</li><li>'tidyr'</li><li>'dplyr'</li><li>'stats'</li><li>'graphics'</li><li>'grDevices'</li><li>'utils'</li><li>'datasets'</li><li>'methods'</li><li>'base'</li></ol>\n",
       "</dd>\n",
       "\t<dt>$reticulate</dt>\n",
       "\t\t<dd><style>\n",
       ".list-inline {list-style: none; margin:0; padding: 0}\n",
       ".list-inline>li {display: inline-block}\n",
       ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
       "</style>\n",
       "<ol class=list-inline><li>'reticulate'</li><li>'tidygeocoder'</li><li>'randgeo'</li><li>'ids'</li><li>'lubridate'</li><li>'data.table'</li><li>'tidyr'</li><li>'dplyr'</li><li>'stats'</li><li>'graphics'</li><li>'grDevices'</li><li>'utils'</li><li>'datasets'</li><li>'methods'</li><li>'base'</li></ol>\n",
       "</dd>\n",
       "</dl>\n"
      ],
      "text/latex": [
       "\\begin{description}\n",
       "\\item[\\$dplyr] \\begin{enumerate*}\n",
       "\\item 'dplyr'\n",
       "\\item 'stats'\n",
       "\\item 'graphics'\n",
       "\\item 'grDevices'\n",
       "\\item 'utils'\n",
       "\\item 'datasets'\n",
       "\\item 'methods'\n",
       "\\item 'base'\n",
       "\\end{enumerate*}\n",
       "\n",
       "\\item[\\$tidyr] \\begin{enumerate*}\n",
       "\\item 'tidyr'\n",
       "\\item 'dplyr'\n",
       "\\item 'stats'\n",
       "\\item 'graphics'\n",
       "\\item 'grDevices'\n",
       "\\item 'utils'\n",
       "\\item 'datasets'\n",
       "\\item 'methods'\n",
       "\\item 'base'\n",
       "\\end{enumerate*}\n",
       "\n",
       "\\item[\\$data.table] \\begin{enumerate*}\n",
       "\\item 'data.table'\n",
       "\\item 'tidyr'\n",
       "\\item 'dplyr'\n",
       "\\item 'stats'\n",
       "\\item 'graphics'\n",
       "\\item 'grDevices'\n",
       "\\item 'utils'\n",
       "\\item 'datasets'\n",
       "\\item 'methods'\n",
       "\\item 'base'\n",
       "\\end{enumerate*}\n",
       "\n",
       "\\item[\\$lubridate] \\begin{enumerate*}\n",
       "\\item 'lubridate'\n",
       "\\item 'data.table'\n",
       "\\item 'tidyr'\n",
       "\\item 'dplyr'\n",
       "\\item 'stats'\n",
       "\\item 'graphics'\n",
       "\\item 'grDevices'\n",
       "\\item 'utils'\n",
       "\\item 'datasets'\n",
       "\\item 'methods'\n",
       "\\item 'base'\n",
       "\\end{enumerate*}\n",
       "\n",
       "\\item[\\$ids] \\begin{enumerate*}\n",
       "\\item 'ids'\n",
       "\\item 'lubridate'\n",
       "\\item 'data.table'\n",
       "\\item 'tidyr'\n",
       "\\item 'dplyr'\n",
       "\\item 'stats'\n",
       "\\item 'graphics'\n",
       "\\item 'grDevices'\n",
       "\\item 'utils'\n",
       "\\item 'datasets'\n",
       "\\item 'methods'\n",
       "\\item 'base'\n",
       "\\end{enumerate*}\n",
       "\n",
       "\\item[\\$randgeo] \\begin{enumerate*}\n",
       "\\item 'randgeo'\n",
       "\\item 'ids'\n",
       "\\item 'lubridate'\n",
       "\\item 'data.table'\n",
       "\\item 'tidyr'\n",
       "\\item 'dplyr'\n",
       "\\item 'stats'\n",
       "\\item 'graphics'\n",
       "\\item 'grDevices'\n",
       "\\item 'utils'\n",
       "\\item 'datasets'\n",
       "\\item 'methods'\n",
       "\\item 'base'\n",
       "\\end{enumerate*}\n",
       "\n",
       "\\item[\\$tidygeocoder] \\begin{enumerate*}\n",
       "\\item 'tidygeocoder'\n",
       "\\item 'randgeo'\n",
       "\\item 'ids'\n",
       "\\item 'lubridate'\n",
       "\\item 'data.table'\n",
       "\\item 'tidyr'\n",
       "\\item 'dplyr'\n",
       "\\item 'stats'\n",
       "\\item 'graphics'\n",
       "\\item 'grDevices'\n",
       "\\item 'utils'\n",
       "\\item 'datasets'\n",
       "\\item 'methods'\n",
       "\\item 'base'\n",
       "\\end{enumerate*}\n",
       "\n",
       "\\item[\\$reticulate] \\begin{enumerate*}\n",
       "\\item 'reticulate'\n",
       "\\item 'tidygeocoder'\n",
       "\\item 'randgeo'\n",
       "\\item 'ids'\n",
       "\\item 'lubridate'\n",
       "\\item 'data.table'\n",
       "\\item 'tidyr'\n",
       "\\item 'dplyr'\n",
       "\\item 'stats'\n",
       "\\item 'graphics'\n",
       "\\item 'grDevices'\n",
       "\\item 'utils'\n",
       "\\item 'datasets'\n",
       "\\item 'methods'\n",
       "\\item 'base'\n",
       "\\end{enumerate*}\n",
       "\n",
       "\\end{description}\n"
      ],
      "text/markdown": [
       "$dplyr\n",
       ":   1. 'dplyr'\n",
       "2. 'stats'\n",
       "3. 'graphics'\n",
       "4. 'grDevices'\n",
       "5. 'utils'\n",
       "6. 'datasets'\n",
       "7. 'methods'\n",
       "8. 'base'\n",
       "\n",
       "\n",
       "\n",
       "$tidyr\n",
       ":   1. 'tidyr'\n",
       "2. 'dplyr'\n",
       "3. 'stats'\n",
       "4. 'graphics'\n",
       "5. 'grDevices'\n",
       "6. 'utils'\n",
       "7. 'datasets'\n",
       "8. 'methods'\n",
       "9. 'base'\n",
       "\n",
       "\n",
       "\n",
       "$data.table\n",
       ":   1. 'data.table'\n",
       "2. 'tidyr'\n",
       "3. 'dplyr'\n",
       "4. 'stats'\n",
       "5. 'graphics'\n",
       "6. 'grDevices'\n",
       "7. 'utils'\n",
       "8. 'datasets'\n",
       "9. 'methods'\n",
       "10. 'base'\n",
       "\n",
       "\n",
       "\n",
       "$lubridate\n",
       ":   1. 'lubridate'\n",
       "2. 'data.table'\n",
       "3. 'tidyr'\n",
       "4. 'dplyr'\n",
       "5. 'stats'\n",
       "6. 'graphics'\n",
       "7. 'grDevices'\n",
       "8. 'utils'\n",
       "9. 'datasets'\n",
       "10. 'methods'\n",
       "11. 'base'\n",
       "\n",
       "\n",
       "\n",
       "$ids\n",
       ":   1. 'ids'\n",
       "2. 'lubridate'\n",
       "3. 'data.table'\n",
       "4. 'tidyr'\n",
       "5. 'dplyr'\n",
       "6. 'stats'\n",
       "7. 'graphics'\n",
       "8. 'grDevices'\n",
       "9. 'utils'\n",
       "10. 'datasets'\n",
       "11. 'methods'\n",
       "12. 'base'\n",
       "\n",
       "\n",
       "\n",
       "$randgeo\n",
       ":   1. 'randgeo'\n",
       "2. 'ids'\n",
       "3. 'lubridate'\n",
       "4. 'data.table'\n",
       "5. 'tidyr'\n",
       "6. 'dplyr'\n",
       "7. 'stats'\n",
       "8. 'graphics'\n",
       "9. 'grDevices'\n",
       "10. 'utils'\n",
       "11. 'datasets'\n",
       "12. 'methods'\n",
       "13. 'base'\n",
       "\n",
       "\n",
       "\n",
       "$tidygeocoder\n",
       ":   1. 'tidygeocoder'\n",
       "2. 'randgeo'\n",
       "3. 'ids'\n",
       "4. 'lubridate'\n",
       "5. 'data.table'\n",
       "6. 'tidyr'\n",
       "7. 'dplyr'\n",
       "8. 'stats'\n",
       "9. 'graphics'\n",
       "10. 'grDevices'\n",
       "11. 'utils'\n",
       "12. 'datasets'\n",
       "13. 'methods'\n",
       "14. 'base'\n",
       "\n",
       "\n",
       "\n",
       "$reticulate\n",
       ":   1. 'reticulate'\n",
       "2. 'tidygeocoder'\n",
       "3. 'randgeo'\n",
       "4. 'ids'\n",
       "5. 'lubridate'\n",
       "6. 'data.table'\n",
       "7. 'tidyr'\n",
       "8. 'dplyr'\n",
       "9. 'stats'\n",
       "10. 'graphics'\n",
       "11. 'grDevices'\n",
       "12. 'utils'\n",
       "13. 'datasets'\n",
       "14. 'methods'\n",
       "15. 'base'\n",
       "\n",
       "\n",
       "\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "$dplyr\n",
       "[1] \"dplyr\"     \"stats\"     \"graphics\"  \"grDevices\" \"utils\"     \"datasets\" \n",
       "[7] \"methods\"   \"base\"     \n",
       "\n",
       "$tidyr\n",
       "[1] \"tidyr\"     \"dplyr\"     \"stats\"     \"graphics\"  \"grDevices\" \"utils\"    \n",
       "[7] \"datasets\"  \"methods\"   \"base\"     \n",
       "\n",
       "$data.table\n",
       " [1] \"data.table\" \"tidyr\"      \"dplyr\"      \"stats\"      \"graphics\"  \n",
       " [6] \"grDevices\"  \"utils\"      \"datasets\"   \"methods\"    \"base\"      \n",
       "\n",
       "$lubridate\n",
       " [1] \"lubridate\"  \"data.table\" \"tidyr\"      \"dplyr\"      \"stats\"     \n",
       " [6] \"graphics\"   \"grDevices\"  \"utils\"      \"datasets\"   \"methods\"   \n",
       "[11] \"base\"      \n",
       "\n",
       "$ids\n",
       " [1] \"ids\"        \"lubridate\"  \"data.table\" \"tidyr\"      \"dplyr\"     \n",
       " [6] \"stats\"      \"graphics\"   \"grDevices\"  \"utils\"      \"datasets\"  \n",
       "[11] \"methods\"    \"base\"      \n",
       "\n",
       "$randgeo\n",
       " [1] \"randgeo\"    \"ids\"        \"lubridate\"  \"data.table\" \"tidyr\"     \n",
       " [6] \"dplyr\"      \"stats\"      \"graphics\"   \"grDevices\"  \"utils\"     \n",
       "[11] \"datasets\"   \"methods\"    \"base\"      \n",
       "\n",
       "$tidygeocoder\n",
       " [1] \"tidygeocoder\" \"randgeo\"      \"ids\"          \"lubridate\"    \"data.table\"  \n",
       " [6] \"tidyr\"        \"dplyr\"        \"stats\"        \"graphics\"     \"grDevices\"   \n",
       "[11] \"utils\"        \"datasets\"     \"methods\"      \"base\"        \n",
       "\n",
       "$reticulate\n",
       " [1] \"reticulate\"   \"tidygeocoder\" \"randgeo\"      \"ids\"          \"lubridate\"   \n",
       " [6] \"data.table\"   \"tidyr\"        \"dplyr\"        \"stats\"        \"graphics\"    \n",
       "[11] \"grDevices\"    \"utils\"        \"datasets\"     \"methods\"      \"base\"        \n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "install_load_packages(packs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5283a0ec",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Set Sample Size\n",
    "# Set low since reverse geocoding takes a LONG time without for example a google API\n",
    "sample_size = 1000"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fbd29bf9",
   "metadata": {},
   "source": [
    "<h3 style=\"color:#98D1B2 \">Create Dummy Data - DataFrame</h3>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4d060b29",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create Vector of factors with colNames\n",
    "colNames = c(\"Customer_ID\", \"Purchase_Date\", \"Cover_Start_Date\", \"LOB\", \"Sale_Flag\", \"Purchase_Price\",\n",
    "             \"Claims_Count\", \"Period_of_Cover\", \"Premium\", \"Age\", \"Broker\")\n",
    "\n",
    "# Create a Empty DataFrame with 0 rows and n columns (set in sample_size)\n",
    "df = data.frame(matrix(nrow = sample_size, ncol = length(colNames))) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0f33ebfc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Assign column names\n",
    "colnames(df) = colNames"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a9d76f66",
   "metadata": {
    "tags": []
   },
   "source": [
    "<h3 style=\"color:#98D1B2 \">Create Dummy Data - populate DataFrame</h3>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "99cdae3c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Generate Random Customer IDs\n",
    "df$Customer_ID <- random_id(sample_size)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "bef4b1fb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# SET date components:\n",
    "s_year <- 2022\n",
    "s_month <- 01 \n",
    "s_day <- 01\n",
    "\n",
    "dt_start <- paste(s_year, s_month, s_day, sep = '-')\n",
    "dt_start <- as.Date(ymd(dt_start))\n",
    "\n",
    "current_dt <- as.Date(today())\n",
    "\n",
    "td <- current_dt - dt_start #time difference"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "e3041ff2",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Warning message in unclass(e1) + unclass(e2):\n",
      "\"longer object length is not a multiple of shorter object length\"\n"
     ]
    }
   ],
   "source": [
    "date_range <- as.Date('2022-01-01') - as.Date('2023-01-01') # date Range\n",
    "date_vec <- as.Date('2023-01-01') + sample(0:td, sample_size, replace = TRUE) # vector of dates\n",
    "\n",
    "df$Purchase_Date <- date_vec\n",
    "df$Cover_Start_Date = date_vec + sample(1:365, replace = TRUE) # start dates up to a year of purchase date - random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "1a3844a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Lines of Business\n",
    "lob_list <- c('Commerical Property', 'Motor', 'Home', 'Gadget', 'Pet', 'Travel')\n",
    "df$LOB <- sample(lob_list, sample_size, replace=TRUE)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "8428946d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sale Flag\n",
    "df$Sale_Flag <- sample(0:1, sample_size, replace=TRUE)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4ecf5ba4",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Purchase Price\n",
    "df$Purchase_Price <- sample(10:100000, sample_size, replace=TRUE)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "deb55055",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Premium\n",
    "df$Premium <- sample(10:1000, sample_size, replace=TRUE)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "b3b3d095",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Claims Count\n",
    "# If there is a sale - there is a possibility of a claim - otherwise it must default to zero\n",
    "df$Claims_Count <- ifelse(df$Sale_Flag == 1, \n",
    "                      sample(0:1, sample_size, replace = T),\n",
    "                      0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44537df4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convictions Count\n",
    "# If there is a sale - there is a possibility of a claim - otherwise it must default to zero\n",
    "df$Claims_Count <- ifelse(df$Sale_Flag == 1, \n",
    "                      sample(0:1, sample_size, replace = T),\n",
    "                      0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "a5cafaeb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Period of cover by months\n",
    "sample_input <- c(12, 24, 36, 48)\n",
    "df$Period_of_Cover <- sample(sample_input, sample_size, TRUE)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "032a5b43",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Lats & Longs - can then Reverse Geocode to get Postcode\n",
    "lats_longs <- rg_position(sample_size)\n",
    "lats_longs <- as.data.frame(t(data.frame(lats_longs)))\n",
    "\n",
    "names(lats_longs) <- c('Latitude', 'Longitude')\n",
    "\n",
    "df$Latitude <- lats_longs$Latitude\n",
    "df$Longitude <- lats_longs$Longitude"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "b76a113a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Age\n",
    "df$Age <- sample(18:80, sample_size, replace=TRUE)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "d1321505",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Lines of Business\n",
    "broker_list <- c('london_ins', 'some_syndicate', 'some_mga')\n",
    "df$Broker <- sample(broker_list, sample_size, replace=TRUE)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "35964b81",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table class=\"dataframe\">\n",
       "<caption>A data.frame: 6 × 13</caption>\n",
       "<thead>\n",
       "\t<tr><th></th><th scope=col>Customer_ID</th><th scope=col>Purchase_Date</th><th scope=col>Cover_Start_Date</th><th scope=col>LOB</th><th scope=col>Sale_Flag</th><th scope=col>Purchase_Price</th><th scope=col>Claims_Count</th><th scope=col>Period_of_Cover</th><th scope=col>Premium</th><th scope=col>Age</th><th scope=col>Broker</th><th scope=col>Latitude</th><th scope=col>Longitude</th></tr>\n",
       "\t<tr><th></th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;date&gt;</th><th scope=col>&lt;date&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;lgl&gt;</th><th scope=col>&lt;lgl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
       "</thead>\n",
       "<tbody>\n",
       "\t<tr><th scope=row>1</th><td>d2d2062d6d73bfe37440b5bc9aebc518</td><td>2023-08-04</td><td>2024-01-15</td><td>Motor</td><td>0</td><td>16898</td><td>0</td><td>48</td><td>802</td><td>NA</td><td>NA</td><td>-115.15198</td><td>-58.22413537</td></tr>\n",
       "\t<tr><th scope=row>2</th><td>ef5865f3cbf1d48b814e9716f235cfbf</td><td>2023-03-30</td><td>2023-12-02</td><td>Motor</td><td>0</td><td>21716</td><td>0</td><td>12</td><td>155</td><td>NA</td><td>NA</td><td>-155.84526</td><td>-55.21116345</td></tr>\n",
       "\t<tr><th scope=row>3</th><td>5a30397fc844734533879fef33313971</td><td>2023-11-28</td><td>2024-07-11</td><td>Motor</td><td>1</td><td>52179</td><td>1</td><td>12</td><td>503</td><td>NA</td><td>NA</td><td>-131.15406</td><td> 17.26387609</td></tr>\n",
       "\t<tr><th scope=row>4</th><td>61474708950929d053ef8a5cb3ca5c8e</td><td>2023-10-02</td><td>2024-05-08</td><td>Motor</td><td>1</td><td>61232</td><td>1</td><td>48</td><td>804</td><td>NA</td><td>NA</td><td>  27.15229</td><td>-20.92771000</td></tr>\n",
       "\t<tr><th scope=row>5</th><td>afc58a586eeae1560526c07651f6bd80</td><td>2023-04-30</td><td>2024-04-12</td><td>Motor</td><td>0</td><td> 2711</td><td>0</td><td>24</td><td> 94</td><td>NA</td><td>NA</td><td> -10.96663</td><td> 17.87203882</td></tr>\n",
       "\t<tr><th scope=row>6</th><td>7fdcdd9fd1a203c40e5743b88132ff99</td><td>2023-04-18</td><td>2023-04-28</td><td>Motor</td><td>0</td><td>17872</td><td>0</td><td>24</td><td>665</td><td>NA</td><td>NA</td><td>  24.09823</td><td>  0.07360046</td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "A data.frame: 6 × 13\n",
       "\\begin{tabular}{r|lllllllllllll}\n",
       "  & Customer\\_ID & Purchase\\_Date & Cover\\_Start\\_Date & LOB & Sale\\_Flag & Purchase\\_Price & Claims\\_Count & Period\\_of\\_Cover & Premium & Age & Broker & Latitude & Longitude\\\\\n",
       "  & <chr> & <date> & <date> & <chr> & <int> & <int> & <dbl> & <dbl> & <int> & <lgl> & <lgl> & <dbl> & <dbl>\\\\\n",
       "\\hline\n",
       "\t1 & d2d2062d6d73bfe37440b5bc9aebc518 & 2023-08-04 & 2024-01-15 & Motor & 0 & 16898 & 0 & 48 & 802 & NA & NA & -115.15198 & -58.22413537\\\\\n",
       "\t2 & ef5865f3cbf1d48b814e9716f235cfbf & 2023-03-30 & 2023-12-02 & Motor & 0 & 21716 & 0 & 12 & 155 & NA & NA & -155.84526 & -55.21116345\\\\\n",
       "\t3 & 5a30397fc844734533879fef33313971 & 2023-11-28 & 2024-07-11 & Motor & 1 & 52179 & 1 & 12 & 503 & NA & NA & -131.15406 &  17.26387609\\\\\n",
       "\t4 & 61474708950929d053ef8a5cb3ca5c8e & 2023-10-02 & 2024-05-08 & Motor & 1 & 61232 & 1 & 48 & 804 & NA & NA &   27.15229 & -20.92771000\\\\\n",
       "\t5 & afc58a586eeae1560526c07651f6bd80 & 2023-04-30 & 2024-04-12 & Motor & 0 &  2711 & 0 & 24 &  94 & NA & NA &  -10.96663 &  17.87203882\\\\\n",
       "\t6 & 7fdcdd9fd1a203c40e5743b88132ff99 & 2023-04-18 & 2023-04-28 & Motor & 0 & 17872 & 0 & 24 & 665 & NA & NA &   24.09823 &   0.07360046\\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "A data.frame: 6 × 13\n",
       "\n",
       "| <!--/--> | Customer_ID &lt;chr&gt; | Purchase_Date &lt;date&gt; | Cover_Start_Date &lt;date&gt; | LOB &lt;chr&gt; | Sale_Flag &lt;int&gt; | Purchase_Price &lt;int&gt; | Claims_Count &lt;dbl&gt; | Period_of_Cover &lt;dbl&gt; | Premium &lt;int&gt; | Age &lt;lgl&gt; | Broker &lt;lgl&gt; | Latitude &lt;dbl&gt; | Longitude &lt;dbl&gt; |\n",
       "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n",
       "| 1 | d2d2062d6d73bfe37440b5bc9aebc518 | 2023-08-04 | 2024-01-15 | Motor | 0 | 16898 | 0 | 48 | 802 | NA | NA | -115.15198 | -58.22413537 |\n",
       "| 2 | ef5865f3cbf1d48b814e9716f235cfbf | 2023-03-30 | 2023-12-02 | Motor | 0 | 21716 | 0 | 12 | 155 | NA | NA | -155.84526 | -55.21116345 |\n",
       "| 3 | 5a30397fc844734533879fef33313971 | 2023-11-28 | 2024-07-11 | Motor | 1 | 52179 | 1 | 12 | 503 | NA | NA | -131.15406 |  17.26387609 |\n",
       "| 4 | 61474708950929d053ef8a5cb3ca5c8e | 2023-10-02 | 2024-05-08 | Motor | 1 | 61232 | 1 | 48 | 804 | NA | NA |   27.15229 | -20.92771000 |\n",
       "| 5 | afc58a586eeae1560526c07651f6bd80 | 2023-04-30 | 2024-04-12 | Motor | 0 |  2711 | 0 | 24 |  94 | NA | NA |  -10.96663 |  17.87203882 |\n",
       "| 6 | 7fdcdd9fd1a203c40e5743b88132ff99 | 2023-04-18 | 2023-04-28 | Motor | 0 | 17872 | 0 | 24 | 665 | NA | NA |   24.09823 |   0.07360046 |\n",
       "\n"
      ],
      "text/plain": [
       "  Customer_ID                      Purchase_Date Cover_Start_Date LOB  \n",
       "1 d2d2062d6d73bfe37440b5bc9aebc518 2023-08-04    2024-01-15       Motor\n",
       "2 ef5865f3cbf1d48b814e9716f235cfbf 2023-03-30    2023-12-02       Motor\n",
       "3 5a30397fc844734533879fef33313971 2023-11-28    2024-07-11       Motor\n",
       "4 61474708950929d053ef8a5cb3ca5c8e 2023-10-02    2024-05-08       Motor\n",
       "5 afc58a586eeae1560526c07651f6bd80 2023-04-30    2024-04-12       Motor\n",
       "6 7fdcdd9fd1a203c40e5743b88132ff99 2023-04-18    2023-04-28       Motor\n",
       "  Sale_Flag Purchase_Price Claims_Count Period_of_Cover Premium Age Broker\n",
       "1 0         16898          0            48              802     NA  NA    \n",
       "2 0         21716          0            12              155     NA  NA    \n",
       "3 1         52179          1            12              503     NA  NA    \n",
       "4 1         61232          1            48              804     NA  NA    \n",
       "5 0          2711          0            24               94     NA  NA    \n",
       "6 0         17872          0            24              665     NA  NA    \n",
       "  Latitude   Longitude   \n",
       "1 -115.15198 -58.22413537\n",
       "2 -155.84526 -55.21116345\n",
       "3 -131.15406  17.26387609\n",
       "4   27.15229 -20.92771000\n",
       "5  -10.96663  17.87203882\n",
       "6   24.09823   0.07360046"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "View(head(df))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "4373109b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Passing 519 coordinates to the Nominatim single coordinate geocoder\n",
      "\n",
      "Query completed in: 528.6 seconds\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# get post_codes \n",
    "# if not in the arctic or lake Victoria\n",
    "# very slow - free but time cost\n",
    "reverse <- lats_longs %>%\n",
    "  reverse_geocode(lat = Latitude, long = Longitude, method = 'osm',\n",
    "                  address = address_found, full_results = TRUE)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "62c3f590",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table class=\"dataframe\">\n",
       "<caption>A data.frame: 6 × 13</caption>\n",
       "<thead>\n",
       "\t<tr><th></th><th scope=col>Customer_ID</th><th scope=col>Purchase_Date</th><th scope=col>Cover_Start_Date</th><th scope=col>LOB</th><th scope=col>Sale_Flag</th><th scope=col>Purchase_Price</th><th scope=col>Claims_Count</th><th scope=col>Period_of_Cover</th><th scope=col>Premium</th><th scope=col>Age</th><th scope=col>Broker</th><th scope=col>Latitude</th><th scope=col>Longitude</th></tr>\n",
       "\t<tr><th></th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;date&gt;</th><th scope=col>&lt;date&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
       "</thead>\n",
       "<tbody>\n",
       "\t<tr><th scope=row>1</th><td>d2d2062d6d73bfe37440b5bc9aebc518</td><td>2023-08-04</td><td>2024-01-15</td><td>Motor</td><td>0</td><td>16898</td><td>0</td><td>48</td><td>802</td><td>27</td><td>london_ins    </td><td>-115.15198</td><td>-58.22413537</td></tr>\n",
       "\t<tr><th scope=row>2</th><td>ef5865f3cbf1d48b814e9716f235cfbf</td><td>2023-03-30</td><td>2023-12-02</td><td>Motor</td><td>0</td><td>21716</td><td>0</td><td>12</td><td>155</td><td>23</td><td>some_syndicate</td><td>-155.84526</td><td>-55.21116345</td></tr>\n",
       "\t<tr><th scope=row>3</th><td>5a30397fc844734533879fef33313971</td><td>2023-11-28</td><td>2024-07-11</td><td>Motor</td><td>1</td><td>52179</td><td>1</td><td>12</td><td>503</td><td>64</td><td>london_ins    </td><td>-131.15406</td><td> 17.26387609</td></tr>\n",
       "\t<tr><th scope=row>4</th><td>61474708950929d053ef8a5cb3ca5c8e</td><td>2023-10-02</td><td>2024-05-08</td><td>Motor</td><td>1</td><td>61232</td><td>1</td><td>48</td><td>804</td><td>28</td><td>some_mga      </td><td>  27.15229</td><td>-20.92771000</td></tr>\n",
       "\t<tr><th scope=row>5</th><td>afc58a586eeae1560526c07651f6bd80</td><td>2023-04-30</td><td>2024-04-12</td><td>Motor</td><td>0</td><td> 2711</td><td>0</td><td>24</td><td> 94</td><td>36</td><td>london_ins    </td><td> -10.96663</td><td> 17.87203882</td></tr>\n",
       "\t<tr><th scope=row>6</th><td>7fdcdd9fd1a203c40e5743b88132ff99</td><td>2023-04-18</td><td>2023-04-28</td><td>Motor</td><td>0</td><td>17872</td><td>0</td><td>24</td><td>665</td><td>47</td><td>some_syndicate</td><td>  24.09823</td><td>  0.07360046</td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "A data.frame: 6 × 13\n",
       "\\begin{tabular}{r|lllllllllllll}\n",
       "  & Customer\\_ID & Purchase\\_Date & Cover\\_Start\\_Date & LOB & Sale\\_Flag & Purchase\\_Price & Claims\\_Count & Period\\_of\\_Cover & Premium & Age & Broker & Latitude & Longitude\\\\\n",
       "  & <chr> & <date> & <date> & <chr> & <int> & <int> & <dbl> & <dbl> & <int> & <int> & <chr> & <dbl> & <dbl>\\\\\n",
       "\\hline\n",
       "\t1 & d2d2062d6d73bfe37440b5bc9aebc518 & 2023-08-04 & 2024-01-15 & Motor & 0 & 16898 & 0 & 48 & 802 & 27 & london\\_ins     & -115.15198 & -58.22413537\\\\\n",
       "\t2 & ef5865f3cbf1d48b814e9716f235cfbf & 2023-03-30 & 2023-12-02 & Motor & 0 & 21716 & 0 & 12 & 155 & 23 & some\\_syndicate & -155.84526 & -55.21116345\\\\\n",
       "\t3 & 5a30397fc844734533879fef33313971 & 2023-11-28 & 2024-07-11 & Motor & 1 & 52179 & 1 & 12 & 503 & 64 & london\\_ins     & -131.15406 &  17.26387609\\\\\n",
       "\t4 & 61474708950929d053ef8a5cb3ca5c8e & 2023-10-02 & 2024-05-08 & Motor & 1 & 61232 & 1 & 48 & 804 & 28 & some\\_mga       &   27.15229 & -20.92771000\\\\\n",
       "\t5 & afc58a586eeae1560526c07651f6bd80 & 2023-04-30 & 2024-04-12 & Motor & 0 &  2711 & 0 & 24 &  94 & 36 & london\\_ins     &  -10.96663 &  17.87203882\\\\\n",
       "\t6 & 7fdcdd9fd1a203c40e5743b88132ff99 & 2023-04-18 & 2023-04-28 & Motor & 0 & 17872 & 0 & 24 & 665 & 47 & some\\_syndicate &   24.09823 &   0.07360046\\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "A data.frame: 6 × 13\n",
       "\n",
       "| <!--/--> | Customer_ID &lt;chr&gt; | Purchase_Date &lt;date&gt; | Cover_Start_Date &lt;date&gt; | LOB &lt;chr&gt; | Sale_Flag &lt;int&gt; | Purchase_Price &lt;int&gt; | Claims_Count &lt;dbl&gt; | Period_of_Cover &lt;dbl&gt; | Premium &lt;int&gt; | Age &lt;int&gt; | Broker &lt;chr&gt; | Latitude &lt;dbl&gt; | Longitude &lt;dbl&gt; |\n",
       "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n",
       "| 1 | d2d2062d6d73bfe37440b5bc9aebc518 | 2023-08-04 | 2024-01-15 | Motor | 0 | 16898 | 0 | 48 | 802 | 27 | london_ins     | -115.15198 | -58.22413537 |\n",
       "| 2 | ef5865f3cbf1d48b814e9716f235cfbf | 2023-03-30 | 2023-12-02 | Motor | 0 | 21716 | 0 | 12 | 155 | 23 | some_syndicate | -155.84526 | -55.21116345 |\n",
       "| 3 | 5a30397fc844734533879fef33313971 | 2023-11-28 | 2024-07-11 | Motor | 1 | 52179 | 1 | 12 | 503 | 64 | london_ins     | -131.15406 |  17.26387609 |\n",
       "| 4 | 61474708950929d053ef8a5cb3ca5c8e | 2023-10-02 | 2024-05-08 | Motor | 1 | 61232 | 1 | 48 | 804 | 28 | some_mga       |   27.15229 | -20.92771000 |\n",
       "| 5 | afc58a586eeae1560526c07651f6bd80 | 2023-04-30 | 2024-04-12 | Motor | 0 |  2711 | 0 | 24 |  94 | 36 | london_ins     |  -10.96663 |  17.87203882 |\n",
       "| 6 | 7fdcdd9fd1a203c40e5743b88132ff99 | 2023-04-18 | 2023-04-28 | Motor | 0 | 17872 | 0 | 24 | 665 | 47 | some_syndicate |   24.09823 |   0.07360046 |\n",
       "\n"
      ],
      "text/plain": [
       "  Customer_ID                      Purchase_Date Cover_Start_Date LOB  \n",
       "1 d2d2062d6d73bfe37440b5bc9aebc518 2023-08-04    2024-01-15       Motor\n",
       "2 ef5865f3cbf1d48b814e9716f235cfbf 2023-03-30    2023-12-02       Motor\n",
       "3 5a30397fc844734533879fef33313971 2023-11-28    2024-07-11       Motor\n",
       "4 61474708950929d053ef8a5cb3ca5c8e 2023-10-02    2024-05-08       Motor\n",
       "5 afc58a586eeae1560526c07651f6bd80 2023-04-30    2024-04-12       Motor\n",
       "6 7fdcdd9fd1a203c40e5743b88132ff99 2023-04-18    2023-04-28       Motor\n",
       "  Sale_Flag Purchase_Price Claims_Count Period_of_Cover Premium Age\n",
       "1 0         16898          0            48              802     27 \n",
       "2 0         21716          0            12              155     23 \n",
       "3 1         52179          1            12              503     64 \n",
       "4 1         61232          1            48              804     28 \n",
       "5 0          2711          0            24               94     36 \n",
       "6 0         17872          0            24              665     47 \n",
       "  Broker         Latitude   Longitude   \n",
       "1 london_ins     -115.15198 -58.22413537\n",
       "2 some_syndicate -155.84526 -55.21116345\n",
       "3 london_ins     -131.15406  17.26387609\n",
       "4 some_mga         27.15229 -20.92771000\n",
       "5 london_ins      -10.96663  17.87203882\n",
       "6 some_syndicate   24.09823   0.07360046"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "View(head(df))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c32e36f6",
   "metadata": {},
   "source": [
    "<h2 style=\"color:#ff6961\"> Works in Progress For Random Address Generation (US ONLY) </h2> <ol  style=\"color:#A7C7E7\">\n",
    "   \n",
    "  <li>Option 1 use the package reticulate (and for the moment manually input the sample_size) </li>\n",
    "  <li>Option 2 update the python code so it can be called by a system call to the cmd</li>\n",
    "  <li>At the moment both options mean writing the data from python to the data folder & recalling it back in via R (read.csv)</li>\n",
    "\n",
    "</ol> "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "372e6c93",
   "metadata": {},
   "outputs": [],
   "source": [
    "library(reticulate)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "953af0b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "1000"
      ],
      "text/latex": [
       "1000"
      ],
      "text/markdown": [
       "1000"
      ],
      "text/plain": [
       "[1] 1000"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Sample Size\n",
    "sample_size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1a5b64ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "#source_python('random_address_py.py')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "306775aa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "d82608c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "py_run_string(\"\n",
    "# pip install random-address\n",
    "# pip install pandas\n",
    "\n",
    "import os\n",
    "import pandas as pd\n",
    "import random_address\n",
    "\n",
    "from random_address import real_random_address\n",
    "\n",
    "# Generate random addresses in the USA\n",
    "\n",
    "def create_random_address_us():\n",
    "    \n",
    "    add_dict = real_random_address()\n",
    "    add_df = pd.json_normalize(add_dict)\n",
    "    \n",
    "    return (add_df)\n",
    "\n",
    "# Create Schema\n",
    "\n",
    "df= pd.DataFrame({'address1': [],\n",
    "                 'address2': [],\n",
    "                 'city': [],\n",
    "                 'state': [],\n",
    "                 'postalCode': [],\n",
    "                 'coordinates.lat': [],\n",
    "                 'coordinates.lng': []\n",
    "                 })\n",
    "\n",
    "# Change Dir to Data Folder\n",
    "os.chdir('C:/Users/alexz/OneDrive/Documents/AGCS/Data')\n",
    "\n",
    "# Create csv if not exist\n",
    "filename = 'random_us_addresses.csv'\n",
    "if not os.path.isfile(filename):\n",
    "    df.to_csv(filename, header='column_names', index=False)\n",
    "else:  # else it exists so append without writing the header\n",
    "    df.to_csv(filename, mode='a', header=False, index=False)\n",
    "\n",
    "for i in range(5):\n",
    "    address_data = create_random_address_us()\n",
    "    # Write data to csv file\n",
    "    address_data.to_csv(filename, mode='a', header=False, index=False)\n",
    "\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8514229f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e8a1d22",
   "metadata": {},
   "outputs": [],
   "source": [
    "appended_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "68203272",
   "metadata": {},
   "outputs": [],
   "source": [
    "library(reticulate)\n",
    "\n",
    "py_evaluate <- function(code) {\n",
    "  builtins <- import_builtins(convert = TRUE)\n",
    "  globals <- py_eval(\"globals()\", convert = FALSE)\n",
    "  locals <- globals\n",
    "  parsed <- builtins$compile(code, \"<string>\", \"single\")\n",
    "  builtins$eval(parsed, globals, locals)\n",
    "}\n",
    "\n",
    "py_evaluate(\"2\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65fa8c04",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "R 4.2",
   "language": "R",
   "name": "ir42"
  },
  "language_info": {
   "codemirror_mode": "r",
   "file_extension": ".r",
   "mimetype": "text/x-r-source",
   "name": "R",
   "pygments_lexer": "r",
   "version": "4.2.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
