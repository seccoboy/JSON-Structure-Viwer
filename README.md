# JSON-Structure-Viwer
A Python code for visualizing JSON's files structures

To use it: 
Run the getJsonStrucutre.py on the same folder as your JSON
Or, you can pass the file as parameter ex:
(py.exe .\getJsonStructure.py '.\YourJSONs\YourFile.json')


It might be skill issue, but i couldnt fiund any solution for this problem, so, I wrote my own.

It will save the structure in a .txt file called "estrutura_(your file name).txt"
Output example:

Processing file: YourFile.json
ballPosition - (array)
    ... (more elements)
playerTracking - (object)
    people - (array)
        centerOfMass - (array)
            ... (more elements)
        heightOfGround - (float)
        jerseyNumber - (str)
        jointIds - (array)
            ... (more elements)
        positions - (array)
            ... (more elements)
        roleId - (int)
        skeletonType - (str)
        teamId - (int)
        trackId - (int)
        ... (more elements)
    roles - (array)
        name - (str)
        ... (more elements)
    skeletons - (object)
        COCO - (object)
            connections - (array)
                ... (more elements)
    teams - (array)
        name - (str)
        ... (more elements)
time - (int)
version - (int)
