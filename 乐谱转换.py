
tone=['1d','1','1g',
      '1d#','1#','1g#',
      '2d','2','2g',
'2d#','2#','2g#',
      '3d','3','3g',

      '4d','4','4g',
'4d#','4#','4g#',
      '5d','5','5g',
'5d#','5#','5g#',
      '6d','6','6g',
'6d#', '6#', '6g#',
      '7d','7','7g',
      ]     #乐谱音调
frequency=[262,523,1046,
           277,544,1109,
           294,587,1175,
           311,622,1245,
           330,659,1318,
           349,698,1397,
           370,740,1480,
           392,784,1568,
           415,831,1661,
           440,880,1760,
           466,932,1865,
           494,988,1976
           ]  #音调频率
beat=[375,750,1500,3000]  #节拍时长
length=['0.5','1','2','4']#节拍数
pinlv=dict(zip(tone,frequency))   #对应压缩成字典
changdu=dict(zip(length,beat))

def scoremake():   #输入简谱音符
    score=[]
    while True:
        n = input('输入每个音符后回车:')
        score.append(n)
        if n == 'OK':
            score.remove('OK')
            break
    return score

def jiepaimake():#输入对应节拍数
    jiepai1=[]
    while True:
        n = input('输入每个节拍后回车:')
        jiepai1.append(n)
        if n == 'ok':
            jiepai1.remove('ok')
            break
    return jiepai1
def thescore(*yuepu_make):  #寻找对应频率
    abc=[]
    for each in yuepu_make:
        a = pinlv[each]
        abc.append(a)
    return abc

def thejiepai(*changdu_make): #寻找对应时长
    abc=[]
    for each in changdu_make:
        a = changdu[each]
        abc.append(a)
    return abc
def printscore(*lise2):
    c=len(lise2)   
    for i in range(c):
        print("%d,"%score[i],"%d,"%jiepai[i])
      

if __name__ == '__main__':

    yuepu = scoremake()
    paishu= jiepaimake()
    score=thescore(*yuepu)
    jiepai=thejiepai(*paishu)
    printscore(*score)


