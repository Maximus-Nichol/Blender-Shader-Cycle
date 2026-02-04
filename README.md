# Blender-Texture-Cycle
A Blender Python add-on that iterates over all actively used materials in a scene and replaces the shader connected to each Material Output (MO) with a configurable replacement shader.

This tool is non-destructive, meaning original node connections are preserved and shaders are not removed or replaced.

## Features (planned):
- Filters all of the inactive materials in a project
- Identifies the final node connected to the MO
- Identifies and saves colour of every material
- Creates new shader based on stored colour and user input
- Keeps memory of previous node connections to the MO to restore original configuration
- Option to select textures assigned to a specific mesh vs. entire project

## Top-down Workflow
1. Iterate over every actively assigned material
2. For each material, locate the node connected to the MO surface input
3. Store the shader node connected to the output and the approximate base/diffuse colour
4. Disconnect the node and insert a specified replacement shader node
5. Initialize the replacement shader with the stored colour value and connect it to the output