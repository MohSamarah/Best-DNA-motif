from pprint import pprint

necolotidemap = {'a':0 , 'c':1 , 'g':2  , 't':3}
reversemap={0:'a' , 1:'c' , 2:'g' , 3:'t'}


def score(s, DNA, l):
  cstring = ""
  score = 0
  aligment = list()
  for i in range(len(DNA)):
    DNA_standrd = DNA[i]
    aligment.append(DNA_standrd[s[i]-1 : s[i]+l-1])
  profile = [0 for x in range(4)]
  for i in range(l):
    profile = [0 for x in range(4)]
    for x in range(len(aligment)):
      sval = aligment[x][i]
      profile[necolotidemap[sval]] += 1
    score += max(profile)
    cstring += reversemap[profile.index(max(profile))]
  print(cstring)
  pr = (cstring, score)
  return pr


def BruteForceMotifSearch(DNA, t, n, l):
    main_list = []
    for i in range(t):
        temp_list = []
        temp_list = list(range(0, n-l+1))
        main_list.append(temp_list)
    pprint(main_list)
    bestScore = 0
    for a in range(1,len(DNA[0])-l-1):
        for b in range(1,len(DNA[1])-l-1):
            for c in range(1,len(DNA[2])-l-1):
                for d in range(1,len(DNA[3])-l-1):
                    for e in range(1,len(DNA[4])-l-1):
                        s_ = [a, b, c, d, e]
                        s = score(s_, DNA, l)
                        if s[1] > bestScore:
                            bestScore = s[1]
                            bestm = s[0]
                        print(bestScore)
                        if bestScore == l*t:
                            return s_
    return
DNA = ["cctgatagacgctatctggctatccaggtacttaggtcctctgtgcgaatctatgcgtttccaaccat","agtactggtgtacatttgatccatacgtacaccggcaacctgaaacaaacgctcagaaccagaagtgc","aaacgttagtgcaccctctttcttcgtggctctggccaacgagggctgatgtataagacgaaaatttt","agcctccgatgtaagtcatagctgtaactattacctgccacccctattacatcttacgtccatataca","ctgttatacaacgcgtcatggcggggtatgcgttttggtcgtcgtacgctcgatcgttaccgtacggc"]
l = 4
listt = list(range(0, len(DNA[0])-l+2))

print(listt)
best = BruteForceMotifSearch(DNA, 5, 69, 4)
print("best score is their", best)


