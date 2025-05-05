import rclpy
from geometry_msgs.msg import Twist
import time

def move_square(publisher):
    move_cmd = Twist()
    turn_cmd = Twist()

    # Set linear velocity (m/s)
    move_cmd.linear.x = 2.0
    move_cmd.angular.z = 0.0

    # Set angular velocity (rad/s)
    turn_cmd.linear.x = 0.0
    turn_cmd.angular.z = 1.57  # About 90 degrees per second

    for _ in range(4):
        # Move forward
        publisher.publish(move_cmd)
        print('Moving forward...')
        time.sleep(2)  # Move forward for 2 seconds

        # Stop briefly
        publisher.publish(Twist())
        time.sleep(1)

        # Turn 90 degrees
        publisher.publish(turn_cmd)
        print('Turning...')
        time.sleep(1.6)  # Turn approximately 90 degrees

        # Stop briefly
        publisher.publish(Twist())
        time.sleep(1)

    print('Done with square!')

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('turtle_mover')
    publisher = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    time.sleep(4)  # Wait for publisher to set up

    move_square(publisher)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
