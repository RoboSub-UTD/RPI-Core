import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class VideoPublisher(Node):

    def __init__(self):
        super().__init__('video_publisher')
        self.publisher_ = self.create_publisher(Image, 'video', 10)
        self.timer_period = 0.1  # seconds (10 Hz)
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.i = 0
        self.bridge = CvBridge()

    def timer_callback(self):
        cap = cv2.VideoCapture(0)  # Capture video from the webcam (device 0)
        ret, frame = cap.read()  # Read the current frame
        cap.release()  # Release the video capture object

        if ret:
            image_message = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
            self.publisher_.publish(image_message)

def main(args=None):
    rclpy.init(args=args)

    video_publisher = VideoPublisher()

    rclpy.spin(video_publisher)

    video_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


