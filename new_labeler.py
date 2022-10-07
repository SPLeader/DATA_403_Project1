import pandas as pd

liquor = pd.read_csv("/home/datasets/Iowa_Liquor_Sales.csv", low_memory = False)
liquor = liquor.dropna(axis=0,subset=['Item Description','Bottles Sold'])

def liquor_labeler(df):

    drinks = ['Vodka','Triple Sec','Tequila','Amaretto','Brandy','Schnapps','Gin','Rum','Scotch','Baileys','Rye',
              'Sangria','Kahlua','Bourbon','Whiskey','Everclear',
             'Hennessy','Captain Morgan','Limoncello','Jagermeister']

    vodkalt = ['Vodka','New Amsterdam','Smirnoff','Svedka','Absolut','Grey Goose','Ketel One']

    tequilalt = ['Tequila','Jose Cuervo']

    whiskeyalt = ['Whiksey','Whisky','Jack Daniels',"Jack Daniel's",'Johnnie Walker','Jim Beam','Fireball Cinnamon']

    rumalt = ['Rum','Bacardi']

    drinks.sort()

    data_dict = {drink : [] for drink in drinks}

    for row in range(len(df)):

        alc_type = df.loc[row,'Item Description']
        bottle_count = df.loc[row, 'Bottles Sold']
        did_find = False


        if [vodtype for vodtype in vodkalt if vodtype in alc_type] != []:
            alc_type = "Vodka"

        elif [teqtype for teqtype in tequilalt if teqtype in alc_type] != []:
            alc_type = "Tequila"

        elif [whitype for whitype in whiskeyalt if whitype in alc_type] != []:
            alc_type = "Whiskey"

        elif [rumtype for rumtype in whiskeyalt if rumtype in alc_type] != []:
            alc_type = "Rum"

        found_drinks = [drink for drink in drinks if drink in alc_type]
        for drink in drinks:

            if drink in found_drinks:
                data_dict[drink].append(bottle_count)
                did_find = True
            else:
                data_dict[drink].append(0)

        if did_find:
            if 'OTHER' not in data_dict:
                data_dict['OTHER'] = []
            data_dict['OTHER'].append(0)
            
        else:
            data_dict['OTHER'].append(bottle_count)
        did_find = False

    count_df = pd.DataFrame(data_dict)
    #print({thing : len(data_dict[thing]) for thing in data_dict})
    print(count_df)
    return count_df

labeled_liquor = liquor_labeler(liquor)

big_liquorset = pd.concat([liquor,labeled_liquor],axis=1)
big_liquorset.to_csv("Iowa_liquor_with_Counts.csv",index=False)