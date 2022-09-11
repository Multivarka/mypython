import random


class MyRandom:
    def __init__(self,end_number):
        self.nums = []
        self.end_number = end_number


    def get_random(self):
        num = random.randint(1, self.end_number)
        while len(self.nums) != self.end_number:
            if num in self.nums:
                num = random.randint(1, self.end_number)
            else:
                self.nums.append(num)
        return self.nums






m = MyRandom(10).get_random()
for i in m:
    a = input(f"Вы загадали число {i}?\n")
    if a.lower() == "да":
        print("Победа")
        break
    else:
        print("Попробую еще раз")


