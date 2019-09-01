

class FileLoader:
    
    def load(self,  path,  cbk):
        #第一种方法
        f = open(path, "r",  encoding = 'UTF-8')   #设置文件对象
        line = f.readline()
        line = line[:-1]
        while line:             #直到读取完文件
            line = f.readline()  #读取一行文件，包括换行符
            cbk(line)
        f.close() #关闭文件
        
    def save(self, lines,  path):
        with open(path,"w") as f:
            f.writelines(lines)
        

def line_parser(line):
    print(line)
    

if __name__ == '__main__':
    loader = FileLoader();
    loader.load('test.txt', line_parser)
