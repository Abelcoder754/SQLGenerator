class Commands(object):
    """This class has the possible commands that can be used to generate a sql command"""
    _data1: dict
    _data2: dict
    _data3: dict

    def __init__(self):
        self._data1 = {
            0:"TABLE ",
            1:"SELECT ",
            2:"CREATE ",
            3:"UPDATE ",
            4:"DELETE ",
            5:"FROM ",
            6:"WHERE ",
            7:"VALUES ",
            8:"INSERT ",
            9:"INTO "
        }
        self._data2 = {
            0:"AND ",
            1:"OR ",
            2:"SET ",
            3:"INNER ",
            4:"LEFT ",
            5:"RIGHT ",
            6:"JOIN ",
            7:"AS "
        }
        self._data3 = {
            0:"(",
            1:")",
            2:";",
            3:",",
            4:".",
            5:"=",
            6:"?"
        }
    
    def getData1(self,idx:int):
        if idx < 0 or idx >= self._data1.__len__():
            return None
        return self._data1.__getitem__(idx)

    def getData2(self,idx:int):
        if idx < 0 or idx >= self._data2.__len__():
            return None
        return self._data2.__getitem__(idx)
    
    def getData3(self,idx:int):
        if idx < 0 or idx >= self._data3.__len__():
            return None
        return self._data3.__getitem__(idx)

