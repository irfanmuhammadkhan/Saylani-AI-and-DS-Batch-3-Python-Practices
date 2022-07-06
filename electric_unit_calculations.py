unit = int(input("Enter Units: "))
if unit > 0 and unit <= 100:            #0-100 units Rs. 10
    rate = unit * 10 
    print("Your billing amount for units", unit, "is Rs.", rate)
    
elif unit > 100 and unit <= 200:        #101-200 unit Rs. 15
    rate = ((100 * 10) + ((unit - 100) * 15))
    print("Your billing amount for units", unit, "is Rs.", rate)
    
elif unit > 200 and unit <= 300:        #201-300 unit Rs. 20
    rate = ((100 * 10) + (100 * 15) + ((unit - 200) * 20))
    print("Your billing amount for units", unit, "is Rs.", rate)
    
elif unit > 300 and unit <= 500:        #301-500 unit Rs. 25
    rate = ((100 * 10) + (100 * 15) + (100 * 20) + ((unit - 300) * 25))
    print("Your billing amount for units", unit, "is Rs.", rate)
    
elif unit > 500 and unit <= 1000:       #501-1000 unit Rs. 35
    rate = ((100 * 10) + (100 * 15) + (100 * 20) + (200 * 25) + ((unit - 500) * 35))
    print("Your billing amount for units", unit, "is Rs.", rate)
    
elif unit > 1000 and unit <= 10000:     #1001-10000 unit Rs. 50
    rate = ((100 * 10) + (100 * 15) + (100 * 20) + (200 * 25) + (500 * 35) + ((unit - 1000) * 50))
    print("Your billing amount for units", unit, "is Rs.", rate)

elif unit > 10000 and unit <= 100000:   #10001-100000 unit Rs. 70
    rate = ((100 * 10) + (100 * 15) + (100 * 20) + (200 * 25) + (500 * 35) + (9000 * 50) + ((unit - 10000) * 70))
    print("Your billing amount for units", unit, "is Rs.", rate)

else:                                   #100001-up unit Rs. 100
    rate = ((100 * 10) + (100 * 15) + (100 * 20) + (200 * 25) + (500 * 35) + (9000 * 50) + (90000 * 70) + ((unit - 100000) * 100))
    print("Your billing amount for units", unit, "is Rs.", rate)
    