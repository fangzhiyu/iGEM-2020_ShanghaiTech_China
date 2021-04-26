import os 

with open('./target.txt','r') as f:
    target = f.read().replace('\n','')


'''
given protospacer
examine potential off-target
'''

protospacer = 'GCGATCTGGTTTTCCGCCAGCTC'
PAM = 'TTTG'

seed_len = 8
def mutation(number_mutation:int,protospacer:str):
    mutation_box = []
    nucleotides = ['A','T','C','G']
    for i in range(len(protospacer)):
        tmp = list(protospacer)
        for i in range(3):
            repository = list(set(nucleotides).difference([tmp[i]]))
            tmp[i] = repository[i]
            mutation_box.append(''.join(tmp))
    
    print('the number of mutations is %d \nresult' % (len(mutation_box)))
    print(mutation_box)
    return mutation_box

def find_off_target(target:str, protospacer:str, PAM:str, seed_len:str):
    specific_seq = protospacer[:seed_len]
    def search(to_search:str, search_in:str):
        tmp = [i for i in range(len(search_in)) if search_in.find(to_search,i) == i ]
        if len(tmp) == 0 :
            print('not found')
        else:
            print('find PAM at ', tmp)
        return tmp
    search(PAM,target)
    search(protospacer,target)
    '''
    generate mutations 
    mutation number 1 
    '''
    mutation(1,protospacer)
    for i in mutation(1,protospacer):
        search(i,target)

    
    
find_off_target(target,protospacer,PAM,seed_len)