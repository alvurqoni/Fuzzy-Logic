#EMOSI
emosi = [97, 36, 63, 82, 71, 79, 55, 57, 40, 57, 77, 68, 60, 82, 40, 80, 60, 50, 100, 11, 58, 68, 64, 57, 77, 98, 91, 50, 95, 27]
def fuzzyemosi(emosi, rendah, sedang,tinggi):
    if(emosi <= 27.0):
        rendah = 1.0
    elif(emosi > 27.0 and emosi <50.0):
        rendah = (50.0 - emosi)/ 23.0
        sedang = (emosi - 27.0)/ 23.0
    elif (emosi >= 50.0 and emosi <= 68.0):
        sedang = 1.0
    elif(emosi > 68.0 and emosi < 79.0):
        sedang = (79.0 - emosi)/ 11.0
        tinggi = (emosi - 68.0)/ 11.0
    elif(emosi >= 79.0):
        tinggi = 1.0

    return rendah, sedang, tinggi

#PROVOKASI
provokasi  = [74, 85, 43, 90, 25, 81, 62, 45, 65, 45, 70, 75, 70, 90, 85, 68, 72, 95,  18, 99, 63, 70, 66, 77, 55, 64, 59, 95, 55, 79]
def fuzzyprovokasi(provokasi, prendah, psedang, ptinggi):
    if (provokasi <= 53.0):
        prendah = 1.0
    elif(provokasi > 53.0 and provokasi < 57.0):
        prendah = (57.0 - provokasi)/ 4.0
        psedang = (provokasi - 53.0)/ 4.0
    elif(provokasi >= 57.0 and provokasi <= 63.0):
        psedang = 1.0
    elif(provokasi > 63.0 and provokasi < 87.0 ):
        psedang = (87.0 - provokasi)/ 24.0
        ptinggi = (provokasi-63.0)/ 24.0
    elif(provokasi >= 87.0):
        ptinggi = 1.0

    return prendah, psedang, ptinggi

#INFERENSIANSI
def inferensiasi (rendah, sedang, tinggi, prendah, psedang, ptinggi):
    yes = 0
    yes1 = 0
    yes2 = 0
    yes3 = 0
    yes4 = 0
    ya5 = 0

    no = 0
    no1 = 0
    no2 = 0
    no3 = 0
    no4 = 0
    
    if(rendah != 0 and prendah != 0):
        no1 = min (rendah,prendah)
    if(rendah != 0 and psedang != 0):
        no2 = min (rendah,prendah)
    if(rendah != 0 and ptinggi != 0):
        yes1 = min (rendah,ptinggi)
    if(sedang != 0 and prendah != 0):
        no3 = min (sedang,prendah)
    if(sedang !=0 and psedang != 0):
       no4 = min (sedang, psedang)
    if(sedang != 0 and ptinggi != 0):
        yes2 = min (sedang,ptinggi)
    if(tinggi != 0 and prendah != 0):
        no3 = min (tinggi,prendah)
    if(tinggi != 0 and psedang != 0):
        yes4 = min (tinggi, psedang)
    if(tinggi != 0 and ptinggi != 0):
        ya5 = min(tinggi,ptinggi)

    yes = max(yes1,yes2,yes3,yes4,ya5)
    no = max (no1,no2,no3,no4)

    if(no < yes):
        ket= "ya"
        
        
    else:
        ket= "tidak"

    return yes, no, ket

def fuzifikasi(yes,no):
    hoax = (no * 45 + yes * 55 )/(no + yes)
    return hoax


#INPUTAN
jumlah = 0
tampung = [ "ya", "ya", "tidak", "ya", "tidak", "ya", "tidak","tidak", "tidak", "tidak", "ya", "ya", "tidak","ya", "tidak", "ya", "tidak","ya", "tidak", "ya"]

while jumlah <30:
    rendah = 0
    sedang = 0
    tinggi = 0
    prendah = 0
    psedang = 0
    ptinggi = 0
    
    yes = -1
    no = -1
    sugeno = 0
    

    rendah, sedang, tinggi = fuzzyemosi(emosi[jumlah], rendah, sedang, tinggi)
    prendah, psedang, ptinggi = fuzzyprovokasi(provokasi[jumlah], prendah, psedang, ptinggi)
    yes, no, ket = inferensiasi(rendah, sedang, tinggi, prendah, psedang, ptinggi)
    sugeno = fuzifikasi(yes, no)
   

    
   
    print("berita:  ",jumlah+1,  "emosi : ",emosi[jumlah], "provokasi: ", provokasi[jumlah], "hoax : ", ket )

    print(" ")
    jumlah += 1
    

