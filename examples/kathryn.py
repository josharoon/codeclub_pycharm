


def katfunc(*args):

    #'print num1+" "+num2
    for anything in ourlist:
        if type(anything)==list:
            for item in anything:
                print item
        print anything
    print ourlist[0]
fruits=["apples","bananas","pears"]
ourlist=["kat","Gep","Lar","J",7,fruits]
katfunc(ourlist)


