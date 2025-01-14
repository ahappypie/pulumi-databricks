// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class AzureBlobMount extends pulumi.CustomResource {
    /**
     * Get an existing AzureBlobMount resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AzureBlobMountState, opts?: pulumi.CustomResourceOptions): AzureBlobMount {
        return new AzureBlobMount(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'databricks:index/azureBlobMount:AzureBlobMount';

    /**
     * Returns true if the given object is an instance of AzureBlobMount.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AzureBlobMount {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AzureBlobMount.__pulumiType;
    }

    public readonly authType!: pulumi.Output<string>;
    public readonly clusterId!: pulumi.Output<string | undefined>;
    public readonly containerName!: pulumi.Output<string>;
    public readonly directory!: pulumi.Output<string | undefined>;
    public readonly mountName!: pulumi.Output<string>;
    public /*out*/ readonly source!: pulumi.Output<string>;
    public readonly storageAccountName!: pulumi.Output<string>;
    public readonly tokenSecretKey!: pulumi.Output<string>;
    public readonly tokenSecretScope!: pulumi.Output<string>;

    /**
     * Create a AzureBlobMount resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AzureBlobMountArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AzureBlobMountArgs | AzureBlobMountState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as AzureBlobMountState | undefined;
            resourceInputs["authType"] = state ? state.authType : undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["containerName"] = state ? state.containerName : undefined;
            resourceInputs["directory"] = state ? state.directory : undefined;
            resourceInputs["mountName"] = state ? state.mountName : undefined;
            resourceInputs["source"] = state ? state.source : undefined;
            resourceInputs["storageAccountName"] = state ? state.storageAccountName : undefined;
            resourceInputs["tokenSecretKey"] = state ? state.tokenSecretKey : undefined;
            resourceInputs["tokenSecretScope"] = state ? state.tokenSecretScope : undefined;
        } else {
            const args = argsOrState as AzureBlobMountArgs | undefined;
            if ((!args || args.authType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'authType'");
            }
            if ((!args || args.containerName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'containerName'");
            }
            if ((!args || args.mountName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'mountName'");
            }
            if ((!args || args.storageAccountName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'storageAccountName'");
            }
            if ((!args || args.tokenSecretKey === undefined) && !opts.urn) {
                throw new Error("Missing required property 'tokenSecretKey'");
            }
            if ((!args || args.tokenSecretScope === undefined) && !opts.urn) {
                throw new Error("Missing required property 'tokenSecretScope'");
            }
            resourceInputs["authType"] = args ? args.authType : undefined;
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["containerName"] = args ? args.containerName : undefined;
            resourceInputs["directory"] = args ? args.directory : undefined;
            resourceInputs["mountName"] = args ? args.mountName : undefined;
            resourceInputs["storageAccountName"] = args ? args.storageAccountName : undefined;
            resourceInputs["tokenSecretKey"] = args ? args.tokenSecretKey : undefined;
            resourceInputs["tokenSecretScope"] = args ? args.tokenSecretScope : undefined;
            resourceInputs["source"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(AzureBlobMount.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AzureBlobMount resources.
 */
export interface AzureBlobMountState {
    authType?: pulumi.Input<string>;
    clusterId?: pulumi.Input<string>;
    containerName?: pulumi.Input<string>;
    directory?: pulumi.Input<string>;
    mountName?: pulumi.Input<string>;
    source?: pulumi.Input<string>;
    storageAccountName?: pulumi.Input<string>;
    tokenSecretKey?: pulumi.Input<string>;
    tokenSecretScope?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AzureBlobMount resource.
 */
export interface AzureBlobMountArgs {
    authType: pulumi.Input<string>;
    clusterId?: pulumi.Input<string>;
    containerName: pulumi.Input<string>;
    directory?: pulumi.Input<string>;
    mountName: pulumi.Input<string>;
    storageAccountName: pulumi.Input<string>;
    tokenSecretKey: pulumi.Input<string>;
    tokenSecretScope: pulumi.Input<string>;
}
