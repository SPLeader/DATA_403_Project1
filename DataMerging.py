import pandas as pd


def main():

    poverty = pd.read_csv("Final Data/PovertyRatesFinal.csv")
    age = pd.read_csv("Final Data/AgeWider.csv")
    population = pd.read_csv("Final Data/AnnualPopulationEstimatesFinal.csv")
    race = pd.read_csv("Final Data/IowaRaceDistFinal.csv")
    income = pd.read_csv("Final Data/IncomeWider.csv")

    overall_df = poverty.merge(age, on = ["County", "Year"], how = "inner")
    overall_df = overall_df.merge(population, on = ["County", "Year"], how = "inner")
    overall_df = overall_df.merge(race, on = ["County", "Year"], how = "inner")
    overall_df = overall_df.merge(income, on = ["County", "Year"], how = "inner")

    overall_df.to_csv("Final Data/EstimatesFinal.csv", index = False)

    print(overall_df)

if __name__ == "__main__":

    main()
