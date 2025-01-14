# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetGroupResult',
    'AwaitableGetGroupResult',
    'get_group',
    'get_group_output',
]

@pulumi.output_type
class GetGroupResult:
    """
    A collection of values returned by getGroup.
    """
    def __init__(__self__, allow_cluster_create=None, allow_instance_pool_create=None, child_groups=None, databricks_sql_access=None, display_name=None, external_id=None, groups=None, id=None, instance_profiles=None, members=None, recursive=None, service_principals=None, users=None, workspace_access=None):
        if allow_cluster_create and not isinstance(allow_cluster_create, bool):
            raise TypeError("Expected argument 'allow_cluster_create' to be a bool")
        pulumi.set(__self__, "allow_cluster_create", allow_cluster_create)
        if allow_instance_pool_create and not isinstance(allow_instance_pool_create, bool):
            raise TypeError("Expected argument 'allow_instance_pool_create' to be a bool")
        pulumi.set(__self__, "allow_instance_pool_create", allow_instance_pool_create)
        if child_groups and not isinstance(child_groups, list):
            raise TypeError("Expected argument 'child_groups' to be a list")
        pulumi.set(__self__, "child_groups", child_groups)
        if databricks_sql_access and not isinstance(databricks_sql_access, bool):
            raise TypeError("Expected argument 'databricks_sql_access' to be a bool")
        pulumi.set(__self__, "databricks_sql_access", databricks_sql_access)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if external_id and not isinstance(external_id, str):
            raise TypeError("Expected argument 'external_id' to be a str")
        pulumi.set(__self__, "external_id", external_id)
        if groups and not isinstance(groups, list):
            raise TypeError("Expected argument 'groups' to be a list")
        pulumi.set(__self__, "groups", groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_profiles and not isinstance(instance_profiles, list):
            raise TypeError("Expected argument 'instance_profiles' to be a list")
        pulumi.set(__self__, "instance_profiles", instance_profiles)
        if members and not isinstance(members, list):
            raise TypeError("Expected argument 'members' to be a list")
        if members is not None:
            warnings.warn("""Please use `users`, `service_principals`, and `child_groups` instead""", DeprecationWarning)
            pulumi.log.warn("""members is deprecated: Please use `users`, `service_principals`, and `child_groups` instead""")

        pulumi.set(__self__, "members", members)
        if recursive and not isinstance(recursive, bool):
            raise TypeError("Expected argument 'recursive' to be a bool")
        pulumi.set(__self__, "recursive", recursive)
        if service_principals and not isinstance(service_principals, list):
            raise TypeError("Expected argument 'service_principals' to be a list")
        pulumi.set(__self__, "service_principals", service_principals)
        if users and not isinstance(users, list):
            raise TypeError("Expected argument 'users' to be a list")
        pulumi.set(__self__, "users", users)
        if workspace_access and not isinstance(workspace_access, bool):
            raise TypeError("Expected argument 'workspace_access' to be a bool")
        pulumi.set(__self__, "workspace_access", workspace_access)

    @property
    @pulumi.getter(name="allowClusterCreate")
    def allow_cluster_create(self) -> Optional[bool]:
        """
        True if group members can create clusters
        """
        return pulumi.get(self, "allow_cluster_create")

    @property
    @pulumi.getter(name="allowInstancePoolCreate")
    def allow_instance_pool_create(self) -> Optional[bool]:
        """
        True if group members can create instance pools
        """
        return pulumi.get(self, "allow_instance_pool_create")

    @property
    @pulumi.getter(name="childGroups")
    def child_groups(self) -> Sequence[str]:
        """
        Set of Group identifiers, that can be modified with databricks_group_member resource.
        """
        return pulumi.get(self, "child_groups")

    @property
    @pulumi.getter(name="databricksSqlAccess")
    def databricks_sql_access(self) -> Optional[bool]:
        return pulumi.get(self, "databricks_sql_access")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> str:
        """
        ID of the group in an external identity provider.
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter
    def groups(self) -> Sequence[str]:
        """
        Set of group identifiers, that can be modified with databricks_group_member resource.
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceProfiles")
    def instance_profiles(self) -> Sequence[str]:
        """
        Set of instance profile ARNs, that can be modified by GroupInstanceProfile resource.
        """
        return pulumi.get(self, "instance_profiles")

    @property
    @pulumi.getter
    def members(self) -> Sequence[str]:
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def recursive(self) -> Optional[bool]:
        return pulumi.get(self, "recursive")

    @property
    @pulumi.getter(name="servicePrincipals")
    def service_principals(self) -> Sequence[str]:
        """
        Set of ServicePrincipal identifiers, that can be modified with databricks_group_member resource.
        """
        return pulumi.get(self, "service_principals")

    @property
    @pulumi.getter
    def users(self) -> Sequence[str]:
        """
        Set of User identifiers, that can be modified with databricks_group_member resource.
        """
        return pulumi.get(self, "users")

    @property
    @pulumi.getter(name="workspaceAccess")
    def workspace_access(self) -> Optional[bool]:
        return pulumi.get(self, "workspace_access")


class AwaitableGetGroupResult(GetGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupResult(
            allow_cluster_create=self.allow_cluster_create,
            allow_instance_pool_create=self.allow_instance_pool_create,
            child_groups=self.child_groups,
            databricks_sql_access=self.databricks_sql_access,
            display_name=self.display_name,
            external_id=self.external_id,
            groups=self.groups,
            id=self.id,
            instance_profiles=self.instance_profiles,
            members=self.members,
            recursive=self.recursive,
            service_principals=self.service_principals,
            users=self.users,
            workspace_access=self.workspace_access)


def get_group(allow_cluster_create: Optional[bool] = None,
              allow_instance_pool_create: Optional[bool] = None,
              child_groups: Optional[Sequence[str]] = None,
              databricks_sql_access: Optional[bool] = None,
              display_name: Optional[str] = None,
              external_id: Optional[str] = None,
              groups: Optional[Sequence[str]] = None,
              instance_profiles: Optional[Sequence[str]] = None,
              members: Optional[Sequence[str]] = None,
              recursive: Optional[bool] = None,
              service_principals: Optional[Sequence[str]] = None,
              users: Optional[Sequence[str]] = None,
              workspace_access: Optional[bool] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGroupResult:
    """
    ## Related Resources

    The following resources are used in the same context:

    * End to end workspace management guide
    * Cluster to create [Databricks Clusters](https://docs.databricks.com/clusters/index.html).
    * Directory to manage directories in [Databricks Workpace](https://docs.databricks.com/workspace/workspace-objects.html).
    * databricks_group_member to attach users and groups as group members.
    * Permissions to manage [access control](https://docs.databricks.com/security/access-control/index.html) in Databricks workspace.
    * User to [manage users](https://docs.databricks.com/administration-guide/users-groups/users.html), that could be added to Group within the workspace.


    :param bool allow_cluster_create: True if group members can create clusters
    :param bool allow_instance_pool_create: True if group members can create instance pools
    :param Sequence[str] child_groups: Set of Group identifiers, that can be modified with databricks_group_member resource.
    :param str display_name: Display name of the group. The group must exist before this resource can be planned.
    :param str external_id: ID of the group in an external identity provider.
    :param Sequence[str] groups: Set of group identifiers, that can be modified with databricks_group_member resource.
    :param Sequence[str] instance_profiles: Set of instance profile ARNs, that can be modified by GroupInstanceProfile resource.
    :param bool recursive: Collect information for all nested groups. *Defaults to true.*
    :param Sequence[str] service_principals: Set of ServicePrincipal identifiers, that can be modified with databricks_group_member resource.
    :param Sequence[str] users: Set of User identifiers, that can be modified with databricks_group_member resource.
    """
    __args__ = dict()
    __args__['allowClusterCreate'] = allow_cluster_create
    __args__['allowInstancePoolCreate'] = allow_instance_pool_create
    __args__['childGroups'] = child_groups
    __args__['databricksSqlAccess'] = databricks_sql_access
    __args__['displayName'] = display_name
    __args__['externalId'] = external_id
    __args__['groups'] = groups
    __args__['instanceProfiles'] = instance_profiles
    __args__['members'] = members
    __args__['recursive'] = recursive
    __args__['servicePrincipals'] = service_principals
    __args__['users'] = users
    __args__['workspaceAccess'] = workspace_access
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('databricks:index/getGroup:getGroup', __args__, opts=opts, typ=GetGroupResult).value

    return AwaitableGetGroupResult(
        allow_cluster_create=__ret__.allow_cluster_create,
        allow_instance_pool_create=__ret__.allow_instance_pool_create,
        child_groups=__ret__.child_groups,
        databricks_sql_access=__ret__.databricks_sql_access,
        display_name=__ret__.display_name,
        external_id=__ret__.external_id,
        groups=__ret__.groups,
        id=__ret__.id,
        instance_profiles=__ret__.instance_profiles,
        members=__ret__.members,
        recursive=__ret__.recursive,
        service_principals=__ret__.service_principals,
        users=__ret__.users,
        workspace_access=__ret__.workspace_access)


@_utilities.lift_output_func(get_group)
def get_group_output(allow_cluster_create: Optional[pulumi.Input[Optional[bool]]] = None,
                     allow_instance_pool_create: Optional[pulumi.Input[Optional[bool]]] = None,
                     child_groups: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                     databricks_sql_access: Optional[pulumi.Input[Optional[bool]]] = None,
                     display_name: Optional[pulumi.Input[str]] = None,
                     external_id: Optional[pulumi.Input[Optional[str]]] = None,
                     groups: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                     instance_profiles: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                     members: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                     recursive: Optional[pulumi.Input[Optional[bool]]] = None,
                     service_principals: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                     users: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                     workspace_access: Optional[pulumi.Input[Optional[bool]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGroupResult]:
    """
    ## Related Resources

    The following resources are used in the same context:

    * End to end workspace management guide
    * Cluster to create [Databricks Clusters](https://docs.databricks.com/clusters/index.html).
    * Directory to manage directories in [Databricks Workpace](https://docs.databricks.com/workspace/workspace-objects.html).
    * databricks_group_member to attach users and groups as group members.
    * Permissions to manage [access control](https://docs.databricks.com/security/access-control/index.html) in Databricks workspace.
    * User to [manage users](https://docs.databricks.com/administration-guide/users-groups/users.html), that could be added to Group within the workspace.


    :param bool allow_cluster_create: True if group members can create clusters
    :param bool allow_instance_pool_create: True if group members can create instance pools
    :param Sequence[str] child_groups: Set of Group identifiers, that can be modified with databricks_group_member resource.
    :param str display_name: Display name of the group. The group must exist before this resource can be planned.
    :param str external_id: ID of the group in an external identity provider.
    :param Sequence[str] groups: Set of group identifiers, that can be modified with databricks_group_member resource.
    :param Sequence[str] instance_profiles: Set of instance profile ARNs, that can be modified by GroupInstanceProfile resource.
    :param bool recursive: Collect information for all nested groups. *Defaults to true.*
    :param Sequence[str] service_principals: Set of ServicePrincipal identifiers, that can be modified with databricks_group_member resource.
    :param Sequence[str] users: Set of User identifiers, that can be modified with databricks_group_member resource.
    """
    ...
