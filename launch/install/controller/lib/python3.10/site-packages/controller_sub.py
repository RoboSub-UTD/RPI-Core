import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
import serial


class ControllerSub(Node):
    def __init__(self):
        super().__init__('controller_sub')
        self.get_logger().info('Starting initialization..')
        self.subscription = self.create_subscription(
            Joy,
            '/joy',
            self.listener_callback,
            10)
        #self.serial_port = serial.Serial('/dev/ttyAMA0', 9600)

        self.get_logger().info('Reached the end of initialization..')

    def listener_callback(self, msg):
        #self.get_logger().info('Received joystick data: axes=%s, buttons=%s' % (msg.axes, msg.buttons))
        try:
            #self.serial_port.write(str(msg.axes).encode() + b'\n')
            #self.serial_port.write(str(msg.buttons).encode() + b'\n')

            self.get_logger().info(str(msg.axes).encode() + b'\n')
            self.get_logger().info(str(msg.buttons).encode() + b'\n')
        except:
            self.get_logger().info('Input being received...')

        #self.get_logger().info('Reached the end of the callback..')


def main(args=None):
    rclpy.init(args=args)
    controller_sub = ControllerSub()
    rclpy.spin(controller_sub)
    controller_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

