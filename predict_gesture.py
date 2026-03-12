import cv2
import mediapipe as mp
import joblib

# load trained model
model = joblib.load("gesture_model.pkl")

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(img_rgb)

    gesture = "None"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            row = []

            for lm in hand_landmarks.landmark:
                row.append(lm.x)
                row.append(lm.y)

            prediction = model.predict([row])

            gesture = prediction[0]

    cv2.putText(img, gesture, (50,100),
                cv2.FONT_HERSHEY_SIMPLEX,
                2, (0,255,0), 3)

    cv2.imshow("Gesture Recognition", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()