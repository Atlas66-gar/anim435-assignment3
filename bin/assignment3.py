import maya.standalone
import maya.cmds as cmds
import argparse

#Initialize Maya in batch mode
def setup_maya():
    maya.standalone.initialize(name='python')

#Create Sphere
def createSphere():
    if not cmds.objExists('newPolySphere')
        cmds.polySphere(name = 'newPolySphere')
        print('Sphere created.')
    else:
        print('Sphere already exists.')
    

#Create and add material to sphere
def sphereMaterial():
    if cmds.objExists('newPolySphere'):
        if not cmds.objExists('newShader'):
            #Create shader
            cmds.shadingNode('lambert', asShader=True, name='newShader')
            cmds.setAttr('newShader' + '.color', 1, 0, 0, type='double3')
            
            #Create shading group
            cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='newShader_shadingGroup')
    
            #Connect shader to shading group
            cmds.connectAttr('newShader.outColor', 'newShader_shadingGroup.surfaceShader')
            print('Shader created and connected.')
    
        #Assign material to sphere
        cmds.sets('newPolySphere', e=True, forceElement='newShader_shadingGroup')
        print('Material applied to sphere.')
    else:
        print('Please create the sphere first.')

# Main function to handle argparse
def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Run Maya commands in batch mode")
    
    # Add command-line options for sphere creation and material application
    parser.add_argument('--createSphere', action='store_true', help='Create a polySphere in Maya')
    parser.add_argument('--applyMaterial', action='store_true', help='Apply a red lambert material to the sphere')

    # Parse arguments
    args = parser.parse_args()

    # Initialize Maya in batch mode
    setup_maya()

    # Run based on the arguments provided
    if args.createSphere:
        create_sphere()
    
    if args.applyMaterial:
        sphere_material()

# Entry point
if __name__ == '__main__':
    main()