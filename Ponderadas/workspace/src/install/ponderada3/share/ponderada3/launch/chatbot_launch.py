from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ponderada3',
            executable='chatbot',
            name='ponderada3',
            output='screen',
            prefix=['gnome-terminal --'],
        )
    ])