def Register(Fixedfilename, Movingfilename, OutVolumefilename, ind):
    Nodename = 'Volume_{:02d}'.format(ind)
    RegistrationPresets_ParameterFilenames = 5
    # Load Volume
    [success, movingVolumeNode] = slicer.util.loadVolume(Movingfilename, returnNode=True)
    [success, fixedVolumeNode] = slicer.util.loadVolume(Fixedfilename, returnNode=True)

    from Elastix import ElastixLogic
    logic = ElastixLogic()
    parameterFilenames = logic.getRegistrationPresets()[0][RegistrationPresets_ParameterFilenames]
    outputVolume = slicer.vtkMRMLScalarVolumeNode()
    slicer.mrmlScene.AddNode(outputVolume)
    outputVolume.CreateDefaultDisplayNodes()
    outputVolume.SetName(Nodename)
    logic.registerVolumes(fixedVolumeNode, movingVolumeNode, parameterFilenames=parameterFilenames,
                          outputVolumeNode=outputVolume)

    # Create OutputVolume Node.
    myNode = getNode(Nodename)
    myStorageNode = myNode.CreateDefaultStorageNode()
    myStorageNode.SetFileName(OutVolumefilename)
    myStorageNode.WriteData(myNode)
    slicer.mrmlScene.Clear(0)


def BatchRegister():
    path2subjects = r'D:\CSE DOCUMENT\Image Processing\Data\Moving'
    OutputDirectory = r'D:\CSE DOCUMENT\Image Processing\Data\Dataset'
    import os
    Fixedfilename = r'D:\CSE DOCUMENT\Image Processing\Data\Fixed\template.nii'
    print(Fixedfilename)
    for ind, dir in enumerate(os.listdir(path2subjects)):
        Movingfilename = os.path.join(path2subjects, dir)
        OutVolumefilename = os.path.join(OutputDirectory, dir)
        Register(Fixedfilename, Movingfilename, OutVolumefilename, ind)


BatchRegister()