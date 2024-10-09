def temperature_converter(temperature, unit):
    if unit == "C":
        
        fahrenheit = (temperature * 9/5) + 32
        return f"{round(fahrenheit)} F"
    elif unit == "F":
       
        celsius = (temperature - 32) * 5/9
        return f"{round(celsius)} C"
    else:
        return "Invalid unit"

# Example usage:
print(temperature_converter(100, "C"))  
print(temperature_converter(50, "C"))   
print(temperature_converter(32, "F"))   
print(temperature_converter(68, "F"))   

def reverse(string):
    
    if len(string) == 0:
        return string
    
    return reverse(string[1:]) + string[0]

# Example usage:
print(reverse("hello"))  
print(reverse("world"))  
print(reverse("a"))      
print(reverse(""))       

def fib(N):
   
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    return fib(N - 1) + fib(N - 2)

# Example usage:
print(fib(0))  
print(fib(1))  
print(fib(2))  
print(fib(8))  