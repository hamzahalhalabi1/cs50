import emoji

x = input("Input: ")
output = emoji.emojize(x, language="alias")
print("Output:", output)