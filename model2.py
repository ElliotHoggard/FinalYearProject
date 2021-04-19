from os import listdir
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import poisson
from tkinter import *
import numpy as np
import pandas as pd
import tkinter as tk

Filepath = ['./Dat2/' + f for f in listdir("./Dat2") if f.endswith('.csv')]
premier = pd.concat(map(pd.read_csv, Filepath), ignore_index=True, sort=False)

cols = ['HomeTeam', 'AwayTeam','FTR','FTHG','FTAG','HTGC','ATGC','HTP','ATP','HST','AST','HF','AF','HC','AC','HY','AY','HR','AR','B365H','B365D','B365A','HomeTeamLP','AwayTeamLP','ELO Home','ELO Away','HM1Conv','HTFormPts']
premier = premier[cols]
teams = ['HomeTeam', 'AwayTeam']


def matchSimulator(foot_model, homeTeam, awayTeam, max_goals=10):
    cols = [[awayTeam + ' Goals'] * (max_goals + 1), [goal for goal in range(max_goals + 1)]]
    ind = [[homeTeam + ' Goals'] * (max_goals + 1), [goal for goal in range(max_goals + 1)]]
    tuplesCols = list(zip(*cols))
    tuplesInd = list(zip(*ind))
    columns = pd.MultiIndex.from_tuples(tuplesCols, names=['Away Team', 'Goals'])
    index = pd.MultiIndex.from_tuples(tuplesInd, names=['Home Team', 'Percent Probability'])
    home_goals_avg = foot_model.predict(pd.DataFrame(data={'team': homeTeam,
                                                           'opponent': awayTeam, 'home': 1},
                                                     index=[1])).values[0]
    away_goals_avg = foot_model.predict(pd.DataFrame(data={'team': awayTeam,
                                                           'opponent': homeTeam, 'home': 0},
                                                     index=[1])).values[0]
    team_pred = [[round(poisson.pmf(i, team_avg), 1) for i in range(0, max_goals + 1)] for team_avg in
                 [home_goals_avg, away_goals_avg]]

    HomeVsAway = pd.DataFrame(np.outer(np.array(team_pred[0]), np.array(team_pred[1])), columns=columns, index=index)
    HomeVsAway = HomeVsAway.style.set_table_styles([dict(selector='th', props=[('text-align', 'center')])])
    HomeVsAway.set_properties(**{'text-align': 'center'})

    HomeAwayDraw = {'Home': round(np.sum(np.tril(np.outer(np.array(team_pred[0]), np.array(team_pred[1])), -1)), 3),
                    'Draw': round(np.sum(np.diag(np.outer(np.array(team_pred[0]), np.array(team_pred[1])))), 3),
                    'Away': round(np.sum(np.triu(np.outer(np.array(team_pred[0]), np.array(team_pred[1])), 1)), 3)}

    returnable = []
    returnable.append([round(home_goals_avg, 0), round(away_goals_avg, 0)])
    returnable.append(HomeVsAway)
    returnable.append(pd.DataFrame(HomeAwayDraw.values(), index=HomeAwayDraw.keys()).T)
    return returnable


def ResultSearchstart(root_frame):
    lower_frame = Frame(root_frame, bg='#4c8a27', bd=2, )
    lower_frame.place(relx=0.5, rely=0.3, relheight=0.2, relwidth=0.8, anchor="n")
    Label(root_frame, text="Enter the home team followed by the away team to make a prediction", font="AutobusBold 15 bold",bg="#4c8a27").place(x=200, y= 75, width=800)

    def print_selection():
        value = lb.get(lb.curselection())
        HT = value
        Result2(HT, root_frame)

    var2 = tk.StringVar()
    lb = tk.Listbox(lower_frame, listvariable=var2)
    b1 = tk.Button(lower_frame, text='Enter Home Team', font="AutobusBold 15 bold", bg="#add8e6", width=15, height=1, pady=2, padx=10, command=print_selection)
    b1.pack()
    list_items = ['Man City', 'Man United', 'Leicester', 'West Ham', 'Chelsea', 'Leeds', 'Liverpool', 'Tottenham', 'Everton', 'Aston Villa', 'Arsenal', 'Wolves', 'Crystal Palace', 'Southampton', 'Burnley', 'Brighton',
                  'Newcastle', 'Fulham', 'West Brom', 'Sheffield United']
    for item in list_items:
        lb.insert('end', item)
    lb.pack(padx=5,pady=5,fill=tk.BOTH,expand=True)


def Result2(HT, root_frame):
    lower_frame = Frame(root_frame, bg='#4c8a27', bd=2, )
    lower_frame.place(relx=0.5, rely=0.3, relheight=0.2, relwidth=0.8, anchor="n")

    def print_selection():
        value = lb.get(lb.curselection())
        AT = value
        ResultSearch(root_frame, HT, AT)

    var2 = tk.StringVar()
    lb = tk.Listbox(lower_frame, listvariable=var2)
    b1 = tk.Button(lower_frame, text='Enter Away Team', font="AutobusBold 15 bold", bg="#add8e6",
                   pady=2, padx=10, command=print_selection)
    b1.pack()
    list_items = ['Man City', 'Man United', 'Leicester', 'West Ham', 'Chelsea', 'Leeds', 'Liverpool', 'Tottenham', 'Everton', 'Aston Villa', 'Arsenal', 'Wolves', 'Crystal Palace', 'Southampton', 'Burnley', 'Brighton',
                  'Newcastle', 'Fulham', 'West Brom', 'Sheffield United']
    for item in list_items:
        lb.insert('end', item)
    lb.pack(padx=5,pady=5,fill=tk.BOTH,expand=True)


def ResultSearch(root_frame, HT, AT):
    n_goals = 5
    goal_model_data = pd.concat([premier[['HomeTeam', 'AwayTeam', 'FTHG']].assign(home=1).rename(
        columns={'HomeTeam': 'team', 'AwayTeam': 'opponent', 'FTHG': 'goals'}),
        premier[['AwayTeam', 'HomeTeam', 'FTAG']].assign(home=0).rename(
            columns={'AwayTeam': 'team', 'HomeTeam': 'opponent', 'FTAG': 'goals'})])

    poisson_model = smf.glm(formula="goals ~ home + team + opponent",
                            data=goal_model_data, family=sm.families.Poisson()).fit()
    n_goals = matchSimulator(poisson_model, HT, AT, max_goals=n_goals)
    lower_frame = Frame(root_frame, bg='#4c8a27', bd=2, )
    lower_frame.place(relx=0.5, rely=0.3, relheight=0.2, relwidth=0.8, anchor="n")
    Label(lower_frame, text="  " + str(HT) + " vs " + str(AT) + "\n" + str(n_goals[2]), font="AutobusBold 15 bold", bg="#add8e6").place(x=375, y=0)
    root_frame.mainloop()