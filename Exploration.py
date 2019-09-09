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
    GROUP BY m.date;""".format(i + 1, i + 1), conn)
    match_df = pd.concat([match_df, df], axis=1)
match_df['avg_overall_rating'] = match_df.drop(
    ['home_goals', 'away_goals', 'shots_on', 'shots_off', 'fouls_commit', 'possession'], axis=1).mean(axis=1)
match_df.drop(['p1_rating', 'p2_rating', 'p3_rating', 'p4_rating',
               'p5_rating', 'p6_rating', 'p7_rating', 'p8_rating', 'p9_rating',
               'p10_rating', 'p11_rating'], axis=1, inplace=True)
match_df.dropna(subset=['avg_overall_rating'], inplace=True)

match_df.dropna(inplace=True)
match_df = match_df.loc[match_df.home_goals != match_df.away_goals]  # Only interested in games with a winner
match_df['home_win'] = 0
match_df.loc[(match_df.home_goals > match_df.away_goals), 'home_win'] = 1
match_df.home_win = match_df.home_win.astype(bool)


def xml_count_extract(series, series_id, count=pd.Series()):
    """ Extracts count of occurrences of the team_id from the XML """
    for i in range(len(series)):
        try:
            root = ET.fromstring(series.iloc[i])
            counter = 0
            for value in root.findall('value'):
                if int(value.find('team').text) == series_id.iloc[i]:
                    counter += 1
            count.at[i] = counter
        except (TypeError, AttributeError) as error:
            count.at[i] = None
            continue
    return count


shots = xml_count_extract(winner_df.shots_on, winner_df.team_id)

match_df.shots_on = pd.concat((match_df, shots.rename('shots_on')), axis=1)
match_df.shots_on = match_df.shots_on.astype(int)
home_win_df = match_df.loc[match_df.home_win == 1]
away_win_df = match_df.loc[match_df.home_win == 0]

df.rename()

for df in both_df:
    df['avg_overall_rating'] = df.drop(['team_id', 'shots_on', 'shots_off', 'fouls_commit', 'possession', 'home_win'],
                                       axis=1).mean(axis=1)
    df.drop(['p1_rating', 'p2_rating', 'p3_rating', 'p4_rating',
             'p5_rating', 'p6_rating', 'p7_rating', 'p8_rating', 'p9_rating',
             'p10_rating', 'p11_rating'], axis=1, inplace=True)


def DropUnimportant(df, home):
    """Drops rows that are not needed for the DataFrame and renames columns to make them consistent across DataFrames."""
    columns = ['team_id', 'shots_on', 'shots_off', 'fouls_commit',
               'possession', 'p1_rating', 'p2_rating', 'p3_rating', 'p4_rating',
               'p5_rating', 'p6_rating', 'p7_rating', 'p8_rating', 'p9_rating',
               'p10_rating', 'p11_rating', 'home_win']
    if home:
        df.drop(['id', 'home_goals', 'away_goals', 'away_id', 'ap1_rating', 'ap2_rating', 'ap3_rating',
                 'ap4_rating', 'ap5_rating', 'ap6_rating', 'ap7_rating', 'ap8_rating',
                 'ap9_rating', 'ap10_rating', 'ap11_rating'], axis=1, inplace=True)
        df.columns = columns
    else:
        df.drop(['id', 'home_goals', 'away_goals', 'home_id', 'hp1_rating', 'hp2_rating', 'hp3_rating', 'hp4_rating',
                 'hp5_rating', 'hp6_rating', 'hp7_rating', 'hp8_rating', 'hp9_rating',
                 'hp10_rating', 'hp11_rating'], axis=1, inplace=True)
        df.columns = columns
    return df


for value, char in zip(('home', 'away'), ('h', 'a')):  # Adds the Overall Rating for every player in the match.
    for i in range(11):
        df = pd.read_sql("""SELECT m.id AS id, p.overall_rating AS {}p{}_rating
                            FROM Match m
                            JOIN Player_Attributes p
                            ON p.player_api_id = m.{}_player_{} AND m.date >= p.date
                            GROUP BY m.date;""".format(char, i + 1, value, i + 1), conn)
        match_df = match_df.merge(df, how='outer')
