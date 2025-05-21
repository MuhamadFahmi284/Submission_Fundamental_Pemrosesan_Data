from utils.extract import extract_data
from utils.transform import clean_and_transform
from utils.load import load_to_postgres,load_to_spreadsheet

# URL koneksi PostgreSQL
db_url = "postgresql://developer:Pratama284@localhost:5432/fashion_product"

# Spreadsheet ID dan nama sheet
spreadsheet_id = '1iB08iXSlxkY_oG-sSGMUtQF-bTWJoXE41akyrZgPv2A'
sheet_name = 'Sheet1'

# 1. 📊 Mengambil data dari website
data = extract_data()

# 2. 🔄 Membersihkan dan transformasi data
cleaned_df = clean_and_transform(data)

# 3. 📥 Memuat data ke PostgreSQL
load_to_postgres(cleaned_df, db_url)

# 4. 🧾 Load ke Google Sheets
load_to_spreadsheet(cleaned_df, spreadsheet_id, sheet_name)

print("Proses ETL selesai!!")