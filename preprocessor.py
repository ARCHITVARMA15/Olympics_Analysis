
import pandas as pd



def preprocess(df, region_df):


    #filtering for summer olympics
    df = df[df['Season']=='Summer']
    #merge with region_df
    #df = df.merge(region_df, how='left', on='NOC')
    #df = df.drop(columns=['region', 'notes'], errors='ignore') \
    df =    df.merge(region_df, how='left', on='NOC')

    #dropping duplicates
    df.drop_duplicates(inplace=True)
    #one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)

    return df


