import random
from hangman_util import *

class HangmanGame:
    def __init__(self):
        self.word = random.choice(words)
        self.user_ans = ['_' for _ in range(len(self.word))]
        self.max_attempts = len(hangman_pics)
        self.num_of_attempts = self.max_attempts
    
    def display(self, result):
        print('\n')
        if result == 1:
            print('맞았습니다!')
        elif result == 0:
            print('틀렸습니다!')
        else:
            print('입력값 오류: 알파벳 한 글자만 입력하세요.')
        print(' '.join(self.user_ans))
        print('+++++++++++++++++++++++++++\n')

    def correct(self, letter):
        for i, l in enumerate(self.word):
            if letter == l:
                self.user_ans[i] = letter
        self.display(1)

    def incorrect(self):
        self.num_of_attempts -= 1
        self.display(0)

    def error(self, letter):
        if len(letter) > 1:
            return 1
        if not (('a' <= letter <= 'z') or ('A' <= letter <= 'Z')):
            return 1
        return 0
    
    def start_display(self):
        print(f'남은 시도 횟수: {self.num_of_attempts}\n(실패하면 -1)')
        print(hangman_pics[self.max_attempts - self.num_of_attempts])
        return input("한 글자만 입력: ").lower()

    def attempt(self):
        letter = self.start_display()
        if self.error(letter):
            self.display(2)
            return 
        if letter in self.word:
            self.correct(letter)
        else:
            self.incorrect()

    def end_game(self, is_success):
        if is_success:
            print("성공!")
        else:
            print("실패!")

    def play(self):
        while self.num_of_attempts > 0:
            self.attempt()
            if ''.join(self.user_ans) == self.word:
                self.end_game(1)
                break
        else:
            self.end_game(0)

if __name__ == '__main__':
    hangman = HangmanGame()
    hangman.play()