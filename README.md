# Ball-Tracker_Robot

## Overview of the Project

This is a twist on a tutorial that was done by Adrian from PyImageSearch. Click [here](https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/) to read about his tutorial. What I did here was take his tutorial and add robotics to it. Here, when the robot detects a green ball, it moves forward. This can be expanded to other colors and I will be doing that in future projects.

### Getting Started

To get things started you will need both hardware and software. For myself, I used the following Hardware:

* Raspberry Pi Zero W
* Pi Camera with Ribbon Cable for the Zero W
* USB Power Bank
* 6 AA Batteries
* Devastator Tank Mobile Platform from DF Robot 
* HDD LEDs for the eyes
* dupont cables
* CamJam Edukit 3 motor controller board
* 3D Printed Camera mount found [here](https://www.tinkercad.com/things/hn6jajTg5Sv)
* Micro SD card
* Bluetooth keyboard and mouse controller for setup
* painted foam ball with dowell

For your hardware requirements you can use any chassis, replace the power bank with a UBEC, and other changes. This will still work for any robot provided you wire things correctly.

Software Requirements:

* Raspbian. Download [here](https://www.raspberrypi.org/downloads/raspbian/)
* OpenCV. Installation Tutorial [here](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/)

### Process

Here are the steps needed to get things running.

* Assemble Robot
* Insert Micro SD card into your laptop or PC. Then, download Raspbian and write the image using etcher or other software.
* Before ejecting your SD card, clone the repository and copy the files into the boot partition of the card in the /home/pi directory. 
* Eject the card and go through the usual installation process. If you have a robot that already uses the Raspberry Pi, ignore these steps but just add the repository in this case.
* Install OpenCV using the tutorial provided.
* Setup your environment as it will protect your main python install. Again, use the tutorial provided.
* Enable the camera by going into Menu > Preferences > Raspberry Pi Configuration > Interfaces > Camera > Enable
* Then go into a terminal (make sure you activate your environment) and type `cd Ball-Tracker-Robot`. Go into the directory and then type `python pi_robot_alarm.py --picamera`. Then the camera will turn on and you can start. Get a ball that is light green or you can paint your own using a foam ball. The robot should now move when it sees the ball. Make sure you use a neutral colored floor.
