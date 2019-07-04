

def job1(a):
    print(a/a)




if __name__ == '__main__':
    for i in [0,2,3,4,-1]:
        try:
            job1(i)
            print("test ok ",i)
        except:
            print("test error ",i)
