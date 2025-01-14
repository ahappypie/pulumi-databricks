// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Import
//
// -> **Note** Importing this resource is not currently supported.
type MwsNetworks struct {
	pulumi.CustomResourceState

	// Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
	AccountId     pulumi.StringOutput                `pulumi:"accountId"`
	CreationTime  pulumi.IntOutput                   `pulumi:"creationTime"`
	ErrorMessages MwsNetworksErrorMessageArrayOutput `pulumi:"errorMessages"`
	// (String) id of network to be used for databricksMwsWorkspace resource.
	NetworkId pulumi.StringOutput `pulumi:"networkId"`
	// name under which this network is regisstered
	NetworkName      pulumi.StringOutput      `pulumi:"networkName"`
	SecurityGroupIds pulumi.StringArrayOutput `pulumi:"securityGroupIds"`
	SubnetIds        pulumi.StringArrayOutput `pulumi:"subnetIds"`
	// mapping of MwsVpcEndpoint for PrivateLink connections
	VpcEndpoints MwsNetworksVpcEndpointsOutput `pulumi:"vpcEndpoints"`
	VpcId        pulumi.StringOutput           `pulumi:"vpcId"`
	// (String) VPC attachment status
	VpcStatus pulumi.StringOutput `pulumi:"vpcStatus"`
	// (Integer) id of associated workspace
	WorkspaceId pulumi.IntOutput `pulumi:"workspaceId"`
}

// NewMwsNetworks registers a new resource with the given unique name, arguments, and options.
func NewMwsNetworks(ctx *pulumi.Context,
	name string, args *MwsNetworksArgs, opts ...pulumi.ResourceOption) (*MwsNetworks, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AccountId == nil {
		return nil, errors.New("invalid value for required argument 'AccountId'")
	}
	if args.NetworkName == nil {
		return nil, errors.New("invalid value for required argument 'NetworkName'")
	}
	if args.SecurityGroupIds == nil {
		return nil, errors.New("invalid value for required argument 'SecurityGroupIds'")
	}
	if args.SubnetIds == nil {
		return nil, errors.New("invalid value for required argument 'SubnetIds'")
	}
	if args.VpcId == nil {
		return nil, errors.New("invalid value for required argument 'VpcId'")
	}
	var resource MwsNetworks
	err := ctx.RegisterResource("databricks:index/mwsNetworks:MwsNetworks", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMwsNetworks gets an existing MwsNetworks resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMwsNetworks(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MwsNetworksState, opts ...pulumi.ResourceOption) (*MwsNetworks, error) {
	var resource MwsNetworks
	err := ctx.ReadResource("databricks:index/mwsNetworks:MwsNetworks", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering MwsNetworks resources.
type mwsNetworksState struct {
	// Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
	AccountId     *string                   `pulumi:"accountId"`
	CreationTime  *int                      `pulumi:"creationTime"`
	ErrorMessages []MwsNetworksErrorMessage `pulumi:"errorMessages"`
	// (String) id of network to be used for databricksMwsWorkspace resource.
	NetworkId *string `pulumi:"networkId"`
	// name under which this network is regisstered
	NetworkName      *string  `pulumi:"networkName"`
	SecurityGroupIds []string `pulumi:"securityGroupIds"`
	SubnetIds        []string `pulumi:"subnetIds"`
	// mapping of MwsVpcEndpoint for PrivateLink connections
	VpcEndpoints *MwsNetworksVpcEndpoints `pulumi:"vpcEndpoints"`
	VpcId        *string                  `pulumi:"vpcId"`
	// (String) VPC attachment status
	VpcStatus *string `pulumi:"vpcStatus"`
	// (Integer) id of associated workspace
	WorkspaceId *int `pulumi:"workspaceId"`
}

type MwsNetworksState struct {
	// Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
	AccountId     pulumi.StringPtrInput
	CreationTime  pulumi.IntPtrInput
	ErrorMessages MwsNetworksErrorMessageArrayInput
	// (String) id of network to be used for databricksMwsWorkspace resource.
	NetworkId pulumi.StringPtrInput
	// name under which this network is regisstered
	NetworkName      pulumi.StringPtrInput
	SecurityGroupIds pulumi.StringArrayInput
	SubnetIds        pulumi.StringArrayInput
	// mapping of MwsVpcEndpoint for PrivateLink connections
	VpcEndpoints MwsNetworksVpcEndpointsPtrInput
	VpcId        pulumi.StringPtrInput
	// (String) VPC attachment status
	VpcStatus pulumi.StringPtrInput
	// (Integer) id of associated workspace
	WorkspaceId pulumi.IntPtrInput
}

func (MwsNetworksState) ElementType() reflect.Type {
	return reflect.TypeOf((*mwsNetworksState)(nil)).Elem()
}

type mwsNetworksArgs struct {
	// Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
	AccountId     string                    `pulumi:"accountId"`
	CreationTime  *int                      `pulumi:"creationTime"`
	ErrorMessages []MwsNetworksErrorMessage `pulumi:"errorMessages"`
	// (String) id of network to be used for databricksMwsWorkspace resource.
	NetworkId *string `pulumi:"networkId"`
	// name under which this network is regisstered
	NetworkName      string   `pulumi:"networkName"`
	SecurityGroupIds []string `pulumi:"securityGroupIds"`
	SubnetIds        []string `pulumi:"subnetIds"`
	// mapping of MwsVpcEndpoint for PrivateLink connections
	VpcEndpoints *MwsNetworksVpcEndpoints `pulumi:"vpcEndpoints"`
	VpcId        string                   `pulumi:"vpcId"`
	// (String) VPC attachment status
	VpcStatus *string `pulumi:"vpcStatus"`
	// (Integer) id of associated workspace
	WorkspaceId *int `pulumi:"workspaceId"`
}

// The set of arguments for constructing a MwsNetworks resource.
type MwsNetworksArgs struct {
	// Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
	AccountId     pulumi.StringInput
	CreationTime  pulumi.IntPtrInput
	ErrorMessages MwsNetworksErrorMessageArrayInput
	// (String) id of network to be used for databricksMwsWorkspace resource.
	NetworkId pulumi.StringPtrInput
	// name under which this network is regisstered
	NetworkName      pulumi.StringInput
	SecurityGroupIds pulumi.StringArrayInput
	SubnetIds        pulumi.StringArrayInput
	// mapping of MwsVpcEndpoint for PrivateLink connections
	VpcEndpoints MwsNetworksVpcEndpointsPtrInput
	VpcId        pulumi.StringInput
	// (String) VPC attachment status
	VpcStatus pulumi.StringPtrInput
	// (Integer) id of associated workspace
	WorkspaceId pulumi.IntPtrInput
}

func (MwsNetworksArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*mwsNetworksArgs)(nil)).Elem()
}

type MwsNetworksInput interface {
	pulumi.Input

	ToMwsNetworksOutput() MwsNetworksOutput
	ToMwsNetworksOutputWithContext(ctx context.Context) MwsNetworksOutput
}

func (*MwsNetworks) ElementType() reflect.Type {
	return reflect.TypeOf((**MwsNetworks)(nil)).Elem()
}

func (i *MwsNetworks) ToMwsNetworksOutput() MwsNetworksOutput {
	return i.ToMwsNetworksOutputWithContext(context.Background())
}

func (i *MwsNetworks) ToMwsNetworksOutputWithContext(ctx context.Context) MwsNetworksOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MwsNetworksOutput)
}

// MwsNetworksArrayInput is an input type that accepts MwsNetworksArray and MwsNetworksArrayOutput values.
// You can construct a concrete instance of `MwsNetworksArrayInput` via:
//
//          MwsNetworksArray{ MwsNetworksArgs{...} }
type MwsNetworksArrayInput interface {
	pulumi.Input

	ToMwsNetworksArrayOutput() MwsNetworksArrayOutput
	ToMwsNetworksArrayOutputWithContext(context.Context) MwsNetworksArrayOutput
}

type MwsNetworksArray []MwsNetworksInput

func (MwsNetworksArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*MwsNetworks)(nil)).Elem()
}

func (i MwsNetworksArray) ToMwsNetworksArrayOutput() MwsNetworksArrayOutput {
	return i.ToMwsNetworksArrayOutputWithContext(context.Background())
}

func (i MwsNetworksArray) ToMwsNetworksArrayOutputWithContext(ctx context.Context) MwsNetworksArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MwsNetworksArrayOutput)
}

// MwsNetworksMapInput is an input type that accepts MwsNetworksMap and MwsNetworksMapOutput values.
// You can construct a concrete instance of `MwsNetworksMapInput` via:
//
//          MwsNetworksMap{ "key": MwsNetworksArgs{...} }
type MwsNetworksMapInput interface {
	pulumi.Input

	ToMwsNetworksMapOutput() MwsNetworksMapOutput
	ToMwsNetworksMapOutputWithContext(context.Context) MwsNetworksMapOutput
}

type MwsNetworksMap map[string]MwsNetworksInput

func (MwsNetworksMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*MwsNetworks)(nil)).Elem()
}

func (i MwsNetworksMap) ToMwsNetworksMapOutput() MwsNetworksMapOutput {
	return i.ToMwsNetworksMapOutputWithContext(context.Background())
}

func (i MwsNetworksMap) ToMwsNetworksMapOutputWithContext(ctx context.Context) MwsNetworksMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MwsNetworksMapOutput)
}

type MwsNetworksOutput struct{ *pulumi.OutputState }

func (MwsNetworksOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**MwsNetworks)(nil)).Elem()
}

func (o MwsNetworksOutput) ToMwsNetworksOutput() MwsNetworksOutput {
	return o
}

func (o MwsNetworksOutput) ToMwsNetworksOutputWithContext(ctx context.Context) MwsNetworksOutput {
	return o
}

type MwsNetworksArrayOutput struct{ *pulumi.OutputState }

func (MwsNetworksArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*MwsNetworks)(nil)).Elem()
}

func (o MwsNetworksArrayOutput) ToMwsNetworksArrayOutput() MwsNetworksArrayOutput {
	return o
}

func (o MwsNetworksArrayOutput) ToMwsNetworksArrayOutputWithContext(ctx context.Context) MwsNetworksArrayOutput {
	return o
}

func (o MwsNetworksArrayOutput) Index(i pulumi.IntInput) MwsNetworksOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *MwsNetworks {
		return vs[0].([]*MwsNetworks)[vs[1].(int)]
	}).(MwsNetworksOutput)
}

type MwsNetworksMapOutput struct{ *pulumi.OutputState }

func (MwsNetworksMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*MwsNetworks)(nil)).Elem()
}

func (o MwsNetworksMapOutput) ToMwsNetworksMapOutput() MwsNetworksMapOutput {
	return o
}

func (o MwsNetworksMapOutput) ToMwsNetworksMapOutputWithContext(ctx context.Context) MwsNetworksMapOutput {
	return o
}

func (o MwsNetworksMapOutput) MapIndex(k pulumi.StringInput) MwsNetworksOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *MwsNetworks {
		return vs[0].(map[string]*MwsNetworks)[vs[1].(string)]
	}).(MwsNetworksOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*MwsNetworksInput)(nil)).Elem(), &MwsNetworks{})
	pulumi.RegisterInputType(reflect.TypeOf((*MwsNetworksArrayInput)(nil)).Elem(), MwsNetworksArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*MwsNetworksMapInput)(nil)).Elem(), MwsNetworksMap{})
	pulumi.RegisterOutputType(MwsNetworksOutput{})
	pulumi.RegisterOutputType(MwsNetworksArrayOutput{})
	pulumi.RegisterOutputType(MwsNetworksMapOutput{})
}
