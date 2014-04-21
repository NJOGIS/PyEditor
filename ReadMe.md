#PyEditor
Python Add-In for ArcGIS Desktop ArcMap application. PyEditor is an ArcMap extension that will "listen" for map edit operations (i.e. split, merge, new segment) 
on a feature class. This is a "stubbed out" version of a complex Add-In that works in conjunction with ESRI's Editor toolbar, and a versioned geodatabase.
The 'PyEditor.esriaddin' file was developed on ArcGIS Desktop 10.2.1 (Python 2.7.5).
##Install
###Option 1
Run `makeaddin.py` to create the `.esriaddin` file. Double-click the `.esriaddin` file to install the Add-In
###Option 2
Double-click the 'PyEditor.esriaddin' file.
###Option 3
Use the Add-In Manager in ArcMap (Customize menu).
##Usage
After installation, the extension must be turned on in ArcMap using the Customize menu (i.e. Customize > Extensions... > PyEditor Extension), along with the ESRI Editor toolbar.
After starting an edit session using the Editor toolbar, the extension will report if the user either made a split, merge, or new feature in the feature class that is being
edited. The messages will be output in the Python window. Since this is a stubbed out code project, it is structured so that the user can easily create a response to the edit operations that took place in
the map document. For example, if a change in segment length of a line feature (e.g. after a split) needs to be reflected in a corresponding table (e.g. non-spatial table) in 
the user's database. Another example would be if a tool dialog needs to be launched after a split, merge, or creating a new feature.   
##License
GPLv3
##Credits
New Jersey Office of Information Technology
Office of Geographic Information Systems (GIS)
