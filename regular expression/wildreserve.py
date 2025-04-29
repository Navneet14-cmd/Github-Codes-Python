location="Nainital"
distance=35
class InvalidLocation(Exception): 
    pass
class ContactDetails(Exception):
    pass
class SafeAddress(Exception):
    pass
class InvalidInput(Exception):
    pass
class ChannelSociety(Exception):
    pass
class EducateSociety(Exception):
    pass
class RelocateSuggest(Exception):
    pass

class survey:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        
    def check(self,name,address):
        global location
        if (address==location):
            pass
        else: raise InvalidLocation("Your location is not near Survey Guidelines")
        
    def locationcheck(self,dist,input):
        global distance
        if (dist<distance):
            if (input=="Y"):
                raise ContactDetails("Please contact wxyz@email.com for further process. ")
            elif (input=="N"):
                pass
            else:
                raise InvalidInput("Kindly enter valid input. ")
            
    def tigercheck(self,input):
        if (input=="Y"):
            raise ChannelSociety("Kindly channel your society and contact authority .")
        elif (input=="N"):
            pass
        else:
            raise InvalidInput
        
    def VillageCheck(self,input):
        if (input=="Y"):
            raise EducateSociety("Ask the authorities to conduct acivities to educate village. ")
        elif (input=="N"):
            pass
        else:
            raise InvalidInput
    def CurrentLoc(self,input):
        if (input=="Y"):
            pop=int(input("Enter the population of your society: "))
            if (pop<=4000):
                raise RelocateSuggest(" Kindly ask the authority to relocate your society. ")
            elif (pop>4000):
                print("Contact Authority ")
                exit() 
        elif (input=="N"):
            exit()
        else:
            raise InvalidInput
try:
    print("WELCOME TO UPES SURVEY: ")
    name=input("Enter your name: ")
    address=input("Enter your address: ")
    user=survey(name,address)
    user.check(name,address)
    
    kpop=int(input("Enter the your address distance from Wild Reserve: \n"))
    intput=input("Is your location near Wild Reserve, Enter only 'Y' or 'N': \n")
    user.locationcheck(kpop,intput)
    
    intput=input("Does Tiger come near your society?,Enter only 'Y' or 'N': \n")
    user.tigercheck(intput)
    
    intput=input("Does your society come under village?,Enter only 'Y' or 'N': \n")
    user.VillageCheck(intput)
    
    intput=input("Is your society too close to Wild Reserve?,Enter only 'Y' or 'N': \n")
    user.CurrentLoc
    
except (InvalidLocation,ContactDetails,SafeAddress,InvalidInput,ChannelSociety,EducateSociety,RelocateSuggest) as e:
        print(f"{e}")
finally:
    print("Thank you for using our survey. ")
    
    
    
        
    
            
            
            
            
            
            
            
            
            
            
        
    
        