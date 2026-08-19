import pandas as pd
from io import BytesIO
from .month import MONTHS_PT
from .helpers import convert_number

def prepare_data(df, month_column, quantity_column):
    data = df[[month_column, quantity_column]].copy()

    data.columns = ["Mês", "Quantidade"]

    data["Mês"] = (
        data["Mês"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    data["Mês Número"] = data["Mês"].map(MONTHS_PT)

    data["Quantidade"] = data["Quantidade"].apply(convert_number)

    # Remove rows that aren't valid months
    data = data.dropna(
        subset=["Mês Número", "Quantidade"]
    )

    data["Mês Número"] = data["Mês Número"].astype(int)

    data = data.sort_values("Mês Número")

    # Month-over-month variation
    data["Variação"] = data["Quantidade"].pct_change() * 100

    # Restore proper month names
    data["Mês"] = data["Mês"].str.capitalize()

    return data


def create_excel(data):
    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        data.to_excel(
            writer,
            index=False,
            sheet_name="Análise"
        )

        # workbook = writer.book
        worksheet = writer.sheets["Análise"]

        # Header formatting
        for cell in worksheet[1]:
            cell.font = cell.font.copy(
                bold=True
            )

        # Number formatting
        for row in worksheet.iter_rows(
            min_row=2
        ):
            row[1].number_format = '#,##0.00'
            row[3].number_format = '0.00%'

        # Adjust column widths
        for column in worksheet.columns:

            max_length = 0
            column_letter = column[0].column_letter

            for cell in column:
                if cell.value is not None:
                    max_length = max(
                        max_length,
                        len(str(cell.value))
                    )

            worksheet.column_dimensions[
                column_letter
            ].width = max_length + 3

    output.seek(0)

    return output
