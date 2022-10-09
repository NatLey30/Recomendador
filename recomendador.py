import pandas as pd
import re 

def extract():
    df = pd.read_csv("disney_plus_titles.csv", sep =',')
    return df

def transform(df):
    buscar = input("¿What film/serie would you like to watch? Insert key word: ") 
    pelis_series = pd.DataFrame(columns = ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description'])
    
    for fila in range(len(df.axes[0])):
        if re.findall(str(buscar), df.loc[:, 'title'][fila], re.IGNORECASE) != []:
            pelis_series.loc[len(pelis_series)] = df.iloc[fila]
    
    show = ""
    for shows in range(len(pelis_series.axes[0])):
        print(pelis_series['title'][shows])
        respuesta = input("Is this the show you are looking for? y/n: ")
        if respuesta == "y":
            show = str(pelis_series['title'][shows])
            break

    if show == "":
        genero = None

    else:
        genero = pelis_series.iloc[shows]['listed_in'].split(",")[0]
        print(f"We are looking for shows in the same genre as {show}, genre: {genero}")

    return genero


def load(genero, df):
    print(genero)

    if genero == None:
        print("We can't find what you are looking for")
    else:
        for fila in range(len(df.axes[0])):
            if re.findall(str(genero), df.loc[:, 'listed_in'][fila], re.IGNORECASE) != []:
                print(df.loc[fila]['title'])
        
    
if __name__ == "__main__":
    df = extract()
    genero = transform(df)
    load(genero, df)
