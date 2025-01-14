# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AzureAdlsGen1MountArgs', 'AzureAdlsGen1Mount']

@pulumi.input_type
class AzureAdlsGen1MountArgs:
    def __init__(__self__, *,
                 client_id: pulumi.Input[str],
                 client_secret_key: pulumi.Input[str],
                 client_secret_scope: pulumi.Input[str],
                 mount_name: pulumi.Input[str],
                 storage_resource_name: pulumi.Input[str],
                 tenant_id: pulumi.Input[str],
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 directory: Optional[pulumi.Input[str]] = None,
                 spark_conf_prefix: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AzureAdlsGen1Mount resource.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "client_secret_key", client_secret_key)
        pulumi.set(__self__, "client_secret_scope", client_secret_scope)
        pulumi.set(__self__, "mount_name", mount_name)
        pulumi.set(__self__, "storage_resource_name", storage_resource_name)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if directory is not None:
            pulumi.set(__self__, "directory", directory)
        if spark_conf_prefix is not None:
            pulumi.set(__self__, "spark_conf_prefix", spark_conf_prefix)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientSecretKey")
    def client_secret_key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "client_secret_key")

    @client_secret_key.setter
    def client_secret_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_secret_key", value)

    @property
    @pulumi.getter(name="clientSecretScope")
    def client_secret_scope(self) -> pulumi.Input[str]:
        return pulumi.get(self, "client_secret_scope")

    @client_secret_scope.setter
    def client_secret_scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_secret_scope", value)

    @property
    @pulumi.getter(name="mountName")
    def mount_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "mount_name")

    @mount_name.setter
    def mount_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "mount_name", value)

    @property
    @pulumi.getter(name="storageResourceName")
    def storage_resource_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "storage_resource_name")

    @storage_resource_name.setter
    def storage_resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_resource_name", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def directory(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "directory")

    @directory.setter
    def directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory", value)

    @property
    @pulumi.getter(name="sparkConfPrefix")
    def spark_conf_prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "spark_conf_prefix")

    @spark_conf_prefix.setter
    def spark_conf_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spark_conf_prefix", value)


@pulumi.input_type
class _AzureAdlsGen1MountState:
    def __init__(__self__, *,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret_key: Optional[pulumi.Input[str]] = None,
                 client_secret_scope: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 directory: Optional[pulumi.Input[str]] = None,
                 mount_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 spark_conf_prefix: Optional[pulumi.Input[str]] = None,
                 storage_resource_name: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AzureAdlsGen1Mount resources.
        """
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if client_secret_key is not None:
            pulumi.set(__self__, "client_secret_key", client_secret_key)
        if client_secret_scope is not None:
            pulumi.set(__self__, "client_secret_scope", client_secret_scope)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if directory is not None:
            pulumi.set(__self__, "directory", directory)
        if mount_name is not None:
            pulumi.set(__self__, "mount_name", mount_name)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if spark_conf_prefix is not None:
            pulumi.set(__self__, "spark_conf_prefix", spark_conf_prefix)
        if storage_resource_name is not None:
            pulumi.set(__self__, "storage_resource_name", storage_resource_name)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientSecretKey")
    def client_secret_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "client_secret_key")

    @client_secret_key.setter
    def client_secret_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_secret_key", value)

    @property
    @pulumi.getter(name="clientSecretScope")
    def client_secret_scope(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "client_secret_scope")

    @client_secret_scope.setter
    def client_secret_scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_secret_scope", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def directory(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "directory")

    @directory.setter
    def directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory", value)

    @property
    @pulumi.getter(name="mountName")
    def mount_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "mount_name")

    @mount_name.setter
    def mount_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mount_name", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="sparkConfPrefix")
    def spark_conf_prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "spark_conf_prefix")

    @spark_conf_prefix.setter
    def spark_conf_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spark_conf_prefix", value)

    @property
    @pulumi.getter(name="storageResourceName")
    def storage_resource_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "storage_resource_name")

    @storage_resource_name.setter
    def storage_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_resource_name", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


class AzureAdlsGen1Mount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret_key: Optional[pulumi.Input[str]] = None,
                 client_secret_scope: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 directory: Optional[pulumi.Input[str]] = None,
                 mount_name: Optional[pulumi.Input[str]] = None,
                 spark_conf_prefix: Optional[pulumi.Input[str]] = None,
                 storage_resource_name: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a AzureAdlsGen1Mount resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AzureAdlsGen1MountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AzureAdlsGen1Mount resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AzureAdlsGen1MountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AzureAdlsGen1MountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret_key: Optional[pulumi.Input[str]] = None,
                 client_secret_scope: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 directory: Optional[pulumi.Input[str]] = None,
                 mount_name: Optional[pulumi.Input[str]] = None,
                 spark_conf_prefix: Optional[pulumi.Input[str]] = None,
                 storage_resource_name: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = AzureAdlsGen1MountArgs.__new__(AzureAdlsGen1MountArgs)

            if client_id is None and not opts.urn:
                raise TypeError("Missing required property 'client_id'")
            __props__.__dict__["client_id"] = client_id
            if client_secret_key is None and not opts.urn:
                raise TypeError("Missing required property 'client_secret_key'")
            __props__.__dict__["client_secret_key"] = client_secret_key
            if client_secret_scope is None and not opts.urn:
                raise TypeError("Missing required property 'client_secret_scope'")
            __props__.__dict__["client_secret_scope"] = client_secret_scope
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["directory"] = directory
            if mount_name is None and not opts.urn:
                raise TypeError("Missing required property 'mount_name'")
            __props__.__dict__["mount_name"] = mount_name
            __props__.__dict__["spark_conf_prefix"] = spark_conf_prefix
            if storage_resource_name is None and not opts.urn:
                raise TypeError("Missing required property 'storage_resource_name'")
            __props__.__dict__["storage_resource_name"] = storage_resource_name
            if tenant_id is None and not opts.urn:
                raise TypeError("Missing required property 'tenant_id'")
            __props__.__dict__["tenant_id"] = tenant_id
            __props__.__dict__["source"] = None
        super(AzureAdlsGen1Mount, __self__).__init__(
            'databricks:index/azureAdlsGen1Mount:AzureAdlsGen1Mount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            client_id: Optional[pulumi.Input[str]] = None,
            client_secret_key: Optional[pulumi.Input[str]] = None,
            client_secret_scope: Optional[pulumi.Input[str]] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            directory: Optional[pulumi.Input[str]] = None,
            mount_name: Optional[pulumi.Input[str]] = None,
            source: Optional[pulumi.Input[str]] = None,
            spark_conf_prefix: Optional[pulumi.Input[str]] = None,
            storage_resource_name: Optional[pulumi.Input[str]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None) -> 'AzureAdlsGen1Mount':
        """
        Get an existing AzureAdlsGen1Mount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AzureAdlsGen1MountState.__new__(_AzureAdlsGen1MountState)

        __props__.__dict__["client_id"] = client_id
        __props__.__dict__["client_secret_key"] = client_secret_key
        __props__.__dict__["client_secret_scope"] = client_secret_scope
        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["directory"] = directory
        __props__.__dict__["mount_name"] = mount_name
        __props__.__dict__["source"] = source
        __props__.__dict__["spark_conf_prefix"] = spark_conf_prefix
        __props__.__dict__["storage_resource_name"] = storage_resource_name
        __props__.__dict__["tenant_id"] = tenant_id
        return AzureAdlsGen1Mount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecretKey")
    def client_secret_key(self) -> pulumi.Output[str]:
        return pulumi.get(self, "client_secret_key")

    @property
    @pulumi.getter(name="clientSecretScope")
    def client_secret_scope(self) -> pulumi.Output[str]:
        return pulumi.get(self, "client_secret_scope")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def directory(self) -> pulumi.Output[str]:
        return pulumi.get(self, "directory")

    @property
    @pulumi.getter(name="mountName")
    def mount_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "mount_name")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[str]:
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="sparkConfPrefix")
    def spark_conf_prefix(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "spark_conf_prefix")

    @property
    @pulumi.getter(name="storageResourceName")
    def storage_resource_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "storage_resource_name")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "tenant_id")

