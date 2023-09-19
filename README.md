# pyRSFedit

Scripts to edit RSF files for NCAA Football 14. These were initially made to attempt to import Blender .OBJ files in place of existing facemask models.

The main script is `obj2hex.py`. This converts the Blender .OBJ output format into a format that is compatible with the NCAA Football 14 .RSF filetype.

In order to use this script the following must be true:

<ul>
<li>The Blender .OBJ file must be exported with `triangulate faces` enabled.</li>
<li>The files from this project must be inside their own folder i.e. `/pyRSFedit/`.</li>
<li>Within the above folder, create another folder named `input`. Place the Blender .OBJ file inside.</li>
</ul>

Run the script by simply running `python3 obj2hex.py` or running it via GUI.

After the script completes, you will see the counts of vertices and faces (triangles) in the terminal. Note these as they can be used to find the corresponding mesh in an OBJ viewer such as Model Researcher Pro.

The `/output/` folder that is created will be numbered based on the most recently existing folder. Open this and you will find two files:

<ul>
<li>strm out.txt</li>
<li>indx out.txt</li>
</ul>

The contents of each can be copied and pasted into the .RSF hex file in place of the existing STRM and INDX you'd like to replace.

# RSF Formatting

The RSF file contains .OBJ Vertex Buffers as `STRM` and .OBJ Face Indices as `INDX`. The vertex buffers (VBs) detail the vertices for each model. The face indices detail the triangles formed by connecting sets of 3 vertices. The full mapping is TBD, but for the most part each STRM segment has its own INDX.

## STRM 
Each STRM includes a header. The header starts with `53 54 52 4D` (`STRM`) which makes it convenient to find each STRM segment. The full general format is as follows:

| STRM Identifier | Filler bytes | # of Vertex Buffers in STRM | Filler Bytes| Length of VB in STRM | Filler bytes |
|-|-|-|-|-|-|
|`STRM`||#4 byte uint||2 byte uint|
|`53 54 52 4D`| `00 00 00 00 00 00 00` | `12 34`| `00 00 00` | `18` | `00 00 00 00`| 

The full header from above would look like

`53 54 52 4D 00 00 00 00 00 00 00 12 34 00 00 00 18 00 00 00 00`

and would detail 4660 vertex buffers, each with a length of 24*2 = 48 bytes.

## Vertex Buffers
The vertex buffers are comprised of different lengths of bytes based on the subject:


#### General Use

#### Helmet Models

#### Facemask Models 
Facemasks do not seem to have UV vertices associated with them.

### VB Format

Each vertex buffer starts with 3 groups of 2 signed shorts corresponding to a vertex point - X Y and Z. The format of these took a bit to figure out. The higher of each short pair is the integer place, and the lower is the decimal place. The integer place reads 0 to 255 and the decimal place reads 0 to 1 in fractions of 256.

Example:

`00 B9 3A 1E FC 9C` = `0.72265 58.1172 ` 

The vertices are read in order as they appear in the STRM file, indexing starts at 0. This is worth noting as the Blender .OBJ output starts at 1. This is accounted for in the script.

## INDX
Each INDX includes a header. The rest of the INDX segment is a stream of data that describes the triangles that make up the .OBJ.

Each triangle consists of 3 groups of 2 shorts (12 bytes in total), each group corresponds to a vertex ID.

Example:

`00 00 00 01 00 03` = Triangle between vertices 0, 1, 3

