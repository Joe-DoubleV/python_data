#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

def npsaves():
    print("# savetxt(),.loadtxt()")
    a = np.arange(24).reshape(4,6)
    print(a)
    # .# savetxt(),.loadtxt()
    # np.savetxt("./data.csv",np.log(a+1),fmt="%.4f",delimiter=",")
    a = np.loadtxt("./data.csv",dtype=np.float,delimiter=",")
    print(a)

    print("# .tofile() .fromfile()")
    # # .tofile() .fromfile()
    # a.tofile("./a.dat",sep=",",format="%.3f")
    b = np.fromfile("./a.dat",dtype=np.float,sep=",")
    print(b.reshape(6,4))

    print("# # save() .load()")
    # # save() .load()
    c = b.reshape(2,3,4)
    # print(c)
    # np.save("c",c)
    d = np.load("c.npy")
    print(d)

    print("# random.rand")
    print(np.random.rand(2,3,4))
    print("# random.randn")
    print(np.random.randn(2,3,4))
    print("# random.randint")
    print(np.random.randint(100,200,(4,6)))

    b = np.random.randint(10,20,(8,))
    print("# random.choice")
    print(b)
    print(np.random.choice(b,(2,4),replace=False))
    print(np.random.choice(b,(2,4),p=b/np.sum(b)))

    b = np.arange(10,31).reshape(3,7)
    print(b)
    print(np.sum(b),np.sum(b,0),np.sum(b,1))
    print("#"*20)
    c = np.arange(24).reshape(2,3,4)
    print(c)
    print(np.sum(c),np.sum(c,0),np.sum(c,(1,2)),sep="\n")
    print("mean")
    print(np.mean(c),np.mean(c,0),np.mean(c,(1,2)),sep="\n")
    print("std")
    print(np.std(c),np.std(c,0),np.std(c,(1,2)),sep="\n")
    print("var")
    print(np.var(c),np.var(c,0),np.var(c,(1,2)),sep="\n")
if __name__ == '__main__':
    npsaves()
