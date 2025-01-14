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

__all__ = ['MwsNetworksArgs', 'MwsNetworks']

@pulumi.input_type
class MwsNetworksArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 network_name: pulumi.Input[str],
                 security_group_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 subnet_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 vpc_id: pulumi.Input[str],
                 creation_time: Optional[pulumi.Input[int]] = None,
                 error_messages: Optional[pulumi.Input[Sequence[pulumi.Input['MwsNetworksErrorMessageArgs']]]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 vpc_endpoints: Optional[pulumi.Input['MwsNetworksVpcEndpointsArgs']] = None,
                 vpc_status: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a MwsNetworks resource.
        :param pulumi.Input[str] account_id: Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
        :param pulumi.Input[str] network_name: name under which this network is regisstered
        :param pulumi.Input[str] network_id: (String) id of network to be used for databricks_mws_workspace resource.
        :param pulumi.Input['MwsNetworksVpcEndpointsArgs'] vpc_endpoints: mapping of MwsVpcEndpoint for PrivateLink connections
        :param pulumi.Input[str] vpc_status: (String) VPC attachment status
        :param pulumi.Input[int] workspace_id: (Integer) id of associated workspace
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "network_name", network_name)
        pulumi.set(__self__, "security_group_ids", security_group_ids)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "vpc_id", vpc_id)
        if creation_time is not None:
            pulumi.set(__self__, "creation_time", creation_time)
        if error_messages is not None:
            pulumi.set(__self__, "error_messages", error_messages)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if vpc_endpoints is not None:
            pulumi.set(__self__, "vpc_endpoints", vpc_endpoints)
        if vpc_status is not None:
            pulumi.set(__self__, "vpc_status", vpc_status)
        if workspace_id is not None:
            pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="networkName")
    def network_name(self) -> pulumi.Input[str]:
        """
        name under which this network is regisstered
        """
        return pulumi.get(self, "network_name")

    @network_name.setter
    def network_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_name", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "creation_time")

    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "creation_time", value)

    @property
    @pulumi.getter(name="errorMessages")
    def error_messages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MwsNetworksErrorMessageArgs']]]]:
        return pulumi.get(self, "error_messages")

    @error_messages.setter
    def error_messages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MwsNetworksErrorMessageArgs']]]]):
        pulumi.set(self, "error_messages", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[str]]:
        """
        (String) id of network to be used for databricks_mws_workspace resource.
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="vpcEndpoints")
    def vpc_endpoints(self) -> Optional[pulumi.Input['MwsNetworksVpcEndpointsArgs']]:
        """
        mapping of MwsVpcEndpoint for PrivateLink connections
        """
        return pulumi.get(self, "vpc_endpoints")

    @vpc_endpoints.setter
    def vpc_endpoints(self, value: Optional[pulumi.Input['MwsNetworksVpcEndpointsArgs']]):
        pulumi.set(self, "vpc_endpoints", value)

    @property
    @pulumi.getter(name="vpcStatus")
    def vpc_status(self) -> Optional[pulumi.Input[str]]:
        """
        (String) VPC attachment status
        """
        return pulumi.get(self, "vpc_status")

    @vpc_status.setter
    def vpc_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_status", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[int]]:
        """
        (Integer) id of associated workspace
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "workspace_id", value)


@pulumi.input_type
class _MwsNetworksState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 creation_time: Optional[pulumi.Input[int]] = None,
                 error_messages: Optional[pulumi.Input[Sequence[pulumi.Input['MwsNetworksErrorMessageArgs']]]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 network_name: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpc_endpoints: Optional[pulumi.Input['MwsNetworksVpcEndpointsArgs']] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 vpc_status: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering MwsNetworks resources.
        :param pulumi.Input[str] account_id: Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
        :param pulumi.Input[str] network_id: (String) id of network to be used for databricks_mws_workspace resource.
        :param pulumi.Input[str] network_name: name under which this network is regisstered
        :param pulumi.Input['MwsNetworksVpcEndpointsArgs'] vpc_endpoints: mapping of MwsVpcEndpoint for PrivateLink connections
        :param pulumi.Input[str] vpc_status: (String) VPC attachment status
        :param pulumi.Input[int] workspace_id: (Integer) id of associated workspace
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if creation_time is not None:
            pulumi.set(__self__, "creation_time", creation_time)
        if error_messages is not None:
            pulumi.set(__self__, "error_messages", error_messages)
        if network_id is not None:
            pulumi.set(__self__, "network_id", network_id)
        if network_name is not None:
            pulumi.set(__self__, "network_name", network_name)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if subnet_ids is not None:
            pulumi.set(__self__, "subnet_ids", subnet_ids)
        if vpc_endpoints is not None:
            pulumi.set(__self__, "vpc_endpoints", vpc_endpoints)
        if vpc_id is not None:
            pulumi.set(__self__, "vpc_id", vpc_id)
        if vpc_status is not None:
            pulumi.set(__self__, "vpc_status", vpc_status)
        if workspace_id is not None:
            pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "creation_time")

    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "creation_time", value)

    @property
    @pulumi.getter(name="errorMessages")
    def error_messages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MwsNetworksErrorMessageArgs']]]]:
        return pulumi.get(self, "error_messages")

    @error_messages.setter
    def error_messages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MwsNetworksErrorMessageArgs']]]]):
        pulumi.set(self, "error_messages", value)

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[pulumi.Input[str]]:
        """
        (String) id of network to be used for databricks_mws_workspace resource.
        """
        return pulumi.get(self, "network_id")

    @network_id.setter
    def network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_id", value)

    @property
    @pulumi.getter(name="networkName")
    def network_name(self) -> Optional[pulumi.Input[str]]:
        """
        name under which this network is regisstered
        """
        return pulumi.get(self, "network_name")

    @network_name.setter
    def network_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_name", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "subnet_ids")

    @subnet_ids.setter
    def subnet_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subnet_ids", value)

    @property
    @pulumi.getter(name="vpcEndpoints")
    def vpc_endpoints(self) -> Optional[pulumi.Input['MwsNetworksVpcEndpointsArgs']]:
        """
        mapping of MwsVpcEndpoint for PrivateLink connections
        """
        return pulumi.get(self, "vpc_endpoints")

    @vpc_endpoints.setter
    def vpc_endpoints(self, value: Optional[pulumi.Input['MwsNetworksVpcEndpointsArgs']]):
        pulumi.set(self, "vpc_endpoints", value)

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "vpc_id")

    @vpc_id.setter
    def vpc_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_id", value)

    @property
    @pulumi.getter(name="vpcStatus")
    def vpc_status(self) -> Optional[pulumi.Input[str]]:
        """
        (String) VPC attachment status
        """
        return pulumi.get(self, "vpc_status")

    @vpc_status.setter
    def vpc_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vpc_status", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[int]]:
        """
        (Integer) id of associated workspace
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "workspace_id", value)


class MwsNetworks(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 creation_time: Optional[pulumi.Input[int]] = None,
                 error_messages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MwsNetworksErrorMessageArgs']]]]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 network_name: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpc_endpoints: Optional[pulumi.Input[pulumi.InputType['MwsNetworksVpcEndpointsArgs']]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 vpc_status: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        ## Import

        -> **Note** Importing this resource is not currently supported.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
        :param pulumi.Input[str] network_id: (String) id of network to be used for databricks_mws_workspace resource.
        :param pulumi.Input[str] network_name: name under which this network is regisstered
        :param pulumi.Input[pulumi.InputType['MwsNetworksVpcEndpointsArgs']] vpc_endpoints: mapping of MwsVpcEndpoint for PrivateLink connections
        :param pulumi.Input[str] vpc_status: (String) VPC attachment status
        :param pulumi.Input[int] workspace_id: (Integer) id of associated workspace
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MwsNetworksArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        -> **Note** Importing this resource is not currently supported.

        :param str resource_name: The name of the resource.
        :param MwsNetworksArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MwsNetworksArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 creation_time: Optional[pulumi.Input[int]] = None,
                 error_messages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MwsNetworksErrorMessageArgs']]]]] = None,
                 network_id: Optional[pulumi.Input[str]] = None,
                 network_name: Optional[pulumi.Input[str]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 vpc_endpoints: Optional[pulumi.Input[pulumi.InputType['MwsNetworksVpcEndpointsArgs']]] = None,
                 vpc_id: Optional[pulumi.Input[str]] = None,
                 vpc_status: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[int]] = None,
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
            __props__ = MwsNetworksArgs.__new__(MwsNetworksArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["creation_time"] = creation_time
            __props__.__dict__["error_messages"] = error_messages
            __props__.__dict__["network_id"] = network_id
            if network_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_name'")
            __props__.__dict__["network_name"] = network_name
            if security_group_ids is None and not opts.urn:
                raise TypeError("Missing required property 'security_group_ids'")
            __props__.__dict__["security_group_ids"] = security_group_ids
            if subnet_ids is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_ids'")
            __props__.__dict__["subnet_ids"] = subnet_ids
            __props__.__dict__["vpc_endpoints"] = vpc_endpoints
            if vpc_id is None and not opts.urn:
                raise TypeError("Missing required property 'vpc_id'")
            __props__.__dict__["vpc_id"] = vpc_id
            __props__.__dict__["vpc_status"] = vpc_status
            __props__.__dict__["workspace_id"] = workspace_id
        super(MwsNetworks, __self__).__init__(
            'databricks:index/mwsNetworks:MwsNetworks',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            creation_time: Optional[pulumi.Input[int]] = None,
            error_messages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MwsNetworksErrorMessageArgs']]]]] = None,
            network_id: Optional[pulumi.Input[str]] = None,
            network_name: Optional[pulumi.Input[str]] = None,
            security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            subnet_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            vpc_endpoints: Optional[pulumi.Input[pulumi.InputType['MwsNetworksVpcEndpointsArgs']]] = None,
            vpc_id: Optional[pulumi.Input[str]] = None,
            vpc_status: Optional[pulumi.Input[str]] = None,
            workspace_id: Optional[pulumi.Input[int]] = None) -> 'MwsNetworks':
        """
        Get an existing MwsNetworks resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
        :param pulumi.Input[str] network_id: (String) id of network to be used for databricks_mws_workspace resource.
        :param pulumi.Input[str] network_name: name under which this network is regisstered
        :param pulumi.Input[pulumi.InputType['MwsNetworksVpcEndpointsArgs']] vpc_endpoints: mapping of MwsVpcEndpoint for PrivateLink connections
        :param pulumi.Input[str] vpc_status: (String) VPC attachment status
        :param pulumi.Input[int] workspace_id: (Integer) id of associated workspace
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MwsNetworksState.__new__(_MwsNetworksState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["creation_time"] = creation_time
        __props__.__dict__["error_messages"] = error_messages
        __props__.__dict__["network_id"] = network_id
        __props__.__dict__["network_name"] = network_name
        __props__.__dict__["security_group_ids"] = security_group_ids
        __props__.__dict__["subnet_ids"] = subnet_ids
        __props__.__dict__["vpc_endpoints"] = vpc_endpoints
        __props__.__dict__["vpc_id"] = vpc_id
        __props__.__dict__["vpc_status"] = vpc_status
        __props__.__dict__["workspace_id"] = workspace_id
        return MwsNetworks(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[int]:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="errorMessages")
    def error_messages(self) -> pulumi.Output[Sequence['outputs.MwsNetworksErrorMessage']]:
        return pulumi.get(self, "error_messages")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[str]:
        """
        (String) id of network to be used for databricks_mws_workspace resource.
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="networkName")
    def network_name(self) -> pulumi.Output[str]:
        """
        name under which this network is regisstered
        """
        return pulumi.get(self, "network_name")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="vpcEndpoints")
    def vpc_endpoints(self) -> pulumi.Output['outputs.MwsNetworksVpcEndpoints']:
        """
        mapping of MwsVpcEndpoint for PrivateLink connections
        """
        return pulumi.get(self, "vpc_endpoints")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vpcStatus")
    def vpc_status(self) -> pulumi.Output[str]:
        """
        (String) VPC attachment status
        """
        return pulumi.get(self, "vpc_status")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[int]:
        """
        (Integer) id of associated workspace
        """
        return pulumi.get(self, "workspace_id")

