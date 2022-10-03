import pandas as pd


def main():

    poverty = pd.read_csv("RawData/PovertyRatesFinal.csv")
    age = pd.read_csv("RawData/AgeBySex21Final.csv")
    population = pd.read_csv("RawData/AnnualPopulationEstimatesFinal.csv")
    race = pd.read_csv("RawData/IowaRaceDistFinal.csv")
    income = pd.read_csv("RawData/IncomeEstimatesFinal.csv")

    overall_df = poverty.merge(age, on = ["County", "Year"], how = "inner")
    overall_df = overall_df.merge(population, on = ["County", "Year"], how = "inner")
    overall_df = overall_df.merge(race, on = ["County", "Year"], how = "inner")
    overall_df = overall_df.merge(income, on = ["County", "Year"], how = "inner")

    overall_df.to_csv("RawData/EstimatesFinal.csv", index = False)

    print(overall_df)

if __name__ == "__main__":

    main()
