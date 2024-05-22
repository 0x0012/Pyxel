'''
    First attempts between Python and MS Excel.

    Idea:
        Composite a range of drill holes logs.
'''

import pandas as pd

def compose(df : pd.DataFrame):
    pass
    return df.count()


def main():
    src_datafile = 'assets/data.xlsx'
    df = pd.read_excel(src_datafile, usecols='A:D')
    print(compose(df))

if __name__ == '__main__':
    main()
