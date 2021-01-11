#Tarea curso ROS
Alejandro Ruiz Esparza Rodríguez

##Robot PUMA560

Modelo URDF: puma560_pos.urdf

###Ver modelo en Rviz

roslaunch puma560_description mostrar.launch model:=puma560_pos.urdf gui:=true

###Simulación en Gazebo

roslaunch puma560_description puma560_model.launch urdf_file:=puma560_pos.urdf
roslaunch puma560_description puma560_pos_ctrl_spawner.launch

rosrun rqt_gui rqt_gui

Los tópicos para publicar los mensajes de control de posición son:
/puma560/joint_elbow_position_controller/command
/puma560/joint_shoulder_position_controller/command
/puma560/joint_waist_position_controller/command
/puma560/joint_wrist_bend_position_controller/command
/puma560/joint_wrist_roll_position_controller/command
/puma560/joint_left_gripper_position_controller/command
/puma560/joint_right_gripper_position_controller/command

Todos los mensajes son del tipo: std_msgs/Float64

###Función para controlar el robot

La función está ubicada en la carpeta "scripts"

Para llevar el robot a la posición cero:
python talker.py zero

Para llevar el robot a la posición home:
python talker.py home

Para llevar el robot a una posición arbitraria:
python talker.py 0.5 1.0 1.0 0.7 1.5 1.5
(Cada número corresponde al ángulo de una articulación de la bae al efector final, el último número indica la apertura de la pinza)
