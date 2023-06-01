# old method
sentence="hello my name is {1} i am from {0}"
name="chirayu"
country="Bhratha"
print(sentence.format(country,name))
# new method
print(f"hello my name is {name} i am from {country}")
# to not display f string we use this method below
print(f"hello my name is {{name}} i am from {{country}}")