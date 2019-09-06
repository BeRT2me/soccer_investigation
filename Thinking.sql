SELECT home_team_goal AS home_goals, away_team_goal AS away_goals, shoton AS shots_on, shotoff AS shots_off,
        foulcommit AS fouls_commit, card AS cards, "cross" AS crosses,
         corner AS corners, possession AS possession
FROM "Match";

SELECT home_player_1 FROM "Match" LIMIT 1000;
SELECT * FROM "Player" LIMIT 100;
SELECT * FROM "Player_Attributes" ORDER BY date DESC, player_api_id;

SELECT date from "Match" ORDER BY date DESC;

SELECT m.date,
    p.overall_rating AS p_rating
FROM Match m
JOIN Player_Attributes p
ON p.player_api_id = m.home_player_1 AND m.date = p.date;

SELECT p.overall_rating AS p1_rating
    FROM Match m
    JOIN Player_Attributes p
    ON p.player_api_id = m.home_player_1 AND m.date >= p.date
    GROUP BY m.date;

SELECT m.home_team_goal AS home_goals,
       m.away_team_goal AS away_goals,
       m.shoton AS shots_on,
       m.shotoff AS shots_off,
       m.foulcommit AS fouls_commit,
       m.possession,
       hp1.overall_rating as hp1_rating,
       hp2.overall_rating as hp2_rating,
       hp3.overall_rating as hp3_rating,
       hp4.overall_rating as hp4_rating,
       hp5.overall_rating as hp5_rating,
       hp6.overall_rating as hp6_rating,
       hp7.overall_rating as hp7_rating,
       hp8.overall_rating as hp8_rating,
       hp9.overall_rating as hp9_rating,
       hp10.overall_rating as hp10_rating,
       hp11.overall_rating as hp11_rating,
       ap1.overall_rating as ap1_rating,
       ap2.overall_rating as ap2_rating,
       ap3.overall_rating as ap3_rating,
       ap4.overall_rating as ap4_rating,
       ap5.overall_rating as ap5_rating,
       ap6.overall_rating as ap6_rating,
       ap7.overall_rating as ap7_rating,
       ap8.overall_rating as ap8_rating,
       ap9.overall_rating as ap9_rating,
       ap10.overall_rating as ap10_rating,
       ap11.overall_rating as ap11_rating
FROM Match m
JOIN Player_Attributes hp1 ON hp1.player_api_id = m.home_player_1 AND hp1.date = m.date
JOIN Player_Attributes hp2 ON hp2.player_api_id = m.home_player_2 AND hp2.date = m.date
JOIN Player_Attributes hp3 ON hp3.player_api_id = m.home_player_3 AND hp3.date = m.date
JOIN Player_Attributes hp4 ON hp3.player_api_id = m.home_player_4 AND hp4.date = m.date
JOIN Player_Attributes hp5 ON hp5.player_api_id = m.home_player_5 AND hp5.date = m.date
JOIN Player_Attributes hp6 ON hp6.player_api_id = m.home_player_6 AND hp6.date = m.date
JOIN Player_Attributes hp7 ON hp7.player_api_id = m.home_player_7 AND hp7.date = m.date
JOIN Player_Attributes hp8 ON hp8.player_api_id = m.home_player_8 AND hp8.date = m.date
JOIN Player_Attributes hp9 ON hp9.player_api_id = m.home_player_9 AND hp9.date = m.date
JOIN Player_Attributes hp10 ON hp10.player_api_id = m.home_player_10 AND hp10.date = m.date
JOIN Player_Attributes hp11 ON hp11.player_api_id = m.home_player_11 AND hp11.date = m.date
JOIN Player_Attributes ap1 ON ap1.player_api_id = m.away_player_1 AND ap1.date = m.date
JOIN Player_Attributes ap2 ON ap2.player_api_id = m.away_player_2 AND ap2.date = m.date
JOIN Player_Attributes ap3 ON ap3.player_api_id = m.away_player_3 AND ap3.date = m.date
JOIN Player_Attributes ap4 ON ap4.player_api_id = m.away_player_4 AND ap4.date = m.date
JOIN Player_Attributes ap5 ON ap5.player_api_id = m.away_player_5 AND ap5.date = m.date
JOIN Player_Attributes ap6 ON ap6.player_api_id = m.away_player_6 AND ap6.date = m.date
JOIN Player_Attributes ap7 ON ap7.player_api_id = m.away_player_7 AND ap7.date = m.date
JOIN Player_Attributes ap8 ON ap8.player_api_id = m.away_player_8 AND ap8.date = m.date
JOIN Player_Attributes ap9 ON ap9.player_api_id = m.away_player_9 AND ap9.date = m.date
JOIN Player_Attributes ap10 ON ap10.player_api_id = m.away_player_10 AND ap10.date = m.date
JOIN Player_Attributes ap11 ON ap11.player_api_id = m.away_player_11 AND ap11.date = m.date;