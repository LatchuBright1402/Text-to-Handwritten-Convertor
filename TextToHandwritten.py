import pywhatkit
import cv2

pywhatkit.text_to_handwriting("A robot is the product of the robotics field, where programmable machines are built that can assist humans or mimic human actions. Robots were originally built to handle monotonous tasks (like building cars on an assembly line), but have since expanded well beyond their initial uses to perform tasks like fighting fires, cleaning homes and assisting with incredibly intricate surgeries. Each robot has a differing level of autonomy, ranging from human-controlled bots that carry out tasks that a human has full control over to fully-autonomous bots that perform tasks without any external influences.")
image = cv2.imread("pywhatkit.png")
cv2.imshow("TextToHandwritten", image)
print("Text to Handwritten Conversion is done successfully", image)
cv2.waitKey(0)
