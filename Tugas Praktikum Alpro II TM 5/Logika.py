#import fungsi mahasiswa dari file Database
from Database import mahasiswa

#membuat fungsi untuk mencari data mahasiswa dari NIMnya
def cari_mahasiswa(NIM):
    for row in mahasiswa():
        if row['NIM'] == NIM:
            return row


