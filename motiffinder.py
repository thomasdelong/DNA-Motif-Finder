#s=DNA string
#t=motif
#given s, find all locations of t in s
s=input('DNA to search:')
t=input('Motif:')
locations=''
instances=0
for i in range(len(s)):
    if s[i:i+len(t)] == t:
        locations += str(i+1)+' '
        instances += 1
print('Locations: '+locations)
print('Instances: '+str(instances))
