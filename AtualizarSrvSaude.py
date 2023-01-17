import os
import shutil
import time

LOG = open("AtualizaSrvSaude_Log.txt", "w+")
ROOT_DIR =os.getcwd()
ROOT_DIR = ROOT_DIR.replace("\dist","")
print(f"Caminho Raiz: {ROOT_DIR}",file=LOG)

lista_pastas = []
#Coletar a lista de nome dos arquivos
for pasta in os.listdir(f"{ROOT_DIR}\\"):
    d = os.path.join(pasta)
    if (os.path.isdir(d)) and ("Srv" in d) or ("Svr" in d):
        shutil.copy(f"{ROOT_DIR}\\SrvSaude.exe",f"{ROOT_DIR}\\"+d)
        print(f"SrvSaude.exe copiado para {ROOT_DIR}\\{d}", file=LOG)
        print(f"SrvSaude.exe copiado para {ROOT_DIR}\\{d}")
        lista_pastas.append(d)

print("-----------------------------------------------")            

for lista in lista_pastas:
    os.chdir(f"{ROOT_DIR}\\{lista}")
    print(f"Atualizar {lista}?")
    x= input("Digite S para Sim e N para Não:").upper()
    if x == "S":
        for exe in os.listdir():
            if ("Srv" in exe) and (".exe" in exe) and ("SrvSaude.exe" not in exe):
                os.system('taskkill /IM "' + exe + '" /F')
                print(f"Finalizou = {ROOT_DIR}\\{lista}\\{exe}", file=LOG)
                print(f"Finalizou = {ROOT_DIR}\\{lista}\\{exe}")
                time.sleep(2)
                os.remove(exe)
                print(f"Deletou = {ROOT_DIR}\\{lista}\\{exe}", file=LOG)
                print(f"Deletou = {ROOT_DIR}\\{lista}\\{exe}")
                os.rename("SrvSaude.exe",f"{exe}")
                print(f"Renomeou = {ROOT_DIR}\\{lista}\\SrvSaude.exe para {exe}", file=LOG)
                print(f"Renomeou = {ROOT_DIR}\\{lista}\\SrvSaude.exe para {exe}")
                time.sleep(1)
                os.startfile(exe)
                print(f"Iniciou = {ROOT_DIR}\\{lista}\\{exe}", file=LOG)
                print(f"Iniciou = {ROOT_DIR}\\{lista}\\{exe}")
                time.sleep(5)
                print("-----------------------------------------------",file=LOG)
                print("-----------------------------------------------")
    else:
        os.remove('SrvSaude.exe')
        print(f"Apagou o SrvSaude.exe da {ROOT_DIR}\\{lista}",file=LOG)
        print(f"Apagou o SrvSaude.exe da {ROOT_DIR}\\{lista}")

print("!!!!Atualização Concluida!!!!",file=LOG)
print("!!!!Atualização Concluida!!!!")
print("-----------------------------------------------")
print("Reiniciar o explorer.exe, afins de limpar de recarregar a bandeja dos icones?")
decisao = input("S = Sim | N = Não : ").upper()
if decisao == "S":
    os.system("taskkill /IM explorer.exe /F")
    time.sleep(2)
    os.system("start explorer.exe")