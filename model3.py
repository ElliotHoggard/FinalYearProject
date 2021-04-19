import pandas as pd
import requests
from bs4 import BeautifulSoup
from tkinter import *
import tkinter as tk

def part2(data, root_frame, Home_team, Away_team):
    england = pd.DataFrame(data, columns=['Rank', 'Club', 'Elo', ' ','Last Match', 'Coach'])
    Team1 = england[england['Club'] == Home_team]['Elo'].values
    Team2 = england[england['Club'] == Away_team]['Elo'].values
    team1_elo = int(Team1)
    team2_elo = int(Team2)
    elo_diff = team1_elo - team2_elo

    Label(root_frame, text="Using ELO data to predict " + str(Home_team) + " vs " + str(Away_team) , font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=20, width=599)
    Label(root_frame, text="" + str(Home_team) + " have a " + str(prob_of_winning(elo_diff)) + "chance of winning\n"  + str(Away_team) + " have a " + str(prob_of_winning(-elo_diff)) + "chance of winning", font="AutobusBold 15 bold", bg="#add8e6").place(x=300, y=50, width=599)
    root_frame.mainloop()

def prob_of_winning(elo_differential):
    m=(-elo_differential)/400
    return 1/(1+10**m)

def start1(root_frame):
    lower_frame = Frame(root_frame, bg='#4c8a27', bd=2, )
    lower_frame.place(relx=0.5, rely=0.3, relheight=0.2, relwidth=0.8, anchor="n")

    def print_selection():
        value = lb.get(lb.curselection())
        Home_team = value
        start2(root_frame,Home_team)

    var2 = tk.StringVar()
    lb = tk.Listbox(lower_frame, listvariable=var2)
    b1 = tk.Button(lower_frame, text='Home Team', pady=5, padx=10, bg="#add8e6", width=15, height=1, command=print_selection)
    b1.pack()
    list_items = ['1 Man City', '4 Man United', '18 Leicester', '20 West Ham', '9 Chelsea', '6 Liverpool', '16 Tottenham', '28 Everton',
                  '44 Leeds', '39 Aston Villa', '15 Arsenal', '30 Wolves', '50 Crystal Palace', '46 Southampton', '40 Burnley', '52 Brighton',
                  '63 Newcastle', '76 Fulham', '96 West Brom', '91 Sheffield United']
    for item in list_items:
        lb.insert('end', item)
    lb.pack(padx=5,pady=5,fill=tk.BOTH,expand=True)


def start2(root_frame, Home_team):
    lower_frame = Frame(root_frame, bg='#4c8a27', bd=2, )
    lower_frame.place(relx=0.5, rely=0.3, relheight=0.2, relwidth=0.8, anchor="n")

    def print_selection():
        value = lb.get(lb.curselection())
        Away_team = value
        start(Home_team, Away_team, root_frame)

    var2 = tk.StringVar()
    lb = tk.Listbox(lower_frame, listvariable=var2)
    b1 = tk.Button(lower_frame, text='Away Team', pady=5, padx=10, bg="#add8e6", width=15, height=1, command=print_selection)
    b1.pack()
    list_items = ['1 Man City', '4 Man United', '18 Leicester', '20 West Ham', '9 Chelsea', '6 Liverpool', '16 Tottenham', '28 Everton',
                  '44 Leeds', '39 Aston Villa', '15 Arsenal', '30 Wolves', '50 Crystal Palace', '46 Southampton', '40 Burnley', '52 Brighton',
                  '63 Newcastle', '76 Fulham', '96 West Brom', '91 Sheffield United']
    for item in list_items:
        lb.insert('end', item)
    lb.pack(padx=5,pady=5,fill=tk.BOTH,expand=True)

def start(Home_team, Away_team, root_frame):
    url = 'http://clubelo.com/ENG/Ranking'

    r = requests.get(url)
    html = r.text

    soup = BeautifulSoup(html)
    table = soup.find('table', {"class": "ranking"})
    rows = table.find_all('tr')
    data = []
    for row in rows[1:]:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    part2(data, root_frame, Home_team, Away_team)
