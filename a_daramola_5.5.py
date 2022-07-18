#Akinola Daramola Jr
#Programming Exercise: 5.5
#Due Date: 07/17/2022


"""
Property Tax
A county collects property taxes on the assessment value of property,
which is 60 percent of the property’s actual value.
For example, if an acre of land is valued at $10,000,
its assessment value is $6,000. The property tax is then 72¢ for each $100 of the assessment value.
The tax for the acre assessed at $6,000 will be $43.20.
Write a program that asks for the actual value of a piece of property and displays the assessment value and property tax.
"""


#Defining main function
def main():
    #Calling function
    calculate()

#Defining calculate function
def calculate():
        #Declaring value of variable dynamically
        property_value = float(input("What is the property value? "))

        #Calculating assessmnt amount
        assessment = property_value * .60

        #calculating property tax amount
        property_tax = (assessment/100) * 0.72

        #Displaying results of calculations
        print(f"Property value: ${property_value:,.2f}")
        print(f"Assessment value: ${assessment:,.2f}")    
        print(f"Property tax: ${property_tax:,.2f}")

#Calling main function
main()
