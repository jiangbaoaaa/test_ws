import rospy
from geometry_msgs.msg import PoseStamped
from tf.transformations import quaternion_from_euler

def send_goal(x, y, yaw):  # yaw 为朝向偏航角（弧度）
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    rospy.sleep(1)  # 确保发布器已完全初始化

    goal = PoseStamped()
    goal.header.frame_id = "map"
    goal.header.stamp = rospy.get_rostime()  # 使用 ROS 时间戳
    goal.pose.position.x = x
    goal.pose.position.y = y
    goal.pose.position.z = 0

    # 将偏航角转换为四元数
    q = quaternion_from_euler(0, 0, yaw)
    goal.pose.orientation.x = q[0]
    goal.pose.orientation.y = q[1]
    goal.pose.orientation.z = q[2]
    goal.pose.orientation.w = q[3]

    # 发布目标消息
    pub.publish(goal)
    rospy.loginfo("Goal published: x=%.2f, y=%.2f, yaw=%.2f", x, y, yaw)


if __name__ == '__main__':
    try:
        rospy.init_node('goal_publisher')  # 初始化 ROS 节点
        rospy.sleep(1)  # 等待一秒，确保节点已启动
        send_goal(0.2, 0.15, 0.785)  # 示例：目标 (0.1, 0.15)，朝向 45° (0.785 弧度)
    except rospy.ROSInterruptException:
        pass
