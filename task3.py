weigt=int(input("weigt"))
unit=input("kgm or lbs:")
if unit=="k":
    converted=weigt/0.45
    print("weigt in lab:"+str(converted))
else:
    converted=weigt*0.45
    print("weigt in kgm:"+str(converted))






    
