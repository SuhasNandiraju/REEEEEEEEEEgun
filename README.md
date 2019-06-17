# REEEEEEEEEEgun
Hi, I'm Suhas. And if you're like me, you just hate when people barge into your room while you're watching porn. To solve this crisis amongst our generation, I created the REEEEEEEEEEgun to help keep out those pesky intrusions like your mom or the FBI.

The REEEEEEEEEEgun is basically a turret that detects the face of anyone who isn't on a special whitelist and shoots them with any manner of projectiles! 

The REEEEEEEEEEgun has 2 programs that you have to run simultaneously: the Arduino code for operating the turret and the python script for facial detection which will communicate with the Arduino using serial. 

In order to build the REEEEEEEEEEgun, you will need: an Arduino, 2 servos, an Arduino shield that can wire 2 servos, some basic arts and crafts stuff like wood and paper, tape, and an external webcam. For enhanced capabilities, get some extra female to female wires.


You can assemble the REEEEEEEEEEgun any way you want, but the basic idea is for one servo to hold a rotating base with the camera and "gun" on it. The "gun" will be a servo, which in my case, had a wooden skewer along with a piece of folded paper attached to it to make a basic (but shitty) catapult mechanism. The first servo should be held still somehow. I just taped it down to my desk, but not everyone is as bad at engineering as me, so you can probably 3d print a stand to hold it.


To use the REEEEEEEEEEgun, all you have to do is upload the .ino file to the arduino and then run the python script simultaneously as the arduino is plugged in. The result should be a turret that scans for a face. Once it finds one, it should start shooting its gun. The base should also follow your face once you have been detected and make adjustments to get a clean shot.

You may notice that the arduino code has some lines commented out. In the if statement which checks if the serialdata is '1', there is a line that writes the servo's stop value. If the comment out this line and uncomment the commented line, the result should be a rotating base that constantly spins until it detects a face. This is useful if you want to have fun, play a game where you avoid the turret fire. If you decide to switch the turret into this "spinning" mode, you may also want to uncomment the lines in the if statements that check if serialdata is '2' or '3'.

*Note, I am hot garbage at mechanical engineering and you can probably do a better job than I did with my design. dont hate pls.

-Suhas Nandiraju
