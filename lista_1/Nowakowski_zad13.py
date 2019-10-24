student1={"nazwisko":"Manka", "fizyka":4,"matematyka":4.5, "geografia":4,"wf":5}
student2={"nazwisko":"Ramowska", "fizyka":5,"matematyka":5, "geografia":5,"wf":5}
student3={"nazwisko":"Paszyn", "fizyka":3.5,"matematyka":4.5, "geografia":4.5,"wf":5}
student4={"nazwisko":"Zakwinu", "fizyka":3,"matematyka":3, "geografia":5,"wf":4}

lista=[student1,student2,student3,student4]

for i in lista:
    srednia=0
    srednia=(i["fizyka"]+i["matematyka"]+i["geografia"]+i["wf"])/4
    print("Uczeń "+ i["nazwisko"]+ " uzyskał następujące oceny: "
          + str(i["fizyka"]) + ", " + str(i["matematyka"])+ ", "
          + str(i["geografia"]) + ", " + str(i["wf"])
          + " ze średnią: "+str(srednia))


