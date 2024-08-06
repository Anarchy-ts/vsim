import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    urdf_file_name = 'urdfs/vnymous.urdf'
    urdf = os.path.join(
        get_package_share_directory('vsim'),
        urdf_file_name)
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()

    position = [0.0,0.0,0.0]
    orientation = [0.0,0.0,0.0]

    pkg_share = FindPackageShare(package='vsim').find('vsim')
    gazebo_models_path = os.path.join(pkg_share, 'meshes/igvc/')
    os.environ["GAZEBO_MODEL_PATH"] = gazebo_models_path

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_desc}],# 'publish_frequency': 10.0}],
            arguments=[urdf]),
        # Node(
        #    package='joint_state_publisher',
        #    executable='joint_state_publisher',
        #    name='joint_state_publisher',
        #     output='screen',
        #     parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_desc}],
        #     arguments=[urdf]
        # ),
        #Node(
         #   package="tf2_ros",
          #  executable="static_transform_publisher",
           # output="screen" ,
            #arguments=["0", "0", "0", "0", "0", "0", "odom", "base_footprint"]
         #),
        # Node(
        #     package="tf2_ros",
        #     executable="static_transform_publisher",
        #     output="screen" ,
        #     arguments=["0.20", "-0.01", "1.05", "0", "0.2618", "0", "base_link", "zed_camera_link"]
        #  ),
        # Node(
        #     package="tf2_ros",
        #     executable="static_transform_publisher",
        #     output="screen" ,
        #     arguments=["-0.19", "-0.20", "0.30", "0", "0", "0", "base_link", "laser"]
        #  ),

        Node(
           package='gazebo_ros',
           executable='spawn_entity.py',
           arguments=['-topic','/robot_description',
                      '-entity','vnymous'],
            output='screen'
        )        
    ])
