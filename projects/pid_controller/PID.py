class PIDController():
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = 0
        self.previous_error = 0
        self.integral = 0

    def update(self, setpoint, measured_value, dt):
        self.setpoint = setpoint
        error = setpoint - measured_value
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt if dt > 0 else 0

        output = (self.Kp * error) + (self.Ki * self.integral) + (self.Kd * derivative)

        self.previous_error = error

        return output
    
import matplotlib.pyplot as plt
import numpy as np

#Initialize PID controller
setpoint = 100
pid = PIDController(Kp=0., Ki=0., Kd=0.1, setpoint=setpoint)
#Simulation parameters
time = np.linspace(0, 10, 100) # 10 seconds, 100 points

measured_value = 20
dt = time[1] - time[0]
outputs = []
for t in time:
    output = pid.update(setpoint, measured_value, dt)
    outputs.append(output)
    # Simulate system response (for demonstration purposes)
    measured_value += output * dt- 0.1 * (measured_value * dt) # Simulate some system dynamics

#Plotting results
plt.figure(figsize=(10, 5))
plt.plot(time, outputs, label='PID Output')
plt.axhline(setpoint, color='r', linestyle='--', label='Setpoint')
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.title('PID Controller Response')
plt.legend()
plt.grid(True)
plt.show()