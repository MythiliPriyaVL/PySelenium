# Example file for variables and Math Functions

# Declare a variable and initialize it
firstVariable= 0
print(firstVariable)

# Re-declaring the variable works
firstVariable = "Redeclaring the variable"
print(firstVariable)

# ERROR: variables of different types cannot be combined
## print("Error: Combining different variables" + 123)
print("Combining different variables using str command " + str(123))

# Global vs. local variables in functions
def firstFunction():
    # print(firstVariable) ##SyntaxError: name 'firstVariable' is used prior to global declaration
    global firstVariable
    firstVariable = 200
    print(firstVariable)

firstFunction()
print(firstVariable)
del firstVariable #delete the definition of firstVariable
#print(firstVariable) ## NameError: name 'firstVariable' is not defined

# Math functions

varX = 100
varY = 200
varZ = 0

    # a.Addition
varZ = varX+varY
print(varZ)
print(type(varZ))
    # b.Subtraction
varZ = varX-varY
print(varZ)
print(type(varZ))
    # c.Multiplication
varZ = varX*varY
print(varZ)
print(type(varZ))
    # d.Division
varZ = varX/varY
print(varZ)
print(type(varZ))
    # e.Remainder
varZ = varY%varX
print(varZ)
print(type(varZ))
    # f.Boolean
varZ = 0
print(bool(varZ))
print(type(varZ))
    # g.Power
varZ =varX**varY
print(varZ)
print(type(varZ))
    #h.Varied
print(0.1 + 0.2 - 0.3) ## 5.551115123125783e-17 --TBD
