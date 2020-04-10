class Commands(object):
    data1: dict
    data2: dict
    data3: dict

    def __init__(self):
        self.data1 = {
            0:"CREATE ",
            1:"SELECT ",
            3:"UPDATE ",
            4:"DELETE ",
            5:"FROM ",
            6:"WHERE ",
            7:"VALUES " 
        }
        self.data2 = {
            0:"AND ",
            1:"OR ",
            2:"SET ",
            3:"INNER ",
            4:"LEFT ",
            5:"RIGHT ",
            6:"JOIN ",
            7:"AS "
        }
        self.data3 = {
            0:"(",
            1:")",
            2:";",
            3:",",
            4:".",
            5:"=",
            6:"?"
        }

