from view.view import View
from model.model import Model


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.startApp()
        
    def getData(self, file_path):
        category, probability = self.model.returnCategoryAndProbability(file_path)
        
        self.view.setData(category, probability)
    
    def startApp(self):
        self.view.show()