from .helpers import convert_number

MONTHS_PT = {
    "janeiro": 1,
    "fevereiro": 2,
    "março": 3,
    "abril": 4,
    "maio": 5,
    "junho": 6,
    "julho": 7,
    "agosto": 8,
    "setembro": 9,
    "outubro": 10,
    "novembro": 11,
    "dezembro": 12
}

def detect_month_column(df):
    """Try to identify the month column."""

    for column in df.columns:

        values = (
            df[column]
            .dropna()
            .astype(str)
            .str.strip()
            .str.lower()
        )

        matches = values.isin(MONTHS_PT.keys()).sum()

        if matches >= 2:
            return column

    return None

def detect_quantity_column(df):
    """Try to identify a numeric quantity column."""

    # First look for likely names
    keywords = [
        "quantidade",
        "quantity",
        "qtd",
        "total",
        "volume"
    ]

    for column in df.columns:

        column_name = str(column).lower()

        if any(keyword in column_name for keyword in keywords):
            return column

    # Otherwise find the column with the most numeric values
    best_column = None
    best_count = 0

    for column in df.columns:

        converted = df[column].apply(convert_number)
        count = converted.notna().sum()

        if count > best_count:
            best_count = count
            best_column = column

    return best_column
