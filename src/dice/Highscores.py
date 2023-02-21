class Highscores:
    """
    Class Highscores holds methods to view results
    update the scores of users and view game
    instructions
    """
    def dict_results(self):
        """
        Opens the file where previous results are stored
        split them and put them in a dictionary
        where key is the name and value the previous score
        """
        result_dict = {}
        with open("Results.txt", "r", encoding="utf8") as filename:
            for line in filename:
                line = line.strip()
                key, value = line.split(",")
                result_dict[key] = int(value)
        return result_dict

    def scores(self, player):
        """
        Prints the name requested and how many times they won
        If its their first time it prints a message
        """
        score_dict = self.dict_results()
        if player in score_dict:
            # prints weird
            print(
                f"{player} you have won the game \
                {score_dict.get(player)} times!!"
                )
        else:
            print("This user has not been registered")

    def view_instructions(self):
        """
        Opens a txt file with instructions of the game
        and prints them for the user if requested
        """
        with open("Instructions.txt", "r", encoding="utf8") as filename:
            for line in filename:
                print(line)

    def update(self, player):
        """
        Updates the dictionary with the new wins
        of the user.
        """
        update_dict = self.dict_results()
        if player in update_dict:
            update_dict[player] += 1
        else:
            update_dict[player] = 1
        with open("Results.txt", "w", encoding="utf8") as filename:
            for key, value in update_dict.items():
                filename.write(f"{key},{str(value)}\n")
