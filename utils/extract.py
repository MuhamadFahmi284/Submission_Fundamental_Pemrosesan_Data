# extract.py
import requests
from bs4 import BeautifulSoup
import gspread
from google.oauth2.service_account import Credentials
import time
from datetime import datetime

SERVICE_ACCOUNT_FILE = 'project-pemrosesan-data-284-3ff50f58e05b.json'
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open_by_key('1iB08iXSlxkY_oG-sSGMUtQF-bTWJoXE41akyrZgPv2A').sheet1

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.115 Safari/537.36'
}

def get_page_url(base_url, page):
    """Membangun URL halaman sesuai format yang benar."""
    return f"{base_url}/" if page == 1 else f"{base_url}/page{page}"

def extract_product_data(product):
    """Mengambil detail produk dari elemen HTML."""
    try:
        title = product.select_one('.product-title').text.strip()
        price = product.select_one('.price-container').text.strip() if product.select_one('.price-container') else 'Price Unavailable'

        details = product.find_all('p')
        rating = details[0].text.strip().split('/')[0].replace('Rating: ', '') if len(details) > 0 else 'N/A'
        colors = ''.join(filter(str.isdigit, details[1].text.strip())) if len(details) > 1 else 'N/A'
        size = details[2].text.replace('Size: ', '').strip() if len(details) > 2 else 'N/A'
        gender = details[3].text.replace('Gender: ', '').strip() if len(details) > 3 else 'N/A'

        timestamp = datetime.now().isoformat()

        return {
            'Title': title,
            'Price': price,
            'Rating': rating,
            'Colors': colors,
            'Size': size,
            'Gender': gender,
            'Timestamp': timestamp
        }
    except Exception as e:
        print(f"❌ Gagal memproses produk: {e}")
        return None

def extract_data(base_url="https://fashion-studio.dicoding.dev", start_page=1, end_page=50):
    """Scraping data dari website berdasarkan halaman dan mengembalikan list of dictionaries."""
    all_data = []
    print("📊 Memulai proses ekstraksi data...")

    for page in range(start_page, end_page + 1):
        print(f"🔍 Mengambil data dari halaman {page}...")
        url = get_page_url(base_url, page)

        try:
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code != 200:
                print(f"❌ Gagal mengakses halaman {page}: {response.status_code}")
                continue

            soup = BeautifulSoup(response.text, 'html.parser')
            products = soup.select('.collection-card')

            if not products:
                print(f"❌ Tidak ada produk di halaman {page}")
                continue

            for product in products:
                data = extract_product_data(product)
                if data:
                    all_data.append(data)

            time.sleep(2)

        except Exception as e:
            print(f"❌ Kesalahan saat mengambil halaman {page}: {e}")

    print(f"✅ Total data yang diekstrak: {len(all_data)} baris.")
    return all_data
