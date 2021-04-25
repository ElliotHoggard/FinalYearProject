from os import listdir
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import poisson
from tkinter import *
import numpy as np
import pandas as pd
import tkinter as tk

# Reads all Dat2 contents
Filepath = ['./Dat2/' + f for f in listdir("./Dat2") if f.endswith('.csv')]
premier = pd.concat(map(pd.read_csv, Filepath), ignore_index=True, sort=False)

# Columns in CSV required
cols = ['HomeTeam', 'AwayTeam', 'FTR', 'FTHG', 'FTAG', 'HTGC', 'ATGC', 'HTP', 'ATP', 'HST', 'AST', 'HF', 'AF', 'HC',
        'AC', 'HY', 'AY', 'HR', 'AR', 'B365H', 'B365D', 'B365A', 'HomeTeamLP', 'AwayTeamLP', 'ELO Home', 'ELO Away',
        'HM1Conv', 'HTFormPts']
premier = premier[cols]


# Simulates a match using the home teams and away teams contents
def SimulateMatch(model, homeTeam, awayTeam, maxGoals=10):
    cols = [[awayTeam + ' Goals'] * (maxGoals + 1), [goal for goal in range(maxGoals + 1)]]
    ind = [[homeTeam + ' Goals'] * (maxGoals + 1), [goal for goal in range(maxGoals + 1)]]
    tuplesCols = list(zip(*cols))
    tuplesInd = list(zip(*ind))
    columns = pd.MultiIndex.from_tuples(tuplesCols, names=['Away Team', 'Goals'])
    index = pd.MultiIndex.from_tuples(tuplesInd, names=['Home Team', 'Percent Probability'])
    htAvgGoals = model.predict(pd.DataFrame(data={'team': homeTeam,
                                                           'opponent': awayTeam, 'home': 1},
                                                     index=[1])).values[0]
    atAvgGoals = model.predict(pd.DataFrame(data={'team': awayTeam,
                                                           'opponent': homeTeam, 'home': 0},
                                                     index=[1])).values[0]
    FixtureCalculated = [[round(poisson.pmf(i, teamAvg), 1) for i in range(0, maxGoals + 1)] for teamAvg in
                 [htAvgGoals, atAvgGoals]]

    HomeVsAway = pd.DataFrame(np.outer(np.array(FixtureCalculated[0]), np.array(FixtureCalculated[1])), columns=columns, index=index)
    HomeVsAway = HomeVsAway.style.set_table_styles([dict(selector='th', props=[('text-align', 'center')])])
    HomeVsAway.set_properties(**{'text-align': 'center'})

    HomeAwayDraw = {'Home': round(np.sum(np.tril(np.outer(np.array(FixtureCalculated[0]), np.array(FixtureCalculated[1])), -1)), 3),
                    'Draw': round(np.sum(np.diag(np.outer(np.array(FixtureCalculated[0]), np.array(FixtureCalculated[1])))), 3),
                    'Away': round(np.sum(np.triu(np.outer(np.array(FixtureCalculated[0]), np.array(FixtureCalculated[1])), 1)), 3)}

    returnable = [[round(htAvgGoals, 0), round(atAvgGoals, 0)], HomeVsAway,
                  pd.DataFrame(HomeAwayDraw.values(), index=HomeAwayDraw.keys()).T]
    return returnable


def ResultSearchStart(root_frame):
    lower_frame = Frame(root_frame, bg='#4c8a27', bd=2, )
    lower_frame.place(relx=0.5, rely=0.3, relheight=0.2, relwidth=0.8, anchor="n")
    Label(root_frame, text="Enter the home team followed by the away team to make a prediction",
          font="AutobusBold 15 bold", bg="#4c8a27").place(x=200, y=75, width=800)

    def print_selection():
        value = lb.get(lb.curselection())
        HT = value
        Result2(HT, root_frame)

    var2 = tk.StringVar()
    lb = tk.Listbox(lower_frame, listvariable=var2)
    b1 = tk.Button(lower_frame, text='Enter Home Team', font="AutobusBold 15 bold", bg="#add8e6", width=15, height=1,
                   pady=2, padx=10, command=print_selection)
    b1.pack()
    list_items = ['Arsenal', 'Aston Villa', 'Brighton', 'Burnley', 'Chelsea','Crystal Palace', 'Everton', 'Fulham',
                  'Leeds', 'Leicester', 'Liverpool', 'Man City', 'Man United','Newcastle' , 'Sheffield United',
                  'Southampton', 'Tottenham', 'West Brom', 'West Ham','Wolves']
    for item in list_items:
        lb.insert('end', item)
    lb.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)


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
    list_items = ['Arsenal', 'Aston Villa', 'Brighton', 'Burnley', 'Chelsea','Crystal Palace', 'Everton', 'Fulham',
                  'Leeds', 'Leicester', 'Liverpool', 'Man City', 'Man United','Newcastle' , 'Sheffield United',
                  'Southampton', 'Tottenham', 'West Brom', 'West Ham','Wolves']
    for item in list_items:
        lb.insert('end', item)
    lb.pack(padx=5, pady=5, fill=tk.BOTH,
            expand=True)


def ResultSearch(root_frame, HT, AT):
    goals = 5
    goalModel = pd.concat([premier[['HomeTeam', 'AwayTeam', 'FTHG']].assign(home=1).rename(
        columns={'HomeTeam': 'team', 'AwayTeam': 'opponent', 'FTHG': 'goals'}),
        premier[['AwayTeam', 'HomeTeam', 'FTAG']].assign(home=0).rename(
            columns={'AwayTeam': 'team', 'HomeTeam': 'opponent', 'FTAG': 'goals'})])

    poissonModel = smf.glm(formula="goals ~ home + team + opponent",
                            data=goalModel, family=sm.families.Poisson()).fit()
    goals = SimulateMatch(poissonModel, HT, AT, maxGoals=goals)
    lower_frame = Frame(root_frame, bg='#4c8a27', bd=2, )
    lower_frame.place(relx=0.5, rely=0.3, relheight=0.2, relwidth=0.8, anchor="n")
    Label(lower_frame, text="  " + str(HT) + " vs " + str(AT) + "\n" + str(goals[2]), font="AutobusBold 15 bold",
          bg="#add8e6").place(x=375, y=0)
    root_frame.mainloop()
