# скорочення спрощення коду, але без повторного використання
# ітератори
# class Counter:
#    def __init__(self,maxNum):
#        self.maxNum=maxNum
#        self.kol=0
#    def __iter__(self):
#        self.kol=0
#        return self
#    def __next__(self):
#        self.kol+=1
#        if self.kol > self.maxNum:
#            raise StopIteration
#        return self.kol
# count=Counter(3)
# for i in count:
#    print(i, end =' ')
# print(next(count))
# print(iter(count))
# print(next(count))


# num=[4,5,9,6,1]
# numIter=iter(num)
# print(next(numIter))
# print(next(numIter))
# print(next(numIter))

# class WordLen:
#     def __init__(self,word):
#         self.word=word
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index>=len(self.word):
#             raise StopIteration
#         listWordLen=len(self.word[self.index])
#         self.index+=1
#         return listWordLen
#
# wordList=["python", "c++", "java", "js", "php"]
# wordIter=WordLen(wordList)
# for i in wordIter:
#     print(i, end=' ')

#генератори def  ..yield
# def powerNum(num):
#     for i in range(num+1):
#         yield 3**i
# for i in powerNum(4):
#     print(i)

# import random
# def abc(num):
#     letters='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#     for i in range(num):
#         yield random.choice(letters)
# for i in abc(7):
#     print(i,end=' ')

#декоратери @ допоміжна функція
def calcAudit(num):
    def calcAudit(*args,**kwargs):
        try:
            res=num(*args,**kwargs)
        except Exception as e:
            print('Сталася якась проблема',e)
        else:
            print('Результат: ',res)
    return calcAudit
@calcAudit
def calc(num):
    return eval(num)
calc('2+2*3-4')
calc('(12+2)*3-1')