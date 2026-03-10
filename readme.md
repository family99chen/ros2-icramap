太棒了！恭喜你彻底征服了这套源码，并且成功拥有了属于自己的开源仓库！这绝对是值得纪念的时刻。

```markdown
# ICRA 2024 QRC Simulation Map (ROS 2 修复版)

![ROS 2](https://img.shields.io/badge/ROS_2-Humble-blue.svg)
![Gazebo](https://img.shields.io/badge/Gazebo-Classic-orange.svg)

## 📌 项目简介

本项目是为 **ICRA 2024 四足机器人挑战赛 (QRC)** 提供的官方仿真地图的 **ROS 2 原生重构版本**。

**🔥 解决了什么痛点？**
原官方提供的地图包基于 ROS 1 (`catkin` 构建)。如果在 ROS 2 环境下强行加载，由于底层构建系统 (`ament`) 和 Gazebo 的模型寻址机制冲突，会导致 3D 贴图 (Meshes) 丢失，出现**“只有物理碰撞，地图完全隐身透明”**的恶性 Bug。

本项目通过重构 ROS 2 包结构、改写 `CMakeLists.txt` 以及提供原生的 `launch.py` 脚本，彻底修复了跨版本移植导致的寻址问题，实现即插即用。

---

## 🛠️ 环境依赖

* **操作系统:** Ubuntu 22.04 (推荐)
* **ROS 版本:** ROS 2 Humble
* **仿真器:** Gazebo Classic (需安装 `gazebo_ros_pkgs`)

---

## 🚀 快速安装与编译

**1. 克隆代码到你的工作空间 (`src` 目录下)**
```bash
cd ~/workspace/src
git clone [https://github.com/](https://github.com/)<你的用户名>/icra_map_ros2.git

```

**2. 编译节点**

```bash
cd ~/workspace
colcon build --packages-select icra_map_ros2

```

**3. 加载环境变量 (每次打开新终端都要执行)**

```bash
source install/setup.bash

```

---

## 🎮 运行仿真地图

**⚠️ 核心注意（必看！）：**
为了让 Gazebo 能够正确找到 3D 贴图文件，在启动 launch 文件前，**必须**将本 ROS 2 包的安装路径注入到 Gazebo 的模型搜索路径中。

请在终端中按顺序执行以下两行命令：

```bash
# 1. 注入 Gazebo 模型环境变量 (解决地图隐身的关键)
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/workspace/install/icra_map_ros2/share

# 2. 一键启动地图
ros2 launch icra_map_ros2 gazebo_world.launch.py

```

启动后，你将看到完整的带斜坡和台阶的 ICRA 比赛场地！

---

## 💡 常见问题 (FAQ)

* **Q: 终端报出一堆 `ALSA lib ...` 的错误怎么办？**
A: 这是 Linux 系统的声卡驱动报错（尤其在 Docker 容器或云服务器中常见）。Gazebo 找不到音频输出设备导致的，**完全不影响任何物理仿真和画面渲染，直接无视即可**。


