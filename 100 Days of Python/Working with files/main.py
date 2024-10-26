
from pathlib import Path

with open("/home/dan/Downloads/Mail+Merge+Project+Start/"
              "Mail Merge Project Start/Input/Letters/starting_letter.txt")as letter:
    letter_content = letter.read()
with open("/home/dan/Downloads/Mail+Merge+Project+Start/"
          "Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

output_dir = Path("/home/dan/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend")
output_dir.mkdir(parents=True, exist_ok=True)


for name in names:
    stripped_name = name.strip()
    personalized_letter = letter_content.replace("[name]", stripped_name)

    with open(output_dir / f"{name}.txt", "w") as output_file:
        output_file.write(personalized_letter)