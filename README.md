# DataScience_tutorial

This repository is part of a comprehensive Data Science tutorial series. It covers essential concepts, practical data wrangling techniques, and exploratory data analysis to help you develop a deeper understanding of data manipulation and preparation for further modeling or analytics.

Through a combination of theoretical explanation and hands-on examples, you will learn how to clean, transform, and visualize datasets effectively. The tutorial is aimed at data enthusiasts, beginners, and anyone looking to sharpen their data wrangling skills. 

Additional Notebooks in the Repository
This repository also includes several Jupyter notebooks that explore different data science concepts and techniques, such as correlation analysis, linear regression, and exploratory data analysis (EDA):

[CorrelationAnalysis.ipynb](https://github.com/ghatanisuresh/DataScience_tutorial/blob/main/CorrelationAnalysis.ipynb): This notebook demonstrates how to compute and visualize the correlation matrix for a dataset. It includes heatmap visualizations to show the relationships between different variables.

[CorrelationVisualization.ipynb](https://github.com/ghatanisuresh/DataScience_tutorial/blob/main/CorrelationVisulization.ipynb): A continuation of the correlation analysis, this notebook expands on visualizing geospatial data using Python.

[DS.ipynb](https://github.com/ghatanisuresh/DataScience_tutorial/blob/main/DS.ipynb): A foundational notebook that covers basic data science techniques, including descriptive statistics, summary measures, and initial data exploration.

Linear_Regression.ipynb: This notebook covers multiple linear regression models, showcasing how to perform linear regression and visualize the results.

[MelbourneHousePrices](https://github.com/ghatanisuresh/DataScience_tutorial/blob/main/MelbourneHousePrices.ipynb): A simple data exploration notebook focused on analyzing the Melbourne housing market, examining key predictors and trends in the data.

[PractiseDataAnalysis](https://github.com/ghatanisuresh/DataScience_tutorial/blob/main/PractiseDataAnalysis.ipynb): This notebook provides a basic example of data analysis, using a European dataset. It covers common data wrangling and preprocessing tasks.

[Prediction.ipynb](https://github.com/ghatanisuresh/DataScience_tutorial/blob/main/Linear_Regression.ipynb): Focuses on linear regression concepts and predicts target variables based on a given set of predictors.

# Data Wrangling Demo

This repository demonstrates various data wrangling techniques using a dataset related to automobiles. It includes cleaning, transforming, and analyzing the data to derive insights. This project is designed to help individuals understand how to handle messy datasets effectively and prepare them for analysis.

## Project Files

- [**Automobile-Data-Wrangling-Demo.ipynb**](https://github.com/ghatanisuresh/DataScience_tutorial/blob/main/Data-Wrangling/Automobile-Data-Wrangling-Demo.ipynb): This Jupyter notebook contains the main data wrangling process. It walks through the steps of handling missing values, correcting data types, and analyzing relationships between features.
- [**Automobile-Data-Wrangling-Demo.html**](https://github.com/ghatanisuresh/DataScience_tutorial/blob/main/Data-Wrangling/Automobile-Data-Wrangling-Demo.html): An HTML version of the Jupyter notebook, making it accessible for users who prefer to view the process in a browser without running the notebook.
- [**clean_df.csv**](https://github.com/ghatanisuresh/DataScience_tutorial/blob/main/Data-Wrangling/clean_df.cssv): A cleaned version of the automobile dataset after wrangling, ready for analysis or further machine learning tasks.
- [**LaptopPriceEDA.ipynb**](https://github.com/ghatanisuresh/DataScience_tutorial/blob/main/Data-Wrangling/LaptopPriceEDA.ipynb):  A comprehensive exploratory data analysis (EDA) of laptop prices. This notebook examines factors that influence laptop prices, using visualizations and data wrangling techniques to uncover trends and insights in the dataset. It provides an example of how data wrangling is applied to real-world datasets, making it an integral part of this project.

# EDA:

The EDA folder contains Jupyter notebooks focused on analyzing relationships between variables and uncovering patterns in the datasets. These notebooks explore pricing relationships in both cars and laptops, providing a deep dive into factors influencing their prices.

Notebooks in the EDA Folder:

[**CarPriceRelationship.ipynb**]([EDA/CarPriceRelationship.ipynb](https://github.com/ghatanisuresh/DataScience_tutorial/blob/main/EDA/CarPriceRelationship.ipynb)): This notebook analyzes the relationship between various car features and their pricing. It covers:

Feature correlation with price.
Visualizing the influence of engine size, horsepower, and fuel type on car prices.
Regression analysis to predict car prices based on key attributes.

[**LaptopsPricingRelation.ipynb**]([EDA/LaptopsPricingRelation.ipynb](https://github.com/ghatanisuresh/DataScience_tutorial/blob/main/EDA/LaptopsPricingRelation.ipynb)): In this notebook, the pricing trends of laptops are explored. It includes:

Detailed exploration of how specifications like RAM, storage, and processor type impact laptop prices.
Visualization of the relationships between these attributes and price using plots.
A focus on understanding which laptop features are the most significant predictors of price.

# Model Development
This directory contains Jupyter notebooks that focus on developing predictive models using both linear and multiple linear regression techniques. The notebooks provide insights into building and evaluating regression models for real-world datasets.

Notebooks in the Model Development Folder:

[**Linear and Multiple LR.ipynb**](https://github.com/ghatanisuresh/DataScience_tutorial/blob/main/Model%20Development/Linear%20and%20Multiple%20LR.ipynb): This notebook covers both simple linear regression and multiple linear regression. It explores the following:
   * Simple Linear Regression: Demonstrates how to build a model with one predictor variable, examining how the target variable (dependent variable) changes with the predictor.
   * Multiple Linear Regression: Expands the model to include multiple predictor variables. It shows how to evaluate the model using metrics such as R², adjusted R², and Mean Squared Error (MSE).


# Model Evaluation and Refinement

In this section, the models were evaluated using cross-validation, polynomial feature transformations, Ridge Regression and GridSearchCV to improve predictive performance and prevent overfitting.

After the initial model development, two key steps were taken to refine and evaluate the models:

1. **Model Evaluation:**
   - **File:** [model_evaluation.ipynb](https://github.com/ghatanisuresh/DataScience_tutorial/blob/main/ModelEvaluation-Refinement/model_evaluation.ipynb)
   - **Description:** In this notebook, polynomial regression was applied to capture non-linear relationships between the features (`CPU_frequency`, `RAM_GB`, `Storage_GB_SSD`, etc.) and laptop prices. Different polynomial degrees were tested to evaluate their performance. Additionally, Ridge Regression was implemented with various values of alpha to regularize the model and prevent overfitting.

2. **Model Refinement:**
   - **File:** [laptopmodel_evaluation.ipynb](https://github.com/ghatanisuresh/DataScience_tutorial/blob/main/ModelEvaluation-Refinement/laptopmodel_evaluation.ipynb)
   - **Description:** This notebook focused on refining the model by selecting the optimal alpha value in Ridge Regression. The R² scores for both the training and test data were analyzed to find the balance between underfitting and overfitting. The final model utilized polynomial features with Ridge Regression to achieve the best performance on unseen data.

# Project

The "Project" directory includes real-world datasets and projects that integrate all concepts covered.

Datasets:

insurance.csv - Dataset used in medical insurance cost prediction.
kc_house_data.csv - Dataset for predicting house prices.

Notebooks:

[HousePricePrediction.ipynb](/workspaces/DataScience_tutorial/Project/HousePricePrediction.ipynb) - A project to predict house prices based on Seattle housing data.
[Medical_Insurance_Price_Prediction.ipynb](/workspaces/DataScience_tutorial/Project/Medical_Insurance_Price_Prediction.ipynb) - A project focused on predicting medical insurance costs.

## Key Processes

1. **Data Cleaning**:
   - Handling missing values.
   - Correcting data types.
   - Normalizing and transforming values for consistency.
  
2. **Exploratory Data Analysis (EDA)**:
   - Identifying relationships between features.
   - Creating visualizations to summarize the data.

3. **Data Preparation for Modeling**:
   - Transforming categorical variables.
   - Feature scaling and normalization.

4. **Model Development**:
   - Builds models to predict target variables using single and multiple predictors, evaluated with metrics like R² and MSE.
   - Captures non-linear relationships to improve model accuracy.
   -  Adds regularization to reduce overfitting, optimized through hyperparameter tuning (alpha).
   - Streamlines preprocessing and model training, with GridSearchCV for hyperparameter optimization.

5. **Model Evaluation**:
   
   - Assessing model performance using various metrics, including R², Mean Squared Error (MSE), and cross-validation scores.
   - Comparing model predictions against actual values to determine the accuracy and reliability of the model.
   
6. **Hyperparameter Tuning**:

   - Utilizing techniques like GridSearchCV to identify optimal model parameters, improving the accuracy and generalizability of the model.
   - Fine-tuning parameters such as regularization strength in Ridge Regression to balance between underfitting and overfitting.

7. **Pipeline Creation**:

   - Implementing machine learning pipelines to streamline workflows, combining data preprocessing, transformation, and modeling steps.
   - Ensures reproducibility and efficiency, especially when experimenting with different models and parameters.

8. **Project Deployment**:

   - Using Streamlit to deploy interactive data applications, allowing end-users to explore and interact with data insights.
   - Simplifies sharing insights and models by creating accessible web applications that demonstrate the project's findings and predictive capabilities.

## Dependencies

- Python 3.x
- Jupyter Notebook
- google colab
- github codespace
- Pandas
- NumPy
- Matplotlib / Seaborn
- Steamlit




