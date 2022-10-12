import pandas as pd

liquor = pd.read_csv("Iowa_Liquor_Sales.csv", low_memory = False)

def liquor_labeler(df):

    drinks = ['Vodka','Triple Sec','Tequila','Amaretto','Brandy','Schnapps','Gin','Rum','Scotch','Baileys','Rye',
              'Sangria','Kahlua','Bourbon','Whiskey','Everclear',
             'Hennessy','Captain Morgan','Limoncello','Jagermeister']

    vodkalt = ['Vodka','New Amsterdam','Smirnoff','Svedka','Absolut','Grey Goose','Ketel One']

    tequilalt = ['Tequila','Jose Cuervo']

    whiskeyalt = ['Whiksey','Whisky','Jack Daniels',"Jack Daniel's",'Johnnie Walker','Jim Beam','Fireball Cinnamon']

    rumalt = ['Rum','Bacardi']

    drinks.sort()

    rows = []
    for row in range(len(df)):
        
        alc_type = df.iloc[row,]['Item Description']
        bottle_count = df.iloc[row,]['Bottles Sold']
        row_dict = {}
        did_find = False
        if len([vodtype for vodtype in vodkalt if pd.Series(alc_type).str.contains(vodtype,case=False,regex=True)[0] == True]) > 0:
            alc_type = "Vodka"
        elif len([teqtype for teqtype in tequilalt if pd.Series(alc_type).str.contains(teqtype,case=False,regex=True)[0] == True]) > 0:
            alc_type = "Tequila"
        elif len([whitype for whitype in whiskeyalt if pd.Series(alc_type).str.contains(whitype,case=False,regex=True)[0] == True]) > 0:
            alc_type = "Whiskey"
        elif len([rumtype for rumtype in rumalt if pd.Series(alc_type).str.contains(rumtype,case=False,regex=True)[0] == True]) > 0:
            alc_type = "Rum"
        for drink in drinks:
            if pd.Series(alc_type).str.contains(drink,case=False,regex=True)[0] == True:
                row_dict[drink] = bottle_count
                did_find = True
            else:
                row_dict[drink] = 0
        if did_find:
            row_dict['OTHER'] = 0
            did_find = False
        else:
            row_dict['OTHER'] = bottle_count
        rows.append(row_dict)
    count_df = pd.DataFrame.from_dict(rows,orient='columns')
    return count_df

labeled_liquor = liquor_labeler(liquor)
labeled_liquor.to_csv("liquor_counts.csv",index=False)