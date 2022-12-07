import camelot
import pandas as pd

# READ TABLES FROM HTML

# below returns list, multiple tables.
champions = pd.read_html("https://en.wikipedia.org/wiki/List_of_English_football_champions")
# print(len(champions))  # there are 9 tables on the page

# print(champions[3])  # Premier League era champions

# Web scraping using csv files from https://www.football-data.co.uk/englandm.php
# Rather than download each one, we can download all files using scraping and a for loop.

# READ CSV FILES HOSTED ON THE INTERNET

df_champ_23 = pd.read_csv("https://www.football-data.co.uk/mmz4281/2223/E1.csv")


# Rename columns _e.g. FTHG is full time home goals.

df_champ_23.rename(
    columns={
        "FTHG": "home_goals",
        "FTAG": "away_goals",
    },
    inplace=True,
)

# print(df_champ_23)

# READ TABLES FROM PDFs

pdf_tables = camelot.read_pdf("foo.pdf", pages="1")
print(pdf_tables)

pdf_tables.export("foo.csv", f="csv", compress=True)
pdf_tables[0].to_csv("foo.csv")
