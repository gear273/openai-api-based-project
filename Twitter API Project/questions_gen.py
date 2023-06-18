from reqandresponse import generate_chat_response


def extract_categories(filename: str) -> list:
    """Given a filename returns a list of strings, as category names"""
    with open(filename, "r") as c_file:
        categories_list = (c_file.read()).split("\n")
        # Now I have a list of categories as strings
        return categories_list

    # give me x questions about y.


# print(extract_categories("categories.txt"))


def formatter(qstr: str) -> list:
    """Takes a list of questions as a string, and reformats it into a list of strings
    Main purpose is to get rid of numbers

    formatter(qlist = [
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
    ])

    >>>
    ['When did the attack on Pearl Harbor take place?',
    'Which country was responsible for the attack?',
    'What was the main goal of the attack?',
    'How many ships were damaged or destroyed during the attack?',
    'What was the casualty count for the United States during the attack?',
    'How effective was the response of the United States government to the attack?',
    'Do you believe that the United States could have prevented the attack if they had been more vigilant?',
    'Was the attack on Pearl Harbor a justified response to the actions of the United States leading up to the attack?', "What was the impact of the attack on the United States' entry into World War II?",
    'How has the attack on Pearl Harbor shaped the relationship between the United States and Japan in the years since the attack?']
    ['When did the attack on Pearl Harbor take place?',
    'Which country was responsible for the attack?',
    'What was the main goal of the attack?',
    'How many ships were damaged or destroyed during the attack?',
    'What was the casualty count for the United States during the attack?',
    'How effective was the response of the United States government to the attack?', 'Do you believe that the United States could have prevented the attack if they had been more vigilant?',
    'Was the attack on Pearl Harbor a justified response to the actions of the United States leading up to the attack?',
    "What was the impact of the attack on the United States' entry into World War II?",
    'How has the attack on Pearl Harbor shaped the relationship between the United States and Japan in the years since the attack?']
    """

    if qstr == None:
        return qlist

    qlist = qstr.split("\n")

    str_list = []
    for q in qlist:
        if q != "":
            newq = q.split(".", 1)
            if len(newq) == 2:
                str_list.append(newq[1].strip())

    return str_list


def add_questions(filename):
    """Takes a filename as input, and appends questions to the end of the file
    messages = [
    {"role": "user", "content": "What is HTML?"}
    ]
    """

    # Take note of an issue here, program runs in On^2

    categories_list = extract_categories("categories.txt")

    for category in categories_list:
        messages = [
            {"role": "user", "content": "Give me 10 questions related to " + category}
        ]

        qlist = generate_chat_response(messages)
        print(qlist)

        if qlist == None:
            print(category)
            return

        str_list = formatter(qlist)
        for question in str_list:
            with open(filename, "a") as fobj:
                fobj.write(question + "\n")


def main():
    add_questions("my_questions.txt")

    # categories_list = extract_categories("categories.txt")
    # print(categories_list)


if __name__ == "__main__":
    main()
