import pandas as pd
url = r'https://docs.google.com/document/d/e/2PACX-1vSZ1vDD85PCR1d5QC2XwbXClC1Kuh3a4u0y3VbTvTFQI53erafhUkGot24ulET8ZRqFSzYoi3pLTGwM/pub'
#url = r'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'


def decode_message(url):

    df = get_html_table(url)
    df = df.drop(0)
    df.columns = ['x-coordinate','Character','y-coordinate']
    # Convert coordinates to integers for sorting
    df['x-coordinate'] = df['x-coordinate'].astype(int)
    df['y-coordinate'] = df['y-coordinate'].astype(int)
    # Sort by y-coordinate (descending) and x-coordinate (ascending)
    df = df.sort_values(['y-coordinate', 'x-coordinate'], ascending=[False, True])

    # Create a dictionary to store characters by their positions
    positioned_characters = {}
    for _, row in df.iterrows():
        x, y, char = row['x-coordinate'], row['y-coordinate'], row['Character']
        if y not in positioned_characters:
            positioned_characters[y] = {}
        positioned_characters[y][x] = char

    # Print characters row by row    

    for y in sorted(positioned_characters.keys(), reverse=True):  # Highest y-coordinate first
        row = positioned_characters[y]
        min_x = min(row.keys())
        max_x = max(row.keys())
        line = ''.join(row.get(x, ' ') for x in range(min_x, max_x + 1))  # Fill gaps with spaces
        print(line)

def get_html_table(url):
    # Read HTML tables from the URL
    tables = pd.read_html(url)  # Returns list of all tables on page
    df = tables[0]  # Select table of interest
    return df


decode_message(url)
