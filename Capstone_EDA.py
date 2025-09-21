import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

#load datasets
df11 = pd.read_csv("annual_conc_by_monitor_2011.csv")
df12 = pd.read_csv("annual_conc_by_monitor_2012.csv")
df13 = pd.read_csv("annual_conc_by_monitor_2013.csv")
df14 = pd.read_csv("annual_conc_by_monitor_2014.csv")
df15 = pd.read_csv("annual_conc_by_monitor_2015.csv")
df16 = pd.read_csv("annual_conc_by_monitor_2016.csv")
df17 = pd.read_csv("annual_conc_by_monitor_2017.csv")
df18 = pd.read_csv("annual_conc_by_monitor_2018.csv")
df19 = pd.read_csv("annual_conc_by_monitor_2019.csv")
df20 = pd.read_csv("annual_conc_by_monitor_2020.csv")
df21 = pd.read_csv("annual_conc_by_monitor_2021.csv")
asthma_df = pd.read_csv("crude_asthma_2011_2021.csv")

#keep only relevant pollutants in air pollutant datasets
pollutants = ["Ozone", "PM2.5 - Local Conditions", "Nitrogen dioxide (NO2)"]
df11_pollutants = df11[df11["Parameter Name"].isin(pollutants)]
df12_pollutants = df12[df12["Parameter Name"].isin(pollutants)]
df13_pollutants = df13[df13["Parameter Name"].isin(pollutants)]
df14_pollutants = df14[df14["Parameter Name"].isin(pollutants)]
df15_pollutants = df15[df15["Parameter Name"].isin(pollutants)]
df16_pollutants = df16[df16["Parameter Name"].isin(pollutants)]
df17_pollutants = df17[df17["Parameter Name"].isin(pollutants)]
df18_pollutants = df18[df18["Parameter Name"].isin(pollutants)]
df19_pollutants = df19[df19["Parameter Name"].isin(pollutants)]
df20_pollutants = df20[df20["Parameter Name"].isin(pollutants)]
df21_pollutants = df21[df21["Parameter Name"].isin(pollutants)]

#keep only relevant columns and rename for asthma dataset
asthma_df = asthma_df[["CountyFIPS", "Year", "Value"]].rename(columns={
    "CountyFIPS": "FIPS",
    "Value": "Asthma ER Rate"
})

#filter out unneeded columns for air pollutant datasets
columns_to_keep = [
    "State Code", "County Code", "Arithmetic Mean", "Parameter Name",
    "Latitude", "Longitude", "Units of Measure", "Observation Count", "State Name",
    "County Name"
]

df11_pollutants = df11_pollutants[columns_to_keep]
df12_pollutants = df12_pollutants[columns_to_keep]
df13_pollutants = df13_pollutants[columns_to_keep]
df14_pollutants = df14_pollutants[columns_to_keep]
df15_pollutants = df15_pollutants[columns_to_keep]
df16_pollutants = df16_pollutants[columns_to_keep]
df17_pollutants = df17_pollutants[columns_to_keep]
df18_pollutants = df18_pollutants[columns_to_keep]
df19_pollutants = df19_pollutants[columns_to_keep]
df20_pollutants = df20_pollutants[columns_to_keep]
df21_pollutants = df21_pollutants[columns_to_keep]

#drop rows with missing values in arithmetic mean or observation count for air pollutant datasets
df11_pollutants = df11_pollutants.dropna(subset=["Arithmetic Mean", "Observation Count"])
df12_pollutants = df12_pollutants.dropna(subset=["Arithmetic Mean", "Observation Count"])
df13_pollutants = df13_pollutants.dropna(subset=["Arithmetic Mean", "Observation Count"])
df14_pollutants = df14_pollutants.dropna(subset=["Arithmetic Mean", "Observation Count"])
df15_pollutants = df15_pollutants.dropna(subset=["Arithmetic Mean", "Observation Count"])
df16_pollutants = df16_pollutants.dropna(subset=["Arithmetic Mean", "Observation Count"])
df17_pollutants = df17_pollutants.dropna(subset=["Arithmetic Mean", "Observation Count"])
df18_pollutants = df18_pollutants.dropna(subset=["Arithmetic Mean", "Observation Count"])
df19_pollutants = df19_pollutants.dropna(subset=["Arithmetic Mean", "Observation Count"])
df20_pollutants = df20_pollutants.dropna(subset=["Arithmetic Mean", "Observation Count"])
df21_pollutants = df21_pollutants.dropna(subset=["Arithmetic Mean", "Observation Count"])

#drop rows with missing values in asthma dataset and pad FIPS with leading zero
asthma_df = asthma_df.dropna(subset=["FIPS", "Year", "Asthma ER Rate"])
asthma_df["FIPS"] = asthma_df["FIPS"].astype(str).str.zfill(5)

#create FIPS code as a new column for air pollutant datasets
df11_pollutants["FIPS"] = (
    df11_pollutants["State Code"].astype(str).str.zfill(2) +
    df11_pollutants["County Code"].astype(str).str.zfill(3)
)
df12_pollutants["FIPS"] = (
    df12_pollutants["State Code"].astype(str).str.zfill(2) +
    df12_pollutants["County Code"].astype(str).str.zfill(3)
)
df13_pollutants["FIPS"] = (
    df13_pollutants["State Code"].astype(str).str.zfill(2) +
    df13_pollutants["County Code"].astype(str).str.zfill(3)
)
df14_pollutants["FIPS"] = (
    df14_pollutants["State Code"].astype(str).str.zfill(2) +
    df14_pollutants["County Code"].astype(str).str.zfill(3)
)
df15_pollutants["FIPS"] = (
    df15_pollutants["State Code"].astype(str).str.zfill(2) +
    df15_pollutants["County Code"].astype(str).str.zfill(3)
)
df16_pollutants["FIPS"] = (
    df16_pollutants["State Code"].astype(str).str.zfill(2) +
    df16_pollutants["County Code"].astype(str).str.zfill(3)
)
df17_pollutants["FIPS"] = (
    df17_pollutants["State Code"].astype(str).str.zfill(2) +
    df17_pollutants["County Code"].astype(str).str.zfill(3)
)
df18_pollutants["FIPS"] = (
    df18_pollutants["State Code"].astype(str).str.zfill(2) +
    df18_pollutants["County Code"].astype(str).str.zfill(3)
)
df19_pollutants["FIPS"] = (
    df19_pollutants["State Code"].astype(str).str.zfill(2) +
    df19_pollutants["County Code"].astype(str).str.zfill(3)
)
df20_pollutants["FIPS"] = (
    df20_pollutants["State Code"].astype(str).str.zfill(2) +
    df20_pollutants["County Code"].astype(str).str.zfill(3)
)
df21_pollutants["FIPS"] = (
    df21_pollutants["State Code"].astype(str).str.zfill(2) +
    df21_pollutants["County Code"].astype(str).str.zfill(3)
)

#add year column
df11_pollutants["Year"] = 2011
df12_pollutants["Year"] = 2012
df13_pollutants["Year"] = 2013
df14_pollutants["Year"] = 2014
df15_pollutants["Year"] = 2015
df16_pollutants["Year"] = 2016
df17_pollutants["Year"] = 2017
df18_pollutants["Year"] = 2018
df19_pollutants["Year"] = 2019
df20_pollutants["Year"] = 2020
df21_pollutants["Year"] = 2021

#combine all the cleaned data into one dataset
df_all = pd.concat([
    df11_pollutants, df12_pollutants, df13_pollutants,
    df14_pollutants, df15_pollutants, df16_pollutants,
    df17_pollutants, df18_pollutants, df19_pollutants,
    df20_pollutants, df21_pollutants
], ignore_index=True)

#group and aggregate the data
grouped = (
    df_all.groupby(["Year", "FIPS", "State Name", "County Name", "Parameter Name"])["Arithmetic Mean"]
    .mean()
    .reset_index()
)

#pivot so each pollutant becomes a column
df_agg = grouped.pivot_table(
    index=["Year", "FIPS", "State Name", "County Name"],
    columns="Parameter Name",
    values="Arithmetic Mean"
).reset_index()

#rename pollutant columns for better accuracy
df_agg = df_agg.rename(columns={
    "Ozone": "Ozone Mean",
    "PM2.5 - Local Conditions": "PM2.5 Mean",
    "Nitrogen dioxide (NO2)": "NO2 Mean"
})

#merge asthma dataframe with air pollutant dataframe in order to perform statistical analysis
merged_df = pd.merge(df_agg, asthma_df, on=["FIPS", "Year"])

#visualize how PM2.5, Ozone, and NO2 relate to Asthma ER rate using correlation heatmap
corr_cols = ["PM2.5 Mean", "Ozone Mean", "NO2 Mean", "Asthma ER Rate"]
corr_matrix = merged_df[corr_cols].corr()

plt.figure(figsize=[8, 6])
sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu", center=0)
plt.title("Correlation Heatmap: Pollutants vs Asthma ER Rate")
plt.show()

#show a direct relationship between asthma and PM2.5 using a scatter plot and regression trend line
sns.regplot(data=merged_df, x="PM2.5 Mean", y="Asthma ER Rate",
            ci=95, line_kws={"color": "red", "linestyle":"--"},
            scatter_kws={"color": "lightblue", "alpha": 0.7})
plt.title("Asthma ER Rate vs PM2.5 (All Counties & Years)")
plt.xlabel("PM2.5 Mean (µg/m³)")
plt.ylabel("Asthma ER Rate per 10,000")
plt.show()

#show a direct relationship between asthma and Ozone using a scatter plot and regression trend line
sns.regplot(data=merged_df, x="Ozone Mean", y="Asthma ER Rate",
            ci=95, line_kws={"color": "red", "linestyle":"--"},
            scatter_kws={"color": "lightgreen", "alpha": 0.7})
plt.title("Asthma ER Rate vs Ozone (All Counties & Years)")
plt.xlabel("Ozone Mean")
plt.ylabel("Asthma ER Rate per 10,000")
plt.show()

#show a direct relationship between asthma and NO2 using a scatter plot and regression trend line
sns.regplot(data=merged_df, x="NO2 Mean", y="Asthma ER Rate",
            ci=95, line_kws={"color": "red", "linestyle":"--"},
            scatter_kws={"color": "gray", "alpha": 0.7})
plt.title("Asthma ER Rate vs NO2 (All Counties & Years)")
plt.xlabel("NO2 Mean")
plt.ylabel("Asthma ER Rate per 10,000")
plt.show()

#boxplot of asthma by PM2.5 Quartile
merged_df["PM2.5 Quartile"] = pd.qcut(merged_df["PM2.5 Mean"], 4, labels=["Q1", "Q2", "Q3", "Q4"])
sns.boxplot(data=merged_df, x="PM2.5 Quartile", y="Asthma ER Rate", color="lightblue")
plt.title("Asthma ER Rate by PM2.5 Quartile")
plt.xlabel("PM2.5 Quartile")
plt.ylabel("Asthma ER Rate per 10,000")
plt.show()

#boxplot of asthma by Ozone Quartile
merged_df["Ozone Quartile"] = pd.qcut(merged_df["Ozone Mean"], 4, labels=["Q1", "Q2", "Q3", "Q4"])
sns.boxplot(data=merged_df, x="Ozone Quartile", y="Asthma ER Rate", color="lightgreen")
plt.title("Asthma ER Rate by Ozone Quartile")
plt.xlabel("Ozone Quartile")
plt.ylabel("Asthma ER Rate per 10,000")
plt.show()

#boxplot of asthma by NO2 Quartile
merged_df["NO2 Quartile"] = pd.qcut(merged_df["NO2 Mean"], 4, labels=["Q1", "Q2", "Q3", "Q4"])
sns.boxplot(data=merged_df, x="NO2 Quartile", y="Asthma ER Rate", color="gray")
plt.title("Asthma ER Rate by NO2 Quartile")
plt.xlabel("NO2 Quartile")
plt.ylabel("Asthma ER Rate per 10,000")
plt.show()

#trendline over time using the national average of ER visits per 10,000
yearly_ER_avg = merged_df.groupby("Year")[["Asthma ER Rate"]].mean().reset_index()
yearly_ER_avg.plot(x="Year", figsize=(10, 6), color="darkred", marker="o")
plt.title("National Average Trends (2011-2021)")
plt.ylabel("Mean ER Visits per 10,000")
plt.grid(True)
plt.show()

#create dataframe by FIPS and take the mean PM2.5 across all years in order to find the top/bottom most/least polluted counties
pm25_avg = merged_df.groupby(
    ["FIPS", "State Name", "County Name"]
)["PM2.5 Mean"].mean().reset_index()

#top and bottom 5
top5 = pm25_avg.sort_values("PM2.5 Mean", ascending=False).head(5)
bottom5 = pm25_avg[pm25_avg["PM2.5 Mean"] > 0].sort_values("PM2.5 Mean").head(5)

#add average ER rate to both top and bottom
asthma_avg = merged_df.groupby("FIPS")["Asthma ER Rate"].mean().reset_index()
top5 = top5.merge(asthma_avg, on="FIPS", how="left")
bottom5 = bottom5.merge(asthma_avg, on="FIPS", how="left")

#prepare the tables
top5["Rank"] = ["1st", "2nd", "3rd", "4th", "5th"]
bottom5["Rank"] = ["1st", "2nd", "3rd", "4th", "5th"]

top_table = top5[["Rank", "State Name", "County Name", "PM2.5 Mean", "Asthma ER Rate"]].rename(
    columns={
        "Rank": "Rank",
        "State Name": "State",
        "County Name": "County",
        "PM2.5 Mean": "Avg PM2.5",
        "Asthma ER Rate": "Avg Asthma Rate"
    }
).round(2)

bottom_table = bottom5[["Rank", "State Name", "County Name", "PM2.5 Mean", "Asthma ER Rate"]].rename(
    columns={
        "Rank": "Rank",
        "State Name": "State",
        "County Name": "County",
        "PM2.5 Mean": "Avg PM2.5",
        "Asthma ER Rate": "Avg Asthma Rate"
    }
).round(2)

#create the figure
fig, axs = plt.subplots(2, 1, figsize=(10, 6))

axs[0].axis("off")
axs[1].axis("off")

#top 5 Most Polluted
axs[0].set_title("Top 5 Most Polluted Counties (2011–2021 Avg)", fontsize=12, fontweight='bold', pad=10)
table_top = axs[0].table(
    cellText=top_table.values,
    colLabels=top_table.columns,
    loc="center",
    cellLoc="center",
    colLoc="center"
)
table_top.auto_set_font_size(False)
table_top.set_fontsize(10)
table_top.scale(1.1, 1.3)

#Bottom 5 Least Polluted
axs[1].set_title("Top 5 Cleanest Counties (2011–2021 Avg)", fontsize=12, fontweight='bold', pad=10)
table_bottom = axs[1].table(
    cellText=bottom_table.values,
    colLabels=bottom_table.columns,
    loc="center",
    cellLoc="center",
    colLoc="center"
)
table_bottom.auto_set_font_size(False)
table_bottom.set_fontsize(10)
table_bottom.scale(1.1, 1.3)

plt.tight_layout()
plt.show()
