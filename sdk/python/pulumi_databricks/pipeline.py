# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['PipelineArgs', 'Pipeline']

@pulumi.input_type
class PipelineArgs:
    def __init__(__self__, *,
                 filters: pulumi.Input['PipelineFiltersArgs'],
                 allow_duplicate_names: Optional[pulumi.Input[bool]] = None,
                 clusters: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineClusterArgs']]]] = None,
                 configuration: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 continuous: Optional[pulumi.Input[bool]] = None,
                 libraries: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineLibraryArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Pipeline resource.
        :param pulumi.Input[Sequence[pulumi.Input['PipelineClusterArgs']]] clusters: blocks - Clusters to run the pipeline. If none is specified, pipelines will automatically select a default cluster configuration for the pipeline.
        :param pulumi.Input[Mapping[str, Any]] configuration: An optional list of values to apply to the entire pipeline. Elements must be formatted as key:value pairs.
        :param pulumi.Input[bool] continuous: A flag indicating whether to run the pipeline continuously. The default value is `false`.
        :param pulumi.Input[Sequence[pulumi.Input['PipelineLibraryArgs']]] libraries: blocks - Specifies pipeline code and required artifacts. Syntax resembles library configuration block with the addition of a special `notebook` type of library that should have `path` attribute.
        :param pulumi.Input[str] name: A user-friendly name for this pipeline. The name can be used to identify pipeline jobs in the UI.
        :param pulumi.Input[str] storage: A location on DBFS or cloud storage where output data and metadata required for pipeline execution are stored. By default, tables are stored in a subdirectory of this location.
        :param pulumi.Input[str] target: The name of a database for persisting pipeline output data. Configuring the target setting allows you to view and query the pipeline output data from the Databricks UI.
        """
        pulumi.set(__self__, "filters", filters)
        if allow_duplicate_names is not None:
            pulumi.set(__self__, "allow_duplicate_names", allow_duplicate_names)
        if clusters is not None:
            pulumi.set(__self__, "clusters", clusters)
        if configuration is not None:
            pulumi.set(__self__, "configuration", configuration)
        if continuous is not None:
            pulumi.set(__self__, "continuous", continuous)
        if libraries is not None:
            pulumi.set(__self__, "libraries", libraries)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if storage is not None:
            pulumi.set(__self__, "storage", storage)
        if target is not None:
            pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Input['PipelineFiltersArgs']:
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: pulumi.Input['PipelineFiltersArgs']):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter(name="allowDuplicateNames")
    def allow_duplicate_names(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_duplicate_names")

    @allow_duplicate_names.setter
    def allow_duplicate_names(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_duplicate_names", value)

    @property
    @pulumi.getter
    def clusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineClusterArgs']]]]:
        """
        blocks - Clusters to run the pipeline. If none is specified, pipelines will automatically select a default cluster configuration for the pipeline.
        """
        return pulumi.get(self, "clusters")

    @clusters.setter
    def clusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineClusterArgs']]]]):
        pulumi.set(self, "clusters", value)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        An optional list of values to apply to the entire pipeline. Elements must be formatted as key:value pairs.
        """
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter
    def continuous(self) -> Optional[pulumi.Input[bool]]:
        """
        A flag indicating whether to run the pipeline continuously. The default value is `false`.
        """
        return pulumi.get(self, "continuous")

    @continuous.setter
    def continuous(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "continuous", value)

    @property
    @pulumi.getter
    def libraries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineLibraryArgs']]]]:
        """
        blocks - Specifies pipeline code and required artifacts. Syntax resembles library configuration block with the addition of a special `notebook` type of library that should have `path` attribute.
        """
        return pulumi.get(self, "libraries")

    @libraries.setter
    def libraries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineLibraryArgs']]]]):
        pulumi.set(self, "libraries", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-friendly name for this pipeline. The name can be used to identify pipeline jobs in the UI.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[str]]:
        """
        A location on DBFS or cloud storage where output data and metadata required for pipeline execution are stored. By default, tables are stored in a subdirectory of this location.
        """
        return pulumi.get(self, "storage")

    @storage.setter
    def storage(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        """
        The name of a database for persisting pipeline output data. Configuring the target setting allows you to view and query the pipeline output data from the Databricks UI.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)


@pulumi.input_type
class _PipelineState:
    def __init__(__self__, *,
                 allow_duplicate_names: Optional[pulumi.Input[bool]] = None,
                 clusters: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineClusterArgs']]]] = None,
                 configuration: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 continuous: Optional[pulumi.Input[bool]] = None,
                 filters: Optional[pulumi.Input['PipelineFiltersArgs']] = None,
                 libraries: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineLibraryArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Pipeline resources.
        :param pulumi.Input[Sequence[pulumi.Input['PipelineClusterArgs']]] clusters: blocks - Clusters to run the pipeline. If none is specified, pipelines will automatically select a default cluster configuration for the pipeline.
        :param pulumi.Input[Mapping[str, Any]] configuration: An optional list of values to apply to the entire pipeline. Elements must be formatted as key:value pairs.
        :param pulumi.Input[bool] continuous: A flag indicating whether to run the pipeline continuously. The default value is `false`.
        :param pulumi.Input[Sequence[pulumi.Input['PipelineLibraryArgs']]] libraries: blocks - Specifies pipeline code and required artifacts. Syntax resembles library configuration block with the addition of a special `notebook` type of library that should have `path` attribute.
        :param pulumi.Input[str] name: A user-friendly name for this pipeline. The name can be used to identify pipeline jobs in the UI.
        :param pulumi.Input[str] storage: A location on DBFS or cloud storage where output data and metadata required for pipeline execution are stored. By default, tables are stored in a subdirectory of this location.
        :param pulumi.Input[str] target: The name of a database for persisting pipeline output data. Configuring the target setting allows you to view and query the pipeline output data from the Databricks UI.
        """
        if allow_duplicate_names is not None:
            pulumi.set(__self__, "allow_duplicate_names", allow_duplicate_names)
        if clusters is not None:
            pulumi.set(__self__, "clusters", clusters)
        if configuration is not None:
            pulumi.set(__self__, "configuration", configuration)
        if continuous is not None:
            pulumi.set(__self__, "continuous", continuous)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if libraries is not None:
            pulumi.set(__self__, "libraries", libraries)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if storage is not None:
            pulumi.set(__self__, "storage", storage)
        if target is not None:
            pulumi.set(__self__, "target", target)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="allowDuplicateNames")
    def allow_duplicate_names(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "allow_duplicate_names")

    @allow_duplicate_names.setter
    def allow_duplicate_names(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_duplicate_names", value)

    @property
    @pulumi.getter
    def clusters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineClusterArgs']]]]:
        """
        blocks - Clusters to run the pipeline. If none is specified, pipelines will automatically select a default cluster configuration for the pipeline.
        """
        return pulumi.get(self, "clusters")

    @clusters.setter
    def clusters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineClusterArgs']]]]):
        pulumi.set(self, "clusters", value)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        An optional list of values to apply to the entire pipeline. Elements must be formatted as key:value pairs.
        """
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter
    def continuous(self) -> Optional[pulumi.Input[bool]]:
        """
        A flag indicating whether to run the pipeline continuously. The default value is `false`.
        """
        return pulumi.get(self, "continuous")

    @continuous.setter
    def continuous(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "continuous", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input['PipelineFiltersArgs']]:
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input['PipelineFiltersArgs']]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter
    def libraries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PipelineLibraryArgs']]]]:
        """
        blocks - Specifies pipeline code and required artifacts. Syntax resembles library configuration block with the addition of a special `notebook` type of library that should have `path` attribute.
        """
        return pulumi.get(self, "libraries")

    @libraries.setter
    def libraries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PipelineLibraryArgs']]]]):
        pulumi.set(self, "libraries", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-friendly name for this pipeline. The name can be used to identify pipeline jobs in the UI.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[str]]:
        """
        A location on DBFS or cloud storage where output data and metadata required for pipeline execution are stored. By default, tables are stored in a subdirectory of this location.
        """
        return pulumi.get(self, "storage")

    @storage.setter
    def storage(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage", value)

    @property
    @pulumi.getter
    def target(self) -> Optional[pulumi.Input[str]]:
        """
        The name of a database for persisting pipeline output data. Configuring the target setting allows you to view and query the pipeline output data from the Databricks UI.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class Pipeline(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_duplicate_names: Optional[pulumi.Input[bool]] = None,
                 clusters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineClusterArgs']]]]] = None,
                 configuration: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 continuous: Optional[pulumi.Input[bool]] = None,
                 filters: Optional[pulumi.Input[pulumi.InputType['PipelineFiltersArgs']]] = None,
                 libraries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineLibraryArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Use `Pipeline` to deploy [Delta Live Tables](https://docs.databricks.com/data-engineering/delta-live-tables/index.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_databricks as databricks

        dlt_demo = databricks.Notebook("dltDemo")
        #...
        this = databricks.Pipeline("this",
            storage="/test/first-pipeline",
            configuration={
                "key1": "value1",
                "key2": "value2",
            },
            clusters=[
                databricks.PipelineClusterArgs(
                    label="default",
                    num_workers=2,
                    custom_tags={
                        "cluster_type": "default",
                    },
                ),
                databricks.PipelineClusterArgs(
                    label="maintenance",
                    num_workers=1,
                    custom_tags={
                        "cluster_type": "maintenance",
                    },
                ),
            ],
            libraries=[databricks.PipelineLibraryArgs(
                notebook=databricks.PipelineLibraryNotebookArgs(
                    path=dlt_demo.id,
                ),
            )],
            filters=databricks.PipelineFiltersArgs(
                includes=["com.databricks.include"],
                excludes=["com.databricks.exclude"],
            ),
            continuous=False)
        ```
        ## Related Resources

        The following resources are often used in the same context:

        * End to end workspace management guide.
        * Cluster to create [Databricks Clusters](https://docs.databricks.com/clusters/index.html).
        * Job to manage [Databricks Jobs](https://docs.databricks.com/jobs.html) to run non-interactive code in a databricks_cluster.
        * Notebook to manage [Databricks Notebooks](https://docs.databricks.com/notebooks/index.html).

        ## Import

        The resource job can be imported using the id of the pipeline bash

        ```sh
         $ pulumi import databricks:index/pipeline:Pipeline this <pipeline-id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineClusterArgs']]]] clusters: blocks - Clusters to run the pipeline. If none is specified, pipelines will automatically select a default cluster configuration for the pipeline.
        :param pulumi.Input[Mapping[str, Any]] configuration: An optional list of values to apply to the entire pipeline. Elements must be formatted as key:value pairs.
        :param pulumi.Input[bool] continuous: A flag indicating whether to run the pipeline continuously. The default value is `false`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineLibraryArgs']]]] libraries: blocks - Specifies pipeline code and required artifacts. Syntax resembles library configuration block with the addition of a special `notebook` type of library that should have `path` attribute.
        :param pulumi.Input[str] name: A user-friendly name for this pipeline. The name can be used to identify pipeline jobs in the UI.
        :param pulumi.Input[str] storage: A location on DBFS or cloud storage where output data and metadata required for pipeline execution are stored. By default, tables are stored in a subdirectory of this location.
        :param pulumi.Input[str] target: The name of a database for persisting pipeline output data. Configuring the target setting allows you to view and query the pipeline output data from the Databricks UI.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PipelineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Use `Pipeline` to deploy [Delta Live Tables](https://docs.databricks.com/data-engineering/delta-live-tables/index.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_databricks as databricks

        dlt_demo = databricks.Notebook("dltDemo")
        #...
        this = databricks.Pipeline("this",
            storage="/test/first-pipeline",
            configuration={
                "key1": "value1",
                "key2": "value2",
            },
            clusters=[
                databricks.PipelineClusterArgs(
                    label="default",
                    num_workers=2,
                    custom_tags={
                        "cluster_type": "default",
                    },
                ),
                databricks.PipelineClusterArgs(
                    label="maintenance",
                    num_workers=1,
                    custom_tags={
                        "cluster_type": "maintenance",
                    },
                ),
            ],
            libraries=[databricks.PipelineLibraryArgs(
                notebook=databricks.PipelineLibraryNotebookArgs(
                    path=dlt_demo.id,
                ),
            )],
            filters=databricks.PipelineFiltersArgs(
                includes=["com.databricks.include"],
                excludes=["com.databricks.exclude"],
            ),
            continuous=False)
        ```
        ## Related Resources

        The following resources are often used in the same context:

        * End to end workspace management guide.
        * Cluster to create [Databricks Clusters](https://docs.databricks.com/clusters/index.html).
        * Job to manage [Databricks Jobs](https://docs.databricks.com/jobs.html) to run non-interactive code in a databricks_cluster.
        * Notebook to manage [Databricks Notebooks](https://docs.databricks.com/notebooks/index.html).

        ## Import

        The resource job can be imported using the id of the pipeline bash

        ```sh
         $ pulumi import databricks:index/pipeline:Pipeline this <pipeline-id>
        ```

        :param str resource_name: The name of the resource.
        :param PipelineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PipelineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_duplicate_names: Optional[pulumi.Input[bool]] = None,
                 clusters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineClusterArgs']]]]] = None,
                 configuration: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 continuous: Optional[pulumi.Input[bool]] = None,
                 filters: Optional[pulumi.Input[pulumi.InputType['PipelineFiltersArgs']]] = None,
                 libraries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineLibraryArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 storage: Optional[pulumi.Input[str]] = None,
                 target: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PipelineArgs.__new__(PipelineArgs)

            __props__.__dict__["allow_duplicate_names"] = allow_duplicate_names
            __props__.__dict__["clusters"] = clusters
            __props__.__dict__["configuration"] = configuration
            __props__.__dict__["continuous"] = continuous
            if filters is None and not opts.urn:
                raise TypeError("Missing required property 'filters'")
            __props__.__dict__["filters"] = filters
            __props__.__dict__["libraries"] = libraries
            __props__.__dict__["name"] = name
            __props__.__dict__["storage"] = storage
            __props__.__dict__["target"] = target
            __props__.__dict__["url"] = None
        super(Pipeline, __self__).__init__(
            'databricks:index/pipeline:Pipeline',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allow_duplicate_names: Optional[pulumi.Input[bool]] = None,
            clusters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineClusterArgs']]]]] = None,
            configuration: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            continuous: Optional[pulumi.Input[bool]] = None,
            filters: Optional[pulumi.Input[pulumi.InputType['PipelineFiltersArgs']]] = None,
            libraries: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineLibraryArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            storage: Optional[pulumi.Input[str]] = None,
            target: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'Pipeline':
        """
        Get an existing Pipeline resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineClusterArgs']]]] clusters: blocks - Clusters to run the pipeline. If none is specified, pipelines will automatically select a default cluster configuration for the pipeline.
        :param pulumi.Input[Mapping[str, Any]] configuration: An optional list of values to apply to the entire pipeline. Elements must be formatted as key:value pairs.
        :param pulumi.Input[bool] continuous: A flag indicating whether to run the pipeline continuously. The default value is `false`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PipelineLibraryArgs']]]] libraries: blocks - Specifies pipeline code and required artifacts. Syntax resembles library configuration block with the addition of a special `notebook` type of library that should have `path` attribute.
        :param pulumi.Input[str] name: A user-friendly name for this pipeline. The name can be used to identify pipeline jobs in the UI.
        :param pulumi.Input[str] storage: A location on DBFS or cloud storage where output data and metadata required for pipeline execution are stored. By default, tables are stored in a subdirectory of this location.
        :param pulumi.Input[str] target: The name of a database for persisting pipeline output data. Configuring the target setting allows you to view and query the pipeline output data from the Databricks UI.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PipelineState.__new__(_PipelineState)

        __props__.__dict__["allow_duplicate_names"] = allow_duplicate_names
        __props__.__dict__["clusters"] = clusters
        __props__.__dict__["configuration"] = configuration
        __props__.__dict__["continuous"] = continuous
        __props__.__dict__["filters"] = filters
        __props__.__dict__["libraries"] = libraries
        __props__.__dict__["name"] = name
        __props__.__dict__["storage"] = storage
        __props__.__dict__["target"] = target
        __props__.__dict__["url"] = url
        return Pipeline(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowDuplicateNames")
    def allow_duplicate_names(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "allow_duplicate_names")

    @property
    @pulumi.getter
    def clusters(self) -> pulumi.Output[Optional[Sequence['outputs.PipelineCluster']]]:
        """
        blocks - Clusters to run the pipeline. If none is specified, pipelines will automatically select a default cluster configuration for the pipeline.
        """
        return pulumi.get(self, "clusters")

    @property
    @pulumi.getter
    def configuration(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        An optional list of values to apply to the entire pipeline. Elements must be formatted as key:value pairs.
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def continuous(self) -> pulumi.Output[Optional[bool]]:
        """
        A flag indicating whether to run the pipeline continuously. The default value is `false`.
        """
        return pulumi.get(self, "continuous")

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Output['outputs.PipelineFilters']:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def libraries(self) -> pulumi.Output[Optional[Sequence['outputs.PipelineLibrary']]]:
        """
        blocks - Specifies pipeline code and required artifacts. Syntax resembles library configuration block with the addition of a special `notebook` type of library that should have `path` attribute.
        """
        return pulumi.get(self, "libraries")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A user-friendly name for this pipeline. The name can be used to identify pipeline jobs in the UI.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def storage(self) -> pulumi.Output[Optional[str]]:
        """
        A location on DBFS or cloud storage where output data and metadata required for pipeline execution are stored. By default, tables are stored in a subdirectory of this location.
        """
        return pulumi.get(self, "storage")

    @property
    @pulumi.getter
    def target(self) -> pulumi.Output[Optional[str]]:
        """
        The name of a database for persisting pipeline output data. Configuring the target setting allows you to view and query the pipeline output data from the Databricks UI.
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        return pulumi.get(self, "url")

