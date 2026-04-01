# Blender Shader Cycle 
A Blender Python add-on that changes all active materials using principled BSDF

This tool is non-destructive, meaning original node connections are preserved and shaders are not removed or replaced.

## Features:
- Preset shaders: Quickly swap to pre-configured shaders (emission + toon) ✅
- Non-Destructive Memory: Caches previous node connections to restore the original material ✅
- Targeted Swapping: Option to select materials by specific mesh vs. the entire project. ❌
- Texture input support: 🔄
- Custom Shaders: Support for user-defined replacement shaders. ❌


## Top-down Workflow
1. Iterate over every actively assigned material in the scene.
2. Locate the specific node connected directly to the Material Output (MO) surface input.
3. Store the output-connected shader node and the approximate base/diffuse color.
4. Disconnect the active node and insert the specified replacement shader node.
5. Initialize the replacement shader with the stored color value and reconnect it to the output.

   
## Setup Guide
Step 1:
Download all 5 .py files from this repository, place them in a folder on your computer, and compress that folder into a .zip file.

<img width="611" height="143" alt="image" src="https://github.com/user-attachments/assets/e22a2e6a-1e67-4d8a-bf31-d0d1b7a86507" />
<img width="563" height="326" alt="image" src="https://github.com/user-attachments/assets/5d97ab85-019a-4901-a9eb-a6ff568014ef" />

Step 2: 
In Blender, go to Edit > Preferences > Add-ons. Click the dropdown arrow/icon at the top right and select Install from Disk.

<img width="453" height="295" alt="image" src="https://github.com/user-attachments/assets/f260b042-c901-443f-80a1-c688a19a1573" />

Step 3:
Navigate to where you saved your .zip file, select it, and click Install Add-on.

<img width="678" height="60" alt="image" src="https://github.com/user-attachments/assets/847aebfb-47bb-4461-8acb-8239bf560de4" />





