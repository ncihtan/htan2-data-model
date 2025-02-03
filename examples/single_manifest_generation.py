from linkml.generators.excelgen import ExcelGenerator
from pathlib import Path

generator = ExcelGenerator(
    "HTAN2Model.yaml",
    split_workbook_by_class=True,
    include_mixins=False,   
    format='xlsx',
    log_level='WARNING'
)

classes = list(generator.schemaview.all_classes().keys())
component = classes[0]

manifest_path = Path(f"examples/data/synapse_storage_manifest_{component}.xlsx")
if not manifest_path.parent.is_dir():
    manifest_path.parent.mkdir(parents=True,exist_ok=True)

generator.create_workbook_and_worksheets(manifest_path, [component])