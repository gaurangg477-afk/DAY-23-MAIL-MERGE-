
# STEP 1: Read all names
with open("Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

# STEP 2: Read the letter template
with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_template = letter_file.read()

# STEP 3: Loop through each name
for name in names:
    # Remove newline character
    clean_name = name.strip()

    # Replace placeholder with actual name
    personalized_letter = letter_template.replace("[name]", clean_name)

    # STEP 4: Create new file for each person
    output_path = f"Output/ReadyToSend/letter_for_{clean_name}.txt"

    with open(output_path, mode="w") as output_file:
        output_file.write(personalized_letter)
print("Letters have been generated and saved in the Output/ReadyToSend/ directory.")