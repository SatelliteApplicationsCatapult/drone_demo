Thunderbirds Search & Rescue

Source code for the AR Parrot drone for search & rescue missions.

Dependencies:
+ ps_drone
+ time, sys
+ numpy
+ cv2
+ os

The code is written in Python 2.7 using the ps_drone library. To run the program, place the drone in an open space and run the firstTry.py file.
The drone will take off and start a pre-programmed search path. At the moment of development it uses pictures that were taken previously, but still runs real-time image processing to identify any survivors.
The image processing algorithm looks for any orange color (that can be adjusted) to identify people in the image. When it finds a person, it saves the picture, and reports to command. Then it continues it's pre-programmed search path.

For security reasons now, after taking a picture, the operator is asked whether the drone should continue searching. To continue the search enter 'y' and press ENTER. Otherwise, the drone will execute the landing manouver.

Use at your own risk.
