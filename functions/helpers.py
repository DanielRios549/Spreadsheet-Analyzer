import pandas as pd

def normalize_columns(df):
    """Remove unnecessary spaces from column names."""

    df.columns = [
        str(col).strip()
        for col in df.columns
    ]

    return df


def convert_number(value):
    """
    Converts Brazilian-style numbers such as:
        5.943      -> 5943
        8.230      -> 8230
        9.354,50   -> 9354.50

    Also handles regular numeric values.
    """

    if pd.isna(value):
        return None

    if isinstance(value, (int, float)):
        return float(value)

    value = str(value).strip()

    if not value:
        return None

    # Brazilian decimal format: 9.354,50
    if "," in value:
        value = value.replace(".", "").replace(",", ".")

    # Integer thousands format: 5.943
    else:
        value = value.replace(".", "")

    try:
        return float(value)
    except ValueError:
        return None
