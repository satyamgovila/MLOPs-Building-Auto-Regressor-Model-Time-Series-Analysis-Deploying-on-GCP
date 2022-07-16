# MLOPs Project : Building Auto-Regressor Model for Time-Series Analysis and Deploying on GCP

## **Overview of the Project**
Until recently, all of us were learning about software development lifecycle and different agile methodologies and how the complete pipeline goes from requirement gathering designing development testing deployment all the way down to maintenance. 

Now, we are at a stage where almost every other organization today is trying to incorporate AI/ML algorithms into their product. This new requirement of building ml systems adds some principles of the software development lifecycle to give rise to a new engineering discipline called mlops. MLOps is a fairly new term that has popped up recently and is creating buzz and great advancements.

MLOps is short for machine learning operations, also referred to as Model OPs. In this project, we analyze the time series data and also check different parameters such as the presence of white noise, stationarity of the data, seasonality, etc. We also build an auto-regressor model that uses observations from previous time steps as input to a regression equation to predict the value at the next time step. 

Finally, we design an end-to-end machine learning development process to design, build and manage reproducible, testable, and evolvable machine learning models using google cloud platform (gcp) for the time series autoregressor project.


**Definition : MLOps**

MLOps is a set of practices for collaboration and communication between data scientists and operations professionals. Applying these practices increases the quality, simplifies the management process, and automates the deployment of Machine Learning and Deep Learning models in large-scale production environments. It’s easier to align models with business needs, as well as regulatory requirements.

**Introduction: Time-Series Data Analysis:**

* A time-series data is a series of data points or observations recorded at different or regular time intervals. In general, a time series is a sequence of data points taken at equally spaced time intervals. The frequency of recorded data points may be hourly, daily, weekly, monthly, quarterly or annually.

* Time-Series Forecasting is the process of using a statistical model to predict future values of a time-series based on past results.

* A time series analysis encompasses statistical methods for analyzing time series data. These methods enable us to extract meaningful statistics, patterns and other characteristics of the data. Time series are visualized with the help of line charts. So, time series analysis involves understanding inherent aspects of the time series data so that we can create meaningful and accurate forecasts.

**GCP MLOPs Environment**

Google Cloud facilitates end-to-end MLOps with its range of services and products. From conducting exploratory data analysis to deploying machine learning models, there is a need for processes to be in place that ensures practices such as CI/CD and Continuous Training are carried out. In this project, we aim to highlight the core services that help set up the MLOps environment on Google Cloud Platform such as Cloud Build , Container Registry , Google Kubernetes Engine (GKE) , Cloud Storage , etc.


## Technologies and Tech Stack used

* Python Libraries : pandas, numpy, matplotlib, scipy.stats, pylab, statsmodels, seaborn
* Docker
* Kubernetes
* Flask
* uWSGI
* GCP


## Data Description 

* The CSV data used for the project showcases the readings of 3 sensors of a chiller. The file contains data from one chiller, and the sensors give out one value at every hour of the day.
* Data has 1895 rows and 5 columns.
* Here is the description of the variables in the data:
    1.  Time: Timestamp at what time the reading was taken
    2.  IOT_Sensor_Reading: The reading of the sensor at the above-mentioned timestamp 
    3.  Error_Present: The error which may or may not be present while taking the reading
    4.  Sensor 2: The reading from the sub-ordinate sensor 
    5.  Sensor_Value: The final value to be predicted


## Approach used for Time-Series Analysis 

The time series analysis is performed using the following techniques:-

* Perform Descriptive Analysis
* Exploratory Data Analysis (EDA)
* Data Visualization (Q-Q plot)
* Pre-processing
* Checking for white noise and random walk
* Perform Stationarity tests (Augmented Dickey-Fuller test and KPSS test)
* Plotting Seasonal decomposition charts
* Plot an Autocorrelation plot (ACF) , Partial Autocorrelation plot (PACF)
* Perform Autoregression Modelling (ARMA)
* Log Likelihood test
* Calculating Rolling window and Expanding window


## Code Overview

1. **input** directory :- contains the CSV file which will be used as an input dataset, filename - Data-chillers.csv
2. **src/ML_Pipeline/** directory :- 

* **Preprocess.py** : Class to preprocess the data, handle missing values, set time as index and QQ plots
* **Engine.py**: Main class for starting different parts and processes of the lifecycle
* **WhiteNoise.py** : Steps to test if the visualization is white noise or not
* **RandomWalk.py** : Steps to test if the visualization is random walk or not
* **Stationarity.py** : Steps to test if the visualization is stationary or not
* **AcfAndPacf.py** : Steps to test the visualization of lag features
* **Autoregressor.py** : Training the model on autoregression with log likelyhood
* **RollingWindow.py** : Steps to verify the Mean and Std

3. **kubernetes yaml files** directory :- Contains all the required yaml files to trigger Kubernetes (service and deployment)
4. **output** directory :- Contains output plots of all the analysis and pickel file which has results of final model(auto_regressor_model.pkl)
5. **__init__.py** :- required empty file
6. **Dockerfile**
7. **Engine.py** :- File where the ML Pipeline scripts are called
8. **main.py** :-  File to host Flask API
9. **Requirements.txt** :- all the required libraries
10.**uwsgi.ini** :- uWSGI configuration file


## Building and Deployment of Model on GCP

This section of the project demonstrates the process of creating an automated MLOps Pipeline for end to end ML development on GCP.

**Cloud Build Trigger**

* In GCP console, create a new cloud build trigger and point the trigger to source repository

**Google Kubernetes Engine (GKE)**

* In GCP console launch and connect to kubernetes cluster, and create the following two files :  deployment.yaml , service.yaml

* Execute the following commands
    * kubectl apply -f deployment.yaml
    * kubectl apply -f service.yaml
    
* Get the name of the deployment with the following command
    * kubectl get deployments

**Cloud Pub/Sub**

* Create a Pub/Sub topic with the name cloud-build
* Provide a subscription for the topic, which is to trigger a cloud function

**Cloud Functions**

* From Pub/Sub console launch the cloud function window
* Provide the following Environment variables through the GUI console
    * PROJECT (project name)
    * ZONE (Region in which in the project is deployed ex.uscentral-1)
    * CLUSTER (Name of the kubernetes cluster created earlier)
    * DEPLOYMENT (Name of the deployment inside the kubernetes cluster)
* Copy the program code and requirements.txt files for the cloud function from cloud-function-trigger folder
* Configure the Entrypoint for the cloud function as onNewImage
* Deploy the function
After successful deployment, make a commit to source repository and the following will happen in sequence
* Cloud Build will push message to Pub/Sub upon successful build
* Pub/Sub will trigger the cloud function
* Cloud function will deploy the new image on Kubernetes
    * To test the deployment, check the logs on kubernetes cluster using the following command
        * kubectl get pods 
        * kubectl logs <pod name>
    * The deployment will reflect in the logs as well as in the endpoints











