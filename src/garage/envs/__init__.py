"""Garage wrappers for gym environments."""

from garage.envs.base import GarageEnv
from garage.envs.base import Step
from garage.envs.env_spec import EnvSpec
from garage.envs.grid_world_env import GridWorldEnv
from garage.envs.half_cheetah_dir_env import HalfCheetahDirEnv
from garage.envs.half_cheetah_vel_env import HalfCheetahVelEnv
from garage.envs.normalized_env import normalize
from garage.envs.normalized_reward_env import normalize_reward
from garage.envs.point_env import PointEnv

from garage.envs.ml1_wrapper import ML1WithPinnedGoal
__all__ = [
    'GarageEnv', 'Step', 'EnvSpec', 'GridWorldEnv', 'HalfCheetahDirEnv',
    'HalfCheetahVelEnv', 'normalize', 'normalize_reward', 'PointEnv',
    'ML1WithPinnedGoal',
]
