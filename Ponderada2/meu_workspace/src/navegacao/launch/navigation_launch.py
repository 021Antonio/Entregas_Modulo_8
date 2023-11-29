from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, IncludeLaunchDescription, TimerAction
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition

def generate_launch_description():
    return LaunchDescription([

      ExecuteProcess(
        cmd=['ros2', 'launch' ,'turtlebot3_navigation2', 'navigation2.launch.py', 'use_sim_time:=True', 'map:=maps/mapa.yaml'],
        output='screen',
           
      ),

      ExecuteProcess(
        cmd=["sleep", "5"],
        output="screen",
      ),

      ExecuteProcess(
        cmd=['ros2', 'launch', 'turtlebot3_gazebo', 'turtlebot3_world.launch.py'],
        output='screen',
      )

      
      # ExecuteProcess(
      #    cmd=["sleep", "5"],
      #    output="screen",
      # ),

      # ExecuteProcess(
      #   cmd=['ros2', 'run', 'navegacao', 'pontos.py'],
      #    output='screen',
      # )
 ])