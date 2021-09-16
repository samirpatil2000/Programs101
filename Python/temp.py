x=("LOUNGE DIESEL",                          
"1.2 ELX PS DIESEL",
"1.6 DIESEL",
"VAN DIESEL",
"ABARTH PETROL",
"1.4 EVO T JET ABARTH PETROL",
"URBAN CROSS 1.4 T- JET EMOTION PETROL",
"URBAN CROSS 1.3 T- MULTIJET EMOTION DIESEL",
"1.2 EL PETROL                             ",)

FUEL_TYPE={
    "DIESEL":0,
    "PETROL":1,
    "CNG":2,
    "BATTERY":3,
    "EXTERNAL_CNG" :4,
    "EXTERNAL_LPG":5,
    "ELECTRICITY":6,
    "HYDROGEN":7,
    "LPG":8,
}

def isFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False
      
list_=[]
for i in x:
    name_=i.split()
    x_=[]
    for v in name_:
        if isFloat(v):
          x_.append(float(v))
          break
    x_.append(FUEL_TYPE.get(name_[-1].upper(),""))

    print(x_)
    

              
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# | ABARTH 595 COMPETIZIONE 5 STR PETROL       |
# | COMPETIZIONE PETROL                        |
# | SPORT DIESEL                               |
# | ACTIVE MULTIJET 1.3 DIESEL                 |
# | DYNAMIC MULTIJET 1.3 DIESEL                |
# | EMOTION MULTIJET 1.3 DIESEL                |
# | ACTIVE 1.4 PETROL                          |
# | DYNAMIC 1.4 PETROL                         |
# | ACTIVE 1.2 PETROL                          |
# | ACTIVE 1.2 PETROL                          |
# | DYNAMIC 1.2 PETROL                         |
# | EMOTION 1.2 PETROL                         |
# | ACTIVE 1.3 DIESEL                          |
# | DYNAMIC 1.3 DIESEL                         |
# | EMOTION 1.3 DIESEL                         |
# | EMOTION PACK 1.3 DIESEL                    |
# | MULTIJET 1.3 90 HP DIESEL                  |
# | DYNAMIC 1.4 PETROL                         |
# | EMOTION 1.4 DIESEL                         |
# | EMOTION 1.4 PETROL                         |
# | EMOTION PACK 1.4 PETROL                    |
# | 1.3 L MULTIJET PLUS DIESEL                 |
# | 1.3 L MULTIJET DIESEL                      |
# | 1.4 L P CLASSIC PETROL                     |
# | ACTIVE 1.3 MJD DIESEL                      |
# | ACTIVE 1.4 PETROL                          |
# | DYNAMIC 1.3 MJD DIESEL                     |
# | DYNAMIC 1.4 PETROL                         |
# | DYNAMIC PK 1.3 MJD DIESEL                  |
# | DYNAMIC PK 1.4 PETROL                      |
# | ELEGANTE DYNAMIC 1.3 DIESEL                |
# | EMOTION 1.3 DIESEL                         |
# | EMOTION 1.3 MJD DIESEL                     |
# | EMOTION 1.4 PETROL                         |
# | EMOTION PK 1.3 MJD DIESEL                  |
# | EMOTION PK 1.4 PETROL                      |
# | EMOTION T-JET 1.4 PETROL                   |
# | T-JET PETROL                               |
# | T-JET PLUS PETROL                          
# " 1.6 S10 PETROL                            "
# | ACTIVE MULTIJET 1.3 90 HP DIESEL
         