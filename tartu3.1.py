fail = open(&quot;rebased.txt&quot;, encoding=&quot;UTF-8&quot;)
vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))
    input("sisesta aasta 2011-2019: ")
fail.close()
print(vastuvõetud[aasta-2011])