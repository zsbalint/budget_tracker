import pandas as pd

def normalize_columns(df):
    df.columns = [c.strip() for c in df.columns]
    return df


def process_transactions(filepath): # TODO: add a second parameter for the type (eg. OTP, Raiffeisen) and make the column types work for both
    df = pd.read_excel(filepath)
    df = normalize_columns(df)
    df = df.fillna('') # to avoid None

    columns = list(df.columns)
    rows = df.to_dict(orient='records')

    # COLUMN NAME SETTINGS HERE
    col_types = {}
    for c in columns:
        lc = c.lower()
        if lc == 'tranzakció dátuma':
            col_types[c] = 'date'
        if lc == 'típus':
            col_types[c] = 'type'
        if lc == 'partner neve':
            col_types[c] = 'partner'
        if lc == 'összeg':
            col_types[c] = 'value'

    # EXAMPLE CATEGORIES # TODO: handle this with database
    categories = ['egy', 'kettő', 'három']

    return (columns, rows, col_types, categories)


def save_grid():

    return "FING"