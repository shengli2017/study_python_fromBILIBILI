class Cat:

    def eat(self):
        # 哪一个对象调用的方法，self 就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):

        print("%s 爱喝水" % self.name)

# 创建猫对象
tom = Cat()

# 可以使用  .属性名  利用赋值语句就可以了
# tom.name = "Tom"

tom.eat()
tom.drink()
tom.name = "Tom"



