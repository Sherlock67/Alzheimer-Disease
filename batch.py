def Register(Fixedfilename,Movingfilename,OutVolumefilename,ind):
    Nodename = 'Volume_{:02d}'.format(ind)
    RegistrationPresets_ParameterFilenames = 5
    # Load Volume
    [ success,movingVolumeNode ] = slicer.util.loadVolume(Movingfilename,returnNode=True)
    [ success, fixedVolumeNode] = slicer.util.loadVolume(Fixedfilename,returnNode=True)
    

    from Elastix import ElastixLogic
    logic = ElastixLogic()
    parameterFilenames = logic.getRegistrationPresets()[0][RegistrationPresets_ParameterFilenames]
    outputVolume = slicer.vtkMRMLScalarVolumeNode()
    slicer.mrmlScene.AddNode(outputVolume)
    outputVolume.CreateDefaultDisplayNodes()
    outputVolume.SetName(Nodename)
    logic.registerVolumes(fixedVolumeNode, movingVolumeNode, parameterFilenames = parameterFilenames , outputVolumeNode = outputVolume)

    # Create OutputVolume Node.
    myNode = getNode(Nodename)
    myStorageNode = myNode.CreateDefaultStorageNode()
    myStorageNode.SetFileName(OutVolumefilename)
    myStorageNode.WriteData(myNode)
    slicer.mrmlScene.Clear(0)



def BatchRegister():
    path2subjects = 'C:\Users\User\Desktop\Alzheimmers Research\MRI_Image_Preprocessing\data'
    import os
    Fixedfilename = os.path.join(path2subjects,'Fixed.nii')
    print(Fixedfilename)
    for ind,dir in enumerate(os.listdir(path2subjects)):
        if dir == "Fixed.nii":
            continue
        Movingfilename = os.path.join(path2subjects,'Moving.nii')
        print(Movingfilename)
        OutVolumefilename = os.path.join(path2subjects,dir,'OutVolume.nii')
        print(OutVolumefilename)
        Register(Fixedfilename, Movingfilename, OutVolumefilename,ind)

BatchRegister()
