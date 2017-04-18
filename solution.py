def answer(plaintext):
    dic={}
    dic['a']="100000"
    dic['b']="110000"
    dic['c']="100100"
    dic['d']="100110"
    dic['e']="100010"
    dic['f']="110100"
    dic['g']="110110"
    dic['h']="110010"
    dic['i']="010100"
    dic['j']="010110"
    dic['k']="101000"
    dic['l']="111000"
    dic['m']="101100"
    dic['n']="101110"
    dic['o']="101010"
    dic['p']="111100"
    dic['q']="111110"
    dic['r']="111010"
    dic['s']="011100"
    dic['t']="011110"
    dic['u']="101001"
    dic['v']="111011"
    dic['w']="010111"
    dic['x']="101101"
    dic['y']="101111"
    dic['z']="101011"
    words=plaintext.split(" ")
    res=""
    for word in words:
        if word == '':
            continue
        for c in word.strip():
            if c.isupper():
                if res is "":
                    res+="000001"
                else:
                    res=res[:-1]
                    res+="1"
                c=c.lower()
            res+=dic.get(c)
        res+="000000"
    return res[:-6]

print(answer("The Smith Kim"))