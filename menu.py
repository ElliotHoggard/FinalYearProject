from functools import partial
from tkinter import *
from tkhtmlview import HTMLLabel

# Create the GUI
global root
root = Tk()
root.title('Premier League Prediction System')
root.geometry("1200x800")
root.configure(bg="#4c8a27")
# Button format for menu
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
                           font=('Autobus Bold bold', 20), relief=GROOVE,command=partial(button_click, buttons_list, i)))
                buttons[-1].place(relx=0.05,rely=0.01 + (0.005 + b_height) * (left_i - 1),relheight=0.15,relwidth=0.4)
            else:
                right_i += 1
                buttons.append(
                    Button(parent_frame, text=(buttons_list[i]["name"]), bg='#add8e6', fg='Black',font=('Autobus Bold bold', 20),
                           relief=GROOVE, command=partial(button_click, buttons_list, i)))
                buttons[-1].place(relx=0.5,rely=0.01 + (0.005 + b_height) * (left_i - 1),relheight=0.15,relwidth=0.4)
        elif column_num == 1:
            buttons.append(
                Button(parent_frame, text=(buttons_list[i]["name"]), bg='#add8e6', fg='Black',
                       font=('Autobus Bold bold', 20),
                       relief=GROOVE,
                       command=partial(button_click, buttons_list, i)))
            buttons[-1].place(relx=0.05,rely=0.01 + (0.005 + b_height),relheight=0.15,relwidth=0.4)


# Button format for submenu
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


# return to menu button
def create_back_button(parent_frame):
    back_button = Button(parent_frame, text='←', bg="Black", fg="White", font=('Autobus Bold bold', 30), command=Main)
    back_button.place(relx=0.01, rely=0.01, relheight=0.05, relwidth=0.1)
    main_frame = LabelFrame(root, bg='blue', bd=5)
    main_frame.place()


# Button function for model 2
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


# Display results from my two models
def Results():
    Button(root, text="Exit", command=Main)
    root.title('Results')
    root.geometry("1200x800")
    upper_frame = Frame(root, bg='#4c8a27', bd=5, )
    upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.8, anchor="n")
    root_frame = Frame(root, bg='#4c8a27')
    lower_frame = Frame(root, bg='#4c8a27', bd=2, )
    lower_frame.place(relx=0.5, rely=0.1, relheight=0.15, relwidth=1, anchor="n")
    create_back_button(root_frame)
    root_frame.place(relx=0.5, rely=0.0, relheight=1, relwidth=1, anchor='n')
    Label(root_frame, text="Click on the link 'Click to view all results' to open up a Google sheets with all results", bg='#4c8a27', font="AutobusBold 12 bold").place(x=275, y=60)
    Label(root_frame, text="Click to view all results", bg='#add8e6', font="AutobusBold 15 bold").place(x=300, y=20, width=599)
    HTMLLabel(lower_frame, state="normal", fg='black', font="AutobusBold 30 bold", bg='#add8e6',
              html='<a href="https://docs.google.com/spreadsheets/d/1cn8pl7UIQzIvn65ByVGZq8QswEd-FMTGybK50ab84pk/edit?usp=sharing"> Click to view the '
                   'Results </a>').place(
        x=300, y=50, width=599)
    create_back_button(root)
    root.mainloop()


# Game Week 30 fixtures model 1
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


# Game Week 31 fixtures model 1
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


# Game Week 32 fixtures model 1
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


# Game Week 33 fixtures model 1
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


# Game Week 34 fixtures model 1
def runCryMci1():
    from aaa.model1GW34 import CryMci1
    CryMci1()


def runBriLee1():
    from aaa.model1GW34 import BriLee1
    BriLee1()


def runCheFul1():
    from aaa.model1GW34 import CheFul1
    CheFul1()


def runEveAvl1():
    from aaa.model1GW34 import EveAvl1
    EveAvl1()


def runLeeMun1():
    from aaa.model1GW34 import LeeMun1
    LeeMun1()


def runNewArs1():
    from aaa.model1GW34 import NewArs1
    NewArs1()


def runMunLiv1():
    from aaa.model1GW34 import MunLiv1
    MunLiv1()

# Model testing for model analysis

def runLogistic():
    from aaa.modelanalysis import LogRegression
    LogRegression()


def runSVC():
    from aaa.modelanalysis import SVC
    SVC()


def runXGB():
    from aaa.modelanalysis import XGB
    XGB()


def runANN():
    from aaa.modelanalysis import ANN
    ANN()


def runRandForest():
    from aaa.modelanalysis import RandForest
    RandForest()


def runFeatureRating():
    from aaa.modelanalysis import FeatureRating
    FeatureRating()


# Pre-processing graphs
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


# GUI for model analysis
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
               {"name": "Logistic Regression", "func_name": "runLogistic"},
               {"name": "ELO Model", "func_name": "ELOModel"}]
    create_buttons1(root, root_frame, buttons, 1)
    create_back_button(root)
    mainloop()


# Model analysis sub menu
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


# Model analysis sub menu
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


# Model analysis sub menu
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


# Model analysis sub menu
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


# Model 1 select GW
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
               {"name": "Gameweek 33", "func_name": "Gameweek33"},
               {"name": "Gameweek 34", "func_name": "Gameweek34"}]
    create_buttons1(root, root_frame, buttons, 1)
    create_back_button(root)
    mainloop()


# Model 1 GW 30
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
    Label(root_frame, text="Game Week 30", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20, width=599)
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


# Model 1 GW 31
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
    Label(root_frame, text="Game Week 31", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20, width=599)
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


# Model 1 GW 32
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
    Label(root_frame, text="Game Week 32", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20, width=599)
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


# Model 1 GW 33
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
    Label(root_frame, text="Game Week 33", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20, width=599)
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


def Gameweek34():
    Button(root, text="Exit", command=Main)
    root.title('Probable Scoreline')
    root.geometry("1200x800")
    upper_frame = Frame(root, bg='#4c8a27')
    upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.8, anchor="n")
    lower_frame = Frame(root, bg='#4c8a27', bd=2, )
    lower_frame.place(relx=0.5, rely=0.5, relheight=0.2, relwidth=0.8, anchor="n")
    root_frame = Frame(root, bg='#4c8a27')
    root_frame.place(relx=0.5, rely=0.0, relheight=0.8, relwidth=1, anchor='n')
    Label(root_frame, text="Game Week 34", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20, width=599)
    buttons = [{"name": "Crystal Palace vs Man City", "func_name": "runCryMci1"},
               {"name": "Brighton vs Leeds", "func_name": "runBriLee1"},
               {"name": "Chelsea vs Fulham", "func_name": "runCheFul1"},
               {"name": "Everton vs Aston Villa", "func_name": "runEveAvl1"},
               {"name": "Newcastle vs Arsenal", "func_name": "runNewArs1"},
               {"name": "Man United vs Liverpool", "func_name": "runMunLiv1"}]
    create_buttons1(root, root_frame, buttons, 1)
    create_back_button(root)
    mainloop()


# ELO model 3 model
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


# Quit the program
def close():
    root.destroy()


# main function with main menu contents
def Main():
    main_frame = LabelFrame(root, bg='#4c8a27', bd=5)
    main_frame.place()
    upper_frame = Frame(root, bg='#4c8a27', bd=5, )
    upper_frame.place(relx=0.48, rely=0.01, relheight=0.2, relwidth=0.98, anchor="n")
    apps_label = Label(upper_frame, text='Premier League Prediction System', font=("AutobusBold 40 bold"), bg="#4c8a27")
    apps_label.place(relheight=0.5, relwidth=1)
    lower_frame = Frame(root, bg='#4c8a27', bd=5)
    lower_frame.place(relx=0.5, rely=0.1, relheight=0.7, relwidth=0.8, anchor='n')
    apps_label2 = Label(lower_frame, font=('Autobus Bold', 40), bg="#4c8a27")
    apps_label2.place(relheight=1, relwidth=1)
    buttons = [{"name": "Data Analysis", "func_name": "DataAnalysis"},
               {"name": "Model Accuracies", "func_name": "TestAccuracy"},
               {"name": "Model 1", "func_name": "SelectGameweek"},
               {"name": "Model 2", "func_name": "runSearch"},
               {"name": "Results", "func_name": "Results"},
               {"name": "Quit", "func_name": "close"}]
    create_buttons(root, lower_frame, buttons, 2)
    Label(lower_frame,
          text="Data Analysis\nCarries out pre-processing and creates an initial ELO model for analysis purposes "
               "using the initial dataset \n Model Accuracies\nUtilises an ANN, a SVC, a Logistic Regression model, "
               "a XGB Classifier model and a Random Forest \nalgorithm to predict the 2019/2020 season. This measures "
               "the accuracies to determine the chosen model \nModel 1\nPredicts fixtures using Simeon Denis Poisson "
               "Regression, \nthe results are then analysed against bookmakers and provide recommendations\nModel "
               "2\nPredicts fixtures by carrying out Poisson Regression with an enhanced dataset\nResults\nDisplays "
               "the results of both models in relation to the bookmakers Betway and Tipico",
          bg="#32CD32", fg='black', font="Autobus 10 bold").place(x=100, y=425, anchor="w")

    label = Label(lower_frame, bg='#32CD32',
                  text="Features used \nHomeTeam = Home Team \nAwayTeam = Away Team \nMW = Match week \nFTHG = Full "
                       "Time Home Team Goals \nFTAG = Full Time Away Team Goals \nFTR = Full Time Result (H=Home Win, "
                       "D=Draw, A=Away Win) \nHTHG = Half Time Home Team Goals \nHTAG = Half Time Away Team Goals "
                       "\nHTR = Half Time Result (H=Home Win, D=Draw, A=Away Win)\n \nMatch Statistics \nHST = Home "
                       "Team Shots on Target \nAST = Away Team Shots on Target \nHC = Home Team Corners \nAC = Away "
                       "Team Corners \nHY = Home Team Yellow Cards \nAY = Away Team Yellow Cards \nHR = Home Team Red "
                       "Cards \nAR = Away Team Red Cards \nB365H = Bet365 home win odds \nB365D = Bet365 draw odds "
                       "\nB365A = Bet365 away win odds \nELO Home = ELO home rating \nELO Away = ELO away rating "
                       "\nHM1Conv = Previous game result converted to int \nHomeTeamLP = Home team league position "
                       "\nAwayTeamLP = Away team league position")

    def LabelDeactive():
        # hide the features used pop up
        label.pack_forget()

    def LabelActive():
        # show the features used pop up
        label.pack(fill=BOTH)
        label.pack()

    lower_frame2 = Frame(root, bg='#4c8a27', bd=5)
    lower_frame2.place(relx=0.5, rely=0.76, relheight=0.1, relwidth=0.8, anchor='n')
    Button(lower_frame2, text="Features Used", state="normal", fg='black', bg="#add8e6", anchor=CENTER,
           command=LabelActive).pack(side=BOTTOM)
    Button(lower_frame2, text="Hide Feature section", state="normal", fg='black', bg="#add8e6", anchor=CENTER,
           command=LabelDeactive).pack(side=BOTTOM)
    root.mainloop()


Main()