# statements control the flow of logical
#  control flow uses colon and indentation
# if a_condition:
#   command to exe
# else:
#   do another command
# check if multi condition before else, use elif
# if a_condition:
#   command to exe
# elif:             can have as many elifs you want
#   do a diff command
# else:
#   do this command

# simple if statement example
if 1 == 1:
    print("This is true")
bored = False
# if/else statement example
if bored:
    print("Learn more python or go outside.")
else:
    print("Im not bored")

# elif example
activity = "None"

if activity == "None":
    print("Get up and move.")
elif activity == "Somewhat":
    print("Try to be a little more active.")
else:
    print("What is your level of activity.")
