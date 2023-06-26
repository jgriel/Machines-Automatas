import re

def main():
    reader = open("words", "r")
    #string-build (we love string-building!) all words into 1 string to use findall efficiently
    s = ''
    for line in reader:
         s += line

    wxxxe = re.findall("[w][a-z][a-z][a-z][e]", s)
    print("a)")
    print(wxxxe)
    print(len(wxxxe))

    t = set(re.findall("[a-z]*t+[a-z]*", s))
    r = set(re.findall("[a-z][a-z][a-z][a-z][r]", s))
    tr = t & r
    print("\nb)")
    print(list(tr))
    print(len(tr))

    #can reuse r from previous
    h = set(re.findall("[a-z]*h+[a-z]*", s))
    d = set(re.findall("[a-z]*d+[a-z]*", s))
    dhr = h & d & r
    print("\nc)")
    print(list(dhr))
    print(len(dhr))

    #can reuse h and r from previous
    #get sets where d is in positions [1,3] and create a union of them
    xdxxx = set(re.findall("[a-z][d][a-z][a-z][a-z]", s))
    xxdxx = set(re.findall("[a-z][a-z][d][a-z][a-z]", s))
    xxxdx = set(re.findall("[a-z][a-z][a-z][d][a-z]", s))
    hdr = h & (xdxxx | xxdxx | xxxdx) & r
    print("\nd)")
    print(list(hdr))
    print(len(hdr))


main()