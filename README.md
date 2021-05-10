# FinalYearProject
*A machine learning project that predicts Premier League Results and scoreline predominantly using regression.*

**Project Description**

The following project uses machine learning to predict the results and scorelines of future Premier League fixtures. Multiple models were analysed including an Artificial Neural Network, Logistic Regression, a Support Vector Classifier, XGBoost and a Random Forest Classifier. The Regression method was then further developed utilising Siméon Denis Poisson and the probability mass function to predict fixtures. These models analyse the probabilities of fixtures against bookmakers using live betting data to compare accuracies and provide punt recommendations as well as predict a scoreline.

**Software Requirements**

- Python (version 3.9 is recommended)
- Chromedriver
- The Python libraries TKinker, Pandas, Numpy, MatPlotlib, Tensorflow, SciKit-Learn, XGBoost, SciPy and Selenium

**Software Requirements**

To run the application simply head to the build folder where you will find the an executable exe file which can be downloaded and ran. 
* It is recommended to download all software requirements and run within a Python environment because the exe file lacks some functionality as they were unable to be used within PyInstaller *

![menu](https://user-images.githubusercontent.com/43520641/117599176-35e32000-b141-11eb-87f5-36abcfa914ee.PNG)


#### In the GUI's menu shown above you can see the project's general functionality. The project started by enhancing a to dataset and carrying out data analysis to add features including Goals Scored, Goals Conceded, Team Form, Cumulative Points, League Position and ELO ratings. Using this dataset multiple models wre analysed and the optimal model was developed and used in Model 1 and Model 2. These models used Siméon Denis Poisson and the probability mass function to predict fixtures and calculate bookmaker probabilities. I carried out testing of the models using the latest fixtures, all results from the testing is visible in the Results section.
