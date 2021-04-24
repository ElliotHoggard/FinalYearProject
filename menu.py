from functools import partial
from tkinter import *
from tkhtmlview import HTMLLabel

# Title
global root
root = Tk()
root.title('Premier League Prediction System')
root.geometry("1200x800")
root.configure(bg="#4c8a27")


# Button format
def create_buttons(root, parent_frame, buttons_list, column_num=1):
    global b_height

    def button_click(buttons_list2, n=0):
        buttons[n].config(command=eval(buttons_list2[n]['func_name'] + '()'))

    if len(buttons_list) % 2 == 0:
        buttons_qty = len(buttons_list)
    else:
        buttons_qty = len(buttons_list) + 1

    buttons, left_i, right_i = [], 0, 0

    for i in range(len(buttons_list)):
        if column_num == 2:
            b_height = 1.2 / buttons_qty
            if i % 2 == 0:
                left_i += 1
                buttons.append(
                    Button(parent_frame, text=(buttons_list[i]["name"]), bg='#add8e6', foreground='black', fg='Black',
                           font=('Autobus Bold bold', 20),
                           relief=GROOVE,
                           command=partial(button_click, buttons_list, i)))
                buttons[-1].place(relx=0.05,
                                  rely=0.01 + (0.005 + b_height) * (left_i - 1),
                                  relheight=0.15,
                                  relwidth=0.4)
            else:
                right_i += 1
                buttons.append(
                    Button(parent_frame, text=(buttons_list[i]["name"]), bg='#add8e6', fg='Black',
                           font=('Autobus Bold bold', 20),
                           relief=GROOVE,
                           command=partial(button_click, buttons_list, i)))
                buttons[-1].place(relx=0.5,
                                  rely=0.01 + (0.005 + b_height) * (left_i - 1),
                                  relheight=0.15,
                                  relwidth=0.4)
        elif column_num == 1:
            buttons.append(
                Button(parent_frame, text=(buttons_list[i]["name"]), bg='#add8e6', fg='Black',
                       font=('Autobus Bold bold', 20),
                       relief=GROOVE,
                       command=partial(button_click, buttons_list, i)))
            buttons[-1].place(relx=0.05,
                              rely=0.01 + (0.005 + b_height),
                              relheight=0.15,
                              relwidth=0.4)


def create_buttons1(root, parent_frame, buttons_list, column_num=1):
    global b_height

    def button_click(buttons_list2, n=0):
        buttons[n].config(command=eval(buttons_list2[n]['func_name'] + '()'))

    if len(buttons_list) % 2 == 0:
        buttons_qty = len(buttons_list)
    else:
        buttons_qty = len(buttons_list) + 1

    buttons, left_i, right_i = [], 0, 0

    for i in range(len(buttons_list)):
        if column_num == 2:
            b_height = 0.05 / buttons_qty
            if i - 1 % 2 == 0:
                left_i += 0.2
                buttons.append(
                    Button(parent_frame, text=(buttons_list[i]["name"]), fg="White", bg="Red",
                           font=('Autobus Bold', 12),
                           relief=GROOVE, command=partial(button_click, buttons_list, i)))
                buttons[-1].place(relx=0.25, rely=0.10 + (0.005 + 0.1), relheight=0.075, relwidth=0.5)
            else:
                right_i += 1
                buttons.append(
                    Button(parent_frame, text=(buttons_list[i]["name"]), fg="White", bg="Red",
                           font=('Autobus Bold', 12),
                           relief=GROOVE, command=partial(button_click, buttons_list, i)))
                buttons[-1].place(relx=0.25, rely=0.10 + (0.005 + 0.1) * (left_i - 0.2), relheight=0.075, relwidth=0.5)
        elif column_num == 1:
            buttons.append(
                Button(parent_frame, text=(buttons_list[i]["name"]), fg="White", bg="Red", font=('Autobus Bold', 12),
                       relief=GROOVE, command=partial(button_click, buttons_list, i)))
            buttons[-1].place(relx=0.25, rely=0.10 + (0.005 + 0.1) * (i - 0.2), relheight=0.075, relwidth=0.5)


def create_back_button(parent_frame):
    back_button = Button(parent_frame, text='←', bg="Black", fg="White", font=('Autobus Bold bold', 30), command=Main)
    back_button.place(relx=0.01, rely=0.01, relheight=0.05, relwidth=0.1)
    main_frame = LabelFrame(root, bg='blue', bd=5)
    main_frame.place()


# Button functions search
def runSearch():
    Button(root, text="Exit", command=Main)
    root.title('Select Model')
    root.geometry("1200x800")
    upper_frame = Frame(root, bg='#4c8a27', bd=5, )
    upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.8, anchor="n")
    root_frame = Frame(root, bg='#4c8a27')
    root_frame.place(relx=0.5, rely=0.0, relheight=1, relwidth=1, anchor='n')
    Label(root_frame, text="Model 2", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20, width=599)
    from aaa.model2 import ResultSearchStart
    ResultSearchStart(root_frame)
    create_back_button(root)


def Results():
    Button(root, text="Exit", command=Main)
    root.title('Select Model')
    root.geometry("1200x800")
    upper_frame = Frame(root, bg='#4c8a27', bd=5, )
    upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.8, anchor="n")
    root_frame = Frame(root, bg='#4c8a27')
    create_back_button(root_frame)
    root_frame.place(relx=0.5, rely=0.0, relheight=1, relwidth=1, anchor='n')
    Label(root_frame, text="View Results", font="AutobusBold 15 bold").place(x=300, y=20, width=599)
    html_label = HTMLLabel(root, state="normal", fg='black', font="AutobusBold 30 bold",
                           html='<a href="https://docs.google.com/spreadsheets/d/12CnbJg6bi1WCTQIBHp36YcwLEH2ACWRJ5obK-yzIfHw/edit?usp=sharing"> Results </a>').place(
        x=300, y=50, width=599)
    html_label.pack()
    create_back_button(root)
    root.mainloop()


# Game Week 30
def runCheWBA1():
    from aaa.model1GW30 import CheWba1
    CheWba1()


def runLeeShu1():
    from aaa.model1GW30 import LeeShu1
    LeeShu1()


def runLeiMci1():
    from aaa.model1GW30 import LeiMci1
    LeiMci1()


def runArsLiv1():
    from aaa.model1GW30 import ArsLiv1
    ArsLiv1()


def runSouBur1():
    from aaa.model1GW30 import SouBur1
    SouBur1()


def runNewTot1():
    from aaa.model1GW30 import NewTot1
    NewTot1()


def runAvlFul1():
    from aaa.model1GW30 import AvlFul1
    AvlFul1()


def runMunBri1():
    from aaa.model1GW30 import MunBri1
    MunBri1()


def runEveCry1():
    from aaa.model1GW30 import EveCry1
    EveCry1()


# Gameweek 31
def runMciLee1():
    from aaa.model1GW31 import MciLee1
    MciLee1()


def runLivAvl1():
    from aaa.model1GW31 import LivAvl1
    LivAvl1()


def runCryChe1():
    from aaa.model1GW31 import CryChe1
    CryChe1()


def runBurNew1():
    from aaa.model1GW31 import NewBur1
    NewBur1()


def runWhuLei1():
    from aaa.model1GW31 import WhuLei1
    WhuLei1()


def runTotMun1():
    from aaa.model1GW31 import TotMun1
    TotMun1()


def runShuArs1():
    from aaa.model1GW31 import ShuArs1
    ShuArs1()


def runWbaSou1():
    from aaa.model1GW31 import WbaSou1
    WbaSou1()


def runBriEve1():
    from aaa.model1GW31 import BriEve1
    BriEve1()


# GW 32
def runNewWhu1():
    from aaa.model1GW32 import NewWhu1
    NewWhu1()


def runWolShu1():
    from aaa.model1GW32 import WolShu1
    WolShu1()


def runArsFul1():
    from aaa.model1GW32 import ArsFul1
    ArsFul1()


def runMunBur1():
    from aaa.model1GW32 import MunBur1
    MunBur1()


def runLeeLiv1():
    from aaa.model1GW32 import LeeLiv1
    LeeLiv1()


def runCheBri1():
    from aaa.model1GW32 import CheBri1
    CheBri1()


def runTotSou1():
    from aaa.model1GW32 import TotSou1
    TotSou1()


def runAvlMci1():
    from aaa.model1GW32 import AvlMci1
    AvlMci1()


# GW 33
def runLivNew1():
    from aaa.model1GW33 import LivNew1
    LivNew1()


def runWhuChe1():
    from aaa.model1GW33 import WhuChe1
    WhuChe1()


def runShuBri1():
    from aaa.model1GW33 import ShuBri1
    ShuBri1()


def runWolBur1():
    from aaa.model1GW33 import WolBur1
    WolBur1()


def runLeeMun1():
    from aaa.model1GW33 import LeeMun1
    LeeMun1()


def runAvlWba1():
    from aaa.model1GW33 import AvlWba1
    AvlWba1()


def runLeiCry1():
    from aaa.model1GW33 import LeiCry1
    LeiCry1()


# Model testing

def runLogistic():
    from aaa.modelanalysis import logregression
    logregression()


def runSVC():
    from aaa.modelanalysis import SVC1
    SVC1()


def runXGB():
    from aaa.modelanalysis import XGB
    XGB()


def runANN():
    from aaa.modelanalysis import ANN
    ANN()


def runRandForest():
    from aaa.modelanalysis import randfor
    randfor()


def runFeatureRating():
    from aaa.modelanalysis import featurerating
    featurerating()
    featurerating()


# Graphs
def runGraph1p1():
    from aaa.Graphs import graph1p1
    graph1p1()


def runGraph2p1():
    from aaa.Graphs import graph2p1
    graph2p1()


def runGraph3p1():
    from aaa.Graphs import graph3p1
    graph3p1()


def runGraph1p2():
    from aaa.Graphs import graph1p2
    graph1p2()


def runGraph2p2():
    from aaa.Graphs import graph2p2
    graph2p2()


def runGraph1p3():
    from aaa.Graphs import graph1p3
    graph1p3()


def runGraph1p4():
    from aaa.Graphs import graph1p4
    graph1p4()


def runGraph2p4():
    from aaa.Graphs import graph2p4
    graph2p4()


# GUI buttons
def TestAccuracy():
    Button(root, text="Exit", command=Main)
    root.title('Model Testing')
    root.geometry("1200x800")
    upper_frame = Frame(root, bg='#4c8a27', bd=5, )
    upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.8, anchor="n")
    root_frame = Frame(root, bg='#4c8a27')
    root_frame.place(relx=0.5, rely=0.0, relheight=1, relwidth=1, anchor='n')
    Label(root_frame, text="Model Testing", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20, width=599)

    buttons = [{"name": "Feature Rating", "func_name": "runFeatureRating"},
               {"name": "Random Forest Algorithm", "func_name": "runRandForest"},
               {"name": "Artificial Neural Network", "func_name": "runANN"},
               {"name": "XGB Boost", "func_name": "runXGB"},
               {"name": "Support Vector Classifier", "func_name": "runSVC"},
               {"name": "Logistic Regression", "func_name": "runLogistic"}]

    create_buttons1(root, root_frame, buttons, 1)
    create_back_button(root)
    mainloop()


def HomeAdvantage():
    Button(root, text="Exit", command=Main)
    root.title('Data Analysis')
    root.geometry("1200x800")
    upper_frame = Frame(root, bg='#4c8a27', bd=5, )
    upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.8, anchor="n")
    root_frame = Frame(root, bg='#4c8a27')
    root_frame.place(relx=0.5, rely=0.0, relheight=1, relwidth=1, anchor='n')
    Label(root_frame, text="Measuring Home Advantage", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20,
                                                                                                       width=599)
    buttons = [{"name": "Bar Graph Across Multiple Seasons", "func_name": "runGraph1p1"},
               {"name": "Bar Graph Using Aggregate data", "func_name": "runGraph2p1"},
               {"name": "Pie Chart", "func_name": "runGraph3p1"}]
    create_buttons1(root, root_frame, buttons, 1)
    create_back_button(root)
    mainloop()


def Scatter():
    Button(root, text="Exit", command=Main)
    root.title('Data Analysis')
    root.geometry("1200x800")
    upper_frame = Frame(root, bg='#4c8a27', bd=5, )
    upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.8, anchor="n")
    root_frame = Frame(root, bg='#4c8a27')
    root_frame.place(relx=0.5, rely=0.0, relheight=1, relwidth=1, anchor='n')
    Label(root_frame, text="Scatter Matrix's", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20, width=599)
    buttons = [{"name": "Man City Scatter Matrix", "func_name": "runGraph1p2"},
               {"name": "Liverpool Scatter MAtrix", "func_name": "runGraph2p2"}]
    create_buttons1(root, root_frame, buttons, 1)
    create_back_button(root)
    mainloop()


def StatAnalysis():
    Button(root, text="Exit", command=Main)
    root.title('Data Analysis')
    root.geometry("1200x800")
    upper_frame = Frame(root, bg='#4c8a27', bd=5, )
    upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.8, anchor="n")
    root_frame = Frame(root, bg='#4c8a27')
    root_frame.place(relx=0.5, rely=0.0, relheight=1, relwidth=1, anchor='n')
    Label(root_frame, text="Statistical Analysis", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20,
                                                                                                   width=599)
    buttons = [{"name": "Home Form", "func_name": "runGraph1p4"},
               {"name": "Away Form", "func_name": "runGraph2p4"}]
    create_buttons1(root, root_frame, buttons, 1)
    create_back_button(root)
    mainloop()


def DataAnalysis():
    Button(root, text="Exit", command=Main)
    root.title('Data Analysis')
    root.geometry("1200x800")
    upper_frame = Frame(root, bg='#4c8a27', bd=5, )
    upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.8, anchor="n")
    root_frame = Frame(root, bg='#4c8a27')
    root_frame.place(relx=0.5, rely=0.0, relheight=1, relwidth=1, anchor='n')
    Label(root_frame, text="Data Analysis", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20, width=599)
    buttons = [{"name": "Measuring Home Advantage", "func_name": "HomeAdvantage"},
               {"name": "Displaying feature strength", "func_name": "Scatter"},
               {"name": "Analysing average goals scored", "func_name": "runGraph1p3"},
               {"name": "Home and Away form comparison", "func_name": "StatAnalysis"}]

    create_buttons1(root, root_frame, buttons, 1)
    create_back_button(root)
    mainloop()


def SelectGameweek():
    Button(root, text="Exit", command=Main)
    root.title('Select Gameweek')
    root.geometry("1200x800")
    upper_frame = Frame(root, bg='#4c8a27', bd=5, )
    upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.8, anchor="n")
    root_frame = Frame(root, bg='#4c8a27')
    root_frame.place(relx=0.5, rely=0.0, relheight=1, relwidth=1, anchor='n')
    Label(root_frame, text="Select Gameweek", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20, width=599)
    buttons = [{"name": "Gameweek 30", "func_name": "Gameweek30"},
               {"name": "Gameweek 31", "func_name": "Gameweek31"},
               {"name": "Gameweek 32", "func_name": "Gameweek32"},
               {"name": "Gameweek 33", "func_name": "Gameweek33"}]

    create_buttons1(root, root_frame, buttons, 1)
    create_back_button(root)
    mainloop()


def Gameweek30():
    Button(root, text="Exit", command=Main)
    root.title('Probable Scoreline')
    root.geometry("1200x800")
    upper_frame = Frame(root, bg='#4c8a27')
    upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.8, anchor="n")

    lower_frame = Frame(root, bg='#4c8a27', bd=2, )
    lower_frame.place(relx=0.5, rely=0.5, relheight=0.2, relwidth=0.8, anchor="n")

    root_frame = Frame(root, bg='#4c8a27')
    root_frame.place(relx=0.5, rely=0.0, relheight=0.8, relwidth=1, anchor='n')

    Label(root_frame, text="GameWeek 30", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20, width=599)

    buttons = [{"name": "Chelsea vs West Brom", "func_name": "runCheWBA1"},
               {"name": "Leeds vs Sheffield", "func_name": "runLeeShu1"},
               {"name": "Leicester vs Man City", "func_name": "runLeiMci1"},
               {"name": "Arsenal vs Liverpool", "func_name": "runArsLiv1"},
               {"name": "Southampton vs Burnley", "func_name": "runSouBur1"},
               {"name": "Newcastle vs Tottenham", "func_name": "runNewTot1"},
               {"name": "Aston Villa vs Fulham", "func_name": "runAvlFul1"},
               {"name": "Man United vs Brighton", "func_name": "runMunBri1"},
               {"name": "Everton vs Crystal Palace", "func_name": "runEveCry1"}]

    create_buttons1(root, root_frame, buttons, 1)
    create_back_button(root)
    mainloop()


def Gameweek31():
    Button(root, text="Exit", command=Main)
    root.title('Probable Scoreline')
    root.geometry("1200x800")
    upper_frame = Frame(root, bg='#4c8a27')
    upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.8, anchor="n")

    lower_frame = Frame(root, bg='#4c8a27', bd=2, )
    lower_frame.place(relx=0.5, rely=0.5, relheight=0.2, relwidth=0.8, anchor="n")

    root_frame = Frame(root, bg='#4c8a27')
    root_frame.place(relx=0.5, rely=0.0, relheight=0.8, relwidth=1, anchor='n')

    Label(root_frame, text="GameWeek 31", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20, width=599)

    buttons = [{"name": "Man City vs Leeds", "func_name": "runMciLee1"},
               {"name": "Liverpool vs Aston Villa", "func_name": "runLivAvl1"},
               {"name": "Crystal Palace vs Chelsea", "func_name": "runCryChe1"},
               {"name": "Burnley vs Newcastle", "func_name": "runBurNew1"},
               {"name": "West Ham vs Leicester", "func_name": "runWhuLei1"},
               {"name": "Tottenham vs Man United", "func_name": "runTotMun1"},
               {"name": "Sheffield vs Arsenal", "func_name": "runShuArs1"},
               {"name": "West Brom vs Southampton", "func_name": "runWbaSou1"},
               {"name": "Brighton vs Everton", "func_name": "runBriEve1"}]

    create_buttons1(root, root_frame, buttons, 1)
    create_back_button(root)
    mainloop()


def Gameweek32():
    Button(root, text="Exit", command=Main)
    root.title('Probable Scoreline')
    root.geometry("1200x800")
    upper_frame = Frame(root, bg='#4c8a27')
    upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.8, anchor="n")

    lower_frame = Frame(root, bg='#4c8a27', bd=2, )
    lower_frame.place(relx=0.5, rely=0.5, relheight=0.2, relwidth=0.8, anchor="n")

    root_frame = Frame(root, bg='#4c8a27')
    root_frame.place(relx=0.5, rely=0.0, relheight=0.8, relwidth=1, anchor='n')

    Label(root_frame, text="GameWeek 32", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20, width=599)

    buttons = [{"name": "Newcastle vs West Ham", "func_name": "runNewWhu1"},
               {"name": "Wolves vs Sheffield", "func_name": "runWolShu1"},
               {"name": "Arsenal vs Fulham", "func_name": "runArsFul1"},
               {"name": "Man United vs Burnley", "func_name": "runMunBur1"},
               {"name": "Leeds vs Liverpool", "func_name": "runLeeLiv1"},
               {"name": "Chelsea vs Brighton", "func_name": "runCheBri1"},
               {"name": "Tottenham vs Southampton", "func_name": "runTotSou1"},
               {"name": "Aston Villa vs Man City", "func_name": "runAvlMci1"}]

    create_buttons1(root, root_frame, buttons, 1)
    create_back_button(root)
    mainloop()


def Gameweek33():
    Button(root, text="Exit", command=Main)
    root.title('Probable Scoreline')
    root.geometry("1200x800")
    upper_frame = Frame(root, bg='#4c8a27')
    upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.8, anchor="n")

    lower_frame = Frame(root, bg='#4c8a27', bd=2, )
    lower_frame.place(relx=0.5, rely=0.5, relheight=0.2, relwidth=0.8, anchor="n")

    root_frame = Frame(root, bg='#4c8a27')
    root_frame.place(relx=0.5, rely=0.0, relheight=0.8, relwidth=1, anchor='n')

    Label(root_frame, text="GameWeek 33", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20, width=599)

    buttons = [{"name": "Liverpool vs Newcastle", "func_name": "runLivNew1"},
               {"name": "West Ham vs Chelsea", "func_name": "runWhuChe1"},
               {"name": "Sheffield vs Brighton", "func_name": "runShuBri1"},
               {"name": "Wolves vs Burnley", "func_name": "runWolBur1"},
               {"name": "Leeds vs Man United", "func_name": "runLeeMun1"},
               {"name": "Aston Villa vs West Brom", "func_name": "runAvlWba1"},
               {"name": "Leicester vs Crystal Palace", "func_name": "runLeiCry1"}]

    create_buttons1(root, root_frame, buttons, 1)
    create_back_button(root)
    mainloop()


def ELOModel():
    Button(root, text="Exit", command=Main)
    root.title('Select Gameweek')
    root.geometry("1200x800")
    upper_frame = Frame(root, bg='#4c8a27', bd=5, )
    upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.8, anchor="n")
    root_frame = Frame(root, bg='#4c8a27')
    root_frame.place(relx=0.5, rely=0.0, relheight=1, relwidth=1, anchor='n')
    Label(root_frame, text="Uses ELO data to predict the winning team", font="AutobusBold 15 bold", bg="#add8e6").place(
        x=300, y=20, width=599)
    buttons = []
    create_buttons1(root, root_frame, buttons, 1)
    create_back_button(root)
    from aaa.model3 import start1
    start1(root_frame)
    mainloop()


def Main():
    main_frame = LabelFrame(root, bg='#4c8a27', bd=5)
    main_frame.place()
    upper_frame = Frame(root, bg='#4c8a27', bd=5, )
    upper_frame.place(relx=0.5, rely=0.01, relheight=0.2, relwidth=0.98, anchor="n")
    apps_label = Label(upper_frame, text='Premier League Prediction System', font=("AutobusBold 40 bold"), bg="#4c8a27")
    apps_label.place(relheight=0.5, relwidth=1)
    lower_frame = Frame(root, bg='#4c8a27', bd=5)
    lower_frame.place(relx=0.5, rely=0.1, relheight=0.7, relwidth=0.8, anchor='n')
    apps_label2 = Label(lower_frame, font=('Autobus Bold', 40), bg="#4c8a27")
    apps_label2.place(relheight=1, relwidth=1)
    buttons = [{"name": "Data Analysis", "func_name": "DataAnalysis"},
               {"name": "Analysing Models", "func_name": "TestAccuracy"},
               {"name": "Model 1", "func_name": "SelectGameweek"},
               {"name": "Model 2", "func_name": "runSearch"},
               {"name": "ELO Model", "func_name": "ELOModel"},
               {"name": "Results", "func_name": "Results"}]

    create_buttons(root, lower_frame, buttons, 2)
    Label(lower_frame,
          text="Data Analysis\nCarries out pre-processing to conduct analysis on the initial dataset \nAnalysing Models\nUtilises ANN, SVC, Regression, XGB and Random Forest algorithms to predict the 2021 season using statistics\nModel 1\nPredicts fixtures using SIMEON DENIS Poisson regression, this is then analysed against bookmakers\nModel 2\nPredicts fixtures using Poisson regression using an enhanced dataset with additional features\nELO Model\nUses ELO data to determine the accuracy ELO data has on predicting results",
          bg="#32CD32", fg='black', font="Autobus 12 bold").place(x=30, y=425, anchor="w")

    label = Label(lower_frame, bg='#32CD32',
                  text="Features used \nHomeTeam = Home Team \nAwayTeam = Away Team \nMW = Match week \nFTHG = Full Time Home Team Goals \nFTAG = Full Time Away Team Goals \nFTR = Full Time Result (H=Home Win, D=Draw, A=Away Win) \nHTHG = Half Time Home Team Goals \nHTAG = Half Time Away Team Goals \nHTR = Half Time Result (H=Home Win, D=Draw, A=Away Win)\n \nMatch Statistics \nHST = Home Team Shots on Target \nAST = Away Team Shots on Target \nHC = Home Team Corners \nAC = Away Team Corners \nHY = Home Team Yellow Cards \nAY = Away Team Yellow Cards \nHR = Home Team Red Cards \nAR = Away Team Red Cards \nB365H = Bet365 home win odds \nB365D = Bet365 draw odds \nB365A = Bet365 away win odds \nELO Home = ELO home rating \nELO Away = ELO away rating \nHM1Conv = Previous game result converted to int \nHomeTeamLP = Home team league position \nAwayTeamLP = Away team league position")

    def labeldeactive():
        label.pack_forget()

    def labelactive():
        label.pack(fill=BOTH)

        label.pack()

    lower_frame2 = Frame(root, bg='#4c8a27', bd=5)
    lower_frame2.place(relx=0.5, rely=0.76, relheight=0.1, relwidth=0.8, anchor='n')
    Button(lower_frame2, text="Features Used", state="normal", fg='black', bg="#add8e6", anchor=CENTER,
           command=labelactive).pack(side=BOTTOM)
    Button(lower_frame2, text="Hide Feature section", state="normal", fg='black', bg="#add8e6", anchor=CENTER,
           command=labeldeactive).pack(side=BOTTOM)
    root.mainloop()


Main()
