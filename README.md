# Maya Batch Script for Sphere Creation and Material Application

## Description

This Python script is designed to be executed in Maya's batch mode using `mayapy`. It allows you to automate the creation of a 3D polySphere in Maya and apply a red Lambert material to it. The script uses `argparse` to take command-line arguments for controlling these operations, making it suitable for batch processing without the need for a graphical interface.

## Arguments

The script accepts the following command-line arguments:

- `--createSphere`: Creates a polySphere object in Maya if it does not already exist.
- `--applyMaterial`: Applies a red Lambert material to the sphere if it exists. If the sphere does not exist, the material will not be applied.

### Argument Details:

| Argument        | Type   | Description                                                     |
|-----------------|--------|-----------------------------------------------------------------|
| `--createSphere` | Flag   | Creates a polySphere in the scene with the name `newPolySphere`.|
| `--applyMaterial`| Flag   | Applies a red Lambert material to the sphere.                   |

## Example Usage

To run the script, you will need to execute it using `mayapy` in batch mode. Below are some example commands:

### Create a Sphere
To create a sphere, use the following command:

```bash
mayapy your_script.py --createSphere# anim435-assignment3
