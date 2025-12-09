🏀 KenPom Analytics Project — Efficiency, Tempo, and Underrated Teams Analysis

This project analyzes NCAA Division I men's basketball team performance using efficiency metrics inspired by KenPom.
The goal was to explore what drives team success, compare offensive/defensive profiles, evaluate conference tempo styles, and build a data-driven Underrated Index to identify teams that performed better than their win–loss record suggests.

Note: Due to licensing restrictions, the KenPom dataset is not included.
To run the project, provide your own KenpomRatings.csv file.

📂 Project Overview
1. Data Cleaning & Preparation

Loaded and standardized column names from the KenPom ratings file.

Removed unnamed columns and cleaned string formatting.

Split win–loss records into separate numeric columns.

Converted all efficiency and tempo metrics to numeric dtype.

Calculated Win Percentage for every team.
(Shown in your DataFrame preview on page 4 of the PDF: Duke, Houston, Florida, etc. 

kenpom_analysis

)

2. Conference Tempo Analysis

Using Adjusted Tempo (AdjT), the project computed average tempo for each conference.

Output (shown on pages 4–5):

Fastest conferences: MAC, MEAC, SEC, Ivy, SWAC

Slowest conferences: NEC, PL, CAA

A bar chart visualizing every conference’s average AdjT.

This provides insight into stylistic differences across leagues.

3. Strength of Schedule vs Offensive Efficiency

A regression analysis explored the relationship between:

Strength of Schedule (NetRtg.1)

Offensive Rating (ORtg)

Scatterplot and trendline (page 6) show a clear positive correlation:

📈 Correlation = 0.728

A combined z-score metric ranked the top 10 teams excelling in both offensive efficiency and strength of schedule.
(Teams like Alabama, Auburn, Florida, and Purdue appear at the top.)
All shown on page 6 of the PDF. 

kenpom_analysis

4. Underrated Teams Model

The project computes an Underrated Index using standardized efficiency metrics:

UnderratedIndex
=
𝑧
(
ORtg
)
−
𝑧
(
DRtg
)
−
𝑧
(
WinPct
)
UnderratedIndex=z(ORtg)−z(DRtg)−z(WinPct)

This identifies teams with elite efficiency margins but underperforming records.

Results (page 6):

Teams like Duke, Houston, Auburn, Arizona scored as the most underrated.

A scatterplot on page 7 visualizes Underrated Index vs Win Percentage.


kenpom_analysis

Scaled Underrated Index

A second version magnifies undervaluation for low-win teams:

(
𝑧
𝑂
𝑅
𝑡
𝑔
−
𝑧
𝐷
𝑅
𝑡
𝑔
)
×
(
1
−
WinPct
)
(z
ORtg
	​

−z
DRtg
	​

)×(1−WinPct)

Top teams include:
Arizona, Illinois, Kansas, Ohio State, etc. (page 7).

🧠 What I Learned

How tempo, schedule strength, and efficiency metrics interact to shape team profiles.

How to engineer new basketball performance metrics (e.g., Underrated Index).

How to use z-scores and scaling to build robust ranking models.

How to apply real analytics workflows: cleaning, visualizing, modeling, and interpreting results.

How to work responsibly with proprietary sports data.
