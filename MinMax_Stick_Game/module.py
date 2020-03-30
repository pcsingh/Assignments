class Game:
    # this class maintains the information about the game state
    def __init__(self, total_sticks):
        self.sticks = total_sticks
    
    def get_sticks(self):
        return self.sticks

    def decrease_sticks(self, sticks):
        self.sticks -= sticks

    def is_over(self):
        return self.sticks == 1
    pass



class Player:
    # this class represents the AI player class
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "AI " + str(self.name)
    
    def check_move(self, sticks_left, turn, alpha, beta, depth):
        # print(turn, alpha, beta)
        # maximizing move
        if turn == self.name:
            # base case
            if sticks_left == 1:
                return -1
            if depth >= 20:
                if sticks_left > 5:
                    return -0.5
                elif sticks_left == 5:
                    return -1
                elif sticks_left < 5:
                    return 1   

            best_score = alpha            
            turn = 1 if turn == 2 else 2
            for i in range(1, 4):
                sticks_left -= i
                if sticks_left > 0:
                    score = self.check_move(sticks_left, turn, best_score, beta, depth+1)
                    if best_score is None or best_score < score:
                        best_score = score
                        if beta is not None and beta <= best_score:
                            return best_score
                sticks_left += i
            return best_score

        # minimizing move
        else:
            # base case
            if sticks_left == 1:
                return 1  
            if depth >= 20:
                if sticks_left > 5:
                    return 0.5
                elif sticks_left == 5:
                    return 1
                elif sticks_left < 5:
                    return -1    
        
            best_score = beta
            turn = 1 if turn == 2 else 2
            for i in range(1, 4):
                sticks_left -= i
                if sticks_left > 0:
                    score = self.check_move(sticks_left, turn, alpha, best_score, depth+1)
                    if best_score is None or best_score > score:
                        best_score = score
                        if alpha is not None and best_score <= alpha:
                            return best_score
                sticks_left += i
            return best_score  

    
    def best_move(self, sticks_left):
        best_ans = None
        alpha = None
        beta = None
        depth = 0
        turn = 1 if self.name == 2 else 2

        for i in range(1, 4):
            sticks_left -= i
            if sticks_left > 0:
                score = self.check_move(sticks_left, turn, alpha, beta, depth)
                if alpha is None or alpha < score:
                    best_ans = i
                    alpha = score
            sticks_left += i
        
        return best_ans
        pass
    pass
