import pandas as pd

def main():
    #df = pd.read_csv("Reformatted Data/AgeBySex21Reformatted.csv", encoding = "utf-8")
    df = pd.read_csv("Reformatted Data/IncomeEstimatesReformatted.csv", encoding = "utf-8")

    #df['Y'] = df['County'].apply(lambda x : x.rsplit(' ', 1)[0])
    year_ranges = list(df['Year'].value_counts().index)

    year_range_dict = {}
    for year_range in year_ranges:
        year1 = year_range.split("-")[0]
        year2 = year_range.split("-")[1]
        year_range_dict[year_range] = range(int(year1), int(year2) + 1)

    new_df = pd.DataFrame()

    for index, row in df.iterrows():

        for year in year_range_dict[row['Year']]:

            row['Year'] = year
            new_df = pd.concat([new_df, row], axis = 1)

    print(new_df.transpose())
    #new_df.transpose().to_csv("Final Data/AgeBySex21Final.csv", index = False)
    new_df.transpose().to_csv("Final Data/IncomeEstimatesFinal.csv", index = False)

if __name__ == "__main__":

    main()
