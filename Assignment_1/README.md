# CSYE7245 - Assignment_1

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


#### Quick Links

- [CLAAT document](https://codelabs-preview.appspot.com/?file_id=1wYxfi7JVXaJxT_ytsv2Wzg5AU2HHeEqHb57Yh-V9DJY#0)
- [Presentation](https://docs.google.com/document/d/1wYxfi7JVXaJxT_ytsv2Wzg5AU2HHeEqHb57Yh-V9DJY/edit#)
- [DataStudio Dashboard](https://datastudio.google.com/u/0/reporting/6e36cc27-e89a-496d-82db-143142072dd3/page/tAp4B)

---

## Table of Contents

- [Introduction](#Introduction)
- [Data Explanation](#Data-Explanation)
- [Setup](#Setup)
- [Folder Contents](#Folder-Contents)


## Introduction: Three experiments with Big data

In this assignment, we will develop a data pipeline to ingest, process, store it so you can access it through different means.


## Data Explanation

SEVIR: The Storm EVent ImagRy (SEVIR) dataset is a collection of temporally and spatially aligned images containing weather events captured by satellite and radar. 

The dataset contains thousands of samples of 4 hour events captured by one or more of these weather sensors. This loop shows one such event:

![sevir_sample](https://user-images.githubusercontent.com/33648410/110065574-79826d80-7d3d-11eb-9ee7-7ca4055a8beb.gif)

- Start by reading this [tutorial on the dataset](https://nbviewer.jupyter.org/github/MIT-AI-Accelerator/eie-sevir/blob/master/examples/SEVIR_Tutorial.ipynb).

- [Dataset catalog](https://github.com/MIT-AI-Accelerator/eie-sevir/blob/master/CATALOG.csv)


Storm Events Database: The database currently contains data from January 1950 to November 2020, as entered by NOAA's National Weather Service (NWS). Data are available on the Registry of Open Data on AWS. [Dataset](https://registry.opendata.aws/noaa-goes/) and the [Website](https://www.ncdc.noaa.gov/stormevents/ftp.jsp)

More to read:
- [Storm Data Export Format, Field names Event Details File (named storm_data_search_results.csv):](https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/Storm-Data-Export-Format.pdf)
- [SEVIR : A Storm Event Imagery Dataset for Deep Learning Applications in Radar and Satellite Meteorology:](https://proceedings.neurips.cc/paper/2020/file/fa78a16157fed00d7a80515818432169-Paper.pdf)


## Setup

- Python 3.7+
- Python IDE
- Code editor
- Amazon S3 Buckets
- Amazon Glue
- Amazon Athena
- Amazon Quicksight
- Google storage buckets
- Google Dataflow
- Google Bigquery 
- Data studio
- Snowflake
- Sql-alchemy
- Apache Superset

### Clone

Clone this repo to your local machine using `https://github.com/goyal07nidhi/Team6_CSYE7245_Spring2021.git`


## Folder Contents

Refer `README.md` inside the respective directories for setup instructions.

- :white_check_mark: AWS S3: `AWS`
- :white_check_mark: GCP - Dataflow, Datalab: `GCP`
- :white_check_mark: SNOWFLAKE: `SNOWFLAKE`
