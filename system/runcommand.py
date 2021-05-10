import subprocess, time

subprocess.run("ls", shell=True, check=True) # shell=True vypise textovy vystup programu rovnou do konzole
#argument check=True zaridi, ze Python vypise chybu, pokud program skoncil chybou


result = subprocess.run("ls", capture_output=True) #zachyti textovy vystup, ten bude dostupny v navracenem objektu
print(result.stdout, result.stderr) #stdout standardni vystup programu, stderr vypisy errorovych hlasek

result.check_returncode() #zkontroluje, zda program skoncil spravne - alternativa check=True, pokud doslo k chybe, vyvola Exception Error


try: #volani zaobalime do try-except statementu, abychom v except mohli reagovat na timeout exception
  result = subprocess.run(["google-chrome", "ffa.vutbr.cz"], timeout=5) #timeout omezi beh programu na dany pocet sekund, pote jej nasilne ukonci
except subprocess.TimeoutExpired: #reagujeme na timeout exception, takze skript neskonci chybou, ale muze bezet dal
  print("timeout passed")




process = subprocess.Popen(["google-chrome", "avu.cz"]) #Popen neblokuje dalsi prubeh programu

print("process obsahujici prohlizec bezi a my pokraujeme v nasem python kodu")
time.sleep(10) #chvili pockame
process.kill() #a potom process ukoncime

print(process.stdout, process.stderr) #vypiseme stdout a stderr, jestli program nehodil nake chybove hlasky
