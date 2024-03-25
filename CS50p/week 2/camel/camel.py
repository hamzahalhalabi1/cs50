name = input('camelCase: check50 cs50/problems/2022/python/camel')

for c in name:
    if c.isupper():
        character = c
        name = name.replace(c,f'_{character.lower()}' )

print(name)