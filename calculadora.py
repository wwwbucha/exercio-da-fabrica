class calculadora():
    
    
    def calcular(Self,op):
        if op == "adição":
            result = Self.__adicionar()
            return result
        
        
        elif op == "subtrair":
            result = Self.__subtrair()
            return result
        
        
    def __adicionar(Self):
        
        a = int(input("PRIMEIRO: "))
        
        b = int(input("SEGUNDO:" ))
        
        c=a+b
        
        return c
    
    def __subtrair(Self):
        
        a = int(input("PRIMEIRO: "))
        
        b = int(input("SEGUNDO:" ))
        
        c=a-b
        
        return c
    
    