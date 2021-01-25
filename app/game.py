class Game:

    def rock_paper_scissors(self, player1, player2):
        result = {
                "player1_name": player1.name,
                "player1_choice": player1.choice,
                "player2_name": player2.name,
                "player2_choice": player2.choice
                }
        if player1.choice == "rock" and player2.choice == "paper":
            result["message"] = f"{player1.name} wins by playing rock"            
            return result
        elif player1.choice == "paper" and player2.choice == "scissors":
            result["message"] = f"{player2.name} wins by playing scissors"
            return result
        elif player1.choice == "scissors" and player2.choice == "rock":
            result["message"] =  f"{player2.name} wins by playing rock"
            return result
        else:
            return "None"