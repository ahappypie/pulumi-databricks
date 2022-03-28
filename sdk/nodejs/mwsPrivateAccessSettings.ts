// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Import
 *
 * -> **Note** Importing this resource is not currently supported.
 */
export class MwsPrivateAccessSettings extends pulumi.CustomResource {
    /**
     * Get an existing MwsPrivateAccessSettings resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MwsPrivateAccessSettingsState, opts?: pulumi.CustomResourceOptions): MwsPrivateAccessSettings {
        return new MwsPrivateAccessSettings(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'databricks:index/mwsPrivateAccessSettings:MwsPrivateAccessSettings';

    /**
     * Returns true if the given object is an instance of MwsPrivateAccessSettings.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MwsPrivateAccessSettings {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MwsPrivateAccessSettings.__pulumiType;
    }

    /**
     * Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
     */
    public readonly accountId!: pulumi.Output<string | undefined>;
    /**
     * An array of databricks.MwsVpcEndpoint `vpcEndpointId` (not `id`). Only used when `privateAccessLevel` is set to `ENDPOINT`. This is an allow list of databricks.MwsVpcEndpoint that in your account that can connect to your databricks.MwsWorkspaces over AWS PrivateLink. If hybrid access to your workspace is enabled by setting `publicAccessEnabled` to true, then this control only works for PrivateLink connections. To control how your workspace is accessed via public internet, see the article for databricks_ip_access_list.
     */
    public readonly allowedVpcEndpointIds!: pulumi.Output<string[] | undefined>;
    /**
     * The private access level controls which VPC endpoints can connect to the UI or API of any workspace that attaches this private access settings object. `ANY` level access _(default)_ lets any databricks.MwsVpcEndpoint connect to your databricks_mws_workspaces. `ACCOUNT` level access lets only databricks.MwsVpcEndpoint that are registered in your Databricks account connect to your databricks_mws_workspaces. `ENDPOINT` level access lets only specified databricks.MwsVpcEndpoint connect to your workspace. Please see the `allowedVpcEndpointIds` documentation for more details.
     */
    public readonly privateAccessLevel!: pulumi.Output<string | undefined>;
    /**
     * Canonical unique identifier of Private Access Settings in Databricks Account
     */
    public readonly privateAccessSettingsId!: pulumi.Output<string>;
    /**
     * Name of Private Access Settings in Databricks Account
     */
    public readonly privateAccessSettingsName!: pulumi.Output<string>;
    /**
     * - If `true`, the databricks.MwsWorkspaces can be accessed over the databricks.MwsVpcEndpoint as well as over the public network. In such a case, you could also configure an databricks.IpAccessList for the workspace, to restrict the source networks that could be used to access it over the public network. If `false` (default), the workspace can be accessed only over VPC endpoints, and not over the public network.
     */
    public readonly publicAccessEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * Region of AWS VPC
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * Status of Private Access Settings
     */
    public readonly status!: pulumi.Output<string>;

    /**
     * Create a MwsPrivateAccessSettings resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MwsPrivateAccessSettingsArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MwsPrivateAccessSettingsArgs | MwsPrivateAccessSettingsState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as MwsPrivateAccessSettingsState | undefined;
            resourceInputs["accountId"] = state ? state.accountId : undefined;
            resourceInputs["allowedVpcEndpointIds"] = state ? state.allowedVpcEndpointIds : undefined;
            resourceInputs["privateAccessLevel"] = state ? state.privateAccessLevel : undefined;
            resourceInputs["privateAccessSettingsId"] = state ? state.privateAccessSettingsId : undefined;
            resourceInputs["privateAccessSettingsName"] = state ? state.privateAccessSettingsName : undefined;
            resourceInputs["publicAccessEnabled"] = state ? state.publicAccessEnabled : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
        } else {
            const args = argsOrState as MwsPrivateAccessSettingsArgs | undefined;
            if ((!args || args.privateAccessSettingsName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'privateAccessSettingsName'");
            }
            if ((!args || args.region === undefined) && !opts.urn) {
                throw new Error("Missing required property 'region'");
            }
            resourceInputs["accountId"] = args ? args.accountId : undefined;
            resourceInputs["allowedVpcEndpointIds"] = args ? args.allowedVpcEndpointIds : undefined;
            resourceInputs["privateAccessLevel"] = args ? args.privateAccessLevel : undefined;
            resourceInputs["privateAccessSettingsId"] = args ? args.privateAccessSettingsId : undefined;
            resourceInputs["privateAccessSettingsName"] = args ? args.privateAccessSettingsName : undefined;
            resourceInputs["publicAccessEnabled"] = args ? args.publicAccessEnabled : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["status"] = args ? args.status : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(MwsPrivateAccessSettings.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MwsPrivateAccessSettings resources.
 */
export interface MwsPrivateAccessSettingsState {
    /**
     * Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
     */
    accountId?: pulumi.Input<string>;
    /**
     * An array of databricks.MwsVpcEndpoint `vpcEndpointId` (not `id`). Only used when `privateAccessLevel` is set to `ENDPOINT`. This is an allow list of databricks.MwsVpcEndpoint that in your account that can connect to your databricks.MwsWorkspaces over AWS PrivateLink. If hybrid access to your workspace is enabled by setting `publicAccessEnabled` to true, then this control only works for PrivateLink connections. To control how your workspace is accessed via public internet, see the article for databricks_ip_access_list.
     */
    allowedVpcEndpointIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The private access level controls which VPC endpoints can connect to the UI or API of any workspace that attaches this private access settings object. `ANY` level access _(default)_ lets any databricks.MwsVpcEndpoint connect to your databricks_mws_workspaces. `ACCOUNT` level access lets only databricks.MwsVpcEndpoint that are registered in your Databricks account connect to your databricks_mws_workspaces. `ENDPOINT` level access lets only specified databricks.MwsVpcEndpoint connect to your workspace. Please see the `allowedVpcEndpointIds` documentation for more details.
     */
    privateAccessLevel?: pulumi.Input<string>;
    /**
     * Canonical unique identifier of Private Access Settings in Databricks Account
     */
    privateAccessSettingsId?: pulumi.Input<string>;
    /**
     * Name of Private Access Settings in Databricks Account
     */
    privateAccessSettingsName?: pulumi.Input<string>;
    /**
     * - If `true`, the databricks.MwsWorkspaces can be accessed over the databricks.MwsVpcEndpoint as well as over the public network. In such a case, you could also configure an databricks.IpAccessList for the workspace, to restrict the source networks that could be used to access it over the public network. If `false` (default), the workspace can be accessed only over VPC endpoints, and not over the public network.
     */
    publicAccessEnabled?: pulumi.Input<boolean>;
    /**
     * Region of AWS VPC
     */
    region?: pulumi.Input<string>;
    /**
     * Status of Private Access Settings
     */
    status?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a MwsPrivateAccessSettings resource.
 */
export interface MwsPrivateAccessSettingsArgs {
    /**
     * Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/)
     */
    accountId?: pulumi.Input<string>;
    /**
     * An array of databricks.MwsVpcEndpoint `vpcEndpointId` (not `id`). Only used when `privateAccessLevel` is set to `ENDPOINT`. This is an allow list of databricks.MwsVpcEndpoint that in your account that can connect to your databricks.MwsWorkspaces over AWS PrivateLink. If hybrid access to your workspace is enabled by setting `publicAccessEnabled` to true, then this control only works for PrivateLink connections. To control how your workspace is accessed via public internet, see the article for databricks_ip_access_list.
     */
    allowedVpcEndpointIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The private access level controls which VPC endpoints can connect to the UI or API of any workspace that attaches this private access settings object. `ANY` level access _(default)_ lets any databricks.MwsVpcEndpoint connect to your databricks_mws_workspaces. `ACCOUNT` level access lets only databricks.MwsVpcEndpoint that are registered in your Databricks account connect to your databricks_mws_workspaces. `ENDPOINT` level access lets only specified databricks.MwsVpcEndpoint connect to your workspace. Please see the `allowedVpcEndpointIds` documentation for more details.
     */
    privateAccessLevel?: pulumi.Input<string>;
    /**
     * Canonical unique identifier of Private Access Settings in Databricks Account
     */
    privateAccessSettingsId?: pulumi.Input<string>;
    /**
     * Name of Private Access Settings in Databricks Account
     */
    privateAccessSettingsName: pulumi.Input<string>;
    /**
     * - If `true`, the databricks.MwsWorkspaces can be accessed over the databricks.MwsVpcEndpoint as well as over the public network. In such a case, you could also configure an databricks.IpAccessList for the workspace, to restrict the source networks that could be used to access it over the public network. If `false` (default), the workspace can be accessed only over VPC endpoints, and not over the public network.
     */
    publicAccessEnabled?: pulumi.Input<boolean>;
    /**
     * Region of AWS VPC
     */
    region: pulumi.Input<string>;
    /**
     * Status of Private Access Settings
     */
    status?: pulumi.Input<string>;
}