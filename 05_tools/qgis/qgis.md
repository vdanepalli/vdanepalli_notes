 # QGIS

- GIS : Geographical Information Systems
- qgis -- open-source
- Map projections -- 3d earth to 2d surface
  - cylindrical
  - conical
  - planar
- Geodetic Datum -- known locations used as a reference to develop and link features to the projected surface
- Coordinate Reference System -- series of meridians (vertical) and parallels (horizontal) creating a grid
  - Geographic
  - Projected CRSs
- Vector Data 
  - table data with geometry
  - points, lines, polygons
  - format : ShapeFile, Geodatabase, Geopackage ; FGDB - File Geo DataBase 
- Raster Data
  - continuous data
  - types : single-band, composite, thematic
  - format : GeoTIFF, JPEG2000
  - Extension : .tif, 
- OpenMaps 


<br/><br/>

- Layers Styling -- F7
- Attribute table -- F6
- Open Data Source Manager -- Ctrl L


<br/><br/>

- Be mindful of bad data


## Map Academy : QGIS : Udemy

### Basics

- Layer : Single map layer in qgis 
- geographic data file format
  - ShapeFile -- atleast 3 files
    - .shp
    - .shx
    - .dbf
    - .prj
  - Geopackage  -- sigle file
  - GeoJSON -- web mapping
  - KML -- google maps
  - GeoTIF -- roster format
- CRS : Coordinate Reference System
- Vector : Any layer made up of points, lines, or polygons
- Raster : Any layer made up of little pixels
- Properties
  - Layer
  - Project
    - CRS : Map Projections
    - General : Fill Color or Line Color
- `.qgz` -- project file extension -- just save the configuration and not the layers
- Settings > Options
- Map Area / Canvas
- Menu bar, Tool bar, Status bar
- View > Toggle Full Screen, Toggle Pannel Visibility, Toggle Map Only
- Identify Features `Ctrl Shift I`
- X - Longitude; Y - Latitude; CRS - EPSG 4236 WSG 84
- Plugins
  - HCMGIS
  - MapTiler
  - QuickMapServices
  - QuickOSM
- OSM WMS 
- Features
  - `F6` -- Attribute table
  - 
  - Filter > Query Buildre
  - Labels 
    - Background
      - Buffer, X 2, Y 2, 
    - Placement
  - View 
    - Decorations
      - Title Label
      - Copyright label
  - Project
    - Import/Export


- Topic
  - Can map lat/long from csv to a map
  - Add data from Browser Pannel
  - Shape File -- .shx .shp .dbf  -- .prj projection file
  - If the maps look weird, it must have to do with Coordinate Reference System / Projections / Bad data
  - Attribute table - F6