class Animal:
    activityMultiplier=1.2
    def __init__(self,name ,weightKg,heightM,isPredator,speedKph):
        self.name=name
        self.weightKg=weightKg
        self.heightM=heightM
        self.isPredator=isPredator
        self.speedKph=speedKph
    
    def getBmi(self):
        # 体重を身長の二乗で割ったものを返して小数点第三位以下を切り捨てる
        return int(self.weightKg/self.heightM**2*100)/100
    
    def getDailyCalories(self):
        # 体重の0.75乗に70をかけたものにactivityMultiplierをかけたものを返して小数点第三位以下を切り捨てる
        return int(self.weightKg**0.75*70*self.activityMultiplier*100)/100

    def isDangerous(self):
        if self.isPredator:
            return True
        elif self.heightM>=1.7 or self.speedKph>=35:
            return True
        else:
            return False

rabbit = Animal("rabbit", 10, 0.3, False, 20)
snake = Animal("snake", 30, 1, True, 30)
elephant = Animal("elephant", 300, 3, False, 5)
gazelle = Animal("gazelle", 50, 1.5, False, 100)

print(rabbit.getBmi())
print(rabbit.isDangerous())
print(snake.isDangerous())
print(snake.getDailyCalories())
print(elephant.getBmi())
print(elephant.getDailyCalories())
print(gazelle.getDailyCalories())
print(gazelle.isDangerous())   
