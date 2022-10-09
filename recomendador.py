import pandas as pd
import re 

def extract():
    df = pd.read_csv("disney_plus_titles.csv", sep =',')
    return df

def transform(df):
    buscar = input("¿What film/serie would you like to watch? Insert key word") 
    pelis_series = pd.DataFrame(columns = ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description'])
    
    for i in range(len(df.axes[0])):
        if re.findall(str(buscar), df.loc[:, 'title'][i], re.IGNORECASE) != []:
            pelis_series.loc[len(pelis_series)] = df.iloc[i]    
    print(pelis_series)

def load(pelis_series):
    for j in range(len(pelis_series)):
        print("A")
        
    
if __name__ == "__main__":
    df = extract()
    transform(df)
    
    
    #load(pelis_series)
