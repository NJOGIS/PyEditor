import arcpy
import pythonaddins

class ExtensionClass1(object):
    """Implementation for PyEditorDev_addin.extension2 (Extension)"""
    def __init__(self):
        # For performance considerations, please remove all unused methods in this class.
        self.enabled = True
        self.monitorOp = "Empty"
        self.esesh = dict(inSession=0, onStartOperation=0, onBeforStopOperation=0, onStopOperation = 0, onSaveEdits=0, onChangeFeature=0, onCreateFeature=0, onDeleteFeature=0)
    def onEditorSelectionChanged(self):
        print "onEditorSelectionChanged"
        ########################################################################
        ########################################################################
        # Endpoint for NewSegment
        if self.monitorOp == "1010":
            print "NewSegment onEditorSelectionChanged endpoint, self.self.monitorOp is: {0}\nself.esesh and self.monitorOp have been cleared".format(self.monitorOp)
            self.esesh['onStartOperation'] = 0; self.esesh['onChangeFeature'] = 0; self.esesh['onCreateFeature'] = 0; self.esesh['onDeleteFeature'] = 0;
            self.monitorOp = "Empty"

        ########################################################################
        ########################################################################
        if self.monitorOp == "1101": # merge endpoint
            print "Merge onEditorSelectionChanged endpoint, self.self.monitorOp is: {0}\nself.esesh and self.monitorOp have been cleared".format(self.monitorOp)
            self.esesh['onStartOperation'] = 0; self.esesh['onChangeFeature'] = 0; self.esesh['onCreateFeature'] = 0; self.esesh['onDeleteFeature'] = 0;
            self.monitorOp = "Empty"

    def onStartEditing(self):
        print "onStartEditing"
    def onStopEditing(self, save_changes):
        pass
        self.esesh['inSession'] = 0; self.esesh['onStartOperation'] = 0; self.esesh['onChangeFeature'] = 0; self.esesh['onCreateFeature'] = 0; self.esesh['onDeleteFeature'] = 0
        self.monitorOp = "Empty"

    def onStartOperation(self):
        print "onStartOperation"
        self.esesh['onStartOperation'] = 1

    def beforeStopOperation(self):
        pass
    def onStopOperation(self):
        print "onStopOperation"
        #global self.monitorOp
        self.monitorOp = str(self.esesh['onStartOperation']) + str(self.esesh['onChangeFeature']) + str(self.esesh['onCreateFeature']) + str(self.esesh['onDeleteFeature'])
        print "self.monitorOp is: {0}".format(self.monitorOp)
        # New: 1010
        # Delete: 1001
        # Split: 1110
        # Merge: 1101
        # ChangeFeature: 1100
        # Copy Parallel: 1010
        # Buffer: 1010


        if self.monitorOp == "1100": # ChangeFeature
            print "Change Feature -- onStopOperation endpoint, self.monitorOp is: {0}\nself.esesh and self.monitorOp have been cleared".format(self.monitorOp)
            self.esesh['onStartOperation'] = 0; self.esesh['onChangeFeature'] = 0; self.esesh['onCreateFeature'] = 0; self.esesh['onDeleteFeature'] = 0
            self.monitorOp = "Empty"

        if self.monitorOp == "1000": # Hidden Start
            print "Hidden Start -- onStopOperation endpoint, self.monitorOp is: {0}\nself.esesh and self.monitorOp have been cleared".format(self.monitorOp)
            self.esesh['onStartOperation'] = 0; self.esesh['onChangeFeature'] = 0; self.esesh['onCreateFeature'] = 0; self.esesh['onDeleteFeature'] = 0;
            self.monitorOp = "Empty"

        if self.monitorOp == "1010":  # NewFeature
            print "New Feature -- onStopOperation endpoint, self.monitorOp is: {0}\nself.esesh and self.monitorOp have NOT been cleared".format(self.monitorOp)

        if self.monitorOp == "1001": # Delete
            print "Delete -- onStopOperation endpoint, self.monitorOp is: {0}\nself.esesh and self.monitorOp have been cleared".format(self.monitorOp)
            self.esesh['onStartOperation'] = 0; self.esesh['onChangeFeature'] = 0; self.esesh['onCreateFeature'] = 0; self.esesh['onDeleteFeature'] = 0;
            self.monitorOp = "DF"

        if self.monitorOp == "1110": # Split
            print "Split -- onStopOperation endpoint, self.monitorOp is: {0}\nself.esesh and self.monitorOp have been cleared".format(self.monitorOp)
            self.esesh['onStartOperation'] = 0; self.esesh['onChangeFeature'] = 0; self.esesh['onCreateFeature'] = 0; self.esesh['onDeleteFeature'] = 0;
            self.monitorOp = 'Empty'

        if self.monitorOp == "1101": # Merge
            print "Merge -- onStopOperation endpoint, self.monitorOp is: {0}\nself.esesh and self.monitorOp have NOT been cleared".format(self.monitorOp)

    def onSaveEdits(self):
        print "onSaveEdits"
        self.esesh['onStartOperation'] = 0; self.esesh['onChangeFeature'] = 0; self.esesh['onCreateFeature'] = 0; self.esesh['onDeleteFeature'] = 0;
        self.monitorOp = 'Empty'
    def onChangeFeature(self):
        print "OnChangeFeature"
        self.esesh['onChangeFeature'] = 1
    def onCreateFeature(self):
        print "onCreateFeature"
        self.esesh['onCreateFeature'] = 1
    def onDeleteFeature(self):
		print "onDeleteFeature"
		self.esesh['onDeleteFeature'] = 1
    def onUndo(self):
        print "onUndo"
        self.esesh['onStartOperation'] = 0; self.esesh['onChangeFeature'] = 0; self.esesh['onCreateFeature'] = 0; self.esesh['onDeleteFeature'] = 0
        self.monitorOp = 'Empty'
    def onRedo(self):
        pass