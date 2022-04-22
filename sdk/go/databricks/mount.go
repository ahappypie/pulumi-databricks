// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Import
//
// -> **Note** Importing this resource is not currently supported.
type Mount struct {
	pulumi.CustomResourceState

	Abfs           MountAbfsPtrOutput     `pulumi:"abfs"`
	Adl            MountAdlPtrOutput      `pulumi:"adl"`
	ClusterId      pulumi.StringOutput    `pulumi:"clusterId"`
	EncryptionType pulumi.StringPtrOutput `pulumi:"encryptionType"`
	ExtraConfigs   pulumi.MapOutput       `pulumi:"extraConfigs"`
	Gs             MountGsPtrOutput       `pulumi:"gs"`
	Name           pulumi.StringOutput    `pulumi:"name"`
	ResourceId     pulumi.StringPtrOutput `pulumi:"resourceId"`
	S3             MountS3PtrOutput       `pulumi:"s3"`
	// (String) HDFS-compatible url
	Source pulumi.StringOutput    `pulumi:"source"`
	Uri    pulumi.StringPtrOutput `pulumi:"uri"`
	Wasb   MountWasbPtrOutput     `pulumi:"wasb"`
}

// NewMount registers a new resource with the given unique name, arguments, and options.
func NewMount(ctx *pulumi.Context,
	name string, args *MountArgs, opts ...pulumi.ResourceOption) (*Mount, error) {
	if args == nil {
		args = &MountArgs{}
	}

	var resource Mount
	err := ctx.RegisterResource("databricks:index/mount:Mount", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMount gets an existing Mount resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMount(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MountState, opts ...pulumi.ResourceOption) (*Mount, error) {
	var resource Mount
	err := ctx.ReadResource("databricks:index/mount:Mount", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Mount resources.
type mountState struct {
	Abfs           *MountAbfs             `pulumi:"abfs"`
	Adl            *MountAdl              `pulumi:"adl"`
	ClusterId      *string                `pulumi:"clusterId"`
	EncryptionType *string                `pulumi:"encryptionType"`
	ExtraConfigs   map[string]interface{} `pulumi:"extraConfigs"`
	Gs             *MountGs               `pulumi:"gs"`
	Name           *string                `pulumi:"name"`
	ResourceId     *string                `pulumi:"resourceId"`
	S3             *MountS3               `pulumi:"s3"`
	// (String) HDFS-compatible url
	Source *string    `pulumi:"source"`
	Uri    *string    `pulumi:"uri"`
	Wasb   *MountWasb `pulumi:"wasb"`
}

type MountState struct {
	Abfs           MountAbfsPtrInput
	Adl            MountAdlPtrInput
	ClusterId      pulumi.StringPtrInput
	EncryptionType pulumi.StringPtrInput
	ExtraConfigs   pulumi.MapInput
	Gs             MountGsPtrInput
	Name           pulumi.StringPtrInput
	ResourceId     pulumi.StringPtrInput
	S3             MountS3PtrInput
	// (String) HDFS-compatible url
	Source pulumi.StringPtrInput
	Uri    pulumi.StringPtrInput
	Wasb   MountWasbPtrInput
}

func (MountState) ElementType() reflect.Type {
	return reflect.TypeOf((*mountState)(nil)).Elem()
}

type mountArgs struct {
	Abfs           *MountAbfs             `pulumi:"abfs"`
	Adl            *MountAdl              `pulumi:"adl"`
	ClusterId      *string                `pulumi:"clusterId"`
	EncryptionType *string                `pulumi:"encryptionType"`
	ExtraConfigs   map[string]interface{} `pulumi:"extraConfigs"`
	Gs             *MountGs               `pulumi:"gs"`
	Name           *string                `pulumi:"name"`
	ResourceId     *string                `pulumi:"resourceId"`
	S3             *MountS3               `pulumi:"s3"`
	Uri            *string                `pulumi:"uri"`
	Wasb           *MountWasb             `pulumi:"wasb"`
}

// The set of arguments for constructing a Mount resource.
type MountArgs struct {
	Abfs           MountAbfsPtrInput
	Adl            MountAdlPtrInput
	ClusterId      pulumi.StringPtrInput
	EncryptionType pulumi.StringPtrInput
	ExtraConfigs   pulumi.MapInput
	Gs             MountGsPtrInput
	Name           pulumi.StringPtrInput
	ResourceId     pulumi.StringPtrInput
	S3             MountS3PtrInput
	Uri            pulumi.StringPtrInput
	Wasb           MountWasbPtrInput
}

func (MountArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*mountArgs)(nil)).Elem()
}

type MountInput interface {
	pulumi.Input

	ToMountOutput() MountOutput
	ToMountOutputWithContext(ctx context.Context) MountOutput
}

func (*Mount) ElementType() reflect.Type {
	return reflect.TypeOf((**Mount)(nil)).Elem()
}

func (i *Mount) ToMountOutput() MountOutput {
	return i.ToMountOutputWithContext(context.Background())
}

func (i *Mount) ToMountOutputWithContext(ctx context.Context) MountOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MountOutput)
}

// MountArrayInput is an input type that accepts MountArray and MountArrayOutput values.
// You can construct a concrete instance of `MountArrayInput` via:
//
//          MountArray{ MountArgs{...} }
type MountArrayInput interface {
	pulumi.Input

	ToMountArrayOutput() MountArrayOutput
	ToMountArrayOutputWithContext(context.Context) MountArrayOutput
}

type MountArray []MountInput

func (MountArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Mount)(nil)).Elem()
}

func (i MountArray) ToMountArrayOutput() MountArrayOutput {
	return i.ToMountArrayOutputWithContext(context.Background())
}

func (i MountArray) ToMountArrayOutputWithContext(ctx context.Context) MountArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MountArrayOutput)
}

// MountMapInput is an input type that accepts MountMap and MountMapOutput values.
// You can construct a concrete instance of `MountMapInput` via:
//
//          MountMap{ "key": MountArgs{...} }
type MountMapInput interface {
	pulumi.Input

	ToMountMapOutput() MountMapOutput
	ToMountMapOutputWithContext(context.Context) MountMapOutput
}

type MountMap map[string]MountInput

func (MountMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Mount)(nil)).Elem()
}

func (i MountMap) ToMountMapOutput() MountMapOutput {
	return i.ToMountMapOutputWithContext(context.Background())
}

func (i MountMap) ToMountMapOutputWithContext(ctx context.Context) MountMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MountMapOutput)
}

type MountOutput struct{ *pulumi.OutputState }

func (MountOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Mount)(nil)).Elem()
}

func (o MountOutput) ToMountOutput() MountOutput {
	return o
}

func (o MountOutput) ToMountOutputWithContext(ctx context.Context) MountOutput {
	return o
}

type MountArrayOutput struct{ *pulumi.OutputState }

func (MountArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Mount)(nil)).Elem()
}

func (o MountArrayOutput) ToMountArrayOutput() MountArrayOutput {
	return o
}

func (o MountArrayOutput) ToMountArrayOutputWithContext(ctx context.Context) MountArrayOutput {
	return o
}

func (o MountArrayOutput) Index(i pulumi.IntInput) MountOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Mount {
		return vs[0].([]*Mount)[vs[1].(int)]
	}).(MountOutput)
}

type MountMapOutput struct{ *pulumi.OutputState }

func (MountMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Mount)(nil)).Elem()
}

func (o MountMapOutput) ToMountMapOutput() MountMapOutput {
	return o
}

func (o MountMapOutput) ToMountMapOutputWithContext(ctx context.Context) MountMapOutput {
	return o
}

func (o MountMapOutput) MapIndex(k pulumi.StringInput) MountOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Mount {
		return vs[0].(map[string]*Mount)[vs[1].(string)]
	}).(MountOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*MountInput)(nil)).Elem(), &Mount{})
	pulumi.RegisterInputType(reflect.TypeOf((*MountArrayInput)(nil)).Elem(), MountArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*MountMapInput)(nil)).Elem(), MountMap{})
	pulumi.RegisterOutputType(MountOutput{})
	pulumi.RegisterOutputType(MountArrayOutput{})
	pulumi.RegisterOutputType(MountMapOutput{})
}
