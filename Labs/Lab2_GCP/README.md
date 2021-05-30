# Machine learning with structured data: Data analysis and prep (Part 1)

### [CLAAT Document](https://codelabs-preview.appspot.com/?file_id=1cjPre8NfLGxSrj_yVQr5d9846wD42chESrjSfbruptw#0)


## Objectives

Explore a public dataset(structured dataset) with Datalab. Execute queries to collect sample data from the Natality dataset,a public data set from the USA's Centers for Disease Control and Prevention (CDC) that is stored in BigQuery. Identify features to use in your ML model. Visualize the data using the Python data analysis tool Pandas. The Pandas dataframe is an in-memory data structure you can use for statistical calculations and data visualization. Split the data into training and evaluation data files using Dataflow. Launch a preprocessing pipeline using Dataflow to create training and evaluation datasets.


## Requirements

- Google Cloud services Datalab for data exploration
- Dataflow to create your datasets
- BigQuery to store source dataset

## Setup

### Google Cloud Console Configuration 

In the Google Cloud Console, on the project selector page, select or create a Google Cloud project.


### Biling alert

Make sure that billing is enabled for your Cloud project.

### Enable the APIs

Enable the BigQuery, AI Platform, Cloud Source Repositories, Dataflow, and Datalab APIs.

### Launching Datalab

Follow these steps to create a Datalab instance.
Open Cloud Shell. Unless otherwise noted, you execute the rest of the tutorial from inside Cloud Shell.

### Open Cloud Shell

Run the following command to retrieve your project ID.
##### gcloud config list project --format "value(core.project)"

### Create a Datalab instance:

##### datalab create --zone us-central1-a mydatalab
It can take a minute or more to create the instance. After the instance is created, Datalab displays the following output.


The connection to Datalab is now open and will remain until this command is killed.
Click on the *Web Preview* (up-arrow button at top-left), select *port 8081*, and start using Datalab.
> :Note: To use the same instance next time, run datalab connect mydatalab.
Click Cloud Shell Web preview in Cloud Shell to launch the Datalab notebook listing page.
Select Change port and click Port 8081 to open a new tab in your browser.

### Cloning the Datalab notebook

Now that you have a Datalab instance, download the Datalab notebook file for this tutorial. 
In Datalab, create a new notebook by clicking the +Notebook icon in the upper left. The notebook opens in a new tab.

Copy and paste the following command in the first cell of the new notebook.
##### !git clone https://github.com/GoogleCloudPlatform/training-data-analyst
Click Run at the top of the page to download the notebook for this tutorial.

In Datalab, open the notebook training-data-analyst/blogs/babyweight/babyweight.ipynb. In the pull-down menu to the right of Clear, click Clear all Cells.

Fill in the cells as follows:

In the first cell, set the variable PROJECT to your project ID.
Set the variable BUCKET to your bucket name in the first cell. For your bucket name, use your project ID as a prefix and my-bucket: project-ID-my-bucket
Leave REGION as us-central1.
With the first cell selected, click Run to run the code in the first cell. Repeat for the next three cells.

### Reviewing the notebook

The notebook contains details about all the steps in the end-to-end process for creating an ML model. This section provides an overview and context for the first part of the notebook.

### Explore the public Natality dataset

You use the public Natality dataset to create an ML model to predict a baby's weight given a number of factors about the pregnancy and the baby's mother. To train the model, you must explore the dataset, understand its structure, and examine relationships within the data. You then isolate and construct relevant features within the data. A feature is a piece of information that impacts the predictions your model will make. Features can be fields of data in your source dataset, or they can be formed using one or more of the original fields. Identifying the relevant features for your model is called feature engineering. You must also transform, combine, and extract the data to format it for training your model. This is called data preprocessing.

### feature engineering and preprocessing:

Select features that are related to what you want to predict. Transform the data into a format suitable for training.
Split the data into a training set and an evaluation set (also known as a testing set).
Query the data
First you query the data and review some samples. Using the first two cells in the Exploring data section of the notebook, you run a query against the BigQuery table and store the result in a Pandas dataframe.

Split the data using hash values
You split the data using hash values to ensure that:

You use the same subsets of the source data for your training and evaluation sets. If the sets aren't consistent, you can't compare evaluation results reliably, and your training adjustments are imprecise.
You avoid a data skew in the evaluation set.
The hashmonth field is a hash value calculated from the year and month columns of each record in a BigQuery table. You add this column using the FARM_FINGERPRINT function when you collect the year and month columns from the table:


FARM_FINGERPRINT(CONCAT(CAST(YEAR AS STRING), CAST(month AS STRING))) AS hashmonth 
Dataflow uses the following Python code snippet to create the split. You designate a quarter of the data for the evaluation set. You use the remainder of dividing the hash by four (using the modulo function) to define the two datasets.


for step in ['train', 'eval']:
  if step == 'train':
    selquery = 'SELECT * FROM ({}) WHERE MOD(ABS(hashmonth),4) < 3'.format(query)
  else:
    selquery = 'SELECT * FROM ({}) WHERE MOD(ABS(hashmonth),4) = 3'.format(query)
Using this technique ensures that you get a random sampling of the source data in each dataset, which is preferable to dividing data without randomization, because it reduces the risk of accidentally skewing the evaluation set.

For example, if you designate the top quarter of sorted data for the evaluation set, you might select data with characteristics that don't exist in the rest of the data. It is important to guarantee that the evaluation set represents the general characteristics of the data so that you can evaluate the generalization performance of the trained model with it.

Identify useful features for training
Next you determine which features influence the value that you want to predict: the baby's weight. Examine the columns in the source data to determine whether there is a correlation between each column and the target.

Use an interactive notebook in Datalab for this step to quickly visualize each relationship, as shown in the example notebook. Strong correlations appear as lines that you can interpret as mathematical functions, such as linear or quadratic.

You can use the following columns for making predictions in this solution:


is_male, mother_age, plurality, gestation_weeks
Because there might be a historical trend in baby weights, limit the chronological data. Training with old data might reduce the accuracy of the model for predicting the weight of babies born in the future. You should not restrict the data to only the last year, however, because the resulting dataset will be too small.

The function definition that is used to draw bar charts in the notebook is the get_distinct_values function. This function only collects data from the BigQuery table after the year 2001.

The threshold value of 2001 is arbitrary. However, it's the sort of value (not parameter) that you might experiment with in order to balance two factors: the need for fresh data, and the need for enough data to achieve good model performance.

You refresh the model when you obtain new data, so that your model reflects the latest trends.

### Creating an ML dataset using Dataflow
Next, you use Dataflow to extract the data. The columns you specified are pulled out of BigQuery and stored in a CSV file within a Cloud Storage bucket.

You use the hashmonth field to split the dataset into the training set and evaluation set, which you will store in separate files. You will use these files to train your ML model.

### Generate synthetic data
You can use Dataflow to generate synthetic data to make the model more robust to partial or unknown input values.

For example, in the historical dataset, every row in the dataset contains the baby's gender, because this is known after the baby is born. However, you are building a model to predict the weight before the baby is born. You know the sex of the baby only if an ultrasound was performed during the pregnancy. If no ultrasound was performed, the doctor enters the baby's gender as "Unknown". But there is no Unknown value for the sex column in the historical dataset. You generate artificial data by writing each historical datapoint twice, once with the original value (True or False) for the is_male column and again after replacing the is_male column value by Unknown.

Also, it is difficult to count the number of babies without an ultrasound, so while doctors can tell whether there is one baby or multiple babies, they can't differentiate between twins and triplets. You replace the plurality numbers with string values (Single or Multiple) when writing out the data to simulate the absence of an ultrasound.

Submitting the data processing job
The first cell in the Creating ML dataset using Cloud Dataflow section of the notebook contains data processing code written with the Apache Beam SDK. When you run this cell, you submit the data processing job to Dataflow.

### Find the running job
You can find the running job by using the Dataflow page in the Google Cloud Console.

### Open Dataflow

You find two pipelines, one that includes the training set, and the other that includes the evaluation set. The process typically takes about 30 - 45minutes to finish, but might vary depending on the setup.

The following diagram shows the Dataflow data processing pipeline:

![gcp1](https://github.com/goyal07nidhi/Team6_CSYE7245_Spring2021/tree/main/Labs/Lab2_GCP/img/gcp1.png)

Dataflow data processing pipeline.

Find the CSV files for evaluation and training
The job creates multiple CSV files for both sets. Here are the first CSV files for the evaluation set and the training set:


##### gs://${BUCKET}/babyweight/preproc/eval.csv-00000-of-00016
##### gs://${BUCKET}/babyweight/preproc/train.csv-00000-of-00040
Reviewing the CSV files
Use the Cloud Storage page in the Google Cloud Console to see the entire set of files in the babyweight/preproc directory in your bucket.

### Open Cloud Storage

#### Training and evaluation sets
Use the training set to train the ML model, and the evaluation set to evaluate the prediction accuracy of the trained model. 
In general, the trained model is more accurate for the training set than for the evaluation set. If its accuracy for the evaluation set is far worse than for the training set, the model suffers from overfitting.

An overfit model will not make good predictions for new data. In other words, the prediction of the trained model cannot be generalized to new data. You must evaluate the generalization performance of the model using the evaluation set, which wasn't used for training. In Part 2 of this series, you use a high-level TensorFlow interface, the Estimator API, to automate this evaluation process.

#### Cleaning up
If you plan to continue to Part 2 of this tutorial series, keep the resources you created in this step intact. Otherwise, to avoid continued charges, go to the Google Developers Console Project List, choose the project you created for this lab, and delete it.

