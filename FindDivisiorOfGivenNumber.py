
class Divisior:
    # Divisior=[]
    def __init__(self,number):
        self.number=number

    def number_divisior(self):
        divisiors=[]
        for i in range(1,self.number+1):
            if self.number%i==0:
                divisiors.append(i)
        return divisiors
        


number=int(input("Enter Any Number : "))
obj=Divisior(number)
if number <=0:
    print("Write Valid number")
else:
    div=obj.number_divisior()

print(f"The divisiors of {number} are : {div}")