from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, IncludeLaunchDescription, TimerAction
from launch.substitutions import LaunchConfiguration
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
       
        ExecuteProcess(
           cmd=['ros2', 'launch' ,'turtlebot3_navigation2', 'navigation2.launch.py', 'use_sim_time:=True', 'map:=maps/ponderada2_mapa.yaml'],
          output='screen',
           
        ),

        ExecuteProcess(
          cmd=['ros2', 'launch', 'turtlebot3_gazebo', 'turtlebot3_world.launch.py'],
          output='screen',
        ),
        Node(
            package='mapeamento',
            executable='pontos.py',
            name='pontos',
            prefix = 'gnome-terminal --',
            output='screen'
        )
    ])