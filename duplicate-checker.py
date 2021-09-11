import os
import pickle



ans1 = input("have you run this program in two directories y or n\n")


path = input("type in the path to the directory you want to run the program in. use forward slashes (C:/whatever) \n")

files = os.listdir(path)


if(ans1 == 'y'):
    with open(path + 'directory1.pickle', 'rb') as f1, open(path+'directory2.pickle', 'rb') as f2:
        list1 = pickle.load(f1)
        list2 = pickle.load(f2)
        set1 = set(list1)
        set2 = set(list2)
        difference = set2-set1
        print(difference)

else:
    num = 0
    while True:
        try:
            num = int(input("is this your first or second directory running this? type 1 or 2\n"))
        except ValueError:
            print("type a number")
            continue
        if ( not ( num==1) and not ( num==2 )):
            print("type 1 or 2")
            continue
        else:
            break
    filename = 'directory'+str(num)+'.pickle'
    with open(path+filename, 'wb') as f:
        pickle.dump(files, f)