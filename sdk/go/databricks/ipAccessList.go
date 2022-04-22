// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Security-conscious enterprises that use cloud SaaS applications need to restrict access to their own employees. Authentication helps to prove user identity, but that does not enforce network location of the users. Accessing a cloud service from an unsecured network can pose security risks to an enterprise, especially when the user may have authorized access to sensitive or personal data. Enterprise network perimeters apply security policies and limit access to external services (for example, firewalls, proxies, DLP, and logging), so access beyond these controls are assumed to be untrusted. Please see [IP Access List](https://docs.databricks.com/security/network/ip-access-list.html) for full feature documentation.
//
// > **Note** The total number of IP addresses and CIDR scopes provided across all ACL Lists in a workspace can not exceed 1000.  Refer to the docs above for specifics.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-databricks/sdk/go/databricks"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		this, err := databricks.NewWorkspaceConf(ctx, "this", &databricks.WorkspaceConfArgs{
// 			CustomConfig: pulumi.AnyMap{
// 				"enableIpAccessLists": pulumi.Any(true),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = databricks.NewIpAccessList(ctx, "allowed-list", &databricks.IpAccessListArgs{
// 			Label:    pulumi.String("allow_in"),
// 			ListType: pulumi.String("ALLOW"),
// 			IpAddresses: pulumi.StringArray{
// 				pulumi.String("1.2.3.0/24"),
// 				pulumi.String("1.2.5.0/24"),
// 			},
// 		}, pulumi.DependsOn([]pulumi.Resource{
// 			this,
// 		}))
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ## Related Resources
//
// The following resources are often used in the same context:
//
// * End to end workspace management guide.
// * Provisioning AWS Databricks E2 with a Hub & Spoke firewall for data exfiltration protection guide.
// * MwsNetworks to [configure VPC](https://docs.databricks.com/administration-guide/cloud-configurations/aws/customer-managed-vpc.html) & subnets for new workspaces within AWS.
// * MwsPrivateAccessSettings to create a [Private Access Setting](https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html#step-5-create-a-private-access-settings-configuration-using-the-databricks-account-api) that can be used as part of a MwsWorkspaces resource to create a [Databricks Workspace that leverages AWS PrivateLink](https://docs.databricks.com/administration-guide/cloud-configurations/aws/privatelink.html).
// * Permissions to manage [access control](https://docs.databricks.com/security/access-control/index.html) in Databricks workspace.
// * SqlPermissions to manage data object access control lists in Databricks workspaces for things like tables, views, databases, and [more](https://docs.databricks.com/security/access-control/table-acls/object-privileges.html).
//
// ## Import
//
// The databricks_ip_access_list can be imported using idbash
//
// ```sh
//  $ pulumi import databricks:index/ipAccessList:IpAccessList this <list-id>
// ```
type IpAccessList struct {
	pulumi.CustomResourceState

	// Boolean `true` or `false` indicating whether this list should be active.  Defaults to `true`
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
	// This is a field to allow the group to have instance pool create priviliges.
	IpAddresses pulumi.StringArrayOutput `pulumi:"ipAddresses"`
	// This is the display name for the given IP ACL List.
	Label pulumi.StringOutput `pulumi:"label"`
	// Can only be "ALLOW" or "BLOCK"
	ListType pulumi.StringOutput `pulumi:"listType"`
}

// NewIpAccessList registers a new resource with the given unique name, arguments, and options.
func NewIpAccessList(ctx *pulumi.Context,
	name string, args *IpAccessListArgs, opts ...pulumi.ResourceOption) (*IpAccessList, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.IpAddresses == nil {
		return nil, errors.New("invalid value for required argument 'IpAddresses'")
	}
	if args.Label == nil {
		return nil, errors.New("invalid value for required argument 'Label'")
	}
	if args.ListType == nil {
		return nil, errors.New("invalid value for required argument 'ListType'")
	}
	var resource IpAccessList
	err := ctx.RegisterResource("databricks:index/ipAccessList:IpAccessList", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIpAccessList gets an existing IpAccessList resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIpAccessList(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IpAccessListState, opts ...pulumi.ResourceOption) (*IpAccessList, error) {
	var resource IpAccessList
	err := ctx.ReadResource("databricks:index/ipAccessList:IpAccessList", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IpAccessList resources.
type ipAccessListState struct {
	// Boolean `true` or `false` indicating whether this list should be active.  Defaults to `true`
	Enabled *bool `pulumi:"enabled"`
	// This is a field to allow the group to have instance pool create priviliges.
	IpAddresses []string `pulumi:"ipAddresses"`
	// This is the display name for the given IP ACL List.
	Label *string `pulumi:"label"`
	// Can only be "ALLOW" or "BLOCK"
	ListType *string `pulumi:"listType"`
}

type IpAccessListState struct {
	// Boolean `true` or `false` indicating whether this list should be active.  Defaults to `true`
	Enabled pulumi.BoolPtrInput
	// This is a field to allow the group to have instance pool create priviliges.
	IpAddresses pulumi.StringArrayInput
	// This is the display name for the given IP ACL List.
	Label pulumi.StringPtrInput
	// Can only be "ALLOW" or "BLOCK"
	ListType pulumi.StringPtrInput
}

func (IpAccessListState) ElementType() reflect.Type {
	return reflect.TypeOf((*ipAccessListState)(nil)).Elem()
}

type ipAccessListArgs struct {
	// Boolean `true` or `false` indicating whether this list should be active.  Defaults to `true`
	Enabled *bool `pulumi:"enabled"`
	// This is a field to allow the group to have instance pool create priviliges.
	IpAddresses []string `pulumi:"ipAddresses"`
	// This is the display name for the given IP ACL List.
	Label string `pulumi:"label"`
	// Can only be "ALLOW" or "BLOCK"
	ListType string `pulumi:"listType"`
}

// The set of arguments for constructing a IpAccessList resource.
type IpAccessListArgs struct {
	// Boolean `true` or `false` indicating whether this list should be active.  Defaults to `true`
	Enabled pulumi.BoolPtrInput
	// This is a field to allow the group to have instance pool create priviliges.
	IpAddresses pulumi.StringArrayInput
	// This is the display name for the given IP ACL List.
	Label pulumi.StringInput
	// Can only be "ALLOW" or "BLOCK"
	ListType pulumi.StringInput
}

func (IpAccessListArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ipAccessListArgs)(nil)).Elem()
}

type IpAccessListInput interface {
	pulumi.Input

	ToIpAccessListOutput() IpAccessListOutput
	ToIpAccessListOutputWithContext(ctx context.Context) IpAccessListOutput
}

func (*IpAccessList) ElementType() reflect.Type {
	return reflect.TypeOf((**IpAccessList)(nil)).Elem()
}

func (i *IpAccessList) ToIpAccessListOutput() IpAccessListOutput {
	return i.ToIpAccessListOutputWithContext(context.Background())
}

func (i *IpAccessList) ToIpAccessListOutputWithContext(ctx context.Context) IpAccessListOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IpAccessListOutput)
}

// IpAccessListArrayInput is an input type that accepts IpAccessListArray and IpAccessListArrayOutput values.
// You can construct a concrete instance of `IpAccessListArrayInput` via:
//
//          IpAccessListArray{ IpAccessListArgs{...} }
type IpAccessListArrayInput interface {
	pulumi.Input

	ToIpAccessListArrayOutput() IpAccessListArrayOutput
	ToIpAccessListArrayOutputWithContext(context.Context) IpAccessListArrayOutput
}

type IpAccessListArray []IpAccessListInput

func (IpAccessListArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*IpAccessList)(nil)).Elem()
}

func (i IpAccessListArray) ToIpAccessListArrayOutput() IpAccessListArrayOutput {
	return i.ToIpAccessListArrayOutputWithContext(context.Background())
}

func (i IpAccessListArray) ToIpAccessListArrayOutputWithContext(ctx context.Context) IpAccessListArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IpAccessListArrayOutput)
}

// IpAccessListMapInput is an input type that accepts IpAccessListMap and IpAccessListMapOutput values.
// You can construct a concrete instance of `IpAccessListMapInput` via:
//
//          IpAccessListMap{ "key": IpAccessListArgs{...} }
type IpAccessListMapInput interface {
	pulumi.Input

	ToIpAccessListMapOutput() IpAccessListMapOutput
	ToIpAccessListMapOutputWithContext(context.Context) IpAccessListMapOutput
}

type IpAccessListMap map[string]IpAccessListInput

func (IpAccessListMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*IpAccessList)(nil)).Elem()
}

func (i IpAccessListMap) ToIpAccessListMapOutput() IpAccessListMapOutput {
	return i.ToIpAccessListMapOutputWithContext(context.Background())
}

func (i IpAccessListMap) ToIpAccessListMapOutputWithContext(ctx context.Context) IpAccessListMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IpAccessListMapOutput)
}

type IpAccessListOutput struct{ *pulumi.OutputState }

func (IpAccessListOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**IpAccessList)(nil)).Elem()
}

func (o IpAccessListOutput) ToIpAccessListOutput() IpAccessListOutput {
	return o
}

func (o IpAccessListOutput) ToIpAccessListOutputWithContext(ctx context.Context) IpAccessListOutput {
	return o
}

type IpAccessListArrayOutput struct{ *pulumi.OutputState }

func (IpAccessListArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*IpAccessList)(nil)).Elem()
}

func (o IpAccessListArrayOutput) ToIpAccessListArrayOutput() IpAccessListArrayOutput {
	return o
}

func (o IpAccessListArrayOutput) ToIpAccessListArrayOutputWithContext(ctx context.Context) IpAccessListArrayOutput {
	return o
}

func (o IpAccessListArrayOutput) Index(i pulumi.IntInput) IpAccessListOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *IpAccessList {
		return vs[0].([]*IpAccessList)[vs[1].(int)]
	}).(IpAccessListOutput)
}

type IpAccessListMapOutput struct{ *pulumi.OutputState }

func (IpAccessListMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*IpAccessList)(nil)).Elem()
}

func (o IpAccessListMapOutput) ToIpAccessListMapOutput() IpAccessListMapOutput {
	return o
}

func (o IpAccessListMapOutput) ToIpAccessListMapOutputWithContext(ctx context.Context) IpAccessListMapOutput {
	return o
}

func (o IpAccessListMapOutput) MapIndex(k pulumi.StringInput) IpAccessListOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *IpAccessList {
		return vs[0].(map[string]*IpAccessList)[vs[1].(string)]
	}).(IpAccessListOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*IpAccessListInput)(nil)).Elem(), &IpAccessList{})
	pulumi.RegisterInputType(reflect.TypeOf((*IpAccessListArrayInput)(nil)).Elem(), IpAccessListArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*IpAccessListMapInput)(nil)).Elem(), IpAccessListMap{})
	pulumi.RegisterOutputType(IpAccessListOutput{})
	pulumi.RegisterOutputType(IpAccessListArrayOutput{})
	pulumi.RegisterOutputType(IpAccessListMapOutput{})
}
