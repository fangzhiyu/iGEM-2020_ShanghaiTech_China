import sys
import os

with open(os.getcwd()+'/ezbiocloud_qiime_full.fasta') as f:
    raw = f.read()
    raw = raw.split('>')[1:]
    box = []
    for i in raw:
        tmp = i[:-1] 
        tmp = tmp.split('\n')
        box.extend(tmp)
    raw = box
    assert type(raw) == list


dictionary = {}

# print(raw)
print('the length of raw is ',len(raw))
print(raw[:100])


number_repo = []
index = [i for i in range(len(raw))]
for i in index[0::2]:
    number_idx  = i
    inhalt_idx  = i + 1
    number = raw[number_idx]
    number_repo.append(number)
    dictionary[number] = raw[inhalt_idx]
print('there are totally %d sequences'%(len(raw)))


for i in range(145810,145812):
    i = str(i)
    print(i,dictionary[i])


primer_f = 'GAATTGACGGG'
primer_r = 'GGGTTGCGCTCGTTG'

def reverse_complement(a:str):
    replacement = {'A':'T','T':'A','C':'G','G':'C'}
    new = str()
    for i in a:
        new += replacement[i]
    return new

def pcr(tar,fp,rp):
    a = tar.find(fp)
    b = tar.find(rp)
    print(a,b)

pcr(dictionary['145810'],primer_f,primer_r[::-1])

def transcription(a):
    replacement = {'A':'U','T':'A','C':'G','G':'C'}
    a = a.replace(' ','')
    new = str()
    for i in a:
        new += replacement[i]
    print(new)
    return new

transcription('     ACGGACGAGAAGCTTGCTTCTCT')