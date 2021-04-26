import os 
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from reverse_complement import complement

with open('./target.txt','r') as f:
    raw = f.read().replace('\n','')

'''
find conversed sequences in alleles
given 
sequences of alleles
length of target sequences
CG ratio of target sequences   50~60
5' end starts with C
'''
def cal_GC(tmp:str):
    ntar = tmp.count('G')+tmp.count('C')
    target = ntar/len(tmp)
    if target >= .5 and target <= 0.6:
        return True
    else:
        return False

# sequences = 'ATCGATCGATCGATCGATCGATCGATCGATTCGATCGATTCGATCGATTCGATCGATCGATCGATCG'
target_len = 33


protospacer = 'GCGATCTGGTTTTCCGCCAGCTC'
a = raw.split(protospacer)
if len(a[0]) > 100:
    a[0] = a[0][-100:]
    print('before protospacer: ',len(a[0]))
if len(a[1]) > 100:
    a[1] = a[1][:100]
    print('after protospacer: ',len(a[1]))

def fsearch(tmp:str):
    search_times = len(tmp) + 1 - target_len
    print('search %d times'%(search_times))
    box = []
    position = []
    for i in range(search_times):
        target = tmp[i: i + target_len]
        if target[0] == 'C' and cal_GC(target):
            box.append(target)
            position.append(tmp.find(target)+1)
            # print(target)
    return [box, position]
    
def rsearch(tmp:str):
    search_times = len(tmp) + 1 - target_len
    print('search %d times'%(search_times))
    box = []
    position = []
    for i in range(search_times):
        target = tmp[i: i + target_len]
        if target[-1] == 'G' and cal_GC(target):
            box.append(target)
            position.append(tmp.find(target)+1)
            # print(target)
    return [box, position]    
    
    


box = fsearch(a[0])[0]
position = fsearch(a[0])[1]
for j in range(len(box)):
    print('%d ~ %d: %s'%( -1 * (len(a[0]) - position[j]), -1 * (len(a[0])-(position[j] + target_len)), box[j]))
    
box = rsearch(a[1])[0]
position = rsearch(a[1])[1]
for j in range(len(box)):
    print('%d ~ %d: %s'%(   position[j],  (position[j] + target_len), complement(box[j])))