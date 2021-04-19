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
def MciLee1():
    MCIBalancedMean = np.mean([MCIOGoals.mean(), LEEDGoals.mean()])
    LEEBalancedMean = np.mean([LEEOGoals.mean(), MCIDGoals.mean()])
    q = 1
    sim_poissonMciLee(nums,  MCIBalancedMean.mean()), LEEBalancedMean.mean()
    distA, distB = sim_poissonMciLee(10000)
    winPercent(distA, distB, q)


def sim_poissonMciLee(nums, mean1=MCIOGoals.mean() + LEEDGoals.mean(), mean2=LEEOGoals.mean() + MCIDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def LivAvl1():
    LIVBalancedMean = np.mean([LIVOGoals.mean(), AVLDGoals.mean()])
    AVLBalancedMean = np.mean([AVLOGoals.mean(), LIVDGoals.mean()])
    q = 2
    sim_poissonLIVAVL(nums, LIVBalancedMean.mean(), AVLBalancedMean.mean())
    distA, distB = sim_poissonLIVAVL(10000)
    winPercent(distA, distB, q)


def sim_poissonLIVAVL(nums, mean1=LIVOGoals.mean() + AVLDGoals.mean(), mean2=AVLOGoals.mean() + LIVDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def CryChe1():
    CRYBalancedMean = np.mean([CRYOGoals.mean(), CHEDGoals.mean()])
    CHEBalancedMean = np.mean([CHEOGoals.mean(), CRYDGoals.mean()])
    q = 3
    sim_poissonCRYCHE(nums, CRYBalancedMean.mean(), CHEBalancedMean.mean())
    distA, distB = sim_poissonCRYCHE(10000)
    winPercent(distA, distB, q)


def sim_poissonCRYCHE(nums, mean1=CRYOGoals.mean() + CHEDGoals.mean(), mean2=CHEOGoals.mean() + CRYDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def NewBur1():
    NEWBalancedMean = np.mean([NEWOGoals.mean(), BURDGoals.mean()])
    BURBalancedMean = np.mean([BUROGoals.mean(), NEWDGoals.mean()])
    q = 4
    sim_poissonNEWBUR(nums, NEWBalancedMean.mean(), BURBalancedMean.mean())
    distA, distB = sim_poissonCRYCHE(10000)
    winPercent(distA, distB, q)


def sim_poissonNEWBUR(nums, mean1=NEWOGoals.mean() + BURDGoals.mean(), mean2=BUROGoals.mean() + NEWDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def WhuLei1():
    WHUBalancedMean = np.mean([WHUOGoals.mean(), LEIDGoals.mean()])
    LEIBalancedMean = np.mean([LEIOGoals.mean(), WHUDGoals.mean()])
    q = 5
    sim_poissonWHULEI(nums, WHUBalancedMean.mean(), LEIBalancedMean.mean())
    distA, distB = sim_poissonWHULEI(10000)
    winPercent(distA, distB, q)


def sim_poissonWHULEI(nums, mean1=WHUOGoals.mean() + LEIDGoals.mean(), mean2=LEIOGoals.mean() + WHUDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def TotMun1():
    TOTBalancedMean = np.mean([TOTOGoals.mean(), MUNDGoals.mean()])
    MUNBalancedMean = np.mean([MUNOGoals.mean(), TOTDGoals.mean()])
    q = 6
    sim_poissonTOTMUN(nums, TOTBalancedMean.mean(), MUNBalancedMean.mean())
    distA, distB = sim_poissonTOTMUN(10000)
    winPercent(distA, distB, q)


def sim_poissonTOTMUN(nums, mean1=TOTOGoals.mean() + MUNDGoals.mean(), mean2=MUNOGoals.mean() + TOTDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def ShuArs1():
    SHUBalancedMean = np.mean([SHUOGoals.mean(), ARSDGoals.mean()])
    ARSBalancedMean = np.mean([ARSOGoals.mean(), SHUDGoals.mean()])
    q = 7
    sim_poissonSHUARS(nums, SHUBalancedMean.mean(), ARSBalancedMean.mean())
    distA, distB = sim_poissonSHUARS(10000)
    winPercent(distA, distB, q)


def sim_poissonSHUARS(nums, mean1=SHUOGoals.mean() + ARSDGoals.mean(), mean2=ARSOGoals.mean() + SHUDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def WbaSou1():
    WBABalancedMean = np.mean([WBAOGoals.mean(), SOUDGoals.mean()])
    SOUBalancedMean = np.mean([SOUOGoals.mean(), WBADGoals.mean()])
    q = 8
    sim_poissonWBASOU(nums, WBABalancedMean.mean(), SOUBalancedMean.mean())
    distA, distB = sim_poissonWBASOU(10000)
    winPercent(distA, distB, q)


def sim_poissonWBASOU(nums, mean1=WBAOGoals.mean() + SOUDGoals.mean(), mean2=SOUOGoals.mean() + WBADGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)

def BriEve1():
    BRIBalancedMean1 = np.mean([BRIOGoals.mean(), EVEDGoals.mean()])
    EVEBalancedMean1 = np.mean([EVEOGoals.mean(), BRIDGoals.mean()])
    q = 9
    sim_poissonBRIEVE(nums, BRIBalancedMean1.mean(), EVEBalancedMean1.mean())
    distA, distB = sim_poissonBRIEVE(10000)
    winPercent(distA, distB, q)


def sim_poissonBRIEVE(nums, mean1=BRIOGoals.mean() + EVEDGoals.mean(), mean2=EVEOGoals.mean() + BRIDGoals.mean()):
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
    browser.get("file:///C:/Users/ellio/Downloads/Premier League Wetten - englische Fussball Wetten mit top Quoten.html")

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

    if q == 1:
        row = 1
        row2 = 1
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

        Label(game_menu_frame2, text="Man City vs Leeds United", bd=2, fg='#000000', pady=5,
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

        MCIBalancedMean = np.mean([MCIOGoals.mean(), LEEDGoals.mean()])
        LEEBalancedMean = np.mean([LEEOGoals.mean(), MCIDGoals.mean()])
        roundedMCI = round(MCIBalancedMean)
        roundedLEE = round(LEEBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Man City " + str(roundedMCI) + " : " + str(
                  roundedLEE) + " Leeds United").place(x=30, y=50)
        Betway(game_menu_frame2, q, row, row2)

    if q == 2:
        row = 2
        row2 = 1
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

        Label(game_menu_frame2, text="Liverpool vs Aston Villa", bd=2, fg='#000000', pady=5,
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

        AVLBalancedMean = np.mean([AVLOGoals.mean(), LIVDGoals.mean()])
        LIVBalancedMean = np.mean([LIVOGoals.mean(), AVLDGoals.mean()])
        roundedLIV = round(LIVBalancedMean)
        roundedAVL = round(AVLBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Liverpool " + str(roundedLIV) + " : " + str(
                  roundedAVL) + " Aston Villa").place(x=30, y=50)
        Betway(game_menu_frame2, q, row, row2)

    if q == 3:
        row = 3
        row2 = 1
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

        Label(game_menu_frame2, text="Crystal Palace vs Chelsea", bd=2, fg='#000000', pady=5,
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

        CRYBalancedMean = np.mean([CRYOGoals.mean(), CHEDGoals.mean()])
        CHEBalancedMean = np.mean([CHEOGoals.mean(), CRYDGoals.mean()])
        roundedCRY = round(CRYBalancedMean)
        roundedCHE = round(CHEBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Crystal Palace " + str(roundedCRY) + " : " + str(roundedCHE) + " Chelsea").place(
            x=30, y=50)

        Betway(game_menu_frame2, q, row, row2)

    if q == 4:
        row = 1
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

        Label(game_menu_frame2, text="Burnley vs Newcastle", bd=2, fg='#000000', pady=5,
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

        BURBalancedMean = np.mean([BUROGoals.mean(), NEWDGoals.mean()])
        NEWBalancedMean = np.mean([NEWOGoals.mean(), BURDGoals.mean()])
        roundedBUR = round(BURBalancedMean)
        roundedNEW = round(NEWBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Burnley " + str(roundedBUR) + " : " + str(roundedNEW) + " Newcastle").place(
            x=30, y=50)
        Betway(game_menu_frame2, q, row, row2)

    if q == 5:
        row = 2
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

        Label(game_menu_frame2, text="West Ham vs Leicester", bd=2, fg='#000000', pady=5,
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

        WHUBalancedMean = np.mean([WHUOGoals.mean(), LEIDGoals.mean()])
        LEIBalancedMean = np.mean([TOTOGoals.mean(), WHUDGoals.mean()])
        roundedWHU = round(WHUBalancedMean)
        roundedLEI = round(LEIBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: West Ham United " + str(roundedWHU) + " : " + str(
                  roundedLEI) + " Leicester").place(x=30, y=50)
        Betway(game_menu_frame2, q, row, row2)

    if q == 6:
        row2 = 2
        row = 3
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

        Label(game_menu_frame2, text="Tottenham vs Man United", bd=2, fg='#000000', pady=5,
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

        TOTBalancedMean = np.mean([TOTOGoals.mean(), MUNDGoals.mean()])
        MUNBalancedMean = np.mean([MUNOGoals.mean(), TOTDGoals.mean()])
        roundedTOT = round(TOTBalancedMean)
        roundedMUN = round(MUNBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Tottenham " + str(roundedTOT) + " : " + str(roundedMUN) + " Man United").place(
            x=30, y=50)
        Betway(game_menu_frame2, q, row, row2)

    if q == 7:
        row2 = 2
        row = 4
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

        Label(game_menu_frame2, text="Sheffield United vs Arsenal", bd=2, fg='#000000', pady=5,
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

        SHUBalancedMean = np.mean([SHUOGoals.mean(), ARSDGoals.mean()])
        ARSBalancedMean = np.mean([ARSOGoals.mean(), SHUDGoals.mean()])
        roundedSHU = round(SHUBalancedMean)
        roundedARS = round(ARSBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Sheffield United " + str(roundedSHU) + " : " + str(
                  roundedARS) + " Arsenal").place(x=30, y=50)
        Betway(game_menu_frame2, q, row, row2)


# These values have no Betway data as it wasn't available
    if q == 8:
        row2 = 2
        row = 3
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

        Label(game_menu_frame2, text="West Brom vs Southampton", bd=2, fg='#000000', pady=5,
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

        WBABalancedMean = np.mean([WBAOGoals.mean(), SOUDGoals.mean()])
        SOUBalancedMean = np.mean([SOUOGoals.mean(), WBADGoals.mean()])
        roundedWBA = round(WBABalancedMean)
        roundedSOU = round(SOUBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: West Brom " + str(roundedWBA) + " : " + str(
                  roundedSOU) + " Southampton").place(x=30, y=50)
        Betway(game_menu_frame2, q, row, row2)

    if q == 9:
        row2 = 2
        row = 3
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

        Label(game_menu_frame2, text="Brighton vs Everton", bd=2, fg='#000000', pady=5,
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

        BRIBalancedMean = np.mean([BRIOGoals.mean(), EVEDGoals.mean()])
        EVEBalancedMean = np.mean([EVEOGoals.mean(), BRIDGoals.mean()])
        roundedBRI = round(BRIBalancedMean)
        roundedEVE = round(EVEBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Brighton " + str(roundedBRI) + " : " + str(
                  roundedEVE) + " Everton").place(x=30, y=50)
        Betway(game_menu_frame2, q, row, row2)
    else:
        ModelOutput(game_menu_frame2)


def ModelOutput(game_menu_frame2):
    Label(game_menu_frame2, text="Our Probability").place(x=250, y=100)
    Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(Team1WinPercent))) + "%").place(x=250, y=125)
    Label(game_menu_frame2, text="Away wins: " + str(float("{0:.2f}".format(Team2WinPercent))) + "%").place(x=250,
                                                                                                            y=150)
    Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawPercent))) + "%").place(x=250, y=175)
    game_menu_frame2.mainloop()


def Betway(game_menu_frame2, q, row, row2):
    driver_path = r"C:\Users\ellio\Downloads\chromedriver.exe"
    brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    browser = webdriver.Chrome(executable_path=driver_path, options=option)
    browser.get("file:///C:/Users/ellio/Downloads/Premier League Betting & Odds _ Bet on the Premier League.html")

    col_names = ['Home', 'Draw', 'Away']

    lst_odds_tipp1 = []
    lst_odds_tippX = []
    lst_odds_tipp2 = []

    time.sleep(3)

    for i in range(1, 10):
        odds_tipp1 = browser.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/div/div['+ str(row2)+']/div[2]/div/div['+ str(row)+']/article/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[4]/div').text
        odds_tippX = browser.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/div/div['+ str(row2)+']/div[2]/div/div['+ str(row)+']/article/div[1]/div[2]/div/div/div[2]/div/div[2]/div[3]/div/div[4]/div').text
        odds_tipp2 = browser.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/div/div['+ str(row2)+']/div[2]/div/div['+ str(row)+']/article/div[1]/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[4]/div').text

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
