from questions_gen import formatter

# # returned list needs to be in this format
# messages = [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "What is HTML?"},
# ]


# def gen_questions(filename: str) -> list:
#     #
#     questions = []

#     with open(filename, "r") as q_file:
#         # creating an iterable list of strings, with each element being a message
#         text_list: list = (q_file.read()).split("\n")

#         for question in text_list:
#             msg_dict = {"role": "user", "content": question}
#             questions.append(msg_dict)

#     return questions


# gen_questions("my_questions.txt")

qlist = [
    "5 factual questions and 5 opinion-based questions",
    "",
    "Factual questions:",
    "1. When did the attack on Pearl Harbor take place?",
    "2. Which country was responsible for the attack?",
    "3. What was the main goal of the attack?",
    "4. How many ships were damaged or destroyed during the attack?",
    "5. What was the casualty count for the United States during the attack?",
    "",
    "Opinion-based questions:",
    "1. How effective was the response of the United States government to the attack?",
    "2. Do you believe that the United States could have prevented the attack if they had been more vigilant?",
    "3. Was the attack on Pearl Harbor a justified response to the actions of the United States leading up to the attack?",
    "4. What was the impact of the attack on the United States' entry into World War II?",
    "5. How has the attack on Pearl Harbor shaped the relationship between the United States and Japan in the years since the attack?",
]

list2 = []
for q in qlist:
    if q != "":
        newq = q.split(".", 1)
        if len(newq) == 2:
            list2.append(newq[1].strip())
print(list2)

print(formatter(qlist))
