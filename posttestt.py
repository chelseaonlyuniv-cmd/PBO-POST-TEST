class LoginKasir:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
    
    def validasiLogin(self):
        pass

    def logout(self):
        pass

class KoneksiDatabase:
    def __init__(self, host: str, database: str, username: str, password: str):
        self.host = host
        self.database = database
        self.username = username
        self.password = password
    
    def membukaKoneksi(self):
        pass

    def eksekusiQuerySelect(self):
        pass

    def eksekusiQueryInsert(self):
        pass

    def eksekusiQueryUpdate(self):
        pass

    def eksekusiQueryDelete(self):
        pass

    def tutupKoneksi(self):
        pass

class HitungPembayaran:
    def __init__(self, idMenu: str, namaMenu: str, harga: float, jumlah: int):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = harga * jumlah
    
    def insertPembayaran(self):
        pass
    
    def updatePembayaran(self):
        pass
    
    def deleteDataPembayaran(self):
        pass
    
    def cariDataPembayaranByMenu(self, menu: str):
        pass

class PembayaranTunai(HitungPembayaran):
    def hitungTotalHarga(self):
        pass

class PembayaranByCard(HitungPembayaran):
    def hitungTotalHarga(self):
        pass

class CetakStruk:
    def __init__(self, noStruk: str, totalHarga: float):
        self.noStruk = noStruk
        self.totalHarga = totalHarga
    
    def cetakStruk(self):
        pass

class TabelHitungPembayaran:
    def __init__(self, idMenu: str, namaMenu: str, harga: float, jumlah: int):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = harga * jumlah
    
    def setIdMenu(self, idMenu: str): pass
    def setNamaMenu(self, namaMenu: str): pass
    def setHarga(self, harga: float): pass
    def setJumlah(self, jumlah: int): pass
    def getIdMenu(self): pass
    def getNamaMenu(self): pass
    def getHarga(self): pass
    def getJumlah(self): pass
    def getTotalHarga(self): pass

class TabelPembayaranByCard:
    def __init__(self, idCard: str, jenisCard: str, namaBank: str, totalHarga: float):
        self.idCard = idCard
        self.jenisCard = jenisCard
        self.namaBank = namaBank
        self.totalHarga = totalHarga
    
    def setIdCard(self, idCard: str): pass
    def setJenisCard(self, jenisCard: str): pass
    def setNamaBank(self, namaBank: str): pass
    def setTotalHarga(self, totalHarga: float): pass
    def getIdCard(self): pass
    def getJenisCard(self): pass
    def getNamaBank(self): pass
    def getTotalHarga(self): pass

class Main:
    def __init__(self):
        self.loginKasir = None
        self.koneksiDatabase = None
    
    def login(self):
        pass
    
    def uiMenu(self):
        pass

    def pilihMetodePembayaran(self, total: float):
        pass

    def uCetakStruk(self, total: float):
        pass

    def main(self):
        pass

if __name__ == "__main__":
    
    # ini membuat objek dari class
    login_obj = LoginKasir("kasir", "1234")
    db_obj = KoneksiDatabase("localhost", "kasir_db", "root", "pass")
    hitung_obj = HitungPembayaran("M001", "Nasi Goreng", 15000, 2)
    tunai_obj = PembayaranTunai("M002", "Mie Goreng", 12000, 1)
    card_obj = PembayaranByCard("M003", "Sate Ayam", 20000, 1)
    struk_obj = CetakStruk("S001", 30000)
    tabel_menu_obj = TabelHitungPembayaran("M001", "Nasi Goreng", 15000, 2)
    tabel_card_obj = TabelPembayaranByCard("C001", "Debit", "BCA", 20000)

    app = Main()
    app.main()
