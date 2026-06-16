#if and else
menu = input("ketik .menu untuk melihat daftar menu :  ")

if menu==".menu":
    menu = f"""
    =======================
         🛒 DAFTAR PRODUK
    =======================
    │ 1  │ Laptop          
    │ 2  │ Mouse           
    │ 3  │ Keyboard        
    │ 4  │ Monitor         
    │ 5  │ Printer         
    =======================
    0. Keluar
    =======================
    👉 Pilih produk:
    """
    print(menu)

    daftarMenu = input("Silahkan masukkan angka produk :  ")
    if daftarMenu=="1":
        laptop = f"""Laptop : Rp8.000.000
silahkan hubungi owner untuk melakukan pembelian"""
        print(laptop)

    if daftarMenu=="2":
        tikus = f""" Mouse : Rp 100.000
silahkan hubungi sul pantek untuk melakukan pembelian"""
        print(tikus)
    
    if daftarMenu=="3":
        keyboard = f"""Keyboard : Rp 250.000
silahkan hubungi rafi ganteng untuk melakukan pembelian"""
        print(keyboard)

    if daftarMenu=="4":
        monitor = f"""Monitor : Rp 1.500.000
silahkan hubungi rafi ganteng untuk melakukan pembelian"""
        print(monitor)

    if daftarMenu=="5":
        printer = f"""Printer : 1.200.000
silahkan hubungi owner untuk melakukan pembelian"""
        print(printer)
    
    exit = print("anda keluar dari menu")
    if exit=="0" : print(exit)

else:
    print("silahkan masukkan perintah yang benar")
    print()

print()
print("Terimakasih atas kunjungan anda!!!!!")
        