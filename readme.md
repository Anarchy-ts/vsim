# IGVC SIMULATION 

###### Source your workspace and general ros2
###### Also 'source /usr/share/gazebo/setup.sh'
###### Also create an include folder inside this package to avoid an error during colcon build

### To launch world :

```shell
ros2 launch vsim load_world.launch.py
```

### To load bot :
 
```shell
ros2 launch vsim load_bot.launch.py
```

### To run Teleop :

```shell
ros2 run vsim teleop_key.py
```
