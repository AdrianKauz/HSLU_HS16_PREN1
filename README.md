# HSLU HS16 PREN1 - Python test code for Raspberry Pi

Some code that was created during the PREN1-Module in autumn 2016.<br>
Used and tested hardware: Raspberry Pi 3, Sense HAT Module, UltraBorg
Feel free to use it :-).

## Getting Started

### **[PiHaleyCore: Proof of concept](pi_HaleyCore/pi_HaleyCore_PoC)**  
* The idea here is, that the modules, which handles access to the sensors etc., 
are connected through a core-module and they communicate together via message-packets.
The core here will act like a switch and as a watchdog.
If one module fails, the core is trying to restart it and so on.  

### **[Misc Pi Tests](pi_Tests_Misc)**  
* Mixed testcode for TOF-Sensor "VL53L0X", Pigpio and PWM, LED blinking and UltraBorg-Module.  

### **[Tests with Sense HAT](pi_Tests_SenseHat)**  
* Some Sense HAT testcode for IMU Sensors, RGB-Matrix, simple Sensor-Logger etc.  

### **[Tests with UltraBorg module](pi_Tests_UltraBorg/piUltraBorgUltrasonicTest)**  
* Ultrasonic distance test with UltraBorg-Module
