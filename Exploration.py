import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbs
import sqlite3
from xml.etree import ElementTree as ET

conn = sqlite3.connect('database.sqlite')
match_df = pd.read_sql("""SELECT home_team_goal AS home_goals,
                               away_team_goal AS away_goals,
                               shoton AS shots_on,
                               shotoff AS shots_off,
                               foulcommit AS fouls_commit,
                               possession
                          FROM "Match";""", conn)
for i in range(11):
    df = pd.read_sql("""SELECT p.overall_rating AS p{}_rating
    FROM Match m
    JOIN Player_Attributes p
    ON p.player_api_id = m.home_player_{} AND m.date >= p.date
    GROUP BY m.date;""".format(i+1, i+1), conn)
    match_df = pd.concat([match_df, df], axis=1)
match_df['avg_overall_rating'] = match_df.drop(['home_goals', 'away_goals', 'shots_on', 'shots_off', 'fouls_commit', 'possession'], axis=1).mean(axis=1)
match_df.drop(['p1_rating', 'p2_rating', 'p3_rating', 'p4_rating',
       'p5_rating', 'p6_rating', 'p7_rating', 'p8_rating', 'p9_rating',
       'p10_rating', 'p11_rating'], axis=1, inplace=True)
match_df.dropna(subset=['avg_overall_rating'], inplace=True)

match_df.dropna(inplace=True)
match_df = match_df.loc[match_df.home_goals != match_df.away_goals]  # Only interested in games with a winner
match_df['home_win'] = 0
match_df.loc[(match_df.home_goals > match_df.away_goals), 'home_win'] = 1
match_df.home_win = match_df.home_win.astype(bool)


def xml_extract(series, series_id, find_str, count=pd.Series()):
    """ Extracts count of occurrences from the XML """
    for i in range(len(series)):
        root = ET.fromstring(series.iloc[i])
        values = root.findall('{}'.format(find_str))
        counter = 0
        for value in values:
            if value == series_id.iloc[i]:
                counter += 1
        count.at[i] = counter
    return count


shots = xml_extract(match_df.shots_on, match_df.home_id, './/id')

match_df.shots_on = pd.concat((match_df, shots.rename('shots_on')), axis=1)
match_df.shots_on = match_df.shots_on.astype(int)
home_win_df = match_df.loc[match_df.home_win == 1]
away_win_df = match_df.loc[match_df.home_win == 0]

df.rename()