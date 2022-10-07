'''
Thea Yang
Purpose: script to generate lookup table mapping cities to county. 
'''

import pandas as pd
import requests 
from bs4 import BeautifulSoup 
import math as math
import re

# constants
WIKIURL="https://en.wikipedia.org/wiki/List_of_cities_in_Iowa"
TABLE_CLASS="wikitable plainrowheaders sortable"

# input: list of cities and dictionary of name fixes
def create_lookup(cities, name_fixes):
    city = pd.DataFrame(cities, columns=['City'])
    # drop '' row for city
    city = city[city['City'] != '']
    response=requests.get(WIKIURL)

    soup = BeautifulSoup(response.text, 'html.parser')
    cities_table=soup.find('table',{'class':TABLE_CLASS})

    df=pd.read_html(str(cities_table))
    df=pd.DataFrame(df[0])
    df.columns = df.columns.droplevel(1)

    wiki_table = df[['Name', 'Count(ies)[a]']]
    wiki_table.columns = ['Wiki City', 'County']

    city['City Fix'] = city['City'].replace(name_fixes)

    merged_df = city.merge(wiki_table, how='left', left_on='City Fix', right_on='Wiki City')

    county_list = merged_df['County'].unique()
    county_fix = {'County':[], 'County Fix': []}
    for county in county_list:
        if isinstance(county, str):
            county_1 = county.split(sep=' ')[0]
            up_count = sum(1 for c in county_1 if c.isupper())
            if up_count > 1 and "'" not in county_1 and (county_1 != 'DeWitt'):
                res_list = [s for s in re.split("([A-Z][^A-Z]*)", county_1) if s]
                official_county = res_list[0]
            else:
                official_county = county
        county_fix['County'].append(county)
        county_fix['County Fix'].append(official_county)

    county_map = pd.DataFrame(county_fix).dropna()

    df_final = merged_df.merge(county_map, how="left", on='County')
    df_final = df_final[['City', 'County Fix']]
    df_final.columns = ['City', 'County']
    df_final = df_final[df_final['City'] != '']
    return df_final

def main():
    raw_cities = ['GUTTENBERG', 'BELMOND', 'ACKLEY', 'WESLEY', 'EVANSDALE',
       'DES MOINES', 'HARLAN', 'HAMPTON', 'SIGOURNEY', 'CEDAR RAPIDS',
       'CORALVILLE', 'CLARINDA', 'DUBUQUE', 'CHARITON', 'ALTOONA',
       'INDIANOLA', 'IOWA CITY', 'Spencer', 'FORT DODGE', 'Evansdale',
       'Waukee', 'Harlan', 'Davenport', 'Ottumwa', 'Cresco',
       'Cedar Rapids', 'Iowa City', 'Council Bluffs', 'North English',
       'Vinton', 'Muscatine', 'Brooklyn', 'Wesley', 'CRESCO', 'Indianola',
       'Sigourney', 'Des Moines', 'North Liberty', 'Moravia',
       'Mason City', 'Arnolds Park', 'Rockwell', 'DeWitt', 'Pella',
       'Fort Dodge', 'Sioux City', 'Atkins', 'West Des Moines',
       'Glenwood', 'Anamosa', 'Hampton', 'Boone', 'Dubuque', 'Osceola',
       'Larchwood', 'Dunlap', 'Clarinda', 'DAVENPORT', 'Ackley',
       'SEYMOUR', 'DUNLAP', 'OSCEOLA', 'WAVERLY', 'LARCHWOOD',
       'NORTH LIBERTY', 'ATLANTIC', 'SIOUX CITY', 'MASON CITY',
       'ROCKWELL', 'WATERLOO', 'CLINTON', 'PLEASANTVILLE', 'TABOR',
       'RUNNELLS', 'AUDUBON', 'ANTHON', 'Robins', 'Waverly', 'Altoona',
       'ANAMOSA', 'Runnells', 'NORWALK', 'WEST BRANCH', 'REINBECK',
       'COLUMBUS JUNCTION', 'MARSHALLTOWN', 'Center Point',
       'CENTRAL CITY', 'Tabor', 'Belmond', 'Columbus Junction',
       'Marshalltown', 'Pleasantville', 'Coralville', 'Anthon',
       'Central City', 'Waterloo', 'Clinton', 'Sac City', 'Forest City',
       'Norwalk', 'Reinbeck', 'Mitchellville', 'Seymour', 'Atlantic',
       'Audubon', 'Missouri Valley', 'Manson', 'Leon', 'Cedar Falls',
       'West Branch', 'Winthrop', 'Chariton', 'Bettendorf', 'Albert City',
       'Urbandale', 'Onawa', 'Newton', 'Windsor Heights', 'Clarion',
       'Kingsley', 'Story City', 'Rock Valley', 'Webster City', 'Stanton',
       'Humboldt', 'Lawler', 'Ames', 'Carter Lake', 'Alburnett', 'Otumwa']

    stripped_cities = ['Paullina', 'Davenport', 'Woodbine', 'Windsor Heights', '',
       'Iowa Falls', 'Marion', 'Corydon', 'Atlantic', 'Ottumwa',
       'Estherville', 'Wilton', '4th St Waukee', 'URBANDALE', 'Humbolt',
       'Ames', 'Missouri Valey', 'Muscatine', 'CASEY', 'Humest',
       'Cedar Rapids', 'Iowa City', 'Lafayette / Waterloo', 'Waukee',
       'Ft Dodg', 'Newton', 'Sully', 'Northwood', 'Adel',
       'Council Bluffs', 'MLK', 'Lovilia', 'Indianola', 'IOWA CITY',
       'West DSM', 'Coralville', 'Jefferson', 'Centerville', 'Princeton',
       'Hospers', 'Urband', 'Dubuque', 'Emmetsburg', 'Pella',
       ' Coralville', 'Grand Mound', 'Tabor', ' Dubuque', 'Van Meter',
       'Ankeny', 'Marsha', 'Algona', 'Fort Dodge', 'Perry', 'Clear Lake',
       'State Ankeny', 'Corning', 'STUART', 'Lemars', 'Stuart', 'Dumont',
       'St. Ansgar', 'Waterloo', 'Springville', 'Mount Ayr', 'Anita',
       'West Des Moines', 'Storm Lake', 'Spirit Lake', 'Harlan']

    name_fixes = {'4Th St Waukee': 'Waukee', 'Humbolt':'Humboldt', 'Missouri Valey':'Missouri Valley', 
                        'Humest':'Humeston', 'Lafayette / Waterloo': 'Waterloo', 'Ft Dodg':'Fort Dodge', 'West Dsm':'West Des Moines', 
                         'Urband': 'Urbandale', 'Marsha':'Marshalltown', 'State Ankeny':'Ankeny', 'Lemars': 'Le Mars', 'Mlk':'', 
                                                 'Dewitt': 'DeWitt', 'Otumwa':'Ottumwa'}

    raw_cities_set = set([x.title().strip() for x in raw_cities])
    stripped_cities_set = set([x.title().strip() for x in stripped_cities])
    cities = list(raw_cities_set.union(stripped_cities_set))

    df = create_lookup(cities, name_fixes)
    df.to_csv('city_county_lookup.csv', index=False)


if __name__ == '__main__':
    main()