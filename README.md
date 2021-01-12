# Design Document
Authors: William Catzin, Kenneth Addo

Refactoring Tool is a full-stack web application built for software quality research in the Department of Software Engineering at the Rochester Institute of Technoology. Refactoring Tool allows users to enter a commit message in a text box and three machine learning modeles in the back end determine if the message pertains to self-admitted refactoring (SAR) or not (non-SAR). If the message does pertain to SAR, then the type of refactoring and the intention behind the refactoring is also determined.

![refactoring tool](refactoring_tool/refactoring_tool.gif)

----------
# Folders and Files
## refactoring-tool (Folder)

The refactoring-tool folder contains files that coordinate urls and other essential folders. All files were created automatically, except the templates folder and the urls.py file, with the following command in the terminal:


    $ django-admin startproject refactoring-tool

Contents of refactoring-tool:

- templates (Created File)
- __init__.py
- asgi.py
- settings.py
- urls.py (Created File)
- wsgi.py

**templates (Folder)**

- **base.html**

This file is the main html file for Refactoring Tool. It sets the font and style for the navbar and creates two link buttons (Home and Analytics) on the navbar.

**settings.py**
The code in this file was auto generated. I inserted only two lines of code that's required for refactoring-tool to find two other folders I created.


    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'tool',
        'analytics',
    ]

I inserted lines 8 and 9. tool and analytics are two folders I created.

**urls.py**
This file contains urls that are linked to buttons that redirect users to three different pages: the home page, the results page, and the analytics page.

**asgi.py and wsgi.py**
The code in this file was auto generated.


## tool (Folder)

The tool folder contains files that create and update a database, applies machine learning models to user input, and html files that are used in the home page for user to interact with the machine learning models. All files and folders were auto generated except the following: templates(folder), mlModels.py, forms.py, and urls.py.

Contents of tool:

- __pycache__
- migrations(Folder)
- templates(Created Folder)
- __init.py__
- admin.py
- apps.py
- forms.py
- mlModels.py(Created File)
- models.py
- tests.py
- urls.py(Created File)
- views.py

**__pycache__ and migrations (Folders)**
These folders and the files inside were auto generated.

**__init.py__, admin.py, and apps.py**
These files and the code were auto generated.

**templates (Folder)**

- **tool_detail.html**

  This file creates the text box and the submit button in the home page.

- **tool_results.html**

This file redirects the user from the home page to the results page and displays the results after the user has submitted the commit message to be processed by the machine learning model. It also creates a button to allow users to submit another commit message.

**forms.py**
This file contains a class called CommitForm that describes the format for text input from users. When a GET request for the home page is sent, CommitForm renders the text body in HTML.

**mlModels.py**
This file contains a class called MLmodels, which is used in views.py and tests.py. The commit message entered by a user is processed by the function call sarClassification().

**models.py**
This file contains a class called Commit, which describes the database table. The fields of Commit will contain the data from user input and results of the machine learning model and then saved in the database.

**tests.py**
This file contains unit tests that checks if an MLmodels object is returning a string value after processing a string value.

**urls.py**
This file contains paths to tool_detail.html and tool_results.html so it can be recognized by other components.

**views.py**
This file contains two methods: tool_detail(request) and tool_results(request). If a user is requesting to go to the home page (GET request), then tool_detail.html is called and home page is displayed. If a user is requesting to sumbit their input (POST request), then their input is first validated and then processed by an MLmodels object called classifier,


    classifier = MLmodels("commit message") 

MLmodels() has a function called,


    sarClassification()

which returns a list. If the length of the list is 1, then the commit message does not pertain to self-admitted refactoring. The list will only contain the commit message. The data will be saved to the database; the user will remain in the home page with a message notifying them that their commit message was not SAR. If the length of the list is 3, then the commit message does pertain to self-admitted refactoring. The list will contain the commit message, type of refactoring, and the intention of refactoring. The data will then be saved to the database and the user will be redirected to the Results page to see the results.


## **analytics (Folder)** 

The analytics folder contains files and folders that display the contents of the database and data visualizations. This folder is similar to the tool folder. The only file that was altered was views.py. A folder called templates was created and a file called urls.py was created.

**templates (Folder)**

- **analytics_detail.html**

This file displays the contents of the database and embeds data visualizations from Tableau Public.

**urls.py**
This file contains a path to analytics_detail.html to be recognized by other components.

**views.py**
This file renders analytics_detail.html with a dictionary containing database table names as keys and the contents as values.



    return render(request, 'analytics_detail.html', {'messages':messages})


----------


# **Classes**


## **CommitForm (Forms.py)**

This class describes the form of the interface that will be rendered in html to be displayed on the website.

**Fields:**

- body is assigned to a CharField that represents the textbox for the user to input text.
- (Inner Class) Meta class describes meta data for the database.


## **MLmodels (mlModels.py)**

Connects fields to three published machine learning models from Azure Machine Learning Studio.

**Fields:**

- __init__ takes and sets a string value: message.
- __encodeMessage returns an encoded string value
- __classificationResult returns a string value after running a machine learning model.
- sarClassification returns a list containing string values, which were returned from running the machine learning models.
- __typeClassification returns a string value which refers to the type of refactoring using a machine learning model.
- __intentionClassification returns a string value which refers to the intention of refactoring using a machine learning model.


## **Commit (models.py)**

This class describes a database.

**Fields:**

- body is a column name in the database. It stores a string value, which refers to the commit message entered by a user.
- SAR_nonSAR is a column name in the database. It stores a string value, which refers to "SAR" or "nonSAR" determined by sarClassification (mlModels.py)
- intention is a column name in the database. It stores a string value, which refers to some intention of refactoring determined by intentionClassification (mlModels.py)
- type_of_SAR is a column name in the database. It stores a string value, which refers to some type of refactoring determined by typeClassification (mlModels.py)


## **TestMLmodels (tests.py)**

This class checks the output of using the machine learning models.

**Fields:**

- test_sar is a unit test. It instantiates an MLmodels object by passing a commit message that pertains to self-admitted refactoring (SAR) and checks if sarClassification returns a list of length 3 and contains string values.
- test_nonSAR is a unit test. It instantiates an MLmodels ojbect by passing a commit message that pertains to non-self-admitted refactoring (nonSAR) and checks if sarClassification returns a list of length 1 and contains a string value.


----------


# Python **FrameWorks**
- Django
- unittest

