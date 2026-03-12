import cv2
import mediapipe as mp
import csv

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)

gesture = input("Enter gesture name: ")

count = 0

with open("dataset.csv","a",newline="") as f:
    writer = csv.writer(f)

    while True:
        success,img = cap.read()

        img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                row = []

                for lm in hand_landmarks.landmark:
                    row.append(lm.x)
                    row.append(lm.y)

                writer.writerow(row + [gesture])

                count += 1

        cv2.putText(img,f"Samples: {count}",(50,50),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

        cv2.imshow("Collecting Data",img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()