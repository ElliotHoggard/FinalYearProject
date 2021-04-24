from os import listdir
import pandas as pd

Filepath = ['./Dat1/' + f for f in listdir("./Dat1") if f.endswith('.csv')]
premier = pd.concat(map(pd.read_csv, Filepath), ignore_index=True, sort=False)
leagueData = pd.DataFrame(premier, columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

MCIHome = leagueData.loc[leagueData['HomeTeam'] == 'Man City']
MCIAway = leagueData.loc[leagueData['AwayTeam'] == 'Man City']
MCIHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
MCIAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
MCIOGoals = MCIHome["Offence"].append(MCIAway["Offence"])
MCIDGoals = MCIHome["Defence"].append(MCIAway["Defence"])

MUNHome = leagueData.loc[leagueData['HomeTeam'] == 'Man United']
MUNAway = leagueData.loc[leagueData['AwayTeam'] == 'Man United']
MUNHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
MUNAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
MUNOGoals = MUNHome["Offence"].append(MUNAway["Offence"])
MUNDGoals = MUNHome["Defence"].append(MUNAway["Defence"])

LEIHome = leagueData.loc[leagueData['HomeTeam'] == 'Leicester']
LEIAway = leagueData.loc[leagueData['AwayTeam'] == 'Leicester']
LEIHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
LEIAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
LEIOGoals = LEIHome["Offence"].append(LEIAway["Offence"])
LEIDGoals = LEIHome["Defence"].append(LEIAway["Defence"])

CHEHome = leagueData.loc[leagueData['HomeTeam'] == 'Chelsea']
CHEAway = leagueData.loc[leagueData['AwayTeam'] == 'Chelsea']
CHEHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
CHEAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
CHEOGoals = CHEHome["Offence"].append(CHEAway["Offence"])
CHEDGoals = CHEHome["Defence"].append(CHEAway["Defence"])

WHUHome = leagueData.loc[leagueData['HomeTeam'] == 'West Ham']
WHUAway = leagueData.loc[leagueData['AwayTeam'] == 'West Ham']
WHUHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
WHUAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
WHUOGoals = WHUHome["Offence"].append(WHUAway["Offence"])
WHUDGoals = WHUHome["Defence"].append(WHUAway["Defence"])

TOTHome = leagueData.loc[leagueData['HomeTeam'] == 'Tottenham']
TOTAway = leagueData.loc[leagueData['AwayTeam'] == 'Tottenham']
TOTHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
TOTAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
TOTOGoals = TOTHome["Offence"].append(TOTAway["Offence"])
TOTDGoals = TOTHome["Defence"].append(TOTAway["Defence"])

LIVHome = leagueData.loc[leagueData['HomeTeam'] == 'Liverpool']
LIVAway = leagueData.loc[leagueData['AwayTeam'] == 'Liverpool']
LIVHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
LIVAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
LIVOGoals = LIVHome["Offence"].append(LIVAway["Offence"])
LIVDGoals = LIVHome["Defence"].append(LIVAway["Defence"])

EVEHome = leagueData.loc[leagueData['HomeTeam'] == 'Everton']
EVEAway = leagueData.loc[leagueData['AwayTeam'] == 'Everton']
EVEHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
EVEAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
EVEOGoals = EVEHome["Offence"].append(EVEAway["Offence"])
EVEDGoals = EVEHome["Defence"].append(EVEAway["Defence"])

ARSHome = leagueData.loc[leagueData['HomeTeam'] == 'Arsenal']
ARSAway = leagueData.loc[leagueData['AwayTeam'] == 'Arsenal']
ARSHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
ARSAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
ARSOGoals = ARSHome["Offence"].append(ARSAway["Offence"])
ARSDGoals = ARSHome["Defence"].append(ARSAway["Defence"])

AVLHome = leagueData.loc[leagueData['HomeTeam'] == 'Aston Villa']
AVLAway = leagueData.loc[leagueData['AwayTeam'] == 'Aston Villa']
AVLHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
AVLAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
AVLOGoals = AVLHome["Offence"].append(AVLAway["Offence"])
AVLDGoals = AVLHome["Defence"].append(AVLAway["Defence"])

LEEHome = leagueData.loc[leagueData['HomeTeam'] == 'Leeds']
LEEAway = leagueData.loc[leagueData['AwayTeam'] == 'Leeds']
LEEHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
LEEAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
LEEOGoals = LEEHome["Offence"].append(LEEAway["Offence"])
LEEDGoals = LEEHome["Defence"].append(LEEAway["Defence"])

CRYHome = leagueData.loc[leagueData['HomeTeam'] == 'Crystal Palace']
CRYAway = leagueData.loc[leagueData['AwayTeam'] == 'Crystal Palace']
CRYHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
CRYAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
CRYOGoals = CRYHome["Offence"].append(CRYAway["Offence"])
CRYDGoals = CRYHome["Defence"].append(CRYAway["Defence"])

WOLHome = leagueData.loc[leagueData['HomeTeam'] == 'Wolves']
WOLAway = leagueData.loc[leagueData['AwayTeam'] == 'Wolves']
WOLHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
WOLAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
WOLOGoals = WOLHome["Offence"].append(WOLAway["Offence"])
WOLDGoals = WOLHome["Defence"].append(WOLAway["Defence"])

SOUHome = leagueData.loc[leagueData['HomeTeam'] == 'Southampton']
SOUAway = leagueData.loc[leagueData['AwayTeam'] == 'Southampton']
SOUHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
SOUAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
SOUOGoals = SOUHome["Offence"].append(SOUAway["Offence"])
SOUDGoals = SOUHome["Defence"].append(SOUAway["Defence"])

BURHome = leagueData.loc[leagueData['HomeTeam'] == 'Burnley']
BURAway = leagueData.loc[leagueData['AwayTeam'] == 'Burnley']
BURHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
BURAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
BUROGoals = BURHome["Offence"].append(BURAway["Offence"])
BURDGoals = BURHome["Defence"].append(BURAway["Defence"])

BRIHome = leagueData.loc[leagueData['HomeTeam'] == 'Brighton']
BRIAway = leagueData.loc[leagueData['AwayTeam'] == 'Brighton']
BRIHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
BRIAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
BRIOGoals = BRIHome["Offence"].append(BRIAway["Offence"])
BRIDGoals = BRIHome["Defence"].append(BRIAway["Defence"])

NEWHome = leagueData.loc[leagueData['HomeTeam'] == 'Newcastle']
NEWAway = leagueData.loc[leagueData['AwayTeam'] == 'Newcastle']
NEWHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
NEWAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
NEWOGoals = NEWHome["Offence"].append(NEWAway["Offence"])
NEWDGoals = NEWHome["Defence"].append(NEWAway["Defence"])

FULHome = leagueData.loc[leagueData['HomeTeam'] == 'Fulham']
FULAway = leagueData.loc[leagueData['AwayTeam'] == 'Fulham']
FULHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
FULAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
FULOGoals = FULHome["Offence"].append(FULAway["Offence"])
FULDGoals = FULHome["Defence"].append(FULAway["Defence"])

WBAHome = leagueData.loc[leagueData['HomeTeam'] == 'West Brom']
WBAAway = leagueData.loc[leagueData['AwayTeam'] == 'West Brom']
WBAHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
WBAAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
WBAOGoals = WBAHome["Offence"].append(WBAAway["Offence"])
WBADGoals = WBAHome["Defence"].append(WBAAway["Defence"])

SHUHome = leagueData.loc[leagueData['HomeTeam'] == 'Sheffield United']
SHUAway = leagueData.loc[leagueData['AwayTeam'] == 'Sheffield United']
SHUHome.rename(columns={'FTHG': 'Offence', 'FTAG': 'Defence'}, inplace=True)
SHUAway.rename(columns={'FTHG': 'Defence', 'FTAG': 'Offence'}, inplace=True)
SHUOGoals = SHUHome["Offence"].append(SHUAway["Offence"])
SHUDGoals = SHUHome["Defence"].append(SHUAway["Defence"])
