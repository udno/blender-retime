# blender-retime

## Overview
**blender-retime** is a Blender addon designed to facilitate the retiming of animations and scenes.

## Usage Instructions
1. **Select Objects:** Select all the objects you want to retime.
2. **Add to Velo:** Click the "Add to Velo" button.
3. **Toggle Velocity:** For initial setup, toggle the "Enable Velocity" checkbox on and off to avoid potential bugs.
4. **Set Retime Value:** The retime value corresponds to the frame displayed. You can keyframe this value to achieve the desired animation speed and effects.

## Known Issues
- **Video Textures:** Currently, video textures or any media not based on keyframes are not supported.
- **Initial Velocity Toggle:** On the first use, the "Add to Velo" function may have Velocity enabled even if the checkbox is unchecked.
- **NLA Tracks:** If NLA (Non-Linear Animation) tracks are in use, retiming may not work as expected. It is recommended to back up your scene and bake actions before using the addon.

## Bugs
This addon is in active development, and bugs are to be expected. Please report any issues encountered to help improve the addon.
