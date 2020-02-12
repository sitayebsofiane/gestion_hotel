from model.model import Model
from view import View

model = Model("hotel","postgres","as122014","localhost","5432")
view = View(model)
print(view.display())