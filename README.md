# SmartAC - The Future of AC Monitoring and Scheduling

## Project Overview
 
Currently, the common way to use AC timers is a smart plug. There are a lot of problems with 
this method; for example, it can only be used with one AC setting/temperature. Also, this 
method is not safe, as it's simply cuts off power from the AC in order to turn it off. There 
were many cases where this led to fires, that caused a lot of damage.

SmartAC is the future of Air Conditioner scheduling. It uses Infrared signals to turn the AC
on or off. That way, it can be used with different settings, it can be set remotely, and most
importantly - it's safer, as it just simulates the actions of the original AC remote. 

SmartAC can also be used to control or monitor your AC remotely, in addition to setting
timers. Forget to turn off your AC after leaving your house? No need to worry, simply
open the SmartAC interface on your phone and turn it off!

## First Version

### Current Status

This project is in early stages. Currently, I write some Python classes and basic code for
the server. The AC on/off tasks are just filled by placeholders like `print("AC On")` or other 
indicators. When the basic code will be done, I'll start working on the actual hardware. 

### Plans for the First Version

A single unit, that will run on a Pi 3B+ 4GB or Pi 4B 4GB. This unit will include an IR transmitter. \
The device will use FastAPI to serve the front-end web interface and to run the back-end HTTP server. 
It will store a local JSON database with the timers. The device will automate backup/security 
re-runs after each timer (run the same task again to make sure it works properly).

### Optional Features:
* Screen to display the next timer/task, or display the current AC setting. 
* Screen to display actual temp in the room using a temp sensor.
* Listen for IR signals from the actual AC remote, to update the status on the screen (when the AC is turned on by other devices/remotes).

### Hardware Required:
* Pi 3B+ 4GB / Pi 4B 4GB
* IR Transmitter/Receiver
* Screen (Optional)
* Temp Sensor (Optional)

## Future Plans

Main Unit - Pi 3B Plus
Additional Units - Pi Zero W + IR Transmitter/Receiver

Main Unit will include the main interface, using FastAPI. 
It will store a list of the additional units' IP/hostnames. 
The main unit will also serve the front-end of the service, and the main back-end.

Additional Units will include the backend for each room. 
one unit = one room.
Each will store a list of devices in the room, with option to "learn" from other IR remotes (using IR receiver). 
A list of timers will be stored in a local DB. 

### Optional Features:
* Adding temp/humidity sensors to simple units.
* Screen with the current temperature/humidity + AC status (on/off) and AC setting (temp).
* Automatically turn off when too cold/hot.
