import time
from tkinter import *

from os import listdir
import numpy as np
import numpy.random as nr
import pandas as pd
from aaa.modelanalysis import game_menu_frame2
from selenium import webdriver

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


# GW 30
def CheWba1():
    CHEBalancedMean1 = np.mean([CHEOGoals.mean(), WBADGoals.mean()])
    WBABalancedMean1 = np.mean([WBAOGoals.mean(), CHEDGoals.mean()])
    q = 1
    sim_poissonCHEWBA(nums, CHEBalancedMean1.mean(), WBABalancedMean1.mean())
    distA, distB = sim_poissonCHEWBA(10000)
    winPercent(distA, distB, q)


def sim_poissonCHEWBA(nums, mean1=CHEOGoals.mean() + WBADGoals.mean(), mean2=WBAOGoals.mean() + CHEDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def LeeShu1():
    LEEBalancedMean = np.mean([LEEOGoals.mean(), SHUDGoals.mean()])
    SHUBalancedMean = np.mean([SHUOGoals.mean(), LEEDGoals.mean()])
    q = 2
    sim_poissonLEESHU(nums, LEEBalancedMean.mean(), SHUBalancedMean.mean())
    distA, distB = sim_poissonCHEWBA(10000)
    winPercent(distA, distB, q)


def sim_poissonLEESHU(nums, mean1=LEEOGoals.mean() + SHUDGoals.mean(), mean2=SHUOGoals.mean() + LEEDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def LeiMci1():
    LEIBalancedMean = np.mean([LEIOGoals.mean(), MCIDGoals.mean()])
    MCIBalancedMean = np.mean([MCIOGoals.mean(), LEIDGoals.mean()])
    q = 3
    sim_poissonLEIMCI(nums, LEIBalancedMean.mean(), MCIBalancedMean.mean())
    distA, distB = sim_poissonLEIMCI(10000)
    winPercent(distA, distB, q)


def sim_poissonLEIMCI(nums, mean1=LEIOGoals.mean() + MCIDGoals.mean(), mean2=MCIOGoals.mean() + LEIDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def ArsLiv1():
    ARSBalancedMean = np.mean([ARSOGoals.mean(), LIVDGoals.mean()])
    LIVBalancedMean = np.mean([LIVOGoals.mean(), ARSDGoals.mean()])
    q = 4
    sim_poissonLEIMCI(nums, ARSBalancedMean.mean(), LIVBalancedMean.mean())
    distA, distB = sim_poissonARSLIV(10000)
    winPercent(distA, distB, q)


def sim_poissonARSLIV(nums, mean1=ARSOGoals.mean() + LIVDGoals.mean(), mean2=LIVOGoals.mean() + ARSDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def SouBur1():
    SOUBalancedMean = np.mean([SOUOGoals.mean(), BURDGoals.mean()])
    BURBalancedMean = np.mean([BUROGoals.mean(), SOUDGoals.mean()])
    q = 5
    sim_poissonSOUBUR(nums, SOUBalancedMean.mean(), BURBalancedMean.mean())
    distA, distB = sim_poissonARSLIV(10000)
    winPercent(distA, distB, q)


def sim_poissonSOUBUR(nums, mean1=SOUOGoals.mean() + BURDGoals.mean(), mean2=BUROGoals.mean() + SOUDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def NewTot1():
    NEWBalancedMean = np.mean([NEWOGoals.mean(), TOTDGoals.mean()])
    TOTBalancedMean = np.mean([TOTOGoals.mean(), NEWDGoals.mean()])
    q = 6
    sim_poissonNEWTOT(nums, NEWBalancedMean.mean(), TOTBalancedMean.mean())
    distA, distB = sim_poissonNEWTOT(10000)
    winPercent(distA, distB, q)


def sim_poissonNEWTOT(nums, mean1=NEWOGoals.mean() + TOTDGoals.mean(), mean2=TOTOGoals.mean() + NEWDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def AvlFul1():
    AVLBalancedMean = np.mean([AVLOGoals.mean(), FULDGoals.mean()])
    FULBalancedMean = np.mean([FULOGoals.mean(), AVLDGoals.mean()])
    q = 7
    sim_poissonAVLFUL(nums, AVLBalancedMean.mean(), FULBalancedMean.mean())
    distA, distB = sim_poissonAVLFUL(10000)
    winPercent(distA, distB, q)


def sim_poissonAVLFUL(nums, mean1=AVLOGoals.mean() + FULDGoals.mean(), mean2=FULOGoals.mean() + AVLDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def MunBri1():
    MUNBalancedMean = np.mean([MUNOGoals.mean(), BRIDGoals.mean()])
    BRIBalancedMean = np.mean([BRIOGoals.mean(), MUNDGoals.mean()])
    q = 8
    sim_poissonMUNBRI(nums, MUNBalancedMean.mean(), BRIBalancedMean.mean())
    distA, distB = sim_poissonMUNBRI(10000)
    winPercent(distA, distB, q)


def sim_poissonMUNBRI(nums, mean1=MUNOGoals.mean() + BRIDGoals.mean(), mean2=BRIOGoals.mean() + MUNDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def EveCry1():
    EVEBalancedMean = np.mean([EVEOGoals.mean(), CRYDGoals.mean()])
    CRYBalancedMean = np.mean([CRYOGoals.mean(), EVEDGoals.mean()])
    q = 9
    sim_poissonEVECRY(nums, EVEBalancedMean.mean(), CRYBalancedMean.mean())
    distA, distB = sim_poissonEVECRY(10000)
    winPercent(distA, distB, q)


def sim_poissonEVECRY(nums, mean1=EVEOGoals.mean() + CRYDGoals.mean(), mean2=CRYOGoals.mean() + EVEDGoals.mean()):
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
    game_menu2 = Tk()
    game_menu2.withdraw
    game_menu_frame2.place(relx=0.5, rely=0.15, relheight=0.8, relwidth=0.9, anchor='n')
    TipicoFirstGame(game_menu2, game_menu_frame2, q)


def TipicoFirstGame(game_menu2, game_menu_frame2, q):
    driver_path = r"C:\Users\ellio\Downloads\chromedriver.exe"
    brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    browser = webdriver.Chrome(executable_path=driver_path, options=option)
    browser.get("file:///C:/Users/ellio/Downloads/gw 30 eg tipico.html")
    #https://sports.tipico.de/de/alle/1101/1201,32201,30201/1301,36301,42301

    col_names = ['Tipp 1', 'Tipp X', 'Tipp 2']
    lst_odds_tipp1 = []
    lst_odds_tippX = []
    lst_odds_tipp2 = []

    time.sleep(5)
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
        HomeWinP1 = int(HomeWin[0:1])
        HomeWinP2 = int(HomeWin[2:4])
        HomeWinP2New = HomeWinP2 / 100
        HomeFinal = HomeWinP1 + HomeWinP2New
        HomeSub1 = 1 / HomeFinal
        HomeFinalNew = HomeSub1 * 100

        AwayWin = df.loc[0, 'Tipp 2']
        AwayWinP1 = int(AwayWin[0:1])
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

        Label(game_menu_frame2, text="Chelsea vs West Brom ", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's probability ").place(x=50, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(x=50,
                                                                                                      y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(x=50,
                                                                                                      y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=50, y=175)

        if Team1WinPercent > HomeFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=50, y=200)
        elif Team2WinPercent > AwayFinalNew + 10:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=50, y=200)
        elif DrawPercent > DrawFinalNew + 10:
            Label(game_menu_frame2, text="Bet on a Draw").place(x=50, y=200)
        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=50, y=200)

        CHEBalancedMean1 = np.mean([CHEOGoals.mean(), WBADGoals.mean()])
        WBABalancedMean1 = np.mean([WBAOGoals.mean(), CHEDGoals.mean()])
        roundedChe = round(CHEBalancedMean1)
        roundedWBA = round(WBABalancedMean1)
        Label(game_menu_frame2,
              text="Predicted Score line: Chelsea " + str(roundedChe) + " : " + str(roundedWBA) + " West Brom").place(
            x=30, y=50)
        Betway(game_menu2, game_menu_frame2, q, row, row2)

    if q == 2:
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

        Label(game_menu_frame2, text="Leeds United vs Sheffield United", bd=2, fg='#000000', pady=5,
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

        SHUBalancedMean = np.mean([SHUOGoals.mean(), LEEDGoals.mean()])
        LEEBalancedMean = np.mean([LEEOGoals.mean(), SHUDGoals.mean()])
        roundedLEE = round(LEEBalancedMean)
        roundedSHU = round(SHUBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Leeds United " + str(roundedLEE) + " : " + str(
                  roundedSHU) + " Sheffield united").place(x=30, y=50)
        Betway(game_menu2, game_menu_frame2, q, row, row2)

    if q == 3:
        row = 1
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

        Label(game_menu_frame2, text="Leicester City vs Manchester City", bd=2, fg='#000000', pady=5,
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

        LEIBalancedMean = np.mean([LEIOGoals.mean(), MCIDGoals.mean()])
        MCIBalancedMean = np.mean([MCIOGoals.mean(), LEIDGoals.mean()])
        roundedLEI = round(LEIBalancedMean)
        roundedMCI = round(MCIBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Leicester City " + str(roundedLEI) + " : " + str(
                  roundedMCI) + " Manchester City").place(x=30, y=50)
        Betway(game_menu2, game_menu_frame2, q, row, row2)

    if q == 4:
        row = 1
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

        Label(game_menu_frame2, text="Arsenal vs Liverpool", bd=2, fg='#000000', pady=5,
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

        ARSBalancedMean = np.mean([ARSOGoals.mean(), LIVDGoals.mean()])
        LIVBalancedMean = np.mean([LIVOGoals.mean(), ARSDGoals.mean()])
        roundedARS = round(ARSBalancedMean)
        roundedLIV = round(LIVBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Arsenal " + str(roundedARS) + " : " + str(roundedLIV) + " Liverpool").place(
            x=30, y=50)

        Betway(game_menu2, game_menu_frame2, q, row, row2)
        game_menu2.mainloop()

    if q == 5:
        row2 = 1
        row = 2
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

        Label(game_menu_frame2, text="Southampton vs Burnley", bd=2, fg='#000000', pady=5,
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

        ARSBalancedMean = np.mean([ARSOGoals.mean(), LIVDGoals.mean()])
        LIVBalancedMean = np.mean([LIVOGoals.mean(), ARSDGoals.mean()])
        roundedARS = round(ARSBalancedMean)
        roundedLIV = round(LIVBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Southampton " + str(roundedARS) + " : " + str(roundedLIV) + " Burnley").place(
            x=30, y=50)
        Betway(game_menu2, game_menu_frame2, q, row, row2)
        game_menu2.mainloop()

    if q == 6:
        row2 = 2
        row = 2
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

        Label(game_menu_frame2, text="Newcastle United vs Tottenham Hotspur", bd=2, fg='#000000', pady=5,
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

        NEWBalancedMean = np.mean([NEWOGoals.mean(), TOTDGoals.mean()])
        TOTBalancedMean = np.mean([TOTOGoals.mean(), NEWDGoals.mean()])
        roundedNEW = round(NEWBalancedMean)
        roundedTOT = round(TOTBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Newcastle United " + str(roundedNEW) + " : " + str(
                  roundedTOT) + " Tottenham Hotspur").place(x=30, y=50)
        Betway(game_menu2, game_menu_frame2, q, row, row2)
        game_menu2.mainloop()

    if q == 7:
        row2 = 3
        row = 2
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

        Label(game_menu_frame2, text="Aston Villa vs Fulham", bd=2, fg='#000000', pady=5,
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

        AVLBalancedMean = np.mean([AVLOGoals.mean(), FULDGoals.mean()])
        FULBalancedMean = np.mean([FULOGoals.mean(), AVLDGoals.mean()])
        roundedAVL = round(AVLBalancedMean)
        roundedFUL = round(FULBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Aston Villa " + str(roundedAVL) + " : " + str(roundedFUL) + " Fulham").place(
            x=30, y=50)
        Betway(game_menu2, game_menu_frame2, q, row, row2)
        game_menu2.mainloop()

    if q == 8:
        row2 = 4
        row = 2
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

        Label(game_menu_frame2, text="Manchester United vs Brighton", bd=2, fg='#000000', pady=5,
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

        MUNBalancedMean = np.mean([MUNOGoals.mean(), BRIDGoals.mean()])
        BRIBalancedMean = np.mean([BRIOGoals.mean(), MUNDGoals.mean()])
        roundedMUN = round(MUNBalancedMean)
        roundedBRI = round(BRIBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Manchester United " + str(roundedMUN) + " : " + str(
                  roundedBRI) + " Brighton").place(x=30, y=50)
        Betway(game_menu2, game_menu_frame2, q, row, row2)
        game_menu2.mainloop()

    if q == 9:
        row2 = 1
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

        Label(game_menu_frame2, text="Everton vs Crystal Palace", bd=2, fg='#000000', pady=5,
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

        EVEBalancedMean = np.mean([EVEOGoals.mean(), CRYDGoals.mean()])
        CRYBalancedMean = np.mean([CRYOGoals.mean(), EVEDGoals.mean()])
        roundedEVE = round(EVEBalancedMean)
        roundedCRY = round(CRYBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Everton " + str(roundedEVE) + " : " + str(
                  roundedCRY) + " Crystal Palace").place(x=30, y=50)
        Betway(game_menu2, game_menu_frame2, q, row, row2)
        game_menu2.mainloop()
    else:
        ModelOutput(game_menu2, game_menu_frame2)


def ModelOutput(game_menu2, game_menu_frame2):
    Label(game_menu_frame2, text="Our Probability").place(x=250, y=100)
    Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(Team1WinPercent))) + "%").place(x=250, y=125)
    Label(game_menu_frame2, text="Away wins: " + str(float("{0:.2f}".format(Team2WinPercent))) + "%").place(x=250,
                                                                                                            y=150)
    Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawPercent))) + "%").place(x=250, y=175)
    game_menu2.mainloop()


def Betway(game_menu2, game_menu_frame2, q, row, row2):
    driver_path = r"C:\Users\ellio\Downloads\chromedriver.exe"
    brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    browser = webdriver.Chrome(executable_path=driver_path, options=option)
    browser.get("file:///C:/Users/ellio/Downloads/gw 30 eg betway.html")
    #https://betway.com/en/sports/grp/soccer/england/premier-league
    # lost saved webpage


    col_names = ['Home', 'Draw', 'Away']

    lst_odds_tipp1 = []
    lst_odds_tippX = []
    lst_odds_tipp2 = []

    time.sleep(5)  # Sleep for 3 seconds

    for i in range(1, 10):
        odds_tipp1 = browser.find_element_by_xpath(
            '/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/div/div[' + str(
                row) + ']/div[2]/div/div[' + str(
                row2) + ']/article/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[4]/div').text
        odds_tippX = browser.find_element_by_xpath(
            '/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/div/div[' + str(
                row) + ']/div[2]/div/div[' + str(
                row2) + ']/article/div[1]/div[2]/div/div/div[2]/div/div[2]/div[3]/div/div[4]/div').text
        odds_tipp2 = browser.find_element_by_xpath(
            '/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/div/div[' + str(
                row) + ']/div[2]/div/div[' + str(
                row2) + ']/article/div[1]/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[4]/div').text

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
    ModelOutput(game_menu2, game_menu_frame2)
    game_menu2.mainloop()


