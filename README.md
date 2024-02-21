# Lab_3

ME 405-04 with Dr. Ridgely

Members: Jacquelyn Banh, Nathan Chapman, Jessica Perez

Tub: mecha06

Lab 03 Program Description:

The objective of this lab is to develop a closed-loop controller for a DC motor. The main code is capable of controlling the motor, reading an encoder, and generating near-real-time plots of the motor's position. Our team utilized proportional control to develop a user interface that enables one to input a gain value (kp) to account for various operating parameters. With the inputted value, the motor pushes itself to move the load to the desired position quickly and accurately, without causing the system to overshoot or become unstable. 

The developed closed-loop controller file, our motor_contoller_Nathan.py, was created to set the proportional gain, initialize the setpoint in units of encoder counts, and other necessary parameters to perform the closed-loop control. Utilizing this class, the actuation value is calculated using the difference between the measured location of the motor from the setpoint producing an error signal. This error signal is multiplied by a control gain, Kp, to calculate the pulse width modulation, affecting the motor response. The actuation signal calculated is then sent to the motor driver to control the magnitude and direction of the motor torque. 

To ensure that our code was running properly, several tests with various Kp values were performed. We compared the response of the motor position and corresponding time with other gain values, and the developed plots are shown in Figures 1 and 3. The test utilized a step response plot where we continued to adjust the Kp value to obtain a good motor performance. Figure 1 shows the first test with the tested Kp values and Figure 2 shows a zoomed-in view. Examining Figure 1, we tested three Kp values 0.1, 0.5, and 0.9. From the plotted response it appears that 0.1 was the best gain value, although it has a small overshoot but then shows that it was able to quickly correct itself without continuing oscillation. Figure 3 shows the second test conducted analyzing the motor response with Kp values of 0.1, 0.3, 0.5, and 0.9. As expected, 0.1 was our desired gain value due to its ability to quickly reach the desired performance with good accuracy. 

<img width="422" alt="image" src="https://github.com/NathanCo2/Lab_3/assets/156122419/cfa865f3-d3c3-4206-a6ec-3741e8a88a77">

Figure 1: Isolated Motor Response of KP plot with 0.1 0.5 0.9

<img width="422" alt="image" src="https://github.com/NathanCo2/Lab_3/assets/156122419/25a0fd45-24fe-4619-a76c-744cbe68a7cd">

Figure 2: Zoom in of Figure 1

<img width="423" alt="image" src="https://github.com/NathanCo2/Lab_3/assets/156122419/47fcc42c-fd4c-4369-9376-573690a1032c">

Figure 3: Motor with Inertia Response of KP plot with 0.1 0.3 0.5 0.9

<img width="432" alt="image" src="https://github.com/NathanCo2/Lab_3/assets/156122419/8ab9033b-9389-440c-a3a0-6ebac4dd281e">

Figure 4: Zoom in of Figure 4
