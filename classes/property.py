#%% Original
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

#%% Switch to Getters/Setters
# problem, user can no longer access temperature directly
class Celcius_GS:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)
    
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
    def get_temperature(self):
        return self._temperature
    
    def set_temperature(self,value):
        if value<-273:
            raise ValueError("Temp below -273 is not allowed.")
        self._temperature=value

#%% Switch to Getters/Setters + Add Property
# problem, user can no longer access temperature directly
class Celcius_GS_P:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)
    
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
    def get_temperature(self):
        return self._temperature
    
    def set_temperature(self,value):
        if value<-273:
            raise ValueError("Temp below -273 is not allowed.")
        self._temperature=value
    #property(fget=None, fset=None, fdel=None, doc=None)
    temperature=property(get_temperature,set_temperature) 

#%% Eliminate Getter and Setter clutter
class Celcius_compact:
    def __init__(self,temperature=0):
        self._temperature=temperature
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
    @property
    def temperature(self):
        print('Getting Value')
        return self._temperature
    
    @temperature.setter
    def temperature(self,value):
        if value<-273:
            raise ValueError("Temp below -273 is not allowed.")
        print('Setting Value')
        self._temperature=value

#%%
def main():
    mytemp=Celsius(25)
    print('My temp in deg F: ',mytemp.to_fahrenheit())
    print('My temp in deg C: ',mytemp.temperature)

    mytemp_GS=Celcius_GS(2)
    print('Initial GS temp:',mytemp_GS.get_temperature())
    #mytemp_GS.set_temperature(-300)

    mytemp_GS_P=Celcius_GS_P(44)
    print('Initial GS_P temp:',mytemp_GS_P.temperature)


if __name__ == "__main__":
    main()

#%%
mtc=Celcius_compact(22)
mtc.temperature
mtc.temperature=24
mtc.temperature
#%%
