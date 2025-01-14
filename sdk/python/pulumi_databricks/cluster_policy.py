# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ClusterPolicyArgs', 'ClusterPolicy']

@pulumi.input_type
class ClusterPolicyArgs:
    def __init__(__self__, *,
                 definition: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ClusterPolicy resource.
        :param pulumi.Input[str] definition: Policy definition JSON document expressed in [Databricks Policy Definition Language](https://docs.databricks.com/administration-guide/clusters/policies.html#cluster-policy-definition).
        :param pulumi.Input[str] name: Cluster policy name. This must be unique. Length must be between 1 and 100 characters.
        """
        if definition is not None:
            pulumi.set(__self__, "definition", definition)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def definition(self) -> Optional[pulumi.Input[str]]:
        """
        Policy definition JSON document expressed in [Databricks Policy Definition Language](https://docs.databricks.com/administration-guide/clusters/policies.html#cluster-policy-definition).
        """
        return pulumi.get(self, "definition")

    @definition.setter
    def definition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "definition", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Cluster policy name. This must be unique. Length must be between 1 and 100 characters.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ClusterPolicyState:
    def __init__(__self__, *,
                 definition: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ClusterPolicy resources.
        :param pulumi.Input[str] definition: Policy definition JSON document expressed in [Databricks Policy Definition Language](https://docs.databricks.com/administration-guide/clusters/policies.html#cluster-policy-definition).
        :param pulumi.Input[str] name: Cluster policy name. This must be unique. Length must be between 1 and 100 characters.
        :param pulumi.Input[str] policy_id: Canonical unique identifier for the cluster policy.
        """
        if definition is not None:
            pulumi.set(__self__, "definition", definition)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)

    @property
    @pulumi.getter
    def definition(self) -> Optional[pulumi.Input[str]]:
        """
        Policy definition JSON document expressed in [Databricks Policy Definition Language](https://docs.databricks.com/administration-guide/clusters/policies.html#cluster-policy-definition).
        """
        return pulumi.get(self, "definition")

    @definition.setter
    def definition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "definition", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Cluster policy name. This must be unique. Length must be between 1 and 100 characters.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        Canonical unique identifier for the cluster policy.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_id", value)


class ClusterPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 definition: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource creates a cluster policy, which limits the ability to create clusters based on a set of rules. The policy rules limit the attributes or attribute values available for cluster creation. cluster policies have ACLs that limit their use to specific users and groups. Only admin users can create, edit, and delete policies. Admin users also have access to all policies.

        Cluster policies let you:

        * Limit users to create clusters with prescribed settings.
        * Simplify the user interface and enable more users to create their own clusters (by fixing and hiding some values).
        * Control cost by limiting per cluster maximum cost (by setting limits on attributes whose values contribute to hourly price).

        Cluster policy permissions limit which policies a user can select in the Policy drop-down when the user creates a cluster:

        * If no policies have been created in the workspace, the Policy drop-down does not display.
        * A user who has cluster create permission can select the `Free form` policy and create fully-configurable clusters.
        * A user who has both cluster create permission and access to cluster policies can select the Free form policy and policies they have access to.
        * A user that has access to only cluster policies, can select the policies they have access to.

        ## Related Resources

        The following resources are often used in the same context:

        * Dynamic Passthrough Clusters for a Group guide
        * End to end workspace management guide
        * get_clusters data to retrieve a list of Cluster ids.
        * Cluster to create [Databricks Clusters](https://docs.databricks.com/clusters/index.html).
        * get_current_user data to retrieve information about User or databricks_service_principal, that is calling Databricks REST API.
        * GlobalInitScript to manage [global init scripts](https://docs.databricks.com/clusters/init-scripts.html#global-init-scripts), which are run on all Cluster and databricks_job.
        * InstancePool to manage [instance pools](https://docs.databricks.com/clusters/instance-pools/index.html) to reduce cluster start and auto-scaling times by maintaining a set of idle, ready-to-use instances.
        * InstanceProfile to manage AWS EC2 instance profiles that users can launch Cluster and access data, like databricks_mount.
        * IpAccessList to allow access from [predefined IP ranges](https://docs.databricks.com/security/network/ip-access-list.html).
        * Library to install a [library](https://docs.databricks.com/libraries/index.html) on databricks_cluster.
        * get_node_type data to get the smallest node type for Cluster that fits search criteria, like amount of RAM or number of cores.
        * Permissions to manage [access control](https://docs.databricks.com/security/access-control/index.html) in Databricks workspace.
        * get_spark_version data to get [Databricks Runtime (DBR)](https://docs.databricks.com/runtime/dbr.html) version that could be used for `spark_version` parameter in Cluster and other resources.
        * UserInstanceProfile to attach InstanceProfile (AWS) to databricks_user.
        * WorkspaceConf to manage workspace configuration for expert usage.

        ## Import

        The resource cluster policy can be imported using the policy idbash

        ```sh
         $ pulumi import databricks:index/clusterPolicy:ClusterPolicy this <cluster-policy-id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] definition: Policy definition JSON document expressed in [Databricks Policy Definition Language](https://docs.databricks.com/administration-guide/clusters/policies.html#cluster-policy-definition).
        :param pulumi.Input[str] name: Cluster policy name. This must be unique. Length must be between 1 and 100 characters.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ClusterPolicyArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource creates a cluster policy, which limits the ability to create clusters based on a set of rules. The policy rules limit the attributes or attribute values available for cluster creation. cluster policies have ACLs that limit their use to specific users and groups. Only admin users can create, edit, and delete policies. Admin users also have access to all policies.

        Cluster policies let you:

        * Limit users to create clusters with prescribed settings.
        * Simplify the user interface and enable more users to create their own clusters (by fixing and hiding some values).
        * Control cost by limiting per cluster maximum cost (by setting limits on attributes whose values contribute to hourly price).

        Cluster policy permissions limit which policies a user can select in the Policy drop-down when the user creates a cluster:

        * If no policies have been created in the workspace, the Policy drop-down does not display.
        * A user who has cluster create permission can select the `Free form` policy and create fully-configurable clusters.
        * A user who has both cluster create permission and access to cluster policies can select the Free form policy and policies they have access to.
        * A user that has access to only cluster policies, can select the policies they have access to.

        ## Related Resources

        The following resources are often used in the same context:

        * Dynamic Passthrough Clusters for a Group guide
        * End to end workspace management guide
        * get_clusters data to retrieve a list of Cluster ids.
        * Cluster to create [Databricks Clusters](https://docs.databricks.com/clusters/index.html).
        * get_current_user data to retrieve information about User or databricks_service_principal, that is calling Databricks REST API.
        * GlobalInitScript to manage [global init scripts](https://docs.databricks.com/clusters/init-scripts.html#global-init-scripts), which are run on all Cluster and databricks_job.
        * InstancePool to manage [instance pools](https://docs.databricks.com/clusters/instance-pools/index.html) to reduce cluster start and auto-scaling times by maintaining a set of idle, ready-to-use instances.
        * InstanceProfile to manage AWS EC2 instance profiles that users can launch Cluster and access data, like databricks_mount.
        * IpAccessList to allow access from [predefined IP ranges](https://docs.databricks.com/security/network/ip-access-list.html).
        * Library to install a [library](https://docs.databricks.com/libraries/index.html) on databricks_cluster.
        * get_node_type data to get the smallest node type for Cluster that fits search criteria, like amount of RAM or number of cores.
        * Permissions to manage [access control](https://docs.databricks.com/security/access-control/index.html) in Databricks workspace.
        * get_spark_version data to get [Databricks Runtime (DBR)](https://docs.databricks.com/runtime/dbr.html) version that could be used for `spark_version` parameter in Cluster and other resources.
        * UserInstanceProfile to attach InstanceProfile (AWS) to databricks_user.
        * WorkspaceConf to manage workspace configuration for expert usage.

        ## Import

        The resource cluster policy can be imported using the policy idbash

        ```sh
         $ pulumi import databricks:index/clusterPolicy:ClusterPolicy this <cluster-policy-id>
        ```

        :param str resource_name: The name of the resource.
        :param ClusterPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 definition: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ClusterPolicyArgs.__new__(ClusterPolicyArgs)

            __props__.__dict__["definition"] = definition
            __props__.__dict__["name"] = name
            __props__.__dict__["policy_id"] = None
        super(ClusterPolicy, __self__).__init__(
            'databricks:index/clusterPolicy:ClusterPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            definition: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            policy_id: Optional[pulumi.Input[str]] = None) -> 'ClusterPolicy':
        """
        Get an existing ClusterPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] definition: Policy definition JSON document expressed in [Databricks Policy Definition Language](https://docs.databricks.com/administration-guide/clusters/policies.html#cluster-policy-definition).
        :param pulumi.Input[str] name: Cluster policy name. This must be unique. Length must be between 1 and 100 characters.
        :param pulumi.Input[str] policy_id: Canonical unique identifier for the cluster policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ClusterPolicyState.__new__(_ClusterPolicyState)

        __props__.__dict__["definition"] = definition
        __props__.__dict__["name"] = name
        __props__.__dict__["policy_id"] = policy_id
        return ClusterPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def definition(self) -> pulumi.Output[Optional[str]]:
        """
        Policy definition JSON document expressed in [Databricks Policy Definition Language](https://docs.databricks.com/administration-guide/clusters/policies.html#cluster-policy-definition).
        """
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Cluster policy name. This must be unique. Length must be between 1 and 100 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> pulumi.Output[str]:
        """
        Canonical unique identifier for the cluster policy.
        """
        return pulumi.get(self, "policy_id")

