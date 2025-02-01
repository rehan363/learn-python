from pathlib import Path

path = Path('class11(file_handling)/pi_digits.txt')
contents = path.read_text().rstrip()                   #methood chaining both are methoods of stripe
#contents = contents.rstrip() # remove extra space below the text
print(contents)

# lines = contents.splitlines()
# for line in lines:
#  print(line)
 
# path.write_text("i love pograming")  # by this methood we can add any thing to our txt 


contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path.write_text(contents)