"""
Choose a choice with this python class.

IL
"""

import numpy as np

class Choice():
    def __init__(self, prompt="", options=[] , choices=[]):
        self.prompt = prompt
        self.options = options
        self.choices = choices
        
        if options != []:
            self.max = 0
            for option in options: 
                
                print(f"Looking at option: {option}")
                if option[1] == None:
                    self.max += 1
                else:
                    self.max += option[1]
        
    def __str__(self):
        return self.choose()
        
        def sortByTickets(canidate):
            # print(f"Candidate type is {type(canidate)}")
            if type(canidate) is tuple:
                return 1
            else:
                return canidate[1]
    
        # print(f"Options Are {type(self.options)}")

        if self.options != []:
            pass
        
            
            # for option in self.options:
                # choice += " " + option[np.random.randint(0, len(option))]
            # for option in self.options.sort(key=sortByTickets):
                # pool = 
                # print(f"Pool is: {option}")
        else:
            return "" 
        
        choice = self.prompt
        # for option in self.options:
        #     choice += " " + option[np.random.randint(0, len(option))]
            
        return choice
    
    def choose(self):
        
        option = ""
        
        if self.choices != []:
            return self.choices[np.random.randint(0, len(self.choices))]
        
        elif self.options != []:
            for options in self.options:
                option += self.weighOptions(options)
            
        if self.prompt != "":
            return self.prompt + option
        else:
            return "Unknown"            
        
        # if self.choices is None:
        #     return ""
        # else:
        #     return self.choices[np.random.randint(0, len(self.choices))]
        
    def weighOptions(self, options):
        
        # def sortByTickets(canidate):
        #     if type(canidate) is tuple:
        #         print(f"Found a weight on {canidate}")
        #         return canidate[1]
        #     else:
        #         print(f"Found NO weight on {canidate}")
        #         return 1
        
        cur = 0
        choice = np.random.randint(0, self.max)
        for option in options:
            if choice < option[1]:
                return option
            else:
                cur += option[1]
        else:
            print("Finished for for loop without returning")
            
        # print(f"\nLooking at options {options}\n\n")
        
        # options.sort(key=sortByTickets)
        
        # print(f"Pool is {self.options}")
            
                
            
        return ""


method = Choice(choices=[
    "Graphite",
    "Procreate"
])

dimensions = Choice(choices=[
    2,
    3
])

guides = Choice(choices=[
    "2D",
    "Isometric",
    "Perspective",
    "Symmeterical"
])

genre = Choice(choices=[
    "Realism",
    "Horror",
    "Cartoon",
    "Manga"
])

subjects = Choice(choices=[
    Choice(prompt="Human Form", 
           options=[("Face", "Chest", "Arms", "Hands", "Legs", "Feet")]),
    Choice(prompt="Animal", 
           options=[["Bipedal", "Quadrepedal", "Cat", "Dog", "Fox"]]),
    Choice(prompt="Plant", 
           options=[["Tree", "Flower", "Fungi", "Dog", "Fox"]]),
    Choice(prompt="a landscape", 
           options=[[("at night", 3), ("during the day", 1)], 
            [("of a mountain", 1), ("of the sea", 1), ("of an ocean", 1), ("of a forest", 1), ("of the desert", 1), ("of the sky", 1)]]),
    Choice(prompt="The Most Interesting Item Within Sight"),
    "Leonidas",
    "R&TA", #AKA Red & The Asskickers
    "The First Loved One To Come To Mind",
    "IJ"
])

time = Choice(choices=[
    1,
    5,
    10,
    15,
    30,
    60
])

choose = Choice(choices=[
    f"For {time.choose()} minute(s) while using {method.choose()}, draw {subjects.choose()} in {dimensions.choose()} dimensions using a {guides.choose()} guide.",
    f"Draw {subjects.choose()}",
])
print(choose.choose())


#Tests
# no_choices = Choice(choices=[])
# choices = Choice(choices=["This choice", "Other choice"])
# choices_with_choices = Choice(choices=["Some choice", "Another choice"])


# no_weights_1 =    Choice(prompt="No Weights",  options=[["foo", "bar"]])
# no_weights_2 =    Choice(prompt="No Weights",  options=[["fool","bark"], ["fam", "bam"]])

# weighted =      Choice(prompt="With Weights",   options=[[("foo", 3), ("bar",1)], [("luck", 1)]])
# mixed =         Choice(prompt="Mixed",          options=[[("foo", 3), "bar", ("dimple", 2)]])

# print(no_weights_2)
# print(weighted)
# print(mixed.choose())