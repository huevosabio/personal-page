Title: Processing NYC Taxi Data Part 1: Downloading
Date: 2018-01-15 17:45
Tags: data science
Author: Ramon Dario Iglesias
Summary: In this multi-part series, I will process five years of taxi trips from the NYC TLC dataset. This part describes how to move the data to S3.

## Introduction

For our research in Autonomous Mobility-on-Demand, we developed [a real-time controller that leverages short-term travel demand predictions](https://arxiv.org/abs/1709.07032). Naturally, part of the work is to come up with _good_ predictions, so we are testing forecasting models based on Long Short-Term Memory neural networks. To train these models, we previously used small datasets provided by Didi Chuxing. However, we are now going to test to the largest available dataset of taxi trips: the [New York City Taxi and Limousine Commission dataset](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml) (NYC TLC). 

These series of entries will record how to process five years of data in a format that we can then use to train our neural networks. This first entry focuses on copying the data to a location I can readily use, AWS S3.

To the best of my knowledge, there is no easy way to move files from the internet into S3 without first downloading them to a computer or server you own. Thus, the process consists of downloading the files into a local computer, then syncing the files with an S3 bucket.

## Copying the files locally

The first step is to make sure that you have enough space to copy all of the files (~120 GB). There are surely ways to use less space (e.g. download, sync, and delete each file at a time), but since in my case this was not a constraint, I went the easy route.

The second step is to create a folder to host all the files. A single command does this for us:

```
mkdir /media/Big_Data/rdit/nyc-tlc
```

Third, I created a Python script to handle the downloads. The file is called `download_files.py` and is a modification of [someone else's work](https://github.com/sdaulton/TaxiPrediction/blob/master/1.%20Setup%20Project.ipynb). The script is the following:

```python
import urllib
import os
import time
import sys
# modified from https://github.com/sdaulton/TaxiPrediction/blob/master/1.%20Setup%20Project.ipynb
nyc_path = '/media/Big_Data/rdit/nyc-tlc'
# make dir if it does not exist
if not os.path.isdir(nyc_path): os.mkdir(nyc_path)
# variables
baseUrl = "https://s3.amazonaws.com/nyc-tlc/trip+data/"
#Yellow/green cab filename prefix
yCabFNPrefix = "yellow_tripdata_"

#Availaiblity of data set by month & year
yDict = {}
years = range(2012, 2018)

for year in years:
    if year == 2017:
        months = range(1,8)
    else:
        months = range(1,13)
    yDict[year] = months

yCabUrls = []
yCabFilenames = []
for year, monthList in yDict.iteritems():
    yearStr = str(year)
    for month in monthList:
        monthStr = str(month)
        if len(monthStr) == 1:
            monthStr = "0"+monthStr
        url = baseUrl+yCabFNPrefix+yearStr+'-'+monthStr+".csv"
        yCabUrls.append(url)
        yCabFilenames.append(yCabFNPrefix+yearStr+'-'+monthStr+".csv")

def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                    (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()

def save(url, filename):
    urllib.urlretrieve(url, filename, reporthook)

for url,filename in zip(yCabUrls,yCabFilenames):
    print url, filename
    save(url, nyc_path + '/' + filename)
```

Now, simply run

```
python download_files
```
and wait for it to end. Tip: This will likely take hours, make sure you run this in the background (e.g. using `screen`) to ensure that it will continue to run after you log-off.

## Copying to S3

### Installing the AWS toolset

### Creating the S3 Bucket

### Syncing the Files

## Outro with next steps