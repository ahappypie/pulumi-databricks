// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Import
//
// The secret resource scope can be imported using the scope name. `initial_manage_principal` state won't be imported, because the underlying API doesn't include it in the response. bash
//
// ```sh
//  $ pulumi import databricks:index/secretScope:SecretScope object <scopeName>
// ```
type SecretScope struct {
	pulumi.CustomResourceState

	// Either `DATABRICKS` or `AZURE_KEYVAULT`
	BackendType pulumi.StringOutput `pulumi:"backendType"`
	// The principal with the only possible value `users` that is initially granted `MANAGE` permission to the created scope.  If it's omitted, then the SecretAcl with `MANAGE` permission applied to the scope is assigned to the API request issuer's user identity (see [documentation](https://docs.databricks.com/dev-tools/api/latest/secrets.html#create-secret-scope)). This part of the state cannot be imported.
	InitialManagePrincipal pulumi.StringPtrOutput               `pulumi:"initialManagePrincipal"`
	KeyvaultMetadata       SecretScopeKeyvaultMetadataPtrOutput `pulumi:"keyvaultMetadata"`
	// Scope name requested by the user. Must be unique within a workspace. Must consist of alphanumeric characters, dashes, underscores, and periods, and may not exceed 128 characters.
	Name pulumi.StringOutput `pulumi:"name"`
}

// NewSecretScope registers a new resource with the given unique name, arguments, and options.
func NewSecretScope(ctx *pulumi.Context,
	name string, args *SecretScopeArgs, opts ...pulumi.ResourceOption) (*SecretScope, error) {
	if args == nil {
		args = &SecretScopeArgs{}
	}

	var resource SecretScope
	err := ctx.RegisterResource("databricks:index/secretScope:SecretScope", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSecretScope gets an existing SecretScope resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSecretScope(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SecretScopeState, opts ...pulumi.ResourceOption) (*SecretScope, error) {
	var resource SecretScope
	err := ctx.ReadResource("databricks:index/secretScope:SecretScope", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SecretScope resources.
type secretScopeState struct {
	// Either `DATABRICKS` or `AZURE_KEYVAULT`
	BackendType *string `pulumi:"backendType"`
	// The principal with the only possible value `users` that is initially granted `MANAGE` permission to the created scope.  If it's omitted, then the SecretAcl with `MANAGE` permission applied to the scope is assigned to the API request issuer's user identity (see [documentation](https://docs.databricks.com/dev-tools/api/latest/secrets.html#create-secret-scope)). This part of the state cannot be imported.
	InitialManagePrincipal *string                      `pulumi:"initialManagePrincipal"`
	KeyvaultMetadata       *SecretScopeKeyvaultMetadata `pulumi:"keyvaultMetadata"`
	// Scope name requested by the user. Must be unique within a workspace. Must consist of alphanumeric characters, dashes, underscores, and periods, and may not exceed 128 characters.
	Name *string `pulumi:"name"`
}

type SecretScopeState struct {
	// Either `DATABRICKS` or `AZURE_KEYVAULT`
	BackendType pulumi.StringPtrInput
	// The principal with the only possible value `users` that is initially granted `MANAGE` permission to the created scope.  If it's omitted, then the SecretAcl with `MANAGE` permission applied to the scope is assigned to the API request issuer's user identity (see [documentation](https://docs.databricks.com/dev-tools/api/latest/secrets.html#create-secret-scope)). This part of the state cannot be imported.
	InitialManagePrincipal pulumi.StringPtrInput
	KeyvaultMetadata       SecretScopeKeyvaultMetadataPtrInput
	// Scope name requested by the user. Must be unique within a workspace. Must consist of alphanumeric characters, dashes, underscores, and periods, and may not exceed 128 characters.
	Name pulumi.StringPtrInput
}

func (SecretScopeState) ElementType() reflect.Type {
	return reflect.TypeOf((*secretScopeState)(nil)).Elem()
}

type secretScopeArgs struct {
	// Either `DATABRICKS` or `AZURE_KEYVAULT`
	BackendType *string `pulumi:"backendType"`
	// The principal with the only possible value `users` that is initially granted `MANAGE` permission to the created scope.  If it's omitted, then the SecretAcl with `MANAGE` permission applied to the scope is assigned to the API request issuer's user identity (see [documentation](https://docs.databricks.com/dev-tools/api/latest/secrets.html#create-secret-scope)). This part of the state cannot be imported.
	InitialManagePrincipal *string                      `pulumi:"initialManagePrincipal"`
	KeyvaultMetadata       *SecretScopeKeyvaultMetadata `pulumi:"keyvaultMetadata"`
	// Scope name requested by the user. Must be unique within a workspace. Must consist of alphanumeric characters, dashes, underscores, and periods, and may not exceed 128 characters.
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a SecretScope resource.
type SecretScopeArgs struct {
	// Either `DATABRICKS` or `AZURE_KEYVAULT`
	BackendType pulumi.StringPtrInput
	// The principal with the only possible value `users` that is initially granted `MANAGE` permission to the created scope.  If it's omitted, then the SecretAcl with `MANAGE` permission applied to the scope is assigned to the API request issuer's user identity (see [documentation](https://docs.databricks.com/dev-tools/api/latest/secrets.html#create-secret-scope)). This part of the state cannot be imported.
	InitialManagePrincipal pulumi.StringPtrInput
	KeyvaultMetadata       SecretScopeKeyvaultMetadataPtrInput
	// Scope name requested by the user. Must be unique within a workspace. Must consist of alphanumeric characters, dashes, underscores, and periods, and may not exceed 128 characters.
	Name pulumi.StringPtrInput
}

func (SecretScopeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*secretScopeArgs)(nil)).Elem()
}

type SecretScopeInput interface {
	pulumi.Input

	ToSecretScopeOutput() SecretScopeOutput
	ToSecretScopeOutputWithContext(ctx context.Context) SecretScopeOutput
}

func (*SecretScope) ElementType() reflect.Type {
	return reflect.TypeOf((**SecretScope)(nil)).Elem()
}

func (i *SecretScope) ToSecretScopeOutput() SecretScopeOutput {
	return i.ToSecretScopeOutputWithContext(context.Background())
}

func (i *SecretScope) ToSecretScopeOutputWithContext(ctx context.Context) SecretScopeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretScopeOutput)
}

// SecretScopeArrayInput is an input type that accepts SecretScopeArray and SecretScopeArrayOutput values.
// You can construct a concrete instance of `SecretScopeArrayInput` via:
//
//          SecretScopeArray{ SecretScopeArgs{...} }
type SecretScopeArrayInput interface {
	pulumi.Input

	ToSecretScopeArrayOutput() SecretScopeArrayOutput
	ToSecretScopeArrayOutputWithContext(context.Context) SecretScopeArrayOutput
}

type SecretScopeArray []SecretScopeInput

func (SecretScopeArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SecretScope)(nil)).Elem()
}

func (i SecretScopeArray) ToSecretScopeArrayOutput() SecretScopeArrayOutput {
	return i.ToSecretScopeArrayOutputWithContext(context.Background())
}

func (i SecretScopeArray) ToSecretScopeArrayOutputWithContext(ctx context.Context) SecretScopeArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretScopeArrayOutput)
}

// SecretScopeMapInput is an input type that accepts SecretScopeMap and SecretScopeMapOutput values.
// You can construct a concrete instance of `SecretScopeMapInput` via:
//
//          SecretScopeMap{ "key": SecretScopeArgs{...} }
type SecretScopeMapInput interface {
	pulumi.Input

	ToSecretScopeMapOutput() SecretScopeMapOutput
	ToSecretScopeMapOutputWithContext(context.Context) SecretScopeMapOutput
}

type SecretScopeMap map[string]SecretScopeInput

func (SecretScopeMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SecretScope)(nil)).Elem()
}

func (i SecretScopeMap) ToSecretScopeMapOutput() SecretScopeMapOutput {
	return i.ToSecretScopeMapOutputWithContext(context.Background())
}

func (i SecretScopeMap) ToSecretScopeMapOutputWithContext(ctx context.Context) SecretScopeMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecretScopeMapOutput)
}

type SecretScopeOutput struct{ *pulumi.OutputState }

func (SecretScopeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SecretScope)(nil)).Elem()
}

func (o SecretScopeOutput) ToSecretScopeOutput() SecretScopeOutput {
	return o
}

func (o SecretScopeOutput) ToSecretScopeOutputWithContext(ctx context.Context) SecretScopeOutput {
	return o
}

type SecretScopeArrayOutput struct{ *pulumi.OutputState }

func (SecretScopeArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SecretScope)(nil)).Elem()
}

func (o SecretScopeArrayOutput) ToSecretScopeArrayOutput() SecretScopeArrayOutput {
	return o
}

func (o SecretScopeArrayOutput) ToSecretScopeArrayOutputWithContext(ctx context.Context) SecretScopeArrayOutput {
	return o
}

func (o SecretScopeArrayOutput) Index(i pulumi.IntInput) SecretScopeOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *SecretScope {
		return vs[0].([]*SecretScope)[vs[1].(int)]
	}).(SecretScopeOutput)
}

type SecretScopeMapOutput struct{ *pulumi.OutputState }

func (SecretScopeMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SecretScope)(nil)).Elem()
}

func (o SecretScopeMapOutput) ToSecretScopeMapOutput() SecretScopeMapOutput {
	return o
}

func (o SecretScopeMapOutput) ToSecretScopeMapOutputWithContext(ctx context.Context) SecretScopeMapOutput {
	return o
}

func (o SecretScopeMapOutput) MapIndex(k pulumi.StringInput) SecretScopeOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *SecretScope {
		return vs[0].(map[string]*SecretScope)[vs[1].(string)]
	}).(SecretScopeOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SecretScopeInput)(nil)).Elem(), &SecretScope{})
	pulumi.RegisterInputType(reflect.TypeOf((*SecretScopeArrayInput)(nil)).Elem(), SecretScopeArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SecretScopeMapInput)(nil)).Elem(), SecretScopeMap{})
	pulumi.RegisterOutputType(SecretScopeOutput{})
	pulumi.RegisterOutputType(SecretScopeArrayOutput{})
	pulumi.RegisterOutputType(SecretScopeMapOutput{})
}