import time
from tkinter import *
import numpy as np
import numpy.random as nr
import pandas as pd
from aaa.modelanalysis import game_menu_frame2
from selenium import webdriver
from os import listdir
# variables
global nums
nums = 10000

Filepath = ['./Dat1/' + f for f in listdir("./Dat1") if f.endswith('.csv')]
premier = pd.concat(map(pd.read_csv, Filepath), ignore_index=True, sort=False)

leagueData = pd.DataFrame(premier, columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

MCIHome = leagueData.loc[leagueData['HomeTeam'] == 'Man City']
MCIAway = leagueData.loc[leagueData['AwayTeam'] == 'Man City']
MCIHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
MCIAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
MCIOMean = MCIHome["Offence"].mean() + MCIAway["Offence"].mean()
MCIDMean = MCIHome["Defence"].mean() + MCIAway["Defence"].mean()
MCIOGoals = MCIHome["Offence"].append(MCIAway["Offence"])
MCIDGoals = MCIHome["Defence"].append(MCIAway["Defence"])

MUNHome = leagueData.loc[leagueData['HomeTeam'] == 'Man United']
MUNAway = leagueData.loc[leagueData['AwayTeam'] == 'Man United']
MUNHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
MUNAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
MUNOMean = MUNHome["Offence"].mean() + MUNAway["Offence"].mean()
MUNDMean = MUNHome["Defence"].mean() + MUNAway["Defence"].mean()
MUNOGoals = MUNHome["Offence"].append(MUNAway["Offence"])
MUNDGoals = MUNHome["Defence"].append(MUNAway["Defence"])

LEIHome = leagueData.loc[leagueData['HomeTeam'] == 'Leicester']
LEIAway = leagueData.loc[leagueData['AwayTeam'] == 'Leicester']
LEIHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
LEIAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
LEIOMean = LEIHome["Offence"].mean() + LEIAway["Offence"].mean()
LEIDMean = LEIHome["Defence"].mean() + LEIAway["Defence"].mean()
LEIOGoals = LEIHome["Offence"].append(LEIAway["Offence"])
LEIDGoals = LEIHome["Defence"].append(LEIAway["Defence"])

CHEHome = leagueData.loc[leagueData['HomeTeam'] == 'Chelsea']
CHEAway = leagueData.loc[leagueData['AwayTeam'] == 'Chelsea']
CHEHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
CHEAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
CHEOMean = CHEHome["Offence"].mean() + CHEAway["Offence"].mean()
CHEDMean = CHEHome["Defence"].mean() + CHEAway["Defence"].mean()
CHEOGoals = CHEHome["Offence"].append(CHEAway["Offence"])
CHEDGoals = CHEHome["Defence"].append(CHEAway["Defence"])

WHUHome = leagueData.loc[leagueData['HomeTeam'] == 'West Ham']
WHUAway = leagueData.loc[leagueData['AwayTeam'] == 'West Ham']
WHUHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
WHUAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
WHUOMean = WHUHome["Offence"].mean() + WHUAway["Offence"].mean()
WHUDMean = WHUHome["Defence"].mean() + WHUAway["Defence"].mean()
WHUOGoals = WHUHome["Offence"].append(WHUAway["Offence"])
WHUDGoals = WHUHome["Defence"].append(WHUAway["Defence"])

TOTHome = leagueData.loc[leagueData['HomeTeam'] == 'Tottenham']
TOTAway = leagueData.loc[leagueData['AwayTeam'] == 'Tottenham']
TOTHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
TOTAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
TOTOMean = TOTHome["Offence"].mean() + TOTAway["Offence"].mean()
TOTDMean = TOTHome["Defence"].mean() + TOTAway["Defence"].mean()
TOTOGoals = TOTHome["Offence"].append(TOTAway["Offence"])
TOTDGoals = TOTHome["Defence"].append(TOTAway["Defence"])

LIVHome = leagueData.loc[leagueData['HomeTeam'] == 'Liverpool']
LIVAway = leagueData.loc[leagueData['AwayTeam'] == 'Liverpool']
LIVHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
LIVAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
LIVOMean = LIVHome["Offence"].mean() + LIVAway["Offence"].mean()
LIVDMean = LIVHome["Defence"].mean() + LIVAway["Defence"].mean()
LIVOGoals = LIVHome["Offence"].append(LIVAway["Offence"])
LIVDGoals = LIVHome["Defence"].append(LIVAway["Defence"])

EVEHome = leagueData.loc[leagueData['HomeTeam'] == 'Everton']
EVEAway = leagueData.loc[leagueData['AwayTeam'] == 'Everton']
EVEHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
EVEAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
EVEOMean = EVEHome["Offence"].mean() + EVEAway["Offence"].mean()
EVEDMean = EVEHome["Defence"].mean() + EVEAway["Defence"].mean()
EVEOGoals = EVEHome["Offence"].append(EVEAway["Offence"])
EVEDGoals = EVEHome["Defence"].append(EVEAway["Defence"])

ARSHome = leagueData.loc[leagueData['HomeTeam'] == 'Arsenal']
ARSAway = leagueData.loc[leagueData['AwayTeam'] == 'Arsenal']
ARSHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
ARSAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
ARSOMean = ARSHome["Offence"].mean() + ARSAway["Offence"].mean()
ARSDMean = ARSHome["Defence"].mean() + ARSAway["Defence"].mean()
ARSOGoals = ARSHome["Offence"].append(ARSAway["Offence"])
ARSDGoals = ARSHome["Defence"].append(ARSAway["Defence"])

AVLHome = leagueData.loc[leagueData['HomeTeam'] == 'Aston Villa']
AVLAway = leagueData.loc[leagueData['AwayTeam'] == 'Aston Villa']
AVLHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
AVLAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
AVLOMean = AVLHome["Offence"].mean() + AVLAway["Offence"].mean()
AVLDMean = AVLHome["Defence"].mean() + AVLAway["Defence"].mean()
AVLOGoals = AVLHome["Offence"].append(AVLAway["Offence"])
AVLDGoals = AVLHome["Defence"].append(AVLAway["Defence"])

LEEHome = leagueData.loc[leagueData['HomeTeam'] == 'Leeds']
LEEAway = leagueData.loc[leagueData['AwayTeam'] == 'Leeds']
LEEHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
LEEAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
LEEOMean = LEEHome["Offence"].mean() + LEEAway["Offence"].mean()
LEEDMean = LEEHome["Defence"].mean() + LEEAway["Defence"].mean()
LEEOGoals = LEEHome["Offence"].append(LEEAway["Offence"])
LEEDGoals = LEEHome["Defence"].append(LEEAway["Defence"])

CRYHome = leagueData.loc[leagueData['HomeTeam'] == 'Crystal Palace']
CRYAway = leagueData.loc[leagueData['AwayTeam'] == 'Crystal Palace']
CRYHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
CRYAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
CRYOMean = CRYHome["Offence"].mean() + CRYAway["Offence"].mean()
CRYDMean = CRYHome["Defence"].mean() + CRYAway["Defence"].mean()
CRYOGoals = CRYHome["Offence"].append(CRYAway["Offence"])
CRYDGoals = CRYHome["Defence"].append(CRYAway["Defence"])

WOLHome = leagueData.loc[leagueData['HomeTeam'] == 'Wolves']
WOLAway = leagueData.loc[leagueData['AwayTeam'] == 'Wolves']
WOLHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
WOLAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
WOLOMean = WOLHome["Offence"].mean() + WOLAway["Offence"].mean()
WOLDMean = WOLHome["Defence"].mean() + WOLAway["Defence"].mean()
WOLOGoals = WOLHome["Offence"].append(WOLAway["Offence"])
WOLDGoals = WOLHome["Defence"].append(WOLAway["Defence"])

SOUHome = leagueData.loc[leagueData['HomeTeam'] == 'Southampton']
SOUAway = leagueData.loc[leagueData['AwayTeam'] == 'Southampton']
SOUHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
SOUAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
SOUOMean = SOUHome["Offence"].mean() + SOUAway["Offence"].mean()
SOUDMean = SOUHome["Defence"].mean() + SOUAway["Defence"].mean()
SOUOGoals = SOUHome["Offence"].append(SOUAway["Offence"])
SOUDGoals = SOUHome["Defence"].append(SOUAway["Defence"])

BURHome = leagueData.loc[leagueData['HomeTeam'] == 'Burnley']
BURAway = leagueData.loc[leagueData['AwayTeam'] == 'Burnley']
BURHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
BURAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
BUROMean = BURHome["Offence"].mean() + BURAway["Offence"].mean()
BURDMean = BURHome["Defence"].mean() + BURAway["Defence"].mean()
BUROGoals = BURHome["Offence"].append(BURAway["Offence"])
BURDGoals = BURHome["Defence"].append(BURAway["Defence"])

BRIHome = leagueData.loc[leagueData['HomeTeam'] == 'Brighton']
BRIAway = leagueData.loc[leagueData['AwayTeam'] == 'Brighton']
BRIHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
BRIAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
BRIOMean = BRIHome["Offence"].mean() + BRIAway["Offence"].mean()
BRIDMean = BRIHome["Defence"].mean() + BRIAway["Defence"].mean()
BRIOGoals = BRIHome["Offence"].append(BRIAway["Offence"])
BRIDGoals = BRIHome["Defence"].append(BRIAway["Defence"])

NEWHome = leagueData.loc[leagueData['HomeTeam'] == 'Newcastle']
NEWAway = leagueData.loc[leagueData['AwayTeam'] == 'Newcastle']
NEWHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
NEWAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
NEWOMean = NEWHome["Offence"].mean() + NEWAway["Offence"].mean()
NEWDMean = NEWHome["Defence"].mean() + NEWAway["Defence"].mean()
NEWOGoals = NEWHome["Offence"].append(NEWAway["Offence"])
NEWDGoals = NEWHome["Defence"].append(NEWAway["Defence"])

FULHome = leagueData.loc[leagueData['HomeTeam'] == 'Fulham']
FULAway = leagueData.loc[leagueData['AwayTeam'] == 'Fulham']
FULHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
FULAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
FULOMean = FULHome["Offence"].mean() + FULAway["Offence"].mean()
FULDMean = FULHome["Defence"].mean() + FULAway["Defence"].mean()
FULOGoals = FULHome["Offence"].append(FULAway["Offence"])
FULDGoals = FULHome["Defence"].append(FULAway["Defence"])

WBAHome = leagueData.loc[leagueData['HomeTeam'] == 'West Brom']
WBAAway = leagueData.loc[leagueData['AwayTeam'] == 'West Brom']
WBAHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
WBAAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
WBAOMean = WBAHome["Offence"].mean() + WBAAway["Offence"].mean()
WBADMean = WBAHome["Defence"].mean() + WBAAway["Defence"].mean()
WBAOGoals = WBAHome["Offence"].append(WBAAway["Offence"])
WBADGoals = WBAHome["Defence"].append(WBAAway["Defence"])

SHUHome = leagueData.loc[leagueData['HomeTeam'] == 'Sheffield United']
SHUAway = leagueData.loc[leagueData['AwayTeam'] == 'Sheffield United']
SHUHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
SHUAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
SHUOMean = SHUHome["Offence"].mean() + SHUAway["Offence"].mean()
SHUDMean = SHUHome["Defence"].mean() + SHUAway["Defence"].mean()
SHUOGoals = SHUHome["Offence"].append(SHUAway["Offence"])
SHUDGoals = SHUHome["Defence"].append(SHUAway["Defence"])

AVGHome = leagueData.loc[leagueData['FTHG']]
AVGAway = leagueData.loc[leagueData['FTAG']]
AVGHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
AVGAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
AVGOMean = AVGHome["Offence"].mean() + AVGAway["Offence"].mean()
AVGDMean = AVGHome["Defence"].mean() + AVGHome["Defence"].mean()
AVGOMean = float(AVGOMean)
AVGHGoals = AVGHome["Offence"]
AVGAGoals = AVGAway["Offence"]

# GW 31
def NewWhu1():
    NEWBalancedMean = np.mean([NEWOGoals.mean(), WHUDGoals.mean()])
    WHUBalancedMean = np.mean([WHUOGoals.mean(), NEWDGoals.mean()])
    q = 2
    sim_poissonNEWWHU(nums, NEWBalancedMean.mean(), WHUBalancedMean.mean())
    distA, distB = sim_poissonNEWWHU(10000)
    winPercent(distA, distB, q)


def sim_poissonNEWWHU(nums, mean1=NEWOGoals.mean() + WHUDGoals.mean(), mean2=WHUOGoals.mean() + NEWDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def WolShu1():
    WOLBalancedMean = np.mean([WOLOGoals.mean(), SHUDGoals.mean()])
    SHUBalancedMean = np.mean([SHUOGoals.mean(), WOLDGoals.mean()])
    q = 3
    sim_poissonWOLSHU(nums, WOLBalancedMean.mean(), SHUBalancedMean.mean())
    distA, distB = sim_poissonWOLSHU(10000)
    winPercent(distA, distB, q)


def sim_poissonWOLSHU(nums, mean1=WOLOGoals.mean() + SHUDGoals.mean(), mean2=SHUOGoals.mean() + WOLDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)

def ArsFul1():
    ARSBalancedMean = np.mean([ARSOGoals.mean(), FULDGoals.mean()])
    FULBalancedMean = np.mean([FULOGoals.mean(), ARSDGoals.mean()])
    q = 4
    sim_poissonARSFUL(nums, ARSBalancedMean.mean(), FULBalancedMean.mean())
    distA, distB = sim_poissonARSFUL(10000)
    winPercent(distA, distB, q)


def sim_poissonARSFUL(nums, mean1=ARSOGoals.mean() + FULDGoals.mean(), mean2=FULOGoals.mean() + ARSDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)

def MunBur1():
    MUNBalancedMean = np.mean([MUNOGoals.mean(), BURDGoals.mean()])
    BURBalancedMean = np.mean([BUROGoals.mean(), MUNDGoals.mean()])
    q = 5
    sim_poissonMUNBUR(nums, MUNBalancedMean.mean(), BURBalancedMean.mean())
    distA, distB = sim_poissonMUNBUR(10000)
    winPercent(distA, distB, q)


def sim_poissonMUNBUR(nums, mean1=MUNOGoals.mean() + BURDGoals.mean(), mean2=BUROGoals.mean() + MUNDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)



def LeeLiv1():
    LEEBalancedMean = np.mean([LEEOGoals.mean(), LIVDGoals.mean()])
    LIVBalancedMean = np.mean([LIVOGoals.mean(), LEEDGoals.mean()])
    q = 6
    sim_poissonLEELIV(nums, LEEBalancedMean.mean(), LIVBalancedMean.mean())
    distA, distB = sim_poissonLEELIV(10000)
    winPercent(distA, distB, q)


def sim_poissonLEELIV(nums, mean1=LEEOGoals.mean() + LIVDGoals.mean(), mean2=LIVOGoals.mean() + LEEDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def CheBri1():
    CHEBalancedMean = np.mean([CHEOGoals.mean(), BRIDGoals.mean()])
    BRIBalancedMean = np.mean([BRIOGoals.mean(), CHEDGoals.mean()])
    q = 7
    sim_poissonCHEBRI(nums, CHEBalancedMean.mean(), BRIBalancedMean.mean())
    distA, distB = sim_poissonCHEBRI(10000)
    winPercent(distA, distB, q)


def sim_poissonCHEBRI(nums, mean1=CHEOGoals.mean() + BRIDGoals.mean(), mean2=BRIOGoals.mean() + CHEDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def TotSou1():
    TOTBalancedMean = np.mean([TOTOGoals.mean(), SOUDGoals.mean()])
    SOUBalancedMean = np.mean([SOUOGoals.mean(), TOTDGoals.mean()])
    q = 8
    sim_poissonTOTSOU(nums, TOTBalancedMean.mean(), SOUBalancedMean.mean())
    distA, distB = sim_poissonTOTSOU(10000)
    winPercent(distA, distB, q)


def sim_poissonTOTSOU(nums, mean1=TOTOGoals.mean() + SOUDGoals.mean(), mean2=SOUOGoals.mean() + TOTDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)

def AvlMci1():
    AVLBalancedMean1 = np.mean([AVLOGoals.mean(), MCIDGoals.mean()])
    MCIBalancedMean1 = np.mean([MCIOGoals.mean(), AVLDGoals.mean()])
    q = 9
    sim_poissonAVLMCI(nums, AVLBalancedMean1.mean(), MCIBalancedMean1.mean())
    distA, distB = sim_poissonAVLMCI(10000)
    winPercent(distA, distB, q)


def sim_poissonAVLMCI(nums, mean1=AVLOGoals.mean() + MCIDGoals.mean(), mean2=MCIOGoals.mean() + AVLDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)



# Calculates the win percentage
def winPercent(distA, distB, q):
    WinTeam1 = 0
    WinTeam2 = 0
    Draw = 0
    global Team1WinPercent
    global Team2WinPercent
    global DrawPercent
    for x, y in zip(distA, distB):
        if x > y:
            WinTeam1 += 1
        if y > x:
            WinTeam2 += 1
        if x == y:
            Draw += 1
    TotalGames = WinTeam1 + WinTeam2 + Draw
    Team1WinPercent = WinTeam1 / TotalGames * 100
    Team2WinPercent = WinTeam2 / TotalGames * 100
    DrawPercent = Draw / TotalGames * 100

    game_menu_frame2.place(relx=0.5, rely=0.15, relheight=0.8, relwidth=0.9, anchor='n')
    TipicoFirstGame(game_menu_frame2, q)


def TipicoFirstGame(game_menu_frame2, q):
    driver_path = r"C:\Users\ellio\Downloads\chromedriver.exe"
    brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    browser = webdriver.Chrome(executable_path=driver_path, options=option)
    browser.get("file:///C:/Users/ellio/Downloads/Tipico32.html")

    col_names = ['Tipp 1', 'Tipp X', 'Tipp 2']
    lst_odds_tipp1 = []
    lst_odds_tippX = []
    lst_odds_tipp2 = []

    time.sleep(3)
    for i in range(1, 10):
        odds_tipp1 = browser.find_element_by_xpath('/html/body/div[1]/main/main/section/div/div/div[2]/div/a[' + str(
            q) + ']/div[3]/div/div/button[1]/span').text
        odds_tippX = browser.find_element_by_xpath('/html/body/div[1]/main/main/section/div/div/div[2]/div/a[' + str(
            q) + ']/div[3]/div/div/button[2]/span').text
        odds_tipp2 = browser.find_element_by_xpath('/html/body/div[1]/main/main/section/div/div/div[2]/div/a[' + str(
            q) + ']/div[3]/div/div/button[3]/span').text
        lst_odds_tipp1.append(odds_tipp1)
        lst_odds_tippX.append(odds_tippX)
        lst_odds_tipp2.append(odds_tipp2)

    df = pd.DataFrame(np.column_stack([lst_odds_tipp1, lst_odds_tippX, lst_odds_tipp2]),
                      columns=col_names)
    df.style.hide_index()

    if q == 2:
        col = 1
        row2 = 2
        HomeWin = df.loc[0, 'Tipp 1']
        HomeWinP1 = int(HomeWin[0])
        HomeWinP2 = int(HomeWin[2:4])
        HomeWinP2New = HomeWinP2 / 100
        HomeFinal = HomeWinP1 + HomeWinP2New
        HomeSub1 = 1 / HomeFinal
        HomeFinalNew = HomeSub1 * 100

        AwayWin = df.loc[0, 'Tipp 2']
        AwayWinP1 = int(AwayWin[0])
        AwayWinP2 = int(AwayWin[2:4])
        AwayWinP2New = AwayWinP2 / 100
        AwayFinal = AwayWinP1 + AwayWinP2New
        AwaySub1 = 1 / AwayFinal
        AwayFinalNew = AwaySub1 * 100

        Draw = df.loc[0, 'Tipp X']
        DrawP1 = int(Draw[0])
        DrawP2 = int(Draw[2:4])
        DrawP2New = DrawP2 / 100
        DrawFinal = DrawP1 + DrawP2New
        DrawSub1 = 1 / DrawFinal
        DrawFinalNew = DrawSub1 * 100

        Label(game_menu_frame2, text="Newcastle vs West Ham", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's Probability ").place(x=30, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(x=30,
                                                                                                      y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(
            x=30, y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=30, y=175)

        if Team1WinPercent > HomeFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=30, y=200)
        elif Team2WinPercent > AwayFinalNew + 5:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=30, y=200)
        elif DrawPercent > DrawFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a draw").place(x=30, y=200)

        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=30, y=200)

        NEWBalancedMean = np.mean([NEWOGoals.mean(), WHUDGoals.mean()])
        WHUBalancedMean = np.mean([WHUOGoals.mean(), NEWDGoals.mean()])
        roundedNEW = round(NEWBalancedMean)
        roundedWHU = round(WHUBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Newcastle " + str(roundedNEW) + " : " + str(
                  roundedWHU) + " West Ham").place(x=30, y=50)
        Betway(game_menu_frame2, q, col, row2)

    if q == 3:
        col = 2
        row2 = 2
        HomeWin = df.loc[0, 'Tipp 1']
        HomeWinP1 = int(HomeWin[0])
        HomeWinP2 = int(HomeWin[2:4])
        HomeWinP2New = HomeWinP2 / 100
        HomeFinal = HomeWinP1 + HomeWinP2New
        HomeSub1 = 1 / HomeFinal
        HomeFinalNew = HomeSub1 * 100

        AwayWin = df.loc[0, 'Tipp 2']
        AwayWinP1 = int(AwayWin[0])
        AwayWinP2 = int(AwayWin[2:4])
        AwayWinP2New = AwayWinP2 / 100
        AwayFinal = AwayWinP1 + AwayWinP2New
        AwaySub1 = 1 / AwayFinal
        AwayFinalNew = AwaySub1 * 100

        Draw = df.loc[0, 'Tipp X']
        DrawP1 = int(Draw[0])
        DrawP2 = int(Draw[2:4])
        DrawP2New = DrawP2 / 100
        DrawFinal = DrawP1 + DrawP2New
        DrawSub1 = 1 / DrawFinal
        DrawFinalNew = DrawSub1 * 100

        Label(game_menu_frame2, text="Wolves vs Sheffield", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's Probability ").place(x=30, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(x=30,
                                                                                                      y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(x=30,
                                                                                                      y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=30, y=175)

        if Team1WinPercent > HomeFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=30, y=200)
        elif Team2WinPercent > AwayFinalNew + 10:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=30, y=200)
        elif DrawPercent > DrawFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a Draw").place(x=30, y=200)
        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=30, y=200)

        WOLBalancedMean = np.mean([WOLOGoals.mean(), SHUDGoals.mean()])
        SHUBalancedMean = np.mean([SHUOGoals.mean(), WOLDGoals.mean()])
        roundedSHU = round(SHUBalancedMean)
        roundedWOL = round(WOLBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Wolves " + str(roundedWOL) + " : " + str(
                  roundedSHU) + " Sheffield").place(x=30, y=50)
        Betway(game_menu_frame2, q, col, row2)

    if q == 4:
        col = 1
        row2 = 3
        HomeWin = df.loc[0, 'Tipp 1']
        HomeWinP1 = int(HomeWin[0])
        HomeWinP2 = int(HomeWin[2:4])
        HomeWinP2New = HomeWinP2 / 100
        HomeFinal = HomeWinP1 + HomeWinP2New
        HomeSub1 = 1 / HomeFinal
        HomeFinalNew = HomeSub1 * 100

        AwayWin = df.loc[0, 'Tipp 2']
        AwayWinP1 = int(AwayWin[0])
        AwayWinP2 = int(AwayWin[2:4])
        AwayWinP2New = AwayWinP2 / 100
        AwayFinal = AwayWinP1 + AwayWinP2New
        AwaySub1 = 1 / AwayFinal
        AwayFinalNew = AwaySub1 * 100

        Draw = df.loc[0, 'Tipp X']
        DrawP1 = int(Draw[0])
        DrawP2 = int(Draw[2:4])
        DrawP2New = DrawP2 / 100
        DrawFinal = DrawP1 + DrawP2New
        DrawSub1 = 1 / DrawFinal
        DrawFinalNew = DrawSub1 * 100

        Label(game_menu_frame2, text="Arsenal vs Fulham", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's Probability ").place(x=30, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(x=30,
                                                                                                      y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(
            x=30, y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=30, y=175)

        if Team1WinPercent > HomeFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=30, y=200)
        elif Team2WinPercent > AwayFinalNew + 10:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=30, y=200)
        elif DrawPercent > DrawFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a draw").place(x=30, y=200)
        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=30, y=200)

        ARSBalancedMean = np.mean([ARSOGoals.mean(), FULDGoals.mean()])
        FULBalancedMean = np.mean([FULOGoals.mean(), ARSDGoals.mean()])
        roundedARS = round(ARSBalancedMean)
        roundedFUL = round(FULBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Arsenal " + str(roundedARS) + " : " + str(roundedFUL) + " Fulham").place(
            x=30, y=50)

        Betway(game_menu_frame2, q, col, row2)

    if q == 5:
        col = 2
        row2 = 3
        HomeWin = df.loc[0, 'Tipp 1']
        HomeWinP1 = int(HomeWin[0])
        HomeWinP2 = int(HomeWin[2:4])
        HomeWinP2New = HomeWinP2 / 100
        HomeFinal = HomeWinP1 + HomeWinP2New
        HomeSub1 = 1 / HomeFinal
        HomeFinalNew = HomeSub1 * 100

        AwayWin = df.loc[0, 'Tipp 2']
        AwayWinP1 = int(AwayWin[0])
        AwayWinP2 = int(AwayWin[2:4])
        AwayWinP2New = AwayWinP2 / 100
        AwayFinal = AwayWinP1 + AwayWinP2New
        AwaySub1 = 1 / AwayFinal
        AwayFinalNew = AwaySub1 * 100

        Draw = df.loc[0, 'Tipp X']
        DrawP1 = int(Draw[0])
        DrawP2 = int(Draw[2:4])
        DrawP2New = DrawP2 / 100
        DrawFinal = DrawP1 + DrawP2New
        DrawSub1 = 1 / DrawFinal
        DrawFinalNew = DrawSub1 * 100

        Label(game_menu_frame2, text="Man United vs Burnley", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's Probability ").place(x=30, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(
            x=30, y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(x=30,
                                                                                                      y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=30, y=175)

        if Team1WinPercent > HomeFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=30, y=200)
        elif Team2WinPercent > AwayFinalNew + 10:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=30, y=200)
        elif DrawPercent > DrawFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a draw").place(x=30, y=200)
        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=30, y=200)


        MUNBalancedMean = np.mean([MUNOGoals.mean(), BURDGoals.mean()])
        BURBalancedMean = np.mean([BUROGoals.mean(), MUNDGoals.mean()])


        roundedMUN = round(MUNBalancedMean)
        roundedBUR = round(BURBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Man United " + str(roundedMUN) + " : " + str(roundedBUR) + " Burnley").place(
            x=30, y=50)
        Betway(game_menu_frame2, q, col, row2)

    if q == 6:
        col = 1
        row2 = 4

        HomeWin = df.loc[0, 'Tipp 1']
        HomeWinP1 = int(HomeWin[0])
        HomeWinP2 = int(HomeWin[2:4])
        HomeWinP2New = HomeWinP2 / 100
        HomeFinal = HomeWinP1 + HomeWinP2New
        HomeSub1 = 1 / HomeFinal
        HomeFinalNew = HomeSub1 * 100

        AwayWin = df.loc[0, 'Tipp 2']
        AwayWinP1 = int(AwayWin[0])
        AwayWinP2 = int(AwayWin[2:4])
        AwayWinP2New = AwayWinP2 / 100
        AwayFinal = AwayWinP1 + AwayWinP2New
        AwaySub1 = 1 / AwayFinal
        AwayFinalNew = AwaySub1 * 100

        Draw = df.loc[0, 'Tipp X']
        DrawP1 = int(Draw[0])
        DrawP2 = int(Draw[2:4])
        DrawP2New = DrawP2 / 100
        DrawFinal = DrawP1 + DrawP2New
        DrawSub1 = 1 / DrawFinal
        DrawFinalNew = DrawSub1 * 100

        Label(game_menu_frame2, text="Leeds vs Liverpool", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's Probability ").place(x=30, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(x=30, y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(x=30, y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=30, y=175)

        if Team1WinPercent > HomeFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=30, y=200)
        elif Team2WinPercent > AwayFinalNew + 10:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=30, y=200)
        elif DrawPercent > DrawFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a draw").place(x=30, y=200)
        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=30, y=200)

        LEEBalancedMean = np.mean([LEEOGoals.mean(), LIVDGoals.mean()])
        LIVBalancedMean = np.mean([LIVOGoals.mean(), LEEDGoals.mean()])
        roundedLEE = round(LEEBalancedMean)
        roundedLIV = round(LIVBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Leeds " + str(roundedLEE) + " : " + str(
                  roundedLIV) + " Liverpool").place(x=30, y=50)
        Betway(game_menu_frame2, q, col, row2)

    if q == 7:
        col = 1
        row2 = 5
        HomeWin = df.loc[0, 'Tipp 1']
        HomeWinP1 = int(HomeWin[0])
        HomeWinP2 = int(HomeWin[2:4])
        HomeWinP2New = HomeWinP2 / 100
        HomeFinal = HomeWinP1 + HomeWinP2New
        HomeSub1 = 1 / HomeFinal
        HomeFinalNew = HomeSub1 * 100

        AwayWin = df.loc[0, 'Tipp 2']
        AwayWinP1 = int(AwayWin[0])
        AwayWinP2 = int(AwayWin[2:4])
        AwayWinP2New = AwayWinP2 / 100
        AwayFinal = AwayWinP1 + AwayWinP2New
        AwaySub1 = 1 / AwayFinal
        AwayFinalNew = AwaySub1 * 100

        Draw = df.loc[0, 'Tipp X']
        DrawP1 = int(Draw[0])
        DrawP2 = int(Draw[2:4])
        DrawP2New = DrawP2 / 100
        DrawFinal = DrawP1 + DrawP2New
        DrawSub1 = 1 / DrawFinal
        DrawFinalNew = DrawSub1 * 100

        Label(game_menu_frame2, text="Chelsea vs Brighton", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's Probability ").place(x=30, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(x=30, y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(x=30, y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=30, y=175)

        if Team1WinPercent > HomeFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=30, y=200)
        elif Team2WinPercent > AwayFinalNew + 10:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=30, y=200)
        elif DrawPercent > DrawFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a draw").place(x=30, y=200)
        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=30, y=200)

        CHEBalancedMean = np.mean([CHEOGoals.mean(), BRIDGoals.mean()])
        BRIBalancedMean = np.mean([BRIOGoals.mean(), CHEDGoals.mean()])
        roundedCHE = round(CHEBalancedMean)
        roundedBRI = round(BRIBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Chelsea " + str(roundedCHE) + " : " + str(roundedBRI) + " Brighton").place(
            x=30, y=50)
        Betway(game_menu_frame2, q, col, row2)

    if q == 8:
        col = 1
        row2 = 6
        HomeWin = df.loc[0, 'Tipp 1']
        HomeWinP1 = int(HomeWin[0])
        HomeWinP2 = int(HomeWin[2:4])
        HomeWinP2New = HomeWinP2 / 100
        HomeFinal = HomeWinP1 + HomeWinP2New
        HomeSub1 = 1 / HomeFinal
        HomeFinalNew = HomeSub1 * 100

        AwayWin = df.loc[0, 'Tipp 2']
        AwayWinP1 = int(AwayWin[0])
        AwayWinP2 = int(AwayWin[2:4])
        AwayWinP2New = AwayWinP2 / 100
        AwayFinal = AwayWinP1 + AwayWinP2New
        AwaySub1 = 1 / AwayFinal
        AwayFinalNew = AwaySub1 * 100

        Draw = df.loc[0, 'Tipp X']
        DrawP1 = int(Draw[0])
        DrawP2 = int(Draw[2:4])
        DrawP2New = DrawP2 / 100
        DrawFinal = DrawP1 + DrawP2New
        DrawSub1 = 1 / DrawFinal
        DrawFinalNew = DrawSub1 * 100

        Label(game_menu_frame2, text="Tottenham vs Southampton", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's Probability ").place(x=30, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(x=30, y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(x=30, y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=30, y=175)

        if Team1WinPercent > HomeFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=30, y=200)
        elif Team2WinPercent > AwayFinalNew + 10:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=30, y=200)
        elif DrawPercent > DrawFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a draw").place(x=30, y=200)
        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=30, y=200)

        TOTBalancedMean = np.mean([TOTOGoals.mean(), SOUDGoals.mean()])
        SOUBalancedMean = np.mean([SOUOGoals.mean(), TOTDGoals.mean()])
        roundedTOT = round(TOTBalancedMean)
        roundedSOU = round(SOUBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Tottenham " + str(roundedTOT) + " : " + str(
                  roundedSOU) + " Southampton").place(x=30, y=50)
        Betway(game_menu_frame2, q, col, row2)


    if q == 9:
        col = 2
        row2 = 6
        HomeWin = df.loc[0, 'Tipp 1']
        HomeWinP1 = int(HomeWin[0])
        HomeWinP2 = int(HomeWin[2:4])
        HomeWinP2New = HomeWinP2 / 100
        HomeFinal = HomeWinP1 + HomeWinP2New
        HomeSub1 = 1 / HomeFinal
        HomeFinalNew = HomeSub1 * 100

        AwayWin = df.loc[0, 'Tipp 2']
        AwayWinP1 = int(AwayWin[0])
        AwayWinP2 = int(AwayWin[2:4])
        AwayWinP2New = AwayWinP2 / 100
        AwayFinal = AwayWinP1 + AwayWinP2New
        AwaySub1 = 1 / AwayFinal
        AwayFinalNew = AwaySub1 * 100

        Draw = df.loc[0, 'Tipp X']
        DrawP1 = int(Draw[0])
        DrawP2 = int(Draw[2:4])
        DrawP2New = DrawP2 / 100
        DrawFinal = DrawP1 + DrawP2New
        DrawSub1 = 1 / DrawFinal
        DrawFinalNew = DrawSub1 * 100

        Label(game_menu_frame2, text="Aston Villa vs Man City", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's Probability ").place(x=30, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(x=30, y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(x=30, y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=30, y=175)

        if Team1WinPercent > HomeFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=30, y=200)
        elif Team2WinPercent > AwayFinalNew + 10:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=30, y=200)
        elif DrawPercent > DrawFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a draw").place(x=30, y=200)
        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=30, y=200)

        AVLBalancedMean = np.mean([AVLOGoals.mean(), MCIDGoals.mean()])
        MCIBalancedMean = np.mean([MCIOGoals.mean(), AVLDGoals.mean()])
        roundedAVL = round(AVLBalancedMean)
        roundedMCI = round(MCIBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Aston Villa " + str(roundedAVL) + " : " + str(
                  roundedMCI) + " Man City").place(x=30, y=50)
        Betway(game_menu_frame2, q, col, row2)



def ModelOutput(game_menu_frame2):
    Label(game_menu_frame2, text="Our Probability").place(x=250, y=100)
    Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(Team1WinPercent))) + "%").place(x=250, y=125)
    Label(game_menu_frame2, text="Away wins: " + str(float("{0:.2f}".format(Team2WinPercent))) + "%").place(x=250,
                                                                                                            y=150)
    Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawPercent))) + "%").place(x=250, y=175)
    game_menu_frame2.mainloop()


def Betway(game_menu_frame2, q, col, row2):
    driver_path = r"C:\Users\ellio\Downloads\chromedriver.exe"
    brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    browser = webdriver.Chrome(executable_path=driver_path, options=option)
    browser.get("file:///C:/Users/ellio/OneDrive/Documents/AA Project/aaa/BetwayWebsite/betway32.html")

    col_names = ['Home', 'Draw', 'Away']

    lst_odds_tipp1 = []
    lst_odds_tippX = []
    lst_odds_tipp2 = []

    time.sleep(3)

    for i in range(1, 10):
        odds_tipp1 = browser.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/div/div['+ str(row2)+']/div[2]/div/div['+ str(col)+']/article/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[4]/div').text
        odds_tippX = browser.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/div/div['+ str(row2)+']/div[2]/div/div['+ str(col)+']/article/div[1]/div[2]/div/div/div[2]/div/div[2]/div[3]/div/div[4]/div').text
        odds_tipp2 = browser.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/div/div['+ str(row2)+']/div[2]/div/div['+ str(col)+']/article/div[1]/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[4]/div').text

        lst_odds_tipp1.append(odds_tipp1)
        lst_odds_tippX.append(odds_tippX)
        lst_odds_tipp2.append(odds_tipp2)

    df = pd.DataFrame(np.column_stack([lst_odds_tipp1, lst_odds_tippX, lst_odds_tipp2]), columns=col_names)

    df.style.hide_index()

    HomeFinal = float(odds_tipp1)
    HomeSub1 = 1 / HomeFinal
    HomeFinalNew = HomeSub1 * 100

    AwayFinal = float(odds_tipp2)
    AwaySub1 = 1 / AwayFinal
    AwayFinalNew = AwaySub1 * 100

    finaldraw = float(odds_tippX)
    DrawSub1 = 1 / finaldraw
    DrawFinalNew = DrawSub1 * 100

    Label(game_menu_frame2, text="Betway's probability ").place(x=450, y=100)
    Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(x=450, y=125)
    Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(x=450, y=150)
    Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=450, y=175)

    if Team1WinPercent > HomeFinalNew + 10:
        Label(game_menu_frame2, text="Bet on an Home win").place(x=450, y=200)
    elif Team2WinPercent > AwayFinalNew + 10:
        Label(game_menu_frame2, text="Bet on an Away win").place(x=450, y=200)
    elif DrawPercent > DrawFinalNew + 10:
        Label(game_menu_frame2, text="Bet on a Draw").place(x=450, y=200)
    else:
        Label(game_menu_frame2, text="Ignore this bet").place(x=450, y=200)
    ModelOutput(game_menu_frame2)
