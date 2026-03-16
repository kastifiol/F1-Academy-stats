import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image

# Création des données
pilot_data = {
    'ShortName' : ['A.PALMOWSKI', 'A.LARSEN', 'E.FELBERMAYR', 'R.FERREIRA', 'L.BILLARD', 'P.WESTCOTT', 'N.GRANADA', 'N.GADEMAN', 'A.DOBSON', 'E.LLOYD', 'E.STEVENS', 'R.ROBERTSON', 'J.JACQUET', 'M.BRUCE', 'E.KOSTERMAN', 'M.PAATZ', 'K.COUNTRYMAN', 'W.SHI'],
    'FullName' : ['Alisha PALMOWSKI', 'Alba LARSEN', 'Emma FELBERMAYR', 'Rafaela FERREIRA', 'Lisa BILLARD', 'Payton WESTCOTT', 'Natalia GRANADA', 'Nina GADEMAN', 'Ava DOBSON', 'Ella LLOYD', 'Ella STEVENS', 'Rachel ROBERTSON', 'Jade JACQUET', 'Megan BRUCE', 'Esmee KOSTERMAN', 'Mathilda PAATZ', 'Kaylee COUNTRYMAN', 'Wei SHI'],
    'Code' : ['PAL', 'LAR', 'FEL', 'FER', 'BIL', 'WES', 'GRA', 'GAD', 'DOB', 'LLO', 'STE', 'ROB', 'JAC', 'BRU', 'KOS', 'PAA', 'COU', 'SHI'],
    'Number' : [21, 12, 5, 18, 14, 9, 19, 3, 55, 20, 28, 56, 95, 4, 32, 8, 91, 24],
    'Team' : ['Red Bull Racing', 'Ferrari', 'Audi', 'Racing Bulls', 'Gatorade', 'Mercedes', 'SEPHORA', 'Alpine', 'American Express', 'McLaren', 'McLaren', 'PUMA', 'Williams', 'TAG Heuer', 'LEGO', 'Aston Martin', 'Haas', 'Juss Sports'],
    'QualiTimeR1' : ['2:04.143', '2:04.585', '2:04.671', '2:04.699', '2:04.716', '2:04.786', '2:04.914', '2:04.917', '2:05.007', '2:05.009', '2:05.014', '2:05.158', '2:05.325', '2:05.370', '2:05.457', '2:05.673', '2:06.438', '2:06.644'],
    'Sector1' : [32.6, 32.9, 32.8, 33.0, 33.1, 32.8, 33.1, 32.9, 32.9, 32.9, 33.1, 33.0, 33.3, 32.9, 33.1, 33.2, 33.3, 33.0],
    'Sector2' : [37.3, 37.4, 37.5, 37.4, 37.6, 37.4, 37.4, 37.5, 37.7, 37.6, 37.7, 37.7, 37.7, 37.8, 37.9, 37.8, 38.1, 37.9],
    'Sector3' : [54.9, 54.6, 54.6, 54.6, 54.3, 54.8, 55.0, 54.6, 54.7, 54.8, 54.5, 54.6, 54.5, 54.7, 54.5, 54.5, 55.0, 54.3],
    'LapNumber' : [11, 11, 12, 11, 12, 12, 12, 11, 12, 11, 11, 11, 12, 12, 11, 11, 6, 12],
    'SpdTrap' : ['Null', 'Null', 'Null', 'Null', 235, 'Null', 'Null', 'Null', 236, 'Null', 'Null', 235, 235, 237, 235, 'Null', 'Null', 'Null'] # attention : unité => KPH
}

df = pd.DataFrame(pilot_data)

# Colori des teams
team_colors = {
    "Red Bull Racing": ["#081F7E", "logo/redbull.png"],
    "Ferrari": ["#F6382D", "logo/ferrari.png"],
    "Audi": ["#C0C1C1", "logo/audi.png"],
    "Racing Bulls": ["#3465C6", "logo/racing-bulls.png"],
    "Gatorade": ["#FD7322", "logo/gatorade.png"],
    "Mercedes": ["#4CFBAF", "logo/mercedes.png"],
    "SEPHORA": ["#181822", "logo/sephora.png"],
    "Alpine": ["#E36FB0", "logo/alpine.png"],
    "American Express": ["#0360D9", "logo/american-express.png"],
    "McLaren": ["#FB7F09", "logo/mclaren.png"],
    "PUMA": ["#FD91E7", "logo/puma.png"],
    "Williams": ["#0752BA", "logo/williams.png"],
    "TAG Heuer": ["#199773", "logo/tag-heuer.png"],
    "LEGO": ["#FFE235", "logo/lego.png"],
    "Aston Martin": ["#005053", "logo/aston-martin.png"],
    "Haas": ["#C10000", "logo/haas.png"],
    "Juss Sports": ["#86B6F6", "logo/juss-sports.png"],
}

# Monoplace des pilotes
driver_cars = {
    'A.PALMOWSKI' : 'F1-Academy-Livrery/background-false/RedBull.png', 
    'A.LARSEN' : 'F1-Academy-Livrery/background-false/Ferrari.png', 
    'E.FELBERMAYR' : 'F1-Academy-Livrery/background-false/Audi.png', 
    'R.FERREIRA' : 'F1-Academy-Livrery/background-false/Visa-RB.png', 
    'L.BILLARD' : 'F1-Academy-Livrery/background-false/Gatorade.png', 
    'P.WESTCOTT' : 'F1-Academy-Livrery/background-false/MercedesAMG.png', 
    'N.GRANADA' : 'F1-Academy-Livrery/background-false/Sephora.png', 
    'N.GADEMAN' : 'F1-Academy-Livrery/background-false/Alpine.png', 
    'A.DOBSON' : 'F1-Academy-Livrery/background-false/American-Express.png', 
    'E.LLOYD' : 'F1-Academy-Livrery/background-false/McLaren-noire.png', 
    'E.STEVENS' : 'F1-Academy-Livrery/background-false/McLaren-bleue.png', 
    'R.ROBERTSON' : 'F1-Academy-Livrery/background-false/Puma.png', 
    'J.JACQUET' : 'F1-Academy-Livrery/background-false/Williams.png', 
    'M.BRUCE' : 'F1-Academy-Livrery/background-false/TAGHeuer.png', 
    'E.KOSTERMAN' : 'F1-Academy-Livrery/background-false/Lego.png', 
    'M.PAATZ' : 'F1-Academy-Livrery/background-false/Aston-Martin.png', 
    'K.COUNTRYMAN' : 'F1-Academy-Livrery/background-false/Haas.png', 
    'W.SHI' : 'F1-Academy-Livrery/background-false/Juss-Sports.png'
}

# Ajout de minute à ss.ms => 00:mm.ms
def addMinute(addMinuteTo):
    df[f"{addMinuteTo}Min"] = '00:' + df[f"{addMinuteTo}"] + '00'
    return f"{addMinuteTo}Min"

# Conversion de str (mm:ss.ms) en int (s.ms) 
def convertStrTime(toConvert):
    i = df[f"{toConvert}"].str.split(':', expand=True) # Création de 2 colonnes pour ss et mm.ms stockée dans la variable time
    j = i[1].str.split('.', expand=True).astype(int)
    k = i[0].astype(int)
    df[f"{toConvert}Int"] = k*60 + j[0] + j[1]/1000

# Calcul du gap
def gap(lapTime):
    df["Gap"] = abs(df[f"{lapTime}"].min() - df[f"{lapTime}"])

# Affiche data dans le terminal
def showQualiData():
    convertStrTime('QualiTimeR1')
    gap('QualiTimeR1Int')

    # Positionnement du pilote le plus rapide au plus lent
    data = df[['ShortName', 'QualiTimeR1Int', 'Sector1', 'Sector2', 'Sector3', 'Gap']].sort_values('Gap', ascending=True)
    data.index = range(1, len(data) + 1)
    data.index.name = 'Position'

    #Affichage
    print(data)

# Création d'un graphique des gaps par rapport à la pole
def show_gap_graphic():
    # Calcul des limites de l'axe x 
    pole_round = round(df['QualiTimeR1Int'].min(), 0) # ex: 124
    diff_pole_to_round = round((df['QualiTimeR1Int'].min() - pole_round), 3) # ex: 124.143 - 124 = 0.143
    last_round = round(df['QualiTimeR1Int'].max(), 1) # ex: 126.5
    last_plus_one = (last_round - pole_round + 1) % 60 # ex: 126.5 - 124 + 1 = 3.5

    def minute_display(seconds):
        labels = []
        for i in range(len(seconds)):
            minute = int(seconds[i]) // 60 
            second = int(seconds[i]) % 60
            if second < 10:
                x = '0'
            else:
                x = ''
            labels.append(f"{minute}:{x}{second}.00")
        return labels

    ticks = np.arange(pole_round, last_round + 1, 1)
    labels_ticks_x = (minute_display(ticks))

    print(pole_round)
    print(ticks)
    print(labels_ticks_x)
    

    color_line = df['Team'].map(lambda t: team_colors[t][0])
    plt.barh(df['ShortName'], (df['Gap'] + diff_pole_to_round), color = color_line, zorder=2)

    ax = plt.gca()

    # Titre
    plt.title('Gap to pole')

    # axe x
    ax.set_xlabel('Lap time')
    ax.set_xlim(0, df['Gap'].max() + 1)
    ax.set_xticks(ticks - pole_round)
    ax.set_xticklabels(labels_ticks_x)
    ax.grid(axis='x', color="#CFCFCF", zorder=1)

    # axe Y
    #ax.set_ylabel('Drivers')
    ax.invert_yaxis()
    for i, v in enumerate(df['Gap']):
        if i == 0:
            text = f"Pole position : {df.loc[df['QualiTimeR1Int'].idxmin(), 'QualiTimeR1']} m"
        else:
            text = f"+ {v:.4} s"
        plt.text(v + 0.2, i, str(text), va='center')
        
    # Affichage
    plt.tight_layout()
    plt.show()


# TEST
showQualiData()
show_gap_graphic()

