class YanJu:
    name = "LL"
    def printName(self):
        print(YanJu.name)
        print(self.name)

print("ppppp")  #注意运行是 不仅只会运行该行，
                # 而是从上到下【class YanJu:到这里都会执行 顺序执行】
