# MultiplexMicroscopy - Level 3

HTAN Multiplex Microscopy Level 3 - Segmentation masks

**Multiplex Microscopy Level 3 - Segmentation mask. Structured mask data following existing HTAN segmentation templates (RFC Imaging Level 3 & 4 - v1)**

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string, pattern: <code>^(ome-tiff\|ome\.tiff\|tiff\|tif)$</code> | Yes | Format of the segmentation mask file (should be ome-tiff for Level 3) |
| `SEGMENTATION_ANNOTATION_TYPE` | string | No | Type of objects segmented (e.g., Cell, Nucleus, Tissue, ROI) |
| `SEGMENTATION_METHOD` | string | Yes | Method used for segmentation (e.g., CellPose, StarDist, Ilastik, manual annotation) |
| `SEGMENTATION_PARAMETERS` | string | No | Parameters used for segmentation (e.g., model name, threshold values, preprocessing steps) |
| `SEGMENTATION_WORKFLOW_TYPE` | string | Yes | Type of segmentation workflow used to generate the mask |
| `SEGMENTATION_WORKFLOW_URL` | string | No | URL or link to the segmentation workflow used |
| `SEGMENTATION_WORKFLOW_VERSION` | string | No | Version of the segmentation workflow |

