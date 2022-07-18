import cv2
from keras.models import load_model
import numpy as np
from time import time
from random import choice

class RPS:
    def __init__(self, total_rounds=5, delay=3):
        self.model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.last_time = time()
        self.total_rounds = total_rounds
        self.score = [0,0,0] # count of draws, user wins, computer wins
        self.delay = delay
        self.current_round = 1

    def get_prediction(self):
        rps_choices = ['rock', 'paper', 'scissors', 'nothing']
        self.user_prediction = rps_choices[3]
        switch = True
        while True:
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            self.data[0] = normalized_image
            prediction = self.model.predict(self.data, verbose = 0) # this line is noisy without verbose key set to silent
            cv2.imshow('frame', frame)
            self.user_prediction = rps_choices[np.argmax(prediction)]
            #print(user_prediction)
            # Press q to close the window
            if switch == True:  # one time switch to run code so timings are equal between rounds
                self.last_time = time()
                switch = False
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if (time()-self.last_time)>self.delay:
                break
        return self.user_prediction

    def close_prediction(self):
        # After the game release the cap object
        self.cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows()
        return

    def get_computer_choice(self):
        return choice(['rock','paper','scissors'])

    def get_winner(self):
        computer_choice = self.computer_choice
        user_choice = self.user_prediction
        print(f'Computer chose {computer_choice}, User chose {user_choice}')
        if computer_choice == user_choice:
            print('Draw!')
            return 0
        if (computer_choice =='rock' and user_choice =='paper') or (computer_choice =='paper' and user_choice =='scissors') or (computer_choice =='scissors' and user_choice =='rock'):
            print('User wins!')
            return 1
        else:
            print('Computer wins!')
            return 2
        
    def get_overall_winner(self):
        score = self.score
        if score[1]==score[2]:
            print("Draw overall!")
            return
        if score[1]>score[2]:
            print("User wins overall!")
            return
        print("Computer wins overall!")
        return

    def play(self):
        while (self.score[1] + self.score[2]) < self.total_rounds:
            print(f"Start round {self.current_round}")
            self.computer_choice = self.get_computer_choice()
            self.get_prediction()
            self.score[self.get_winner()]+=1
            self.current_round+=1
        self.get_overall_winner()
        self.close_prediction()
        return

game = RPS(3)
game.play()