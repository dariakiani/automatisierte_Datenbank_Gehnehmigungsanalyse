import pandas as pd

datei = "files/NEUEXLX.BImSchG_erster_vorzeitiger_Baubeginn_380-kV-UW_optimierter_Prompt_Daria_12.10.xlsx"

try:
    excel = pd.ExcelFile(datei)

    print("Datei erfolgreich geöffnet")

    print("\nVorhandene Sheets:")
    print(excel.sheet_names)

    for sheet in excel.sheet_names:
        df = pd.read_excel(datei, sheet_name=sheet)

        print("\n===================")
        print("Sheet:", sheet)
        print("Zeilen:", len(df))
        print("Spalten:")
        print(list(df.columns))

except Exception as e:
    print("Fehler:")
    print(e)


# Erstelle eine Funktion die eine Excel-Datei öffnet
# und die erste Zeile ausgibt
