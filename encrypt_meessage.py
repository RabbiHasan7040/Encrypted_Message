# Encode and Decode script using Rakib Sir theory
# The code is written by Md. Rabbi Hasan
# Date: 20-1023

welcome = '''
// // // // // // // // // // // // // // // // // //
// Encode and Decode script using Rakib Sir theory // 
//                                                 //
// The code is written by Md. Rabbi Hasan          //
// NDC-24 G-7 Roll-12407040                        //
// // // // // // // // // // // // // // // // // //
'''
print(welcome)







def rkey(key):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    r_key = []
    for alph in alphabets:
        n = 0
        for x in key:
            if alph == x and n==0:
                r_key.append(x)
                n+=1
    return r_key

# Encode
def encode_func1(key,msg):
    if len(msg)!=len(key)*len(key):
        print("[-] Your message must contain {} character for the key '{}' \n[-] Please try again".format(len(key)*len(key),key))
    else:
        msg=msg.upper()
        key = key.upper()
        dic_L = {}
        for x in range(len(key)):
            for y in key:
                dic_L.update({y:[]})
        n2=0
        for x in key:
            l1 = []
            n=0
            for y in range(len(key)):
                l1.append(msg[y+n+n2:y+1+n+n2])
                n+=(len(key)-1)
            dic_L.update({x:l1})
            n2+=1

        # Final msg
        mg=[]
        for x in rkey(key):
            mg.append(dic_L[x])
        finalmsg=""
        for x in mg:
            for y in x:
                finalmsg+=y
        return "'"+finalmsg+"'"


# Decode
def decode_func(key,etext):
    etext=etext.upper()
    key = key.upper()

    r_key = rkey(key)
    mtext=""   # modified text
    n=0
    for x in etext:
        mtext+=x
        n+=1
        if n==len(key):
            mtext+=','
            n=0
    mtext=mtext.rstrip(',')
    text_l = mtext.split(',')

    dic_l = {}
    for x in range(len(r_key)):
        dic_l.update({r_key[x]:[]})

    all_keys = dic_l.keys()
    key_l=list(all_keys)

    for x in range(len(r_key)):
        l1=[]
        for y in text_l[x]:
            l1.append(y)
        dic_l.update({key_l[x]:l1})
    l2=[]
    for x in range(len(key)):
        l2.append([])

    for x in range(len(key)):
        for y in key:
            l2[x].append(dic_l[y][x])    
    result = ""
    for x in l2:
        for y in x:
            result+=y
    return "'"+result+"'"

def main():
    a = input("[+] Enter 1 to encode or 2 to decode : ")
    if a == '1':
        k = input("[+] Enter the key value : ")
        m = input("[+] Message must contain {} chacracters for the key => {} \n[+] Enter your message : ".format((len(k)*len(k)),k))
        print("[+] => {}".format(encode_func1(k,m)))

    elif a == '2':
        k = input("[+] Enter the key value : ")
        t = input("[+] Encoded text must contain {} chacracters for the key => {} \n[+] Enter your encoded text : ".format((len(k)*len(k)),k))
        print("[+] => {}".format(decode_func(k,t)))

main()


