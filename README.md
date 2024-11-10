# urdf_to_usd
convert object model of `.urdf` format to `.usd` format based on Isaac sim.

revise `file_path` and `dest_path` respectively to urdf path and where you want to save the usd file.

Use the python environment that comes with Isaac sim or Isaac lab to run `urdf_to_usd.py`.

## By the way
If you want to use the saved usd model in [Omnigibon](https://behavior.stanford.edu/omnigibson/), base_link or other link representing root must has a collision geometry, otherwise you can not do convex decomposition to the model using the following code:

```python
#! convex decomposition
box = env.scene.object_registry("name", "partnet_table")
for name, link in box.links.items():
    print('name =', name, 'link =', link)
    if name != 'base':  # if the collision geometry of base_link is a mesh, delete this check.
        for mesh in link.collision_meshes.values():
            mesh.set_collision_approximation('convexDecomposition')
```
