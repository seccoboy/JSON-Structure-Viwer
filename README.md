# JSON-Structure-Viwer
A Python code for visualizing JSON's structures

To use it: 

Run the ```getJsonStrucutre.py``` on the same folder as your JSON file

Or, you can pass the file as parameter ex:
```
py.exe .\getJsonStructure.py '.\YourJSONs\YourFile.json'
```

It might be skill issue, but i couldnt find any solution for this problem, so I wrote my own.

It will save the structure in a .txt file called "estrutura_(your file name).txt"
Output example:
```
Processing file: 630275941520498.json
ballPosition - (array)
playerTracking - (object)
    people - (array)
        centerOfMass - (array)
        heightOfGround - (float)
        jerseyNumber - (str)
        jointIds - (array)
        positions - (array)
        roleId - (int)
        skeletonType - (str)
        teamId - (int)
        trackId - (int)
    roles - (array)
        name - (str)
    skeletons - (object)
        COCO - (object)
            connections - (array)
    teams - (array)
        name - (str)
time - (int)
version - (int)
```
