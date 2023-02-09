class Highscores:

    def list_results(cls):
        result_list = []
        with open("Results.txt", 'r') as filename:
            for line in filename:
                line = line.strip()
                result_list.append(line)
        return result_list

    def update_statistics(cls, player, new_win, new_times_played):
        update_list = cls.list_results()
        for i in range(len(update_list)):
            if update_list[i][0] == player.name:
                old_highscore = int(update_list[i][1])
                update_list[i][1] = old_highscore + new_win
                old_times_played = int(update_list[i][2])
                update_list[i][2] = old_times_played + new_times_played
                return update_list
            else:
                update_list.append(f"{player.name},{new_win},{new_times_played}")
                return update_list
            
    def view_highscore(cls, name):
        with open("Results.txt", 'r') as filename:
            lines = filename.readlines()
            for line in lines:
                line = line.strip()
                parts = line.split(',')
                if parts[0] == name:
                    highscore = parts[1]
                    times_played = parts[2]
                else:
                    highscore, times_played = 0, 0
        return name, highscore, times_played

    def update_results(cls, update_list):
        with open("Results.txt", 'w') as filename:
            for item in update_list:
                filename.write(f"{item[0]},{item[1]},{item[2]}\n")
