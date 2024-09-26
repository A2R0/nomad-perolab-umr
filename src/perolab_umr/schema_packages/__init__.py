from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class NewSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from perolab_umr.schema_packages.schema_package import m_package

        return m_package


schema_package_entry_point = NewSchemaPackageEntryPoint(
    name='NewSchemaPackage',
    description='New schema package entry point configuration.',
)

class PerolabUMRSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from perolab_umr.schema_packages.batch import m_package
        
        return m_package


schema_package_entry_point = PerolabUMRSchemaPackageEntryPoint(
    name='Perolab UMR Schemas',
    description='Schema package for PeroLab Marburg - Schema package entry point configuration.',
)
