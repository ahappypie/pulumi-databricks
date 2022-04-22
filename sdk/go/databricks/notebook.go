// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Import
//
// The resource notebook can be imported using notebook path bash
//
// ```sh
//  $ pulumi import databricks:index/notebook:Notebook this /path/to/notebook
// ```
type Notebook struct {
	pulumi.CustomResourceState

	ContentBase64 pulumi.StringPtrOutput `pulumi:"contentBase64"`
	Format        pulumi.StringPtrOutput `pulumi:"format"`
	// One of `SCALA`, `PYTHON`, `SQL`, `R`.
	Language pulumi.StringPtrOutput `pulumi:"language"`
	Md5      pulumi.StringPtrOutput `pulumi:"md5"`
	// Unique identifier for a NOTEBOOK
	//
	// Deprecated: Use id argument to retrieve object id
	ObjectId pulumi.IntOutput `pulumi:"objectId"`
	// Deprecated: Always is a notebook
	ObjectType pulumi.StringOutput `pulumi:"objectType"`
	// The absolute path of the notebook or directory, beginning with "/", e.g. "/Demo".
	Path pulumi.StringOutput `pulumi:"path"`
	// Path to notebook in source code format on local filesystem. Conflicts with `contentBase64`.
	Source pulumi.StringPtrOutput `pulumi:"source"`
	// Routable URL of the notebook
	Url pulumi.StringOutput `pulumi:"url"`
}

// NewNotebook registers a new resource with the given unique name, arguments, and options.
func NewNotebook(ctx *pulumi.Context,
	name string, args *NotebookArgs, opts ...pulumi.ResourceOption) (*Notebook, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Path == nil {
		return nil, errors.New("invalid value for required argument 'Path'")
	}
	var resource Notebook
	err := ctx.RegisterResource("databricks:index/notebook:Notebook", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNotebook gets an existing Notebook resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNotebook(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NotebookState, opts ...pulumi.ResourceOption) (*Notebook, error) {
	var resource Notebook
	err := ctx.ReadResource("databricks:index/notebook:Notebook", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Notebook resources.
type notebookState struct {
	ContentBase64 *string `pulumi:"contentBase64"`
	Format        *string `pulumi:"format"`
	// One of `SCALA`, `PYTHON`, `SQL`, `R`.
	Language *string `pulumi:"language"`
	Md5      *string `pulumi:"md5"`
	// Unique identifier for a NOTEBOOK
	//
	// Deprecated: Use id argument to retrieve object id
	ObjectId *int `pulumi:"objectId"`
	// Deprecated: Always is a notebook
	ObjectType *string `pulumi:"objectType"`
	// The absolute path of the notebook or directory, beginning with "/", e.g. "/Demo".
	Path *string `pulumi:"path"`
	// Path to notebook in source code format on local filesystem. Conflicts with `contentBase64`.
	Source *string `pulumi:"source"`
	// Routable URL of the notebook
	Url *string `pulumi:"url"`
}

type NotebookState struct {
	ContentBase64 pulumi.StringPtrInput
	Format        pulumi.StringPtrInput
	// One of `SCALA`, `PYTHON`, `SQL`, `R`.
	Language pulumi.StringPtrInput
	Md5      pulumi.StringPtrInput
	// Unique identifier for a NOTEBOOK
	//
	// Deprecated: Use id argument to retrieve object id
	ObjectId pulumi.IntPtrInput
	// Deprecated: Always is a notebook
	ObjectType pulumi.StringPtrInput
	// The absolute path of the notebook or directory, beginning with "/", e.g. "/Demo".
	Path pulumi.StringPtrInput
	// Path to notebook in source code format on local filesystem. Conflicts with `contentBase64`.
	Source pulumi.StringPtrInput
	// Routable URL of the notebook
	Url pulumi.StringPtrInput
}

func (NotebookState) ElementType() reflect.Type {
	return reflect.TypeOf((*notebookState)(nil)).Elem()
}

type notebookArgs struct {
	ContentBase64 *string `pulumi:"contentBase64"`
	Format        *string `pulumi:"format"`
	// One of `SCALA`, `PYTHON`, `SQL`, `R`.
	Language *string `pulumi:"language"`
	Md5      *string `pulumi:"md5"`
	// Unique identifier for a NOTEBOOK
	//
	// Deprecated: Use id argument to retrieve object id
	ObjectId *int `pulumi:"objectId"`
	// Deprecated: Always is a notebook
	ObjectType *string `pulumi:"objectType"`
	// The absolute path of the notebook or directory, beginning with "/", e.g. "/Demo".
	Path string `pulumi:"path"`
	// Path to notebook in source code format on local filesystem. Conflicts with `contentBase64`.
	Source *string `pulumi:"source"`
}

// The set of arguments for constructing a Notebook resource.
type NotebookArgs struct {
	ContentBase64 pulumi.StringPtrInput
	Format        pulumi.StringPtrInput
	// One of `SCALA`, `PYTHON`, `SQL`, `R`.
	Language pulumi.StringPtrInput
	Md5      pulumi.StringPtrInput
	// Unique identifier for a NOTEBOOK
	//
	// Deprecated: Use id argument to retrieve object id
	ObjectId pulumi.IntPtrInput
	// Deprecated: Always is a notebook
	ObjectType pulumi.StringPtrInput
	// The absolute path of the notebook or directory, beginning with "/", e.g. "/Demo".
	Path pulumi.StringInput
	// Path to notebook in source code format on local filesystem. Conflicts with `contentBase64`.
	Source pulumi.StringPtrInput
}

func (NotebookArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*notebookArgs)(nil)).Elem()
}

type NotebookInput interface {
	pulumi.Input

	ToNotebookOutput() NotebookOutput
	ToNotebookOutputWithContext(ctx context.Context) NotebookOutput
}

func (*Notebook) ElementType() reflect.Type {
	return reflect.TypeOf((**Notebook)(nil)).Elem()
}

func (i *Notebook) ToNotebookOutput() NotebookOutput {
	return i.ToNotebookOutputWithContext(context.Background())
}

func (i *Notebook) ToNotebookOutputWithContext(ctx context.Context) NotebookOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NotebookOutput)
}

// NotebookArrayInput is an input type that accepts NotebookArray and NotebookArrayOutput values.
// You can construct a concrete instance of `NotebookArrayInput` via:
//
//          NotebookArray{ NotebookArgs{...} }
type NotebookArrayInput interface {
	pulumi.Input

	ToNotebookArrayOutput() NotebookArrayOutput
	ToNotebookArrayOutputWithContext(context.Context) NotebookArrayOutput
}

type NotebookArray []NotebookInput

func (NotebookArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Notebook)(nil)).Elem()
}

func (i NotebookArray) ToNotebookArrayOutput() NotebookArrayOutput {
	return i.ToNotebookArrayOutputWithContext(context.Background())
}

func (i NotebookArray) ToNotebookArrayOutputWithContext(ctx context.Context) NotebookArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NotebookArrayOutput)
}

// NotebookMapInput is an input type that accepts NotebookMap and NotebookMapOutput values.
// You can construct a concrete instance of `NotebookMapInput` via:
//
//          NotebookMap{ "key": NotebookArgs{...} }
type NotebookMapInput interface {
	pulumi.Input

	ToNotebookMapOutput() NotebookMapOutput
	ToNotebookMapOutputWithContext(context.Context) NotebookMapOutput
}

type NotebookMap map[string]NotebookInput

func (NotebookMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Notebook)(nil)).Elem()
}

func (i NotebookMap) ToNotebookMapOutput() NotebookMapOutput {
	return i.ToNotebookMapOutputWithContext(context.Background())
}

func (i NotebookMap) ToNotebookMapOutputWithContext(ctx context.Context) NotebookMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NotebookMapOutput)
}

type NotebookOutput struct{ *pulumi.OutputState }

func (NotebookOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Notebook)(nil)).Elem()
}

func (o NotebookOutput) ToNotebookOutput() NotebookOutput {
	return o
}

func (o NotebookOutput) ToNotebookOutputWithContext(ctx context.Context) NotebookOutput {
	return o
}

type NotebookArrayOutput struct{ *pulumi.OutputState }

func (NotebookArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Notebook)(nil)).Elem()
}

func (o NotebookArrayOutput) ToNotebookArrayOutput() NotebookArrayOutput {
	return o
}

func (o NotebookArrayOutput) ToNotebookArrayOutputWithContext(ctx context.Context) NotebookArrayOutput {
	return o
}

func (o NotebookArrayOutput) Index(i pulumi.IntInput) NotebookOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Notebook {
		return vs[0].([]*Notebook)[vs[1].(int)]
	}).(NotebookOutput)
}

type NotebookMapOutput struct{ *pulumi.OutputState }

func (NotebookMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Notebook)(nil)).Elem()
}

func (o NotebookMapOutput) ToNotebookMapOutput() NotebookMapOutput {
	return o
}

func (o NotebookMapOutput) ToNotebookMapOutputWithContext(ctx context.Context) NotebookMapOutput {
	return o
}

func (o NotebookMapOutput) MapIndex(k pulumi.StringInput) NotebookOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Notebook {
		return vs[0].(map[string]*Notebook)[vs[1].(string)]
	}).(NotebookOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NotebookInput)(nil)).Elem(), &Notebook{})
	pulumi.RegisterInputType(reflect.TypeOf((*NotebookArrayInput)(nil)).Elem(), NotebookArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*NotebookMapInput)(nil)).Elem(), NotebookMap{})
	pulumi.RegisterOutputType(NotebookOutput{})
	pulumi.RegisterOutputType(NotebookArrayOutput{})
	pulumi.RegisterOutputType(NotebookMapOutput{})
}
