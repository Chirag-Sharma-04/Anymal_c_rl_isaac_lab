# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Backward-compatible aliases for older imports.

Use rough_env_cfg.py and flat_env_cfg.py directly for the canonical task configs.
"""

from .flat_env_cfg import AnymalCFlatEnvCfg, AnymalCFlatEnvCfg_PLAY
from .rough_env_cfg import AnymalCRoughEnvCfg, AnymalCRoughEnvCfg_PLAY

# Legacy names retained for compatibility.
AnymalCRlEnvCfg = AnymalCRoughEnvCfg
AnymalCRlEnvCfg_PLAY = AnymalCRoughEnvCfg_PLAY