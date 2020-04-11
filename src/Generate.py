from commands.Commands import Commands


class Generate(Commands):
    _command: str

    def __init__(self):
        super().__init__()
        self._command = ""
    
    # select part

    def generateSelectCommand(self,table:str,data:list,where:list):
        self.cleanCommand()
        self.setCommand(  # basic command header # select
            self.getData1(1)
        )
        if self.isEmptyList(data) and self.isEmptyList(where):
            self.setCommand(
                "* "+self.getData1(5)+table
            )
        elif not self.isEmptyList(data) and self.isEmptyList(where):
            self.runListData(data)
            self.setCommand(
                self.getCommand()+" "+
                self.getData1(5)+table
            )
        elif self.isEmptyList(data) and not self.isEmptyList(where):
            self.setCommand(
                self.getCommand()+"* "+
                self.getData1(5)+
                table+" "+self.getData1(6)
            )
            self.runListWhere(where)
        else:
            self.runListData(data)
            self.setCommand(
                " "+self.getData1(5)+
                table+" "+self.getData1(6)
            )
            self.runListWhere(where)
        return self.getCommand()
    
    # insert part 

    def generateInsertCommand(self,data:list,table:str):
        self.cleanCommand()
        self.setCommand(
            self.getData1(8)+
            self.getData1(9)+
            table+" "+self.getData3(0)
        )
        self.runListData(data)
        self.setCommand(
            self.getCommand()+
            self.getData3(1)+" "+
            self.getData1(7)+
            self.getData3(0)
        )
        for i in range(data.__len__()):
            self.setCommand(
                self.getCommand()+
                self.getData3(6)
            )
            if i == data.__len__():
                break
            self.setCommand(
                self.getCommand()+
                self.getData3(3)
            )
        self.setCommand(
            self.getCommand()+self.getData1(1)+self.getData3(2)
        )
        return self.getCommand()

    # anothers tools

    def runListWhere(self,thelist:list):
        i = 0
        while True:
            self.setCommand(
                self.getCommand()+
                thelist.__getitem__(i)
            )
            self.setCommand(
                self.getCommand()+
                self.getData3(5)+
                self.getData3(6)
            )
            i += 1
            if thelist.__len__().__eq__(i):
                self.setCommand(
                    self.getCommand()+
                    self.getData3(2)
                )
                break
            else:
                self.setCommand(
                    self.getCommand()+
                    self.getData3(3)+" "
                )

    def runListData(self,thelist:list):
        i = 0
        while True:
            self.setCommand(
                self.getCommand()+
                thelist.__getitem__(i)
            )
            i += 1
            if thelist.__len__().__eq__(i):
                break
            self.setCommand(self.getData3(3))

    def cleanCommand(self):
        self._command = ""
        return self._command
    
    def isEmptyList(self,lists:list):
        return lists.__len__() < 1

    def getCommand(self):
        return self._command
    
    def setCommand(self,command:str):
        self._command = command

