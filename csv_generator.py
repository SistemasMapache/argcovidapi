
from santa_fe_api import *
from argentina_api import *
import datetime
import os

CSV_FOLDER = './csvs'

if __name__ == '__main__':
    # Erase old csv's.
    for fn in [ 'SantaFe_Confirmados.csv', 'SantaFe_Descartados.csv',
                'SantaFe_Sospechosos.csv',
                'Argentina_Provinces.csv' ]:
        if os.path.exists(fn):
            os.remove(fn)
    # Save time of last update
    timestamp = datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    with open(os.path.join(CSV_FOLDER,'last_update.txt'), 'w') as f:
        f.write('Last update on: {}'.format(timestamp))
    # Generate Santa Fe csv's
    santa_fe_api = SantaFeAPI('./')
    santa_fe_api.df_confirmados.to_csv(os.path.join(CSV_FOLDER,'SantaFe_Confirmados.csv'))
    santa_fe_api.df_descartados.to_csv(os.path.join(CSV_FOLDER,'SantaFe_Descartados.csv'))
    santa_fe_api.df_sospechosos.to_csv(os.path.join(CSV_FOLDER,'SantaFe_Sospechosos.csv'))
    # Generate Argentina csv's
    argentina_api = ArgentinaAPI('./')
    argentina_api.df_provinces.to_csv(os.path.join(CSV_FOLDER,'Argentina_Provinces.csv'))
