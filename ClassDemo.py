class ClassDemo:
    count = 0
    name = 'MyClass'
    
    def __init__(self,  name):
        self.name = name
        
        print('类名%s 变量名%s' %  (ClassDemo.name,  self.name))
        
    def setCount(self,  count):
        self.count = count
        
    def getCount(self):
        return self.count
        
if __name__ == "__main__":
    cls = ClassDemo("fuck")
    cls.setCount(100)
    print('count %d' %  cls.getCount())
