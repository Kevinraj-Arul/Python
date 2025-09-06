#simple inheritance
class friends:
    def ball(self):
        print("frn1 ball")
class frnd2(friends):
    def bat(self):
        print("frn2 bat")
f1=frnd2()
f1.bat()
f1.ball()
#multiple inheritance
class dad:
    def shop(self):
        print("shop steel")
class mom:
    def money(self):
        print("2 lakh")
class son(dad,mom):
    def job(self):
        print("50 k")
s1=son()
s1.job()
s1.money()
s1.shop()
#hirachical inheritance
class dad:
    def shop(self):
        print("shop steel")
class son(dad):
    def job(self):
        print("50 k")
class son2(dad):
    def job2(self):
        print("own business")
s1=son2()
s1.job2()
s1.shop





