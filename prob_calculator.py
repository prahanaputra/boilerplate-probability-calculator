import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []

        for i, j  in kwargs.items():
            for k in range(j):
                self.contents.append(i)
        
        # print(self.contents)
        
    def draw(self, num_balls_drawn):
        clone = copy.deepcopy(self.contents)
        drawn_balls = []
        c = 0

        if num_balls_drawn > len(self.contents):
            return self.contents

        else:
            while c < num_balls_drawn:
                draw = random.randint(0, len(self.contents)-1)
                drawn_balls.append(self.contents[draw])
                self.contents.pop(draw)
                c += 1
        # print(drawn_balls)
        return drawn_balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
  
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        
        for m in balls_drawn:
            if m in expected_copy:
                expected_copy[m]-=1
    
        if all(value <= 0 for value in expected_copy.values()):
            count += 1

    probability = count / num_experiments
    
    return probability