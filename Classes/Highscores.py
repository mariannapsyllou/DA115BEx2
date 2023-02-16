class Highscores:

    def dict_results(self):
        result_dict = {}
        with open("Results.txt", 'r') as filename:
            for line in filename:
                line = line.strip()
                key, value = line.split(",")
                result_dict[key] = int(value)
        return result_dict

    def scores(self, player):
        score_dict = self.dict_results()
        if player in score_dict:
            print(f"{player} you have won the game\
                {score_dict.get(player)} times!!")
        else:
            print("This user has not been registered")

    def view_instructions(self):
        with open("Instructions.txt", "r") as filename:
            for line in filename:
                print(line)

    def update(self, player):
        update_dict = self.dict_results()
        if player in update_dict:
            update_dict[player] += 1
        else:
            update_dict[player] = 1
        with open("Results.txt", "w") as filename:
            for key, value in update_dict.items():
                filename.write(f"{key},{str(value)}\n")
