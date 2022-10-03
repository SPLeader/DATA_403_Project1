import pandas as pd


def main():

    poverty = pd.read_csv("FinalData/PovertyRatesFinal.csv")
    age = pd.read_csv("FinalData/AgeBySex21Final.csv")
    population = pd.read_csv("FinalData/AnnualPopulationEstimatesFinal.csv")
    race = pd.read_csv("FinalData/IowaRaceDistFinal.csv")
    income = pd.read_csv("FinalData/IncomeEstimatesFinal.csv")

    overall_df = poverty.merge(age, on = ["County", "Year"], how = "inner")
    overall_df = overall_df.merge(population, on = ["County", "Year"], how = "inner")
    overall_df = overall_df.merge(race, on = ["County", "Year"], how = "inner")
    overall_df = overall_df.merge(income, on = ["County", "Year"], how = "inner")

    overall_df.to_csv("FinalData/EstimatesFinal.csv", index = False)

    print(overall_df)

if __name__ == "__main__":

    main()
