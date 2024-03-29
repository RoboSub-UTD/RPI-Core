import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
import serial


class ControllerSub(Node):
    def __init__(self):
        super().__init__('')
        self.subscription = self.create_subscription(
            Joy,
            '/joy',
            self.listener_callback,
            10)
        self.serial_port = serial.Serial('/dev/ttyACM0', 9600)

    def listener_callback(self, msg):
        self.serial_port.write(str(msg.axes).encode() + b'\n')
        self.serial_port.write(str(msg.buttons).encode() + b'\n')


def main(args=None):
    rclpy.init(args=args)
    controller_sub = ControllerSub()
    rclpy.spin(controller_sub)
    controller_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

