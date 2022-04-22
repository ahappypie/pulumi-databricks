// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package databricks

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

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
// 		_, err := databricks.GetZones(ctx, nil, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetZones(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetZonesResult, error) {
	var rv GetZonesResult
	err := ctx.Invoke("databricks:index/getZones:getZones", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getZones.
type GetZonesResult struct {
	// This is the default zone that gets assigned to your workspace. This is the zone used by default for clusters and instance pools.
	DefaultZone string `pulumi:"defaultZone"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// This is a list of all the zones available for your subnets in your Databricks workspace.
	Zones []string `pulumi:"zones"`
}
