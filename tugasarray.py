#GPA List
listGPA = [3, 2.7, 2.5, 4]

#Bonus
def hadiah(input):
    bonus = 500000
    hadiah = GPA * bonus
    return hadiah

#GPA Condition
for GPA in listGPA :
    print(GPA)
    if GPA > 3 :
        print ("Selamat anda mendpatkan haiah sebesar : Rp", hadiah(GPA))
    else :
        print ("Maaf anda tidak mendapatkan bonus")