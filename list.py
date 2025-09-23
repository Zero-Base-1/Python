# Write code below 💖

class City:
  def __init__(self,name,country,population,landmarks,mayor):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
    self.mayor = mayor

gero = City('Gero','Philippines','120,000,000',['Bonifacio Monument','SM Caloocan'],'Mayor Along Malapitan')
print(vars(gero))