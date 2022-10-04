import pandas as pd



def age_helper(x):

    if x in ["21 years", "22 to 24 years", "25 to 29 years"]:
        return "Young"
    elif x in ["30 to 34 years", "35 to 39 years", "40 to 44 years"]:
        return "Middle-Young"
    elif x in ["45 to 49 years", "50 to 54 years", "55 to 59 years", "60 to 64 years"]:
        return "Middle-Old"
    else:
        return "Old"

def income_helper(x):

    if x in ["Less than $10,000", "$10,000 to $14,999", "$15,000 to $19,999", "$20,000 to $24,999", "$25,000 to $29,999", "$30,000 to $34,999", "$35,000 to $39,999"]:
        return "LowIncome"
    if x in ["$125,000 to $149,999", "$150,000 to $199,999", "$200,000 or more"]:
        return "HighIncome"
    else:
        return "MidIncome"


def main():

    #df = pd.read_csv("Final Data/IncomeEstimatesFinal.csv", low_memory = False)
    #df['Income'] = df['Income'].apply(lambda x : income_helper(x))
    #df.to_csv("Final Data/IncomeEstimatesFinal.csv", index = False)

    #df = pd.read_csv("Final Data/AgeBySex21Final.csv", low_memory = False)
    #df['Age'] = df['Age'].apply(lambda x : age_helper(x))
    #df.to_csv("Final Data/IncomeEstimatesFinal.csv", index = False)






if __name__ == "__main__":

    main()
