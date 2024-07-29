import json
import os

# JSON dosyasını okuyun
try:
    with open('sepet.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Dosya bulunamadı, dosya adını ve yolunu kontrol edin.")
    exit()

# İlgili city kodlarını tanımlayın
city_codes = [87, 88, 98, 101, 84, 96, 92, "None"]

# Veriyi düzenleyin ve ilgili city kodlarına göre filtreleyin
filtered_data = {}
for item in data:
    city = item.get('city')
    if city in city_codes or city is None:
        user_id = item['id']
        if user_id not in filtered_data:
            filtered_data[user_id] = {
                'id': user_id,
                'name': item['name'],
                'phone': item['phone'],
                'city': item['city'],
                'products': []
            }
        product = {
            'stok_no': item['stok_no'],
            'title': f"{item['title']} / {item['beden']}",
            'date': item['date']
        }
        filtered_data[user_id]['products'].append(product)

# Düzenlenmiş veriyi şehir bazında gruplandır
city_groups = {}
for user in filtered_data.values():
    city = user['city']
    if city not in city_groups:
        city_groups[city] = []
    city_groups[city].append(user)

# Grupları liste haline getirin
final_grouped_data = list(city_groups.values())

# Düzenlenmiş veriyi yeni bir JSON dosyasına kaydedin
output_file = 'final.json'

try:
    if os.path.exists(output_file):
        os.remove(output_file)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_grouped_data, f, ensure_ascii=False, indent=4)
    print(f"Veri seti başarıyla düzenlendi ve {output_file} dosyasına kaydedildi.")
except IOError as e:
    print(f"Dosya yazma hatası: {e}")
