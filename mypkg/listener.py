import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
from person_msgs.msg import Person

rclpy.init()
node = Node("listener")

def cb(msg):
    node.get_logger().info("Listen: %s" % msg)

def main():
    sub = node.create_subscription(Person, "person", cb, 10)  #型、トピック名、コールバック、キュー長
    rclpy.spin(node)
