import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class ArduinoBridge(Node):

    def __init__(self):
        super().__init__('arduino_bridge')
        self.publisher_ = self.create_publisher(String, 'arduino_data', 
10)
        self.serial = serial.Serial('/dev/ttyACM0', 9600)

        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        if self.serial.inWaiting():
            data = self.serial.readline().decode().strip()
            msg = String()
            msg.data = data
            self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    arduino_bridge = ArduinoBridge()

    rclpy.spin(arduino_bridge)

    arduino_bridge.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
