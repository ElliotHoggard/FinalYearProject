from time import time
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
# Libraries used in models
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import scale
from sklearn.ensemble import ExtraTreesClassifier

# Uses the enhanced dataset by reading each seasons data in turn and storing it in the premier dataset
Filepath = ['./Dat2/' + f for f in listdir("./Dat2") if f.endswith('.csv')]
premier = pd.concat(map(pd.read_csv, Filepath), ignore_index=True, sort=False)

# Features used from the dataset
cols = ['HomeTeam', 'AwayTeam', 'FTR', 'HTGC', 'ATGC', 'HTP', 'ATP', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY',
        'HR', 'AR', 'B365H', 'B365D', 'B365A', 'HomeTeamLP', 'AwayTeamLP', 'ELO Home', 'ELO Away', 'HTFormPts']
premier = premier[cols]
data = premier[cols]
data.drop(['HomeTeam', 'AwayTeam'], 1, inplace=True)
# Training set contains all except the full time result, home goals scored and away goals scored
X_all = data.drop(['FTR'], 1)
# Test set compares the predicted full time result against the actual full time result
y_all = data['FTR']
cols = ['HTP', 'ATP', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR', 'B365H', 'B365D', 'B365A',
        'HomeTeamLP', 'AwayTeamLP', 'ELO Home', 'ELO Away', 'HTFormPts']  # Features used in model testing

# Data is standardised
for col in cols:
    X_all[col] = scale(X_all[col])
X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=50, random_state=2, stratify=y_all)

# function gets all data in the correct format
def preprocess_features(X):
    output = pd.DataFrame(index=X.index)
    for col1, col_data in X.iteritems():
        if col_data.dtype == object:
            col_data = pd.get_dummies(col_data, prefix=col1)
        output = output.join(col_data)
    return output


X_all = preprocess_features(X_all)
# trains the data into a training and test set
X_train, X_test, y_train, y_test = train_test_split(X_all, y_all, test_size=50, random_state=2, stratify=y_all)

# Initialise GUI
game_menu2 = Tk()
game_menu2.deiconify()
game_menu2.title('Probable Scoreline')
game_menu2.geometry("700x700")
game_menu2.configure(bg="green")
game_menu_frame2 = Frame(game_menu2)
game_menu_frame2.place(relx=0.5, rely=0.15, relheight=0.8, relwidth=0.7, anchor='n')
# Calculates each features importance and outputs the strengths in a graph
def FeatureRating():
    drop = data.drop(['FTR'], 1)
    X = drop.iloc[:, 0:21]  # All columns
    y = data['FTR']  # target column
    model = ExtraTreesClassifier()
    model.fit(X, y)
    print(model.feature_importances_)  # Outputs feature importance based on the classifiers
    feat_importance = pd.Series(model.feature_importances_, index=X.columns)
    feat_importance.nlargest(21).plot(kind='barh')
    plt.show()

# *All Cross Validation has been commented out as it takes a significant amount of processing time*
# Support Vector Classifier
def SVC():
    Label(game_menu_frame2, text="SVC", font=('Autobus Bold', 20)).place(x=50, y=50)
    start = time()
    SVC5 = SVC(random_state=20, kernel='rbf')
    SVC5.fit(X_train, y_train)
    SVC5_predict = SVC5.predict(X_test)
    confusion_matrix(y_test, SVC5_predict)  # Measures accuracy by comparing training and test set
    a = float(accuracy_score(y_test, SVC5_predict))
    Label(game_menu_frame2, text="Accuracy " + str(a)).place(x=50, y=250)
    Label(game_menu_frame2, text=str(classification_report(y_test, SVC5_predict))).place(x=25, y=100)
    end = time()  # Calculates the time to predict values
    Label(game_menu_frame2, text="Trained model in {:.4f} seconds".format(end - start)).place(x=50, y=275)

    ## Cross Validation used to improve accuracy, over fitting and selection bias can be found
    # clf = svm.SVC(kernel='linear', C=1, random_state=42)
    # SVC50 = cross_val_score(clf, X_train, y_train, cv=50)
    # Label(game_menu_frame2, text="Mean 50 trees = " + str(np.mean(SVC50))).place(x=50, y=300)
    # SVC100 = cross_val_score(clf, X_train, y_train, cv=100)
    # Label(game_menu_frame2, text="Mean 50 trees = " + str(np.mean(SVC100))).place(x=50, y=300)
    # SVC500 = cross_val_score(clf, X_train, y_train, cv=500)
    # Label(game_menu_frame2, text="Mean 50 trees = " + str(np.mean(SVC500))).place(x=50, y=300)


# XGB Boost
def XGB():
    Label(game_menu_frame2, text="XGB Boost", font=('Autobus Bold', 20)).place(x=50, y=50)
    start = time()
    clf_C = xgb.XGBClassifier(seed=82)
    clf_C.fit(X_train, y_train)
    clf_C_predict = clf_C.predict(X_test)
    confusion_matrix(y_test, clf_C_predict)  # Measures accuracy by comparing training and test set
    a = float(accuracy_score(y_test, clf_C_predict))
    Label(game_menu_frame2, text="Accuracy " + str(a)).place(x=50, y=250)
    Label(game_menu_frame2, text=str(classification_report(y_test, clf_C_predict))).place(x=25, y=100)
    end = time()  # Calculates the time to predict values
    Label(game_menu_frame2, text="Trained model in {:.4f} seconds".format(end - start)).place(x=50, y=275)

    ## Cross Validation used to improve accuracy, over fitting and selection bias can be found
    # XGB50 = cross_val_score(clf_C, X_train, y_train, cv=50)
    # Label(game_menu_frame2, text="Mean 50 trees = " + str(np.mean(XGB50))).place(x=50, y=300)
    # XGB100 = cross_val_score(clf_C, X_train, y_train, cv=100)
    # Label(game_menu_frame2, text="Mean 100 trees = " + str(np.mean(XGB100))).place(x=50, y=325)
    # XGB500 = cross_val_score(clf_C, X_train, y_train, cv=500)
    # Label(game_menu_frame2, text="Mean 100 trees = " + str(np.mean(XGB500))).place(x=50, y=350)


# Artificial Neural Network
def ANN():
    Label(game_menu_frame2, text="Artifical Neural Network", font=('Autobus Bold', 20)).place(x=50, y=50)
    start = time()
    ann = MLPClassifier(activation='logistic', hidden_layer_sizes=(500, 4), shuffle=True)
    ann.fit(X_train, y_train)
    y_predict = ann.predict(X_test)
    confusion_matrix(y_test, y_predict)  # Measures accuracy by comparing training and test set
    a = float(accuracy_score(y_test, y_predict))
    Label(game_menu_frame2, text="Accuracy " + str(a)).place(x=50, y=250)
    Label(game_menu_frame2, text=str(classification_report(y_test, y_predict))).place(x=25, y=100)
    end = time()  # Calculates the time to predict values
    Label(game_menu_frame2, text="Trained model in {:.4f} seconds".format(end - start)).place(x=50, y=275)

    ## Cross Validation used to improve accuracy, over fitting and selection bias can be found
    # ANN50 = cross_val_score(MLPClassifier(solver='lbfgs', activation='logistic'), X_train, y_train, cv=50)
    # Label(game_menu_frame2, text="Mean 50 trees = " + str(np.mean(ANN50))).place(x=50, y=300)
    # ANN100 = cross_val_score(MLPClassifier(solver='lbfgs', activation='logistic'), X_train, y_train, cv=100)
    # Label(game_menu_frame2, text="Mean 100 trees = " + str(np.mean(ANN100))).place(x=50, y=325)
    # ANN500 = cross_val_score(MLPClassifier(solver='lbfgs', activation='logistic'), X_train, y_train, cv=500)
    # Label(game_menu_frame2, text="Mean 100 trees = " + str(np.mean(ANN500))).place(x=50, y=350)

    ## Hidden layers are altered to see the effect it has on accuracy
    # ANN50 = cross_val_score(MLPClassifier(solver='lbfgs', activation='logistic', hidden_layer_sizes=(50, 50)), X_train, y_train, cv=10)
    # Label(game_menu_frame2, text="Mean 50 trees = " + str(np.mean(ANN50))).place(x=50, y=375)
    # ANN100 = cross_val_score(MLPClassifier(solver='lbfgs', activation='logistic', hidden_layer_sizes=(100, 100)),X_train, y_train, cv=10)
    # Label(game_menu_frame2, text="Mean 100 trees = " + str(np.mean(ANN100))).place(x=50, y=400)
    # ANN500 = cross_val_score(MLPClassifier(solver='lbfgs', activation='logistic', hidden_layer_sizes=(500, 500)),X_train, y_train, cv=10)
    # Label(game_menu_frame2, text="Mean 100 trees = " + str(np.mean(ANN500))).place(x=50, y=425)


# Random Forest
def RandForest():
    Label(game_menu_frame2, text="Random Forest", font=('Autobus Bold', 20)).place(x=50, y=50)
    start = time()
    rfc5 = RandomForestClassifier(n_estimators=1000, min_samples_leaf=5)
    rfc5.fit(X_train, y_train)
    rfc5_predict = rfc5.predict(X_test)
    confusion_matrix(y_test, rfc5_predict)  # Measures accuracy by comparing training and test set
    a = float(accuracy_score(y_test, rfc5_predict))
    Label(game_menu_frame2, text="Accuracy " + str(a)).place(x=50, y=250)
    Label(game_menu_frame2, text=str(classification_report(y_test, rfc5_predict))).place(x=25, y=100)
    end = time()  # Calculates the time to predict values
    Label(game_menu_frame2, text="Trained model in {:.4f} seconds".format(end - start)).place(x=50, y=275)

    ## Cross Validation used to improve accuracy, over fitting and selection bias can be found
    # rfc50 = cross_val_score(RandomForestClassifier(X_train, y_train, cv=50))
    # Label(game_menu_frame2, text="Mean 50 trees = " + str(np.mean(rfc50))).place(x=50, y=300)
    # rfc100 = cross_val_score(RandomForestClassifier(X_train, y_train, cv=100))
    # Label(game_menu_frame2, text="Mean 100 trees = " + str(np.mean(rfc100))).place(x=50, y=325)
    # rfc500 = cross_val_score(RandomForestClassifier(X_train, y_train, cv=500))
    # Label(game_menu_frame2, text="Mean 100 trees = " + str(np.mean(rfc500))).place(x=50, y=350)

    ## Alters the number of trees to see the effect on accuracy
    # rfc50 = cross_val_score(RandomForestClassifier(n_estimators=50), X_train, y_train, cv=10)
    # Label(game_menu_frame2, text="Mean 50 trees = " + str(np.mean(rfc50))).place(x=50, y=375)
    # rfc100 = cross_val_score(RandomForestClassifier(n_estimators=100), X_train, y_train, cv=10)
    # Label(game_menu_frame2, text="Mean 100 trees = " + str(np.mean(rfc100))).place(x=50, y=400)
    # rfc500 = cross_val_score(RandomForestClassifier(n_estimators=500), X_train, y_train, cv=10)
    # Label(game_menu_frame2, text="Mean 100 trees = " + str(np.mean(rfc500))).place(x=50, y=425)


# Logistic Regression
def LogRegression():
    Label(game_menu_frame2, text="Logistic Regression", font=('Autobus Bold', 20)).place(x=50, y=50)
    start = time()
    log5 = LogisticRegression(random_state=25)
    log5.fit(X_train, y_train)
    log5_predict = log5.predict(X_test)
    confusion_matrix(y_test, log5_predict)  # Measures accuracy by comparing training and test set
    a = float(accuracy_score(y_test, log5_predict))
    Label(game_menu_frame2, text="Accuracy " + str(a)).place(x=50, y=250)
    Label(game_menu_frame2, text=str(classification_report(y_test, log5_predict))).place(x=25, y=100)
    end = time()  # Calculates the time to predict values
    Label(game_menu_frame2, text="Trained model in {:.4f} seconds".format(end - start)).place(x=50, y=275)

    ## Cross Validation used to improve accuracy, over fitting and selection bias can be found
    # CV50 = cross_val_score(log5, X_train, y_train, cv=50)
    # Label(game_menu_frame2, text="Mean 50 trees = " + str(np.mean(CV50))).place(x=50, y=300)
    # CV100 = cross_val_score(log5, X_train, y_train, cv=100)
    # Label(game_menu_frame2, text="Mean 50 trees = " + str(np.mean(CV100))).place(x=50, y=325)
    # CV500 = cross_val_score(log5, X_train, y_train, cv=100)
    # Label(game_menu_frame2, text="Mean 500 trees = " + str(np.mean(CV500))).place(x=50, y=350)
