# Streak Engine

Personal Analytic dashboard built w/ Python tracking habits and long-term progress.

This project helps to answer questions like:

- May I improve mood and productivity with more sleep?
- What habits create the longest streaks?
- Which days are most productive?

Instead of guessing, this repo uses real data and Python analysis to find patterns.

---

## Features

- Daily habit tracking
- CSV-based data storage
- Streak calculations
- Productivity trend analysis
- Sleep vs mood correlation
- Weekly and monthly reports
- Data visualizations with charts
- Optional future Streamlit dashboard

---

## Tracked Metrics

Examples include:

- Coding hours
- Workout completion
- Reading pages
- Sleep hours
- Mood score
- Spending
- Deep work sessions
- Weekly consistency

You can customize this for your own system.

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- CSV / Excel
- Streamlit (future upgrade)

---

## Project Structure

life-analytics/
│
├── data/
│ └── habits.csv
│
├── analysis/
│ ├── streaks.py
│ ├── trends.py
│ ├── correlations.py
│
├── automation/
│ └── add_today.py
│
├── dashboard/
│ └── streamlit_app.py
│
├── requirements.txt
└── README.md

---

## Example Questions This Project Answers

- What is my longest coding streak?
- Which weekday gives me the highest output?
- Is there a relationship between sleep and productivity?
- How often do workouts improve focus?
- What habits break my momentum?

---

## Example CSV Format

- date,coding_hours,workout,reading_pages,sleep_hours,mood
- 2026-04-01,3,1,20,7,8
- 2026-04-02,5,0,10,6,6
- 2026-04-03,4,1,15,8,9

---

## Future Improvements

- Notion integration
- Google Sheets sync
- Streamlit dashboard
- Monthly PDF reports
- Goal forecasting
- Personal score system
- Discipline index

---

## Why This Exists

Consistency beats wishful hoping.

This project turns daily actions into measurable feedback so progress becomes visible and improvable.

Built for discipline, not motivation.
