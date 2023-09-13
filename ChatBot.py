import re
import random

class RuleBot:
    negative_responses = ("no","nope","nah","naw","not a chance","sorry")
    exit_commands = ("quit","pause","exit","goodbye","bye","later")
    random_questions = (
        "Why are you here ?\n",
        "Are there many humans like you ?\n",
        "What do you consume for sustenance ?\n",
        "Is there intelligent life in this planet ?\n",
        "Does Earth have a leader ?",
        "What planets have you visited ?",
        "What technology do you have on this planet ?\n",
      )

    def __init__(self):
        self.alienbot = {'Describe_planet_intent': r' .*\s*your planet.*',
                         'Answer_why_intent': r'why\sare.*',
                         'About_intellipat': r'.*\s*intellipaat'
                        }

    def greet(self):
        self.name = input("What is your name ?\n")
        will_help = input(
            f"hi {self.name}, I am alien-bot. Will you help me learn about your planet ?\n")
        if will_help in self.negative_responses:
            print("Ok, Have a nice Earth day !")
            return
        self.chat()

    def make_exit(self, reply):
        for commands in self.exit_commands:
            if reply==commands:
                print("Okay, Have a nice Earth day !")
                return True

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for key, value in self.alienbot.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'Describe_planet_intent':
                return self.Describe_planet_intent()
            elif found_match and intent == 'Answer_why_intent':
                return self.Answer_why_intent()
            elif found_match and intent == 'About_intellipat':
                return self.About_intellipat()
        if not found_match:
            return self.no_match_intent()

    def Describe_planet_inten(self):
        responses = ("My palnet is an utopia of diverse organisms and species.\n",
                     "I am from Fantasia, in the Vineyard Galaxies.\n")
        return random.choice(responses)

    def Answer_why_intent(self):
        responses = ("I am harmless.\n","I came to research your planet.\n",
                     "The food has many varieties and is very good.\n")
        return random.choice(responses)

    def About_intellipat(self):
        responses = ("Intellipaat is a company.\n","It researches on space and alien matter.\n",
                     "It is where you will get all the secret information.\n")
        return random.choice(responses)

    def no_match_intent(self):
        responses = ("Tell me more.\n","Can you elaborate on that.\n",
                     " Tell me more about it please!\n","Why do you feel that ?\n","How can you say that?\n",
                     "How do you think your reply will affect me ?\n","Why ?\n","Please tell me more details.\n")
        return random.choice(responses)

AlienBot = RuleBot()
AlienBot.greet()






    

    
