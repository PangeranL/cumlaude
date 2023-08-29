# nama file :cumlaude.py
# pembuat : Ahmad Fahrezi (24060122140146)
# tanggal : 02-09-2022
# deskripsi :  menentukan apakah cumlaude atau tidak dari masa studi 

# definisi dan spsifikasi :
# masa_studi : integer --> real
# cumlaude : real --> boolean
# IPK [0...4]
# true artinya cumlaude
# false artinya tidak cumlaude 

# realisasi
def masa_studi (bulan) :
    return bulan/12

def cumlaude (bulan, IPK) : 
    return bulan<=4.5 and IPK >=3.5

# aplikasi
print(cumlaude(masa_studi(32),2.5))
print(cumlaude(masa_studi(42),3,4))
