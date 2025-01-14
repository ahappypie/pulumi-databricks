// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class AzureAdlsGen2Mount extends pulumi.CustomResource {
    /**
     * Get an existing AzureAdlsGen2Mount resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AzureAdlsGen2MountState, opts?: pulumi.CustomResourceOptions): AzureAdlsGen2Mount {
        return new AzureAdlsGen2Mount(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'databricks:index/azureAdlsGen2Mount:AzureAdlsGen2Mount';

    /**
     * Returns true if the given object is an instance of AzureAdlsGen2Mount.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AzureAdlsGen2Mount {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AzureAdlsGen2Mount.__pulumiType;
    }

    public readonly clientId!: pulumi.Output<string>;
    public readonly clientSecretKey!: pulumi.Output<string>;
    public readonly clientSecretScope!: pulumi.Output<string>;
    public readonly clusterId!: pulumi.Output<string | undefined>;
    public readonly containerName!: pulumi.Output<string>;
    public readonly directory!: pulumi.Output<string>;
    public readonly initializeFileSystem!: pulumi.Output<boolean>;
    public readonly mountName!: pulumi.Output<string>;
    public /*out*/ readonly source!: pulumi.Output<string>;
    public readonly storageAccountName!: pulumi.Output<string>;
    public readonly tenantId!: pulumi.Output<string>;

    /**
     * Create a AzureAdlsGen2Mount resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AzureAdlsGen2MountArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AzureAdlsGen2MountArgs | AzureAdlsGen2MountState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as AzureAdlsGen2MountState | undefined;
            resourceInputs["clientId"] = state ? state.clientId : undefined;
            resourceInputs["clientSecretKey"] = state ? state.clientSecretKey : undefined;
            resourceInputs["clientSecretScope"] = state ? state.clientSecretScope : undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["containerName"] = state ? state.containerName : undefined;
            resourceInputs["directory"] = state ? state.directory : undefined;
            resourceInputs["initializeFileSystem"] = state ? state.initializeFileSystem : undefined;
            resourceInputs["mountName"] = state ? state.mountName : undefined;
            resourceInputs["source"] = state ? state.source : undefined;
            resourceInputs["storageAccountName"] = state ? state.storageAccountName : undefined;
            resourceInputs["tenantId"] = state ? state.tenantId : undefined;
        } else {
            const args = argsOrState as AzureAdlsGen2MountArgs | undefined;
            if ((!args || args.clientId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clientId'");
            }
            if ((!args || args.clientSecretKey === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clientSecretKey'");
            }
            if ((!args || args.clientSecretScope === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clientSecretScope'");
            }
            if ((!args || args.containerName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'containerName'");
            }
            if ((!args || args.initializeFileSystem === undefined) && !opts.urn) {
                throw new Error("Missing required property 'initializeFileSystem'");
            }
            if ((!args || args.mountName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'mountName'");
            }
            if ((!args || args.storageAccountName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'storageAccountName'");
            }
            if ((!args || args.tenantId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'tenantId'");
            }
            resourceInputs["clientId"] = args ? args.clientId : undefined;
            resourceInputs["clientSecretKey"] = args ? args.clientSecretKey : undefined;
            resourceInputs["clientSecretScope"] = args ? args.clientSecretScope : undefined;
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["containerName"] = args ? args.containerName : undefined;
            resourceInputs["directory"] = args ? args.directory : undefined;
            resourceInputs["initializeFileSystem"] = args ? args.initializeFileSystem : undefined;
            resourceInputs["mountName"] = args ? args.mountName : undefined;
            resourceInputs["storageAccountName"] = args ? args.storageAccountName : undefined;
            resourceInputs["tenantId"] = args ? args.tenantId : undefined;
            resourceInputs["source"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(AzureAdlsGen2Mount.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AzureAdlsGen2Mount resources.
 */
export interface AzureAdlsGen2MountState {
    clientId?: pulumi.Input<string>;
    clientSecretKey?: pulumi.Input<string>;
    clientSecretScope?: pulumi.Input<string>;
    clusterId?: pulumi.Input<string>;
    containerName?: pulumi.Input<string>;
    directory?: pulumi.Input<string>;
    initializeFileSystem?: pulumi.Input<boolean>;
    mountName?: pulumi.Input<string>;
    source?: pulumi.Input<string>;
    storageAccountName?: pulumi.Input<string>;
    tenantId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AzureAdlsGen2Mount resource.
 */
export interface AzureAdlsGen2MountArgs {
    clientId: pulumi.Input<string>;
    clientSecretKey: pulumi.Input<string>;
    clientSecretScope: pulumi.Input<string>;
    clusterId?: pulumi.Input<string>;
    containerName: pulumi.Input<string>;
    directory?: pulumi.Input<string>;
    initializeFileSystem: pulumi.Input<boolean>;
    mountName: pulumi.Input<string>;
    storageAccountName: pulumi.Input<string>;
    tenantId: pulumi.Input<string>;
}
