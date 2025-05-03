class MathUtils:

    @staticmethod
    def add(a,b):
        return a+b
    

result = MathUtils.add(2,4)
print(result)

obj = MathUtils()

print(obj.add(1,3))