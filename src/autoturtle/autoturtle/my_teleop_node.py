import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import tty
import termios


print("Press 'w' to move forward, 's' to move backward, 'a' to turn right, 'd' to turn left and press 'q' to exit.\n")

def main(args=None):
    rclpy.init(args=args)
    my_teleop_node = My_Teleop_Node()
    try:
        while True:
            button = catch_button()
            if button == 'w' or button == 'W':
                my_teleop_node.publish_twist(2.0, 0.0)  
                print(f"You pressed {button}. Move forward.\n Press 'w' to move forward, 's' to move backward, 'a' to turn right, 'd' to turn left and press 'q' to exit.\n")
            elif button == 's' or button == 'S':
                my_teleop_node.publish_twist(-2.0, 0.0)  
                print(f"You pressed {button}. Move backward.\n Press 'w' to move forward, 's' to move backward, 'a' to turn right, 'd' to turn left and press 'q' to exit.\n")
            elif button == 'a' or button == 'A':
                my_teleop_node.publish_twist(0.0, 1.2)  
                print(f"You pressed {button}. Move left.\n Press 'w' to move forward, 's' to move backward, 'a' to turn right, 'd' to turn left and press 'q' to exit.\n")
            elif button == 'd' or button == 'D':
                my_teleop_node.publish_twist(0.0, -1.2)  
                print(f"You pressed {button}. Move right.\n Press 'w' to move forward, 's' to move backward, 'a' to turn right, 'd' to turn left and press 'q' to exit.\n")
            elif button == 'q' or button == 'Q':
                print("You exited by pressing 'q'. Good bye.")
                break 
    finally:
        my_teleop_node.destroy_node()
        rclpy.shutdown()
        
class My_Teleop_Node(Node):
    def __init__(self):
        super().__init__('my_teleop_node')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.twist_msg_ = Twist()

    def publish_twist(self, linear_x, angular_z):
        self.twist_msg_.linear.x = linear_x
        self.twist_msg_.angular.z = angular_z
        self.publisher_.publish(self.twist_msg_)
        
def catch_button():
    f = sys.stdin.fileno()
    old_settings = termios.tcgetattr(f)
    try:
        tty.setraw(f)
        a = sys.stdin.read(1)
    finally:
        termios.tcsetattr(f, termios.TCSADRAIN, old_settings)
    return a

if __name__ == '__main__':
    main()


