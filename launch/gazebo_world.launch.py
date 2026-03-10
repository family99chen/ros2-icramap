import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    pkg_dir = get_package_share_directory('icra_map_ros2')
    urdf_file = os.path.join(pkg_dir, 'urdf', 'map_sloped.urdf')

    return LaunchDescription([
        # 1. 启动 Gazebo 物理引擎
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        # 2. 把地图空投进 Gazebo
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'icra_arena', '-file', urdf_file],
            output='screen'
        )
    ])
