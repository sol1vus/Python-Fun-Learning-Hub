from game import Game


def clear_screen() -> None:
    print('\033c', end='')


def main_game() -> None:
    game = Game()
    game_over: bool = False
    while not game_over:
        game.board.draw_board()
        
        user_guess = input('Enter Your Guess (1, 10): ')

        try:
            user_guess: int = int(user_guess)
        except:
            clear_screen()
            
            print(
                "⚠️ Wrong input!\n"
                "Please guess a number between 1 and 10."
            )

            continue

        if game.make_guess(user_guess):
            if game.check_winner(user_guess):
                clear_screen()
                game.board.draw_board()

                if game.score < 5:
                    print(
                        f"Congratulations! 🎉 You Have Beat This Game 🔥!\n"
                        f"After: {game.score} tries.\n"
                    )

                else:
                    print(
                        f"Great job! you got it after: {game.score} tries.\n"
                        f"But i am sure that you can do better 👍.\n"
                    )

                game_over = True

            else:
                clear_screen()
                print("It's not in this hand buddy!, try again")

        else:
            clear_screen()
            print("Please choose a closed hand!")
    

    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again in ('yes', 'y'):
        clear_screen()
        print("Welcome again to the guessing diamond game!")
        main_game()

    else:
        clear_screen()
        print("Have a nice day -_-/")


if __name__ == '__main__':
    
    print(
        "==============================\n"
        "== WELCOME TO GUESSING GAME ==\n"
        "==============================\n"
    )

    main_game()