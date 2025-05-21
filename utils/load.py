import pandas as pd
from sqlalchemy import create_engine, text
import gspread
from google.oauth2.service_account import Credentials

def load_to_spreadsheet(df, spreadsheet_id, sheet_name):
    SCOPES = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive.file'
    ]
    
    try:
        creds = Credentials.from_service_account_file(
            'project-pemrosesan-data-284-3ff50f58e05b.json',
            scopes=SCOPES
        )
        client = gspread.authorize(creds)
        
        # Debug: Cetak email service account
        print(f"Menggunakan service account: {creds.service_account_email}")
        
        sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
        sheet.clear()
        
        # Format data untuk Google Sheets
        data = [df.columns.tolist()] + df.values.tolist()
        sheet.update('A1', data)
        
        print("✅ Data berhasil ditulis ke Google Spreadsheet!")
    except Exception as e:
        print(f"❌ Gagal menulis ke Google Sheets: {str(e)}")
        raise

def load_to_postgres(data_bersih, db_url):
    try:
        engine = create_engine(db_url)

        # Validasi koneksi ke database
        with engine.begin() as con:
            print("✅ Koneksi ke database berhasil!")

            # Pastikan tabel tersedia
            create_table_query = text("""
                CREATE TABLE IF NOT EXISTS fashion_products (
                    id SERIAL PRIMARY KEY,
                    "Title" TEXT NOT NULL,
                    "Price" NUMERIC(10, 2) NOT NULL,
                    "Rating" NUMERIC(3, 2) NOT NULL,
                    "Colors" INTEGER NOT NULL,
                    "Size" TEXT NOT NULL,
                    "Gender" TEXT NOT NULL,
                    "Timestamp" TIMESTAMP NOT NULL
                );
            """)
            con.execute(create_table_query)
            print("✅ Tabel 'fashion_products' berhasil dicek atau dibuat.")

            # Validasi data yang dimuat
            # Validasi kolom (versi cepat)
            print("🔎 Kolom di data:", list(data_bersih.columns))
            expected = {'Title', 'Price', 'Rating', 'Colors', 'Size', 'Gender', 'Timestamp'}
            if not expected.issubset(data_bersih.columns):
                missing = expected - set(data_bersih.columns)
                raise ValueError(f"❌ Kolom tidak sesuai. Yang hilang: {missing}")

            # Load data ke tabel
            data_bersih.to_sql('fashion_products', con=con, if_exists='append', index=False,chunksize=500,
                method='multi')
            print("✅ Data berhasil disimpan ke tabel 'fashion_products'.")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")
        raise