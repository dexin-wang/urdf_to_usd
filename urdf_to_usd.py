# Copyright (c) 2020-2023, NVIDIA CORPORATION. All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto. Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.
#

from isaacsim import SimulationApp

# URDF import, configuration and simulation sample
kit = SimulationApp({"renderer": "RayTracedLighting", "headless": True})
import omni.kit.commands
from omni.isaac.core.articulations import Articulation
from omni.isaac.core.utils.extensions import get_extension_path_from_name
from pxr import Gf, PhysxSchema, Sdf, UsdLux, UsdPhysics

# Setting up import configuration:
result, import_config = omni.kit.commands.execute("URDFCreateImportConfig")
# Set defaults
import_config.set_merge_fixed_joints(False)
import_config.set_replace_cylinders_with_capsules(False)
import_config.set_convex_decomp(True)   #!!
import_config.set_fix_base(False)    #!!
import_config.set_import_inertia_tensor(False)
import_config.set_distance_scale(1.0)
import_config.set_density(1000.0)  #!!
import_config.set_default_drive_type(0) #!!
# import_config.set_default_drive_strength(100)   #!!
# import_config.set_default_position_drive_damping(10000) #!!
import_config.set_self_collision(False)
import_config.set_up_vector(0, 0, 1)
import_config.set_make_default_prim(True)
import_config.set_parse_mimic(True)
import_config.set_create_physics_scene(True)
import_config.set_collision_from_visuals(False)


file_path = "urdf_path"
dest_path = "usd_path"

_, _robot_model = omni.kit.commands.execute(
                "URDFParseFile", urdf_path=file_path, import_config=import_config
            )

omni.kit.commands.execute(
                "URDFImportRobot",
                urdf_path=file_path,
                urdf_robot=_robot_model,
                import_config=import_config,
                dest_path=dest_path,
            )