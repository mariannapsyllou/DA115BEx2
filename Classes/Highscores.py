class Highscores():

    def dict_results(self):
        result_dict = {}
        with open("Results.txt", 'r') as filename:
            for line in filename:
                line = line.strip()
                key, value = line.split(",")
                result_dict[key] = value
        return result_dict

    def scores(self, player):
        score_dict = self.dict_results()
        if player in score_dict:
            print(f"{player} you have won the game {score_dict.get(player)} times!!")
        else:
            print(f"You have not any registered scores yet")

    def view_instructions(self):
        with open("Instructions.txt", "r") as filename:
            for line in filename:
                print(line)


   