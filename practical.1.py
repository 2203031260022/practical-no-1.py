fh=open("output1.txt",'w')
# F = (9/5)C + 32  celsius to fahrenheit
c=float(input("enter celsius value : "))
f=(c*(9/5)+32)
fh.write("fahrenheit is : " +str(f))
    
#, °C = (°F - 32) × 5/9  fahrenheit to celsius
f=int(input("enter fahrenheit value : "))
c=((f-32)*5/9)
fh.write("celsius convertion "+str(c))
