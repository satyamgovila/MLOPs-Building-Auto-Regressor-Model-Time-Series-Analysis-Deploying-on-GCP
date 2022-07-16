## MLOps On GCP

This repository contains the code files involved in creating an automated MLOps Pipeline on GCP (Google Cloud Platform).

## Autoregressor

The auto regressive model or a model for short, relies on past period values and past periods only to predict current period values.
It's a linear model where current period values are a sum of past outcomes multiplied by a numeric factor.
Value of phi lies between -1 and 1.

## Basics

-   Chronological Data
- Cannot be shuffled
- Each row indicate specific time record
- Train – Test split happens chronologically
- Data is analyzed univariately (for given use case)
- Nature of the data represents if it can be predicted or not

## Code Description

    File Name : Preprocess.py
    File Description : Class to preprocess the data, handle missing values, set time as index and QQ plots



    File Name : Engine.py
    File Description : Main class for starting different parts and processes of the lifecycle



    File Name : WhiteNoise.py
    File Description : Steps to test if the visualization is white noise or not



    File Name : RandomWalk.py
    File Description : Steps to test if the visualization is random walk or not



    File Name : Stationarity.py
    File Description : Steps to test if the visualization is stationary or not



    File Name : AcfAndPacf.py
    File Description : Steps to test the visualization of lag features



    File Name : Autoregressor.py
    File Description : Training the model on autoregression with log likelyhood

    
    
    File Name : RollingWindow.py
    File Description : Steps to verify the mean and Std

### Steps:
* Clone the repository
* Place your model file inside the ```output``` folder

Once you made the changes, create a new repository and commit the changes. From here on, this will be your source repository. Proceed with the below steps
###### Cloud Build Trigger
* In your GCP concole, create a new cloud build trigger.
* Point the trigger to your source repository
###### Google Kubernetes Engine (GKE)
* From the console lauch a kubernetes cluster
* Connect to the cluster and create the following two files
  * deployment.yaml
  * service.yaml
* Copy the code for both files from "Kubernetes Files" folder in cloned repository
* Execute the following commands
    * ```kubectl apply -f deployment.yaml```
    * ```kubectl apply -f service.yaml```
* Get the name of the deployment with the following command
    * ```kubectl get deployments```
###### Cloud Pub/Sub
* Create a Pub/Sub topic with the name ```cloud-build```
* Provide a subscription for the topic, which is to trigger a cloud function
###### Cloud Functions
* From Pub/Sub console launch the cloud function window
* Provide the following Environment variables through the GUI console
    * ```PROJECT``` (project name)
    * ```ZONE``` (Region in which in the project is deployed ex.uscentral-1)
    * ```CLUSTER``` (Name of the kubernetes cluster created earlier)
    * ```DEPLOYMENT``` (Name of the deployment inside the kubernetes cluster)
* Copy the program code and requirements.txt files for the cloud function from ```cloud-function-trigger``` folder
* Configure the Entrypoint for the cloud function as ```onNewImage``` 
* Deploy the function

After successful deployment, make a commit to source repository and the following will happen in sequence
* Cloud Build will push message to Pub/Sub upon successful build
* Pub/Sub will trigger the cloud function
* Cloud function will deploy the new image on Kubernetes
    * To test the deployment, check the logs on kubernetes cluster using the following command
        * ```kubectl get pods```
        * ```kubectl logs <pod name>```
    * The deployment will reflect in the logs as well as in the endpoints