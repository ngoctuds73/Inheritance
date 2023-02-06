from zoo_ex.project.animal import Animal
from zoo_ex.project.mammal import Mammal
from zoo_ex.project.reptile import Reptile
from zoo_ex.project.bear import Bear
from zoo_ex.project.gorilla import Gorilla
from zoo_ex.project.lizard import Lizard
from zoo_ex.project.snake import Snake

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
print(mammal._Animal__name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
print(lizard._Animal__name)