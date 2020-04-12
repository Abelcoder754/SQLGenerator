from Generate import Generate


class Service:
    _generate: Generate

    def __init__(self):
        self._generate = Generate
    
    def validateSelect(self,data:list,table:str,where:list,cond:list):
        if self.isEmptyStr(table):
            return False
        self.getGenerator().generateSelectCommand(table,data,where,cond)
        return self.getGenerator().getCommand()
    
    def validadeUpdate(self,data:list,table:str,where:list,cond:list):
        if self.isEmptyStr(table):
            return False
        self.getGenerator().generateUpdateCommand(table,data,where,cond)
        return self.getGenerator().getCommand()

    def isEmptyStr(self,table:str):
        return table.__len__() < 1
    
    def getGenerator(self):
        return self._generate

