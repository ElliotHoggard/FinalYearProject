import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.special import factorial
from pandas.plotting import scatter_matrix
import seaborn as sns


def get_result_stats(playing_stats, year):
    return pd.DataFrame(data=[len(playing_stats[playing_stats.FTR == 'H']),
                              len(playing_stats[playing_stats.FTR == 'A']),
                              len(playing_stats[playing_stats.FTR == 'D'])],
                        index=['Home Wins', 'Away Wins', 'Draws'],
                        columns=[year]
                        ).T


def graph1p1():
    leagueData = ['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']

    dat = pd.read_csv('Dat1/Dat121.csv', error_bad_lines=False)
    data = dat.dropna()

    data_ = data[leagueData]

    scores1617 = pd.read_csv("Dat1/Dat117.csv")
    scores1718 = pd.read_csv("Dat1/Dat118.csv")
    scores1819 = pd.read_csv("Dat1/Dat119.csv")
    scores1920 = pd.read_csv("Dat1/Dat120.csv")
    scores2021 = pd.read_csv("Dat1/Dat121.csv")

    sc16 = scores1617[leagueData]
    sc17 = scores1718[leagueData]
    sc18 = scores1819[leagueData]
    sc19 = scores1920[leagueData]
    sc20 = scores2021[leagueData]

    result_stats_agg = get_result_stats(data_, 'Overall')
    result_stats_1 = get_result_stats(sc16, '2016-17')
    result_stats_2 = get_result_stats(sc17, '2017-18')
    result_stats_3 = get_result_stats(sc18, '2018-19')
    result_stats_4 = get_result_stats(sc19, '2019-20')
    result_stats_5 = get_result_stats(sc20, '2020-21')
    result_stats = pd.concat(
        [result_stats_1, result_stats_2, result_stats_3, result_stats_4, result_stats_5, result_stats_agg])

    ax = result_stats.plot(kind='bar', color=['steelblue', 'sandybrown', 'turquoise'], figsize=[16, 7.5],
                           title='Result Statistics for Different Years')
    plt.xticks(rotation=0)
    ax.set_ylabel('Frequency', size=12)
    ax.set_xlabel('Season', size=12)
    plt.show()


def graph2p1():
    leagueData = ['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']
    dat = pd.read_csv('Dat1/Dat121.csv', error_bad_lines=False)
    data = dat.dropna()
    scores1617 = pd.read_csv("Dat1/Dat117.csv")
    scores1718 = pd.read_csv("Dat1/Dat118.csv")
    scores1819 = pd.read_csv("Dat1/Dat119.csv")
    scores1920 = pd.read_csv("Dat1/Dat120.csv")
    scores2021 = pd.read_csv("Dat1/Dat121.csv")

    sc16 = scores1617[leagueData]
    sc17 = scores1718[leagueData]
    sc18 = scores1819[leagueData]
    sc19 = scores1920[leagueData]
    sc20 = scores2021[leagueData]

    result_stats_1 = get_result_stats(sc16, '2016-17')
    result_stats_2 = get_result_stats(sc17, '2017-18')
    result_stats_3 = get_result_stats(sc18, '2018-19')
    result_stats_4 = get_result_stats(sc19, '2019-20')
    result_stats_5 = get_result_stats(sc20, '2020-21')
    result_stats = pd.concat([result_stats_1, result_stats_2, result_stats_3, result_stats_4, result_stats_5])

    ax1 = result_stats.T.plot(kind='bar', color=['steelblue', 'sandybrown', 'turquoise'], figsize=[16, 7.5],
                              title='Aggregate Result Statistics', legend=False)
    plt.xticks(rotation=0)
    ax1.set_ylabel('Frequency', size=12)
    ax1.set_xlabel('Season', size=12)
    plt.show()


def graph3p1():
    leagueData = ['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']
    dat = pd.read_csv('Dat1/Dat121.csv', error_bad_lines=False)
    data = dat.dropna()
    data_ = data[leagueData]
    scores1617 = pd.read_csv("Dat1/Dat117.csv")
    scores1718 = pd.read_csv("Dat1/Dat118.csv")
    scores1819 = pd.read_csv("Dat1/Dat119.csv")
    scores1920 = pd.read_csv("Dat1/Dat120.csv")
    scores2021 = pd.read_csv("Dat1/Dat121.csv")

    sc16 = scores1617[leagueData]
    sc17 = scores1718[leagueData]
    sc18 = scores1819[leagueData]
    sc19 = scores1920[leagueData]
    sc20 = scores2021[leagueData]

    result_stats_agg = get_result_stats(data_, 'Overall')
    result_stats_1 = get_result_stats(sc16, '2016-17')
    result_stats_2 = get_result_stats(sc17, '2017-18')
    result_stats_3 = get_result_stats(sc18, '2018-19')
    result_stats_4 = get_result_stats(sc19, '2019-20')
    result_stats_5 = get_result_stats(sc20, '2020-21')
    result_stats = pd.concat(
        [result_stats_1, result_stats_2, result_stats_3, result_stats_4, result_stats_5, result_stats_agg])
    result_prop = result_stats.T

    for column in result_prop.columns:
        result_prop[column] = (result_prop[column] * 100) / 380

    result_prop.rename(index={'Home Wins': 'Home', 'Away Wins': 'Away', 'Draws': 'Draw'}, inplace=True)
    result_avg_prop = pd.DataFrame((result_prop['2016-17'] + result_prop['2017-18'] + result_prop['2018-19'] +
                                    result_prop['2019-20'] + result_prop['2020-21']) / 5,
                                   columns=['Win Percentage'])

    ax = result_avg_prop.plot(kind='pie', figsize=[6, 6], autopct='%.2f', y='Win Percentage', fontsize=20, labels=None,
                              legend=True, colors=['steelblue', 'sandybrown', 'turquoise'])
    ax.set_title('Aggregate Win Percentage', size=25)
    plt.show()



def graph1p2():
    dat = pd.read_csv('Dat2/Dat2_1920.csv', error_bad_lines=False)
    data = dat.dropna()
    temp = data[data['HomeTeam'] == 'Man City'][['FTHG', 'FTAG', 'HY', 'AY', 'FTR']]
    sns.pairplot(temp, hue='FTR', palette='coolwarm')
    plt.show()

def graph2p2():
    dat = pd.read_csv('Dat2/Dat2_1920.csv', error_bad_lines=False)
    data = dat.dropna()
    temp = data[data['HomeTeam'] == 'Liverpool'][['FTHG', 'FTAG', 'HST', 'AST', 'FTR']]
    sns.pairplot(temp, hue='FTR', palette='coolwarm')
    plt.show()


def graph1p3():
    k = []
    p_k = []
    for i in range(10):
        p_k.append(poisson(i, 2.74) * 100)
        k.append(i)

    fig = plt.figure()
    plt.plot(k, p_k, 'o-')
    plt.xticks(range(10))
    fig.suptitle('Probability of goals in a match', fontsize=25)
    plt.xlabel('Number of goals')
    plt.ylabel('Probability (in percenatge)')
    for x, y in zip(k, p_k):
        label = "{:.2f}".format(y)
        plt.annotate(label, (x, y), textcoords="offset pixels", xytext=(0, 4), ha='left', fontsize=15)
    plt.grid(True)
    plt.show()

def poisson(k, exp_events):
    lam = (exp_events)
    p_k = np.exp(-lam) * np.power(lam, k) / factorial(k)
    return p_k

def graph1p4():
    #home form
    epl = pd.read_csv("Dat1/Dat121.csv", sep=',')
    results = epl.groupby('HomeTeam')['FTR'].value_counts().to_frame()
    results.columns = ['Count']
    sns.set(rc={'figure.figsize': (30, 10)})

    ax = sns.countplot(x="HomeTeam", data=epl, hue="FTR", hue_order=['H', 'A', 'D'],
                       saturation=.65)
    ax.set_title("Number of Wins, Draws, and Losses for Each Team", fontsize=20)
    ax.set_xlabel('')
    ax.set_ylabel('Count', fontsize=12)
    ax.tick_params(labelsize=12)
    plt.show()

def graph2p4():
    #away form
    epl = pd.read_csv("Dat1/Dat121.csv", sep=',')
    results = epl.groupby('AwayTeam')['FTR'].value_counts().to_frame()
    results.columns = ['Count']
    sns.set(rc={'figure.figsize': (30, 10)})

    ax = sns.countplot(x="AwayTeam", data=epl, hue="FTR", hue_order=['H', 'A', 'D'],
                       saturation=.65)
    ax.set_title("Number of Wins, Draws, and Losses for Each Team", fontsize=20)
    ax.set_xlabel('')
    ax.set_ylabel('Count', fontsize=12)
    ax.tick_params(labelsize=12)
    plt.show()


