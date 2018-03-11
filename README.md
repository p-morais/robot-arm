# robot-arm
Ongoing code for a robotic arm I'm developing

The plan is to: be able to control individual joints from a computer via usb serial (or wifi/bluetooth) -> compute inverse kinematics and command those poses -> model the arm in MuJoCo -> rip out the servo potentiometers and hard stops and control the dc motors directly with PD/iLQR/model based or model free RL/state space control/kalman filtering/whatever interesting technique -> add a camera and vision -> make it play chess or something. I'll also iterate over the physical design over time, but probably very slowly as I'm not great with CAD.