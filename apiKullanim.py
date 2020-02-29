import request as rq

#print(rq.get(url).text)
bdoviz=input("bozulan doviz turu(usd,eur,try)").upper()
adoviz=input("alinan doviz turu(usd,eur,try)").upper()
miktar=float
url="https://api.exchangeratesapi.io/latest?base="+bdoviz
siteveri=rq.get(url).json()
print(float(siteveri["rates"][adoviz])*miktar)

with open("person_data.txt","r",encoding="utf-8") as dosya
    boyliste=[]
    for veri in dosya.readlines()
        boy=veri.strip().split()[2]
        boyliste.append(boy)
        #print(boy)
