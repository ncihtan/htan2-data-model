# MultiplexMicroscopy - Level 2

HTAN Multiplex Microscopy Level 2 - Imaging data with channel metadata

**Multiplex Microscopy Level 2 - Imaging data compiled into a single file format (preferably tiled and pyramidal OME-TIFF), accompanied by a CSV file containing channel metadata**

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CHANNEL_METADATA_ID` | string, pattern: <code>^syn\d+$</code> | Yes | Unique identifier specifying the location of the required channel metadata (Synapse ID) |
| `FILE_FORMAT` | string, pattern: <code>^(ome-tiff\|tiff\|qptiff\|svs)$</code> | Yes | Format of the imaging file. Must be compatible with Bio-Formats or OpenSlide Python. |
| `IMAGING_ASSAY_TYPE` | [ImagingAssayType](#imagingassaytype) | Yes | Type of imaging assay |
| `PHYSICAL_SIZE_X` | float | Yes | Physical size of a single pixel in the x dimension. In microns. |
| `PHYSICAL_SIZE_Y` | float | Yes | Physical size of a single pixel in the y dimension. In microns. |
| `PHYSICAL_SIZE_Z` | float | Yes | Physical size of a single pixel in the z dimension. In microns. |
| `PYRAMID` | boolean | No | The data file contains an image pyramid |
| `SIZE_C` | integer | Yes | Number of channels. Integer >= 1 |
| `SIZE_T` | integer | Yes | Number of timepoints. Integer >= 1 |
| `SIZE_X` | integer | Yes | The number of pixels in the x dimension at the highest resolution available |
| `SIZE_Y` | integer | Yes | The number of pixels in the y dimension at the highest resolution available |
| `SIZE_Z` | integer | Yes | The number of pixels in the z dimension at the highest resolution available |
| `WORKING_DISTANCE` | string | No | The working distance of the lens, expressed as a floating point number. Floating point > 0. Size needs to be specified in microns (um) |

