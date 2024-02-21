# Lab_3

ME 405-04 with Dr. Ridgely

Members: Jacquelyn Banh, Nathan Chapman, Jessica Perez

Tub: mecha06

Lab 03 Program Description:

The objective of this lab is to develop a closed-loop controller for a DC motor. The main code is capable of controlling the motor, reading an encoder, and generating near-real-time plots of the motor's position. Our team utilized proportional control to develop a user interface that enables one to input a gain value (kp) to account for various operating parameters. With the inputted value, the motor pushes itself to move the load to the desired position quickly and accurately, without causing the system to overshoot or become unstable. 

The developed closed-loop controller file, our motor_contoller_Nathan.py, 

To ensure that our code was running properly, several tests with various Kp values were performed. We compared the response of the motor position and corresponding time with other gain values, and the developed plots are shown in Figures 1 and 3. The test utilized a step response plot where we continued to adjust the Kp value to obtain a good motor performance. Figure 1 shows the tested Kp values and Figure 2 shows a zoomed-in view. Examining Figure 1, we tested three Kp values 0.1, 0.5, and 0.9. From the plotted response it appears that 

had the best gain value because of its


![image](https://github.com/NathanCo2/Lab_3/assets/156120309/14ff0b8e-cbfe-48c0-969b-ee4a9880c240)
Figure 1: Isolated Motor Response of KP plot with 0.1 0.5 0.9
![image](https://github.com/NathanCo2/Lab_3/assets/156120309/e1c47428-0275-4127-a956-a74576b784cc)
Figure 2: Zoom in of Figure 1

![image](https://github.com/NathanCo2/Lab_3/assets/156120309/a8af1ff5-37c8-42b6-8782-15407aec3d80)
Figure 3: Motor with Inertia Response of KP plot with 0.1 0.3 0.5 0.9
![image](https://github.com/NathanCo2/Lab_3/assets/156120309/244dc3c5-3e65-4a6c-ba69-bd20572154ae)
Figure 4: Zoom in of Figure 4

