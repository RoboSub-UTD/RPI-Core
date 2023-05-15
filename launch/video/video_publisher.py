import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class VideoPublisher(Node):

  def __init__(self):
    super().__init__('video_publisher')

    self.publisher_ = self.create_publisher(Image, 'video_stream', 10)

    timer_period = 1  # seconds (4 Hz)
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.cap = cv2.VideoCapture(0, cv2.CAP_V4L2)  # Capture video from the webcam (device 0)

    #self.cap.set(cv2.CAP_PROP_FPS, 5)
    self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

    self.bridge = CvBridge()

  def timer_callback(self):

    ret, frame = self.cap.read()  # Read the current frame

    if ret == True:
      #Publish the images to the topic
      cv2.normalize(frame, frame, 0, 255, cv2.NORM_MINMAX)
      image_message = self.bridge.cv2_to_imgmsg(frame)
      self.publisher_.publish(image_message)
      self.get_logger().info('Publishing video frame')


def main(args=None):
  rclpy.init(args=args)

  video_publisher = VideoPublisher()

  rclpy.spin(video_publisher)

  video_publisher.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()

