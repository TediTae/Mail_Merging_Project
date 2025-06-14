with open("./Input/Names/invited_names.txt") as names_file:
    list_of_names = names_file.readlines()
    # print(list_of_names)


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in list_of_names:
        stripped_name = name.strip()
        new_letter = letter_content.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
