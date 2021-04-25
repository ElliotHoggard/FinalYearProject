import time
from tkinter import *
import numpy as np
import numpy.random as nr
import pandas as pd
from aaa.modelanalysis import game_menu_frame2
from selenium import webdriver
global nums
nums = 10000
from aaa.OffDefStrength import NEWOGoals, NEWDGoals, WHUDGoals, WHUOGoals, WOLOGoals, WOLDGoals, SHUOGoals, SHUDGoals, \
    FULOGoals, FULDGoals, EVEDGoals, EVEOGoals, ARSOGoals, ARSDGoals, MUNOGoals, MUNDGoals, BUROGoals, BURDGoals, \
    LEEOGoals, LEEDGoals, LIVOGoals, LIVDGoals, CHEOGoals, CHEDGoals, BRIOGoals, BRIDGoals, TOTOGoals, TOTDGoals, \
    SOUOGoals, SOUDGoals, AVLOGoals, AVLDGoals, MCIOGoals, MCIDGoals, CRYOGoals, CRYDGoals, LEIOGoals, LEIDGoals, \
    WBAOGoals, WBADGoals

def LivNew1():
    LIVBalancedMean = np.mean([LIVOGoals.mean(), NEWDGoals.mean()])
    NEWBalancedMean = np.mean([NEWOGoals.mean(), LIVDGoals.mean()])
    q = 2
    sim_poissonLIVNEW(nums, LIVBalancedMean.mean(), NEWBalancedMean.mean())
    distA, distB = sim_poissonLIVNEW(10000)
    winPercent(distA, distB, q)


def sim_poissonLIVNEW(nums, mean1=LIVOGoals.mean() + NEWDGoals.mean(), mean2=NEWOGoals.mean() + LIVDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def WhuChe1():
    WHUBalancedMean = np.mean([WHUOGoals.mean(), CHEDGoals.mean()])
    CHEBalancedMean = np.mean([CHEOGoals.mean(), WHUDGoals.mean()])
    q = 3
    sim_poissonWHUCHE(nums, WHUBalancedMean.mean(), CHEBalancedMean.mean())
    distA, distB = sim_poissonWHUCHE(10000)
    winPercent(distA, distB, q)


def sim_poissonWHUCHE(nums, mean1=WHUOGoals.mean() + CHEDGoals.mean(), mean2=CHEOGoals.mean() + WHUDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def ShuBri1():
    SHUBalancedMean = np.mean([SHUOGoals.mean(), BRIDGoals.mean()])
    BRIBalancedMean = np.mean([BRIOGoals.mean(), SHUDGoals.mean()])
    q = 4
    sim_poissonSHUBRI(nums, SHUBalancedMean.mean(), BRIBalancedMean.mean())
    distA, distB = sim_poissonSHUBRI(10000)
    winPercent(distA, distB, q)


def sim_poissonSHUBRI(nums, mean1=SHUOGoals.mean() + BRIDGoals.mean(), mean2=BRIOGoals.mean() + SHUDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def WolBur1():
    WOLBalancedMean = np.mean([WOLOGoals.mean(), BURDGoals.mean()])
    BURBalancedMean = np.mean([BUROGoals.mean(), WOLDGoals.mean()])
    q = 5
    sim_poissonWOLBUR(nums, WOLBalancedMean.mean(), BURBalancedMean.mean())
    distA, distB = sim_poissonWOLBUR(10000)
    winPercent(distA, distB, q)


def sim_poissonWOLBUR(nums, mean1=WOLOGoals.mean() + BURDGoals.mean(), mean2=BUROGoals.mean() + WOLDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def LeeMun1():
    LEEBalancedMean = np.mean([LEEOGoals.mean(), MUNDGoals.mean()])
    MUNBalancedMean = np.mean([MUNOGoals.mean(), LEEDGoals.mean()])
    q = 6
    sim_poissonLEEMUN(nums, LEEBalancedMean.mean(), MUNBalancedMean.mean())
    distA, distB = sim_poissonLEEMUN(10000)
    winPercent(distA, distB, q)


def sim_poissonLEEMUN(nums, mean1=LEEOGoals.mean() + MUNDGoals.mean(), mean2=MUNOGoals.mean() + LEEDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def AvlWba1():
    AVLBalancedMean = np.mean([AVLOGoals.mean(), WBADGoals.mean()])
    WBABalancedMean = np.mean([WBAOGoals.mean(), AVLDGoals.mean()])
    q = 7
    sim_poissonAVLWBA(nums, AVLBalancedMean.mean(), WBABalancedMean.mean())
    distA, distB = sim_poissonAVLWBA(10000)
    winPercent(distA, distB, q)


def sim_poissonAVLWBA(nums, mean1=AVLOGoals.mean() + WBADGoals.mean(), mean2=WBAOGoals.mean() + AVLDGoals.mean()):
    n = 1
    while n < nums:
        dist1 = nr.poisson(lam=mean1, size=n)
        dist2 = nr.poisson(lam=mean2, size=n)
        n = n + 1
    return (dist1, dist2)


def LeiCry1():
    LEIBalancedMean = np.mean([LEIOGoals.mean(), CRYDGoals.mean()])
    CRYBalancedMean = np.mean([CRYOGoals.mean(), LEIDGoals.mean()])
    q = 8
    sim_poissonLEICRY(nums, LEIBalancedMean.mean(), CRYBalancedMean.mean())
    distA, distB = sim_poissonLEICRY(10000)
    winPercent(distA, distB, q)


def sim_poissonLEICRY(nums, mean1=LEIOGoals.mean() + CRYDGoals.mean(), mean2=CRYOGoals.mean() + LEIDGoals.mean()):
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
    browser.get("file:///C:/Users/ellio/OneDrive/Documents/AA Project/aaa/TipicoWebsite/Tipico33.html")

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
        row2 = 1
        HomeWin = df.loc[0, 'Tipp 1']
        HomeWinP1 = int(HomeWin[0])
        HomeWinP2 = int(HomeWin[2:4])
        HomeWinP2New = HomeWinP2 / 100
        HomeFinal = HomeWinP1 + HomeWinP2New
        HomeSub1 = 1 / HomeFinal
        HomeFinalNew = HomeSub1 * 100

        AwayWin = df.loc[0, 'Tipp 2']
        AwayWinP1 = int(AwayWin[0:2])
        AwayWinP2 = int(AwayWin[3:4])
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

        Label(game_menu_frame2, text="Liverpool vs Newcastle", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's Probability ").place(x=30, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(x=30,
                                                                                                      y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(
            x=30, y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=30, y=175)

        if Team1WinPercent > HomeFinalNew + 8:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=30, y=200)
        elif Team2WinPercent > AwayFinalNew + 8:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=30, y=200)
        elif DrawPercent > DrawFinalNew + 8:
            Label(game_menu_frame2, text="Bet on a draw").place(x=30, y=200)

        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=30, y=200)

        LIVBalancedMean = np.mean([LIVOGoals.mean(), NEWDGoals.mean()])
        NEWBalancedMean = np.mean([NEWOGoals.mean(), LIVDGoals.mean()])
        roundedNEW = round(NEWBalancedMean)
        roundedLIV = round(LIVBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Liverpool " + str(roundedLIV) + " : " + str(
                  roundedNEW) + " Newcastle").place(x=30, y=50)
        Betway(game_menu_frame2, q, col, row2)

    if q == 3:
        col = 2
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

        Label(game_menu_frame2, text="West Ham vs Chelsea", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's Probability ").place(x=30, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(x=30,
                                                                                                      y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(x=30,
                                                                                                      y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=30, y=175)

        if Team1WinPercent > HomeFinalNew + 8:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=30, y=200)
        elif Team2WinPercent > AwayFinalNew + 8:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=30, y=200)
        elif DrawPercent > DrawFinalNew + 8:
            Label(game_menu_frame2, text="Bet on a Draw").place(x=30, y=200)
        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=30, y=200)

        WHUBalancedMean = np.mean([WHUOGoals.mean(), CHEDGoals.mean()])
        CHEBalancedMean = np.mean([CHEOGoals.mean(), WHUDGoals.mean()])
        roundedCHE = round(CHEBalancedMean)
        roundedWHU = round(WHUBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: West Ham " + str(roundedWHU) + " : " + str(
                  roundedCHE) + " Chelsea").place(x=30, y=50)
        Betway(game_menu_frame2, q, col, row2)

    if q == 4:
        col = 3
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

        Label(game_menu_frame2, text="Sheffield vs Brighton", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's Probability ").place(x=30, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(x=30,
                                                                                                      y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(
            x=30, y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=30, y=175)

        if Team1WinPercent > HomeFinalNew + 8:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=30, y=200)
        elif Team2WinPercent > AwayFinalNew + 8:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=30, y=200)
        elif DrawPercent > DrawFinalNew + 8:
            Label(game_menu_frame2, text="Bet on a draw").place(x=30, y=200)
        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=30, y=200)

        SHUBalancedMean = np.mean([SHUOGoals.mean(), BRIDGoals.mean()])
        BRIBalancedMean = np.mean([BRIOGoals.mean(), SHUDGoals.mean()])
        roundedSHU = round(SHUBalancedMean)
        roundedBRI = round(BRIBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Sheffield " + str(roundedSHU) + " : " + str(roundedBRI) + " Brighton").place(
            x=30, y=50)

        Betway(game_menu_frame2, q, col, row2)

    if q == 5:
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

        Label(game_menu_frame2, text="Wolves vs Burnley", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's Probability ").place(x=30, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(
            x=30, y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(x=30,
                                                                                                      y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=30, y=175)

        if Team1WinPercent > HomeFinalNew + 8:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=30, y=200)
        elif Team2WinPercent > AwayFinalNew + 8:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=30, y=200)
        elif DrawPercent > DrawFinalNew + 8:
            Label(game_menu_frame2, text="Bet on a draw").place(x=30, y=200)
        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=30, y=200)

        WOLBalancedMean = np.mean([WOLOGoals.mean(), BURDGoals.mean()])
        BURBalancedMean = np.mean([BUROGoals.mean(), WOLDGoals.mean()])

        roundedWOL = round(WOLBalancedMean)
        roundedBUR = round(BURBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Wolves " + str(roundedWOL) + " : " + str(roundedBUR) + " Burnley").place(
            x=30, y=50)
        Betway(game_menu_frame2, q, col, row2)

    if q == 6:
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

        Label(game_menu_frame2, text="Leeds vs Man United", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's Probability ").place(x=30, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(x=30, y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(x=30, y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=30, y=175)

        if Team1WinPercent > HomeFinalNew + 8:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=30, y=200)
        elif Team2WinPercent > AwayFinalNew + 8:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=30, y=200)
        elif DrawPercent > DrawFinalNew + 8:
            Label(game_menu_frame2, text="Bet on a draw").place(x=30, y=200)
        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=30, y=200)

        LEEBalancedMean = np.mean([LEEOGoals.mean(), MUNDGoals.mean()])
        MUNBalancedMean = np.mean([MUNOGoals.mean(), LEEDGoals.mean()])
        roundedLEE = round(LEEBalancedMean)
        roundedMUN = round(MUNBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Leeds " + str(roundedLEE) + " : " + str(
                  roundedMUN) + " Man United").place(x=30, y=50)
        Betway(game_menu_frame2, q, col, row2)

    if q == 7:
        col = 3
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

        Label(game_menu_frame2, text="Aston Villa vs West Brom", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's Probability ").place(x=30, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(x=30, y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(x=30, y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=30, y=175)

        if Team1WinPercent > HomeFinalNew + 8:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=30, y=200)
        elif Team2WinPercent > AwayFinalNew + 8:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=30, y=200)
        elif DrawPercent > DrawFinalNew + 8:
            Label(game_menu_frame2, text="Bet on a draw").place(x=30, y=200)
        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=30, y=200)

        AVLBalancedMean = np.mean([AVLOGoals.mean(), WBADGoals.mean()])
        WBABalancedMean = np.mean([WBAOGoals.mean(), AVLDGoals.mean()])
        roundedAVL = round(AVLBalancedMean)
        roundedWBA = round(WBABalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Aston Villa " + str(roundedAVL) + " : " + str(roundedWBA) + " West Brom ").place(
            x=30, y=50)
        Betway(game_menu_frame2, q, col, row2)

    if q == 8:
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

        Label(game_menu_frame2, text="Leicester vs Crystal Palace", bd=2, fg='#000000', pady=5,
              font=('Arial', 14, 'bold')).pack()
        Label(game_menu_frame2, text="Tipico's Probability ").place(x=30, y=100)
        Label(game_menu_frame2, text="Home win: " + str(float("{0:.2f}".format(HomeFinalNew)))).place(x=30, y=125)
        Label(game_menu_frame2, text="Away win: " + str(float("{0:.2f}".format(AwayFinalNew)))).place(x=30, y=150)
        Label(game_menu_frame2, text="Draw: " + str(float("{0:.2f}".format(DrawFinalNew)))).place(x=30, y=175)

        if Team1WinPercent > HomeFinalNew + 8:
            Label(game_menu_frame2, text="Bet on a Home win").place(x=30, y=200)
        elif Team2WinPercent > AwayFinalNew + 8:
            Label(game_menu_frame2, text="Bet on an Away win").place(x=30, y=200)
        elif DrawPercent > DrawFinalNew + 8:
            Label(game_menu_frame2, text="Bet on a draw").place(x=30, y=200)
        else:
            Label(game_menu_frame2, text="Ignore this bet").place(x=30, y=200)

        LEIBalancedMean = np.mean([LEIOGoals.mean(), CRYDGoals.mean()])
        CRYBalancedMean = np.mean([CRYOGoals.mean(), LEIDGoals.mean()])
        roundedLEI = round(LEIBalancedMean)
        roundedCRY = round(CRYBalancedMean)
        Label(game_menu_frame2,
              text="Predicted Score line: Leicester " + str(roundedLEI) + " : " + str(
                  roundedCRY) + " Crystal Palace").place(x=30, y=50)
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
    browser.get("file:///C:/Users/ellio/OneDrive/Documents/AA Project/aaa/BetwayWebsite/betway33.html")

    col_names = ['Home', 'Draw', 'Away']

    lst_odds_tipp1 = []
    lst_odds_tippX = []
    lst_odds_tipp2 = []

    time.sleep(3)

    for i in range(1, 10):
        odds_tipp1 = browser.find_element_by_xpath(
            '/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/div/div[' + str(
                row2) + ']/div[2]/div/div[' + str(
                col) + ']/article/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[4]/div').text
        odds_tippX = browser.find_element_by_xpath(
            '/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/div/div[' + str(
                row2) + ']/div[2]/div/div[' + str(
                col) + ']/article/div[1]/div[2]/div/div/div[2]/div/div[2]/div[3]/div/div[4]/div').text
        odds_tipp2 = browser.find_element_by_xpath(
            '/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div[2]/div/div[' + str(
                row2) + ']/div[2]/div/div[' + str(
                col) + ']/article/div[1]/div[2]/div/div/div[2]/div/div[2]/div[4]/div/div[4]/div').text

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

    if Team1WinPercent > HomeFinalNew + 8:
        Label(game_menu_frame2, text="Bet on an Home win").place(x=450, y=200)
    elif Team2WinPercent > AwayFinalNew + 8:
        Label(game_menu_frame2, text="Bet on an Away win").place(x=450, y=200)
    elif DrawPercent > DrawFinalNew + 8:
        Label(game_menu_frame2, text="Bet on a Draw").place(x=450, y=200)
    else:
        Label(game_menu_frame2, text="Ignore this bet").place(x=450, y=200)
    ModelOutput(game_menu_frame2)
