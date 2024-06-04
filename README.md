# blender-retime

A Blender addon to retime animations and scenes.

## Usage

1. Select all the objects you want to retime.
2. Click the "Add to Velo" button.
3. Toggle the "Enable Velocity" checkbox on and off the first time you add to Velo to avoid bugs.

The retime value represents the frame displayed, so you can keyframe it to be anything you want and manipulate the speed.

## Known Issues

- Video textures or anything that plays not based on keyframes will not work (yet).
- The first time you click "add to Velo", it might have Velocity enabled even if it is unchecked.
- If NLA tracks are in use, the retime might not work. I recommend backing up the scene and baking the actions.

## Bugs

Bugs are expected as the addon is still in development.
