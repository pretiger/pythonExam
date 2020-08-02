import os


def changeName(path):
    for filename in os.listdir(path):
        print(filename, '=>', filename.replace('ㅁㄱㅇ', '마검왕'))
        os.rename(path+filename, path+filename.replace('ㅁㄱㅇ', '마검왕'))


changeName('C:/LocalData/novel/(완)마검왕/')
