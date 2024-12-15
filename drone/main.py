from gym_multirotor.envs.mujoco.quadrotor_plus_hover import QuadrotorPlusHoverEnv
import os
from stable_baselines3 import PPO


env = QuadrotorPlusHoverEnv()

model = PPO("MlpPolicy", env, verbose=1)
if os.path.isfile("temp.model"):
    model.load("temp.model")
model.learn(total_timesteps=100000)

model.save("temp.model")

num_steps = 1500

obs = env.reset()

vec_env = model.get_env()
obs = vec_env.reset()
for i in range(num_steps):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = vec_env.step(action)
    vec_env.render()
    # VecEnv resets automatically
    # if done:
    #   obs = env.reset()

env.close()