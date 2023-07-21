# Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression
The primary objective of this project is to develop a real-time hybrid model employing Decision Tree, Random Forest, Logistic Regression to forecast the menstrual cycle length of women. With this knowledge they can gain valuable information about their reproductive health, fertility, and overall well-being. Predicting the menstrual cycle length of women helps in family planning, identifying potential health concerns, and seeking appropriate medical care when necessary.

# Step 1: Data Collection
Menstrual cycle dataset was collected from kaggle


# Step 2 : Data Preprocessing
The dataset was preprocessed to remove irrelevant data, null values. Also, feature engineering was done on the dataset. Out of the 80 columns contained in the dataset, only 3 columns were extracted. These columns include: The 'Estimated Ovulation Day', 'Length of Luteal Phase', and 'Length of Cycle'. The columns were then splitted into feature columns and target columns. The feature columns include: "Estimated Ovulation Day" and "Length of Luteal Phase". While the target column is "Length of Cycle". The feature columns were used to predict the Length of Cycle of a woman.

# Step 3: Training the Model
In training the model, we used three machine learning algorithm which include: Random Forest, Decision Tree, and Linear Regression Algorithm. The libraries used are listed below:
#Import the necessary librabries
1.import numpy as np
2.import pandas as pd
3.from sklearn.ensemble import RandomForestClassifier
4.from sklearn.tree import DecisionTreeClassifier
5.from sklearn.linear_model import LogisticRegression
6.from sklearn.model_selection import train_test_split
7.from sklearn.metrics import accuracy_score, f1_score, recall_score, r2_score
8.import matplotlib.pyplot as plt
9.import seaborn as sn

# Step 4: Import the dataset
**The code below shows how to import the dataset using pandas:**
- ovulation_dataset = pd.read_csv("C:\Users\MINISTER JOHN\Downloads\ovulation_dataset.csv")
  
**To view five rows out of the dataset**
- ovulation_dataset.head()

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/22c1d6d7-c852-4a82-bb45-a83c70b2a05b)

**To determine the shape of the dataset**

[The shape of the dataset is used to show the number of rows and columns in the dataset. The function below does that: ]:# 

- ovulation_dataset.shape

  ![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/60910729-a7fb-4ae2-962e-b14533be4903)


**To check if there are missing values**

[To check if there are missing values and the sum of the missing values, the function below is used: ]:# 

- ovulation_dataset.isnull().sum()

  ![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/c386ca47-5a82-4759-a688-9f3f1552fe6f)


**To determine the datatype and the data columns of the dataset**

[ The datatype and data columns of the dataset is determined using the following function:]:# 

- ovulation_dataset.info()

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/8d75cf0e-803c-4577-8768-337d0f7f954d)

**To describe the dataset**

[To determine some statistics values of the dataset such as the mean, standard deviation, etc, the function below is used: ]:# 

- ovulation_dataset.describe()

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/28a76965-1f69-4ec6-ac79-741db50fb869)

# Step 5: Splitting the dataset

After preprocessing the dataset, it was then splitted into features and target set. X represent the features dataset, while Y represent the target dataset. The drop() function used here is used to drop the 'Length of Cycle' from the dataset so as to separate it from the features dataset. It is therefore shown below:
X = ovulation_dataset.drop('LengthofCycle', axis= 1)
y = ovulation_dataset['LengthofCycle']

**To view the values of X dataset**

[The X represent the features dataset. It is shown by just typing X as shown in the figure below: ]:# 

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/362a29b5-e395-4ba8-8d43-f38a3c9ccf96)

**To view the values of y dataset**

[The y represent the target dataset. It is shown by just typing y as shown in the figure below ]:# 

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/0ff37419-ad5d-49de-89f3-b241ca1fa7fe)


# Step 6: Split the dataset into training and testing set
The 'X_train' represent the 85% of the training dataset. The 'X_test' represent the 15% for testing the model. The 'y_train' represent the 85% of the target dataset that was used to train the model. The 'y_test' represent the 15% of the target dataset that was used to test the model.

- X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15, random_state = 42)
  
# Step 7: Develop the model

[To develop the model the following was carried out: ]:# 
- from sklearn.tree import DecisionTreeRegressor
[  Create an instance of the Decision Tree model]:#

- decision_tree = DecisionTreeRegressor()

  
# Step 8: Train the model

- decision_tree.fit(X_train, y_train)

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/84618361-c007-4bcf-85a4-e535991a15c9)


**Testing the trained model using the X_train set**

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/f0f7af2f-eb2e-4928-9b5d-5fd5725f5b37)


# Step 9: Evaluating the model using some evaluation parameters.

**The evaluation metrics output is shown in the figure below:**

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/e1fc61ba-479a-4ae5-b729-5a03338e7c1f)

[The metrics output is shwon in the figure below]:#

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/0f650c28-b2a6-4c8e-8d71-50f5202b0291)


**To take input from users in the command line form**

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/eaecdc10-bb95-4fe2-b71d-6dc642015678)


# Step 10: Pickling the model

The pickled model helps to be able to deploy the model using Django. Meanwhile, you have to specify the path you want the pickled model to be saved. I specified Desktop as my own path.

# Deploying the model Using Django
After developing the model and have pickled the model, the next thing to do is to deploy the model in a web application where a user can input their estimated ovulation day and the length of luteal phase so as to determine their menstrual cycle length. The steps below shows how to deploy the model using Django.
**1.** **Step 1: Download Python**
   
For Django to run, python is required. Hence, first of all download Python. However, if you have downloaded python in your system, you can start.

**2. Step 2: Install Django**

**To install Django kindly use the code below:**

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/70116b3d-e345-4c04-b702-6b5761f9995b)

It will give you the result as shown below:

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/f39a7c88-5df5-4f6f-820f-84f3177f8711)


**3. Step 3: Create your Project**

Once you have come up with a suitable name for your Django project, like mine: DeployModel, Open your command prompt and specify where you want to store your project name. I stored mine in the Desktop, so when I navigate to the desktop, I should see the project name. See the figure below:

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/a8538e22-7f14-4bc7-9c73-18393a8eba48)


## To navigate into the Django project

To enter into the project you have created, the figure below shows it.

**4. Step 4: Create an App**

- We have a Django project!
- The next step is to make an app in your project.
- You cannot have a web page created with Django without an app.
- I will name my app DeployModelApp.
- Start by navigating to the selected location where you want to store the app, and run the command below.

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/7507a8e4-afe4-48ca-abae-72bb78c1e9d6)



If the server is still running, and you are not able to write commands, press [CTRL] [BREAK] to stop the server and you should be back in the virtual environment.
Django creates a folder named DeployModelApp in my project, with this content:

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/62ab9e2d-dd88-46be-b7f6-0b019ee809c7)


**5. Step 5: Run your project**

The figure below shows how to check if your Django project has been successfully created.
Kindly copy the URL Link to a browser : http://127.0.0.1:8000/

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/0a231738-cd5f-46e6-b6c2-e2033cd61822)


**6. Step 6: Deploying the model**

## Navigate to the Views in your Django app.
- Django views are Python functions that takes http requests and returns http response, like HTML documents. A web page that uses Django is full of views with different tasks and missions. Views are usually put in a file called views.py located on your app's folder.
**There is a views.py in your DeployModelApp folder that looks like this:**

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/1cea1456-4032-4177-9106-9116f1df787e)


**Find it and open it, and replace the content with this:**

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/d8de320e-1653-4271-a310-89c7e7a37d15)


**Note: Navigate to the settings.py file in the DeployModel project and then type the name of your Django app for configuration purpose. The figure below shows where to put the Django app**__

Note: However, in the content in the views.py contains two important file "home.html" and "result.html". To create these files, create a folder named "templates" in the DeployModelApp and then navigate to the settings in the Django project named "DeployModel" and then type "templates" in the DIR[]section as shown below: 

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/d73bea6d-4ec8-4788-93a2-b098ff11c0a1)


![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/857bbdd0-5b9d-4142-9272-2c1ee891f8e1)


## Create a URL file in your DeployModelApp

Create a file named urls.py in the same folder as the views.py file, and type this code in it:

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/41b44682-4a87-455a-9f21-f9267e4728f0)

## Creating the template files.

Inside the template, we have two files: "home.html" and "result.html". The "home.html" contains the user interface of the web while the "result.html" is the page where the result is been displayed.
The content of the "home.html" can be found in the 'DeployModelApp' folder


The content of the "result.html" can be found in the 'DeployModelApp' folder. 

**Put the code in the URLS of the DeployModel project**

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/8d32174d-5037-4476-980e-5a246fffd409)


**Run the project using the following syntax**

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/5c0cc5ba-f3e6-4bb7-9dbc-0071104395ab)


kindly copy the urls and paste it on a web browser. The home page is displayed thus:

![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/bad20a4b-3b24-4788-b044-a35f4f818509)


**To start the prediction**



To start the prediction, input the required data: "Ovulation day" and "Length of Luteal Phase" and then click "Predict"

The result will be shown in the "result.html" page which is show below:
![image](https://github.com/MinisterJohn/Menstrual-Cycle-Prediction-System-Using-Decision-Tree-Random-Forest-and-Logistic-Regression/assets/94996679/cf2664eb-10f8-492a-b68f-d4c5e444692c)



 
