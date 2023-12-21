Title: Processing NYC Taxi Data Part 3: Labeling and Aggregating
Date: 2018-01-22 13:30
Tags: data science
Author: Ramon Dario Iglesias
Summary: In this multi-part series, I will process five years of taxi trips from the NYC TLC dataset. This part describes how to cluster and aggregate the dataset using PySpark.


Steps:
- load station data
- label using kmeans model
- bucket into 5min intervals
- aggregate into odt 
- store

### Load Station Locations

```
wget https://raw.githubusercontent.com/huevosabio/notebooks/master/notebooks/assets/manhattan_demands_50.json -P /media/Big_Data/rdit/nyc-tlc/manhattan/
```

  