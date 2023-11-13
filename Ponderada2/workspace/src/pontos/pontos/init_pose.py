# #! /usr/bin/env python3 
# import rclpy
# from nav2_simple_commander.robot_navigator import BasicNavigator
# from geometry_msgs.msg import PoseStamped
# from tf_transformations import quaternion_from_euler
# from math import pi

# rclpy.init()
# nav = BasicNavigator()
# q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, 0.0)
# initial_pose = PoseStamped()
# initial_pose.header.frame_id = 'map'
# initial_pose.header.stamp = nav.get_clock().now().to_msg()
# initial_pose.pose.position.x = 0.0
# initial_pose.pose.position.y = 0.0
# initial_pose.pose.position.z = 0.0
# initial_pose.pose.orientation.x = q_x
# initial_pose.pose.orientation.y = q_y
# initial_pose.pose.orientation.z = q_z
# initial_pose.pose.orientation.w = q_w

# goal_pose1 = create_pose_stamped(nav, 2.5, 1.0, 1.57)
# goal_pose2 = create_pose_stamped(nav, 0.0, 1.0, 1.57)
# goal_pose3 = create_pose_stamped(nav, 0.0, 0.0, 0.00)

# waypoints = [goal_pose1, goal_pose2, goal_pose3]

# nav.followWaypoints(waypoints)
# while not nav.isTaskComplete():
#     print(nav.getFeedback())

# nav.setInitialPose(initial_pose)
# nav.waitUntilNav2Active()

# rclpy.shutdown()

# if __name__ == '__main__':
#     main()
