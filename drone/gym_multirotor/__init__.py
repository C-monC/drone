from gymnasium.envs.registration import register
from gym_multirotor import envs  # noqa: F401
from gym_multirotor.envs import mujoco  # noqa: F401
from gym_multirotor.envs.mujoco import *  # noqa: F403


# Quadrotors with Plus(+)-configuration
register(
    id="QuadrotorPlusHoverEnv-v0",
    entry_point="gym_multirotor.envs.mujoco.quadrotor_plus_hover:QuadrotorPlusHoverEnv",
)


register(
    id="TiltrotorPlus8DofHoverEnv-v0",
    entry_point="gym_multirotor.envs.mujoco.tiltrotor_plus_hover:TiltrotorPlus8DofHoverEnv",
)

# Quadrotor with X-configuration
register(
    id="QuadrotorXHoverEnv-v0",
    entry_point="gym_multirotor.envs.mujoco.quadrotor_x_hover:QuadrotorXHoverEnv",
)
