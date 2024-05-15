player1_name = input("Enter Your Name:")
player2_name = input("Enter Your friend Name:")

name1 = player1_name.lower()
name2 = player2_name.lower()

name_to_count = ""

for letter in name1:
    if letter in name2:
        name2 = name2.replace(letter, '', 1)
        name1 = name1.replace(letter, '', 1) 

total_length = len(name1) + len(name2)

flames = ['Friends', 'Love', 'Attraction', 'Marriage', 'Enemies', 'Siblings']

count = 1
index = 0

while True:
    if index == len(flames):
        index = 0

    if count % total_length == 0:
        flames.pop(index)
        index -= 1

    count += 1
    index += 1

    if len(flames) == 1:
        break

print(f"The relationship between {player1_name} and {player2_name} is '{flames[0].upper()}'")
