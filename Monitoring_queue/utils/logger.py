class Logger(object):
    def __init__ (self, prefix: None, level: None):
        self.prefix = prefix
        self.level = '>>> ' + level + ": "

    def info(self, *arguments): 
        print(self.level, self.prefix, *arguments, sep = ' ') 


    