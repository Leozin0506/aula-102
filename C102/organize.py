import os
import shutil
from_dir = "C:/Users/Suporte/Documents/Python/C102"
to_dir = "C:/Users/Suporte/Downloads"
list_of_files = os.listdir(from_dir);
#print(list_of_files);
for file_name in list_of_files:
    nome,extencion = os.path.splitext(file_name);
    #print(nome);
    #print(extencion);
    if extencion == "":
        continue
    if extencion in [".gif",".png",".jpg",".jpeg",".jfif"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir + "/" + "Arquivos_image"
        path3 = to_dir + "/" + "Arquivos_image" + "/" + file_name

        #print("path1", path1);
        #print("path3", path3);

        if os.path.exists(path2):
            print("movendo " + file_name + "...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("movendo " + file_name + "...")
            shutil.move(path1, path3)