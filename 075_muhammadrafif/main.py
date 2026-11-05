data_kelembapan = [22, 28, 34, 41, 55,
                   63, 72, 78, 31, 47,
                   66, 81, 19, 58, 69]
#data_kelembapan = [25, 45, 10, 75, 68]

# hitung rata-rata kelembapan (clear)
# hitung status kelembapan (clear)
# hitung kategori kelembapan (clear)

def rata_rata(data):
    total = 0
    for nilai in data:
        total += nilai
    return total / len(data)

def status_kelembapan(kelembapan):
    if kelembapan < 35:
        return "KERING / POMPA ON"
    elif kelembapan <= 70:
        return "NORMAL / POMPA OFF"
    else:
        return "BASAH / POMPA OFF"
    
print("rata-rata kelembapan:", rata_rata(data_kelembapan), "%")

print("status kelembapan")
for nilai in data_kelembapan:
    print(nilai, "% =", status_kelembapan(nilai))
    
def jumlah_kategori(data):
    kering = 0
    normal = 0
    basah = 0
    for kelembapan in data:
        status = status_kelembapan(kelembapan)
        if status == "KERING / POMPA ON":
            kering += 1
        elif status == "NORMAL / POMPA OFF":
            normal += 1
        else:
            basah += 1
    return kering, normal, basah
kering, normal, basah = jumlah_kategori(data_kelembapan)
print("jumlah kategori:")
print("KERING:", kering)
print("NORMAL:", normal)
print("BASAH:", basah)

print("=== SOIL MOISTURE MONITORING SYSTEM===")

for i in range(len(data_kelembapan)):
    kelembapan = data_kelembapan[i]
    status = status_kelembapan(kelembapan)
    print(i+1, ".", kelembapan, "%", "->", status)
    
kering, normal, basah = jumlah_kategori(data_kelembapan)
average = rata_rata(data_kelembapan)
    
print()
print("===RINGKASAN===")
print("total data:", len(data_kelembapan))
print("KERING:", kering)
print("NORMAL:", normal)
print("BASAH:", basah)
print("rata-rata suhu:", round(average, 2), "%")
print("minimum suhu:", min(data_kelembapan), "%")
print("maksimum:", max(data_kelembapan), "%")
