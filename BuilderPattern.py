class Director:
    _builder =None
    
    def setBuilder(self,builder):
        self._builder = builder
    
    def getCar(self):
        car = Car()
        
        body = self._builder.getBody()
        car.setBody(body)
        
        engine = self._builder.getEngine()
        car.setEngine(engine)
        
        i = 0
        while i< 4:
            wheel = self._builder.getWheel()
            car.attachWheel(wheel)
            i += 1
            return car
        
        
class Car():
    def __init__(self):
        self._wheels = list()     
        self._engine = None
        self._body = None
        
    def setBody(self,body):
        self._body = body
    def setEngine(self,engine):
        self._engine = engine
    def attachWheel(self,wheel):
        self._wheels.append(wheel)
    def specification(self):
      print( "body: %s") % self._body.shape
      print( "engine horsepower: %d") % self._engine.horsepower
      print( "tire size: %d\'") % self._wheels[0].size
      
class Wheel:
   size = None

class Engine:
   horsepower = None

class Body:
   shape = None
class Builder():
    def getWheel(self):pass
    def getBody(self):pass
    def getEngine(self):pass
    
class JeepBuilder(Builder):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel
    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine
    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body

def main():
   jeepBuilder = JeepBuilder() # initializing the class
   
   director = Director()
   
   # Build Jeep
   print( "Jeep")
   director.setBuilder(jeepBuilder)
   jeep = director.getCar()
   jeep.specification()
   print( "")

if __name__ == "__main__":
   main()