#menghitung harga jual tanah setelah di potong pajak

luasTanah = int(input("Masukkan Luas Tanah : "))
hargaPermeter = 300_000
harga = luasTanah * 300_000

if harga >= 100_000_000:
    pajak = harga *  5/100
    hargaJual = harga - pajak
    print(f"harga jual tanah sebelum dikenakan pajak = {harga}")
    print(f"harga jual Setelah dikenakan pajak 5% = {hargaJual}")
elif harga >= 50_000_000:
    pajak = harga *  3/100
    hargaJual = harga - pajak
    print(f"harga jual tanah sebelum dikenakan pajak = {harga}")
    print(f"harga jual Setelah dikenakan pajak 3% = {hargaJual}")
else:
    pajak = harga *  1/100
    hargaJual = harga - pajak
    print(f"harga jual tanah sebelum dikenakan pajak = {harga}")
    print(f"harga jual Setelah dikenakan pajak 1% = {hargaJual}")