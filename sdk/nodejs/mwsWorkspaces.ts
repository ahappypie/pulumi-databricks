// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * ## Import
 *
 * -> **Note** Importing this resource is not currently supported.
 */
export class MwsWorkspaces extends pulumi.CustomResource {
    /**
     * Get an existing MwsWorkspaces resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MwsWorkspacesState, opts?: pulumi.CustomResourceOptions): MwsWorkspaces {
        return new MwsWorkspaces(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'databricks:index/mwsWorkspaces:MwsWorkspaces';

    /**
     * Returns true if the given object is an instance of MwsWorkspaces.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MwsWorkspaces {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MwsWorkspaces.__pulumiType;
    }

    /**
     * Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/).
     */
    public readonly accountId!: pulumi.Output<string>;
    /**
     * AWS region of VPC
     */
    public readonly awsRegion!: pulumi.Output<string | undefined>;
    public readonly cloud!: pulumi.Output<string>;
    public readonly cloudResourceBucket!: pulumi.Output<outputs.MwsWorkspacesCloudResourceBucket | undefined>;
    /**
     * (Integer) time when workspace was created
     */
    public readonly creationTime!: pulumi.Output<number>;
    public readonly credentialsId!: pulumi.Output<string | undefined>;
    /**
     * @deprecated Use managed_services_customer_managed_key_id instead
     */
    public readonly customerManagedKeyId!: pulumi.Output<string | undefined>;
    /**
     * part of URL: `https://<deployment-name>.cloud.databricks.com`
     */
    public readonly deploymentName!: pulumi.Output<string | undefined>;
    public readonly externalCustomerInfo!: pulumi.Output<outputs.MwsWorkspacesExternalCustomerInfo | undefined>;
    public readonly isNoPublicIpEnabled!: pulumi.Output<boolean | undefined>;
    public readonly location!: pulumi.Output<string | undefined>;
    /**
     * `customerManagedKeyId` from customer managed keys with `useCases` set to `MANAGED_SERVICES`. This is used to encrypt the workspace's notebook and secret data in the control plane.
     */
    public readonly managedServicesCustomerManagedKeyId!: pulumi.Output<string | undefined>;
    public readonly network!: pulumi.Output<outputs.MwsWorkspacesNetwork | undefined>;
    public readonly networkId!: pulumi.Output<string | undefined>;
    public readonly pricingTier!: pulumi.Output<string>;
    /**
     * Canonical unique identifier of databricks.MwsPrivateAccessSettings in Databricks Account
     */
    public readonly privateAccessSettingsId!: pulumi.Output<string | undefined>;
    /**
     * `storageConfigurationId` from storage configuration
     */
    public readonly storageConfigurationId!: pulumi.Output<string | undefined>;
    public readonly storageCustomerManagedKeyId!: pulumi.Output<string | undefined>;
    public readonly token!: pulumi.Output<outputs.MwsWorkspacesToken | undefined>;
    public readonly workspaceId!: pulumi.Output<number>;
    /**
     * name of the workspace, will appear on UI
     */
    public readonly workspaceName!: pulumi.Output<string>;
    /**
     * (String) workspace status
     */
    public readonly workspaceStatus!: pulumi.Output<string>;
    /**
     * (String) updates on workspace status
     */
    public readonly workspaceStatusMessage!: pulumi.Output<string>;
    /**
     * (String) URL of the workspace
     */
    public readonly workspaceUrl!: pulumi.Output<string>;

    /**
     * Create a MwsWorkspaces resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MwsWorkspacesArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MwsWorkspacesArgs | MwsWorkspacesState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as MwsWorkspacesState | undefined;
            resourceInputs["accountId"] = state ? state.accountId : undefined;
            resourceInputs["awsRegion"] = state ? state.awsRegion : undefined;
            resourceInputs["cloud"] = state ? state.cloud : undefined;
            resourceInputs["cloudResourceBucket"] = state ? state.cloudResourceBucket : undefined;
            resourceInputs["creationTime"] = state ? state.creationTime : undefined;
            resourceInputs["credentialsId"] = state ? state.credentialsId : undefined;
            resourceInputs["customerManagedKeyId"] = state ? state.customerManagedKeyId : undefined;
            resourceInputs["deploymentName"] = state ? state.deploymentName : undefined;
            resourceInputs["externalCustomerInfo"] = state ? state.externalCustomerInfo : undefined;
            resourceInputs["isNoPublicIpEnabled"] = state ? state.isNoPublicIpEnabled : undefined;
            resourceInputs["location"] = state ? state.location : undefined;
            resourceInputs["managedServicesCustomerManagedKeyId"] = state ? state.managedServicesCustomerManagedKeyId : undefined;
            resourceInputs["network"] = state ? state.network : undefined;
            resourceInputs["networkId"] = state ? state.networkId : undefined;
            resourceInputs["pricingTier"] = state ? state.pricingTier : undefined;
            resourceInputs["privateAccessSettingsId"] = state ? state.privateAccessSettingsId : undefined;
            resourceInputs["storageConfigurationId"] = state ? state.storageConfigurationId : undefined;
            resourceInputs["storageCustomerManagedKeyId"] = state ? state.storageCustomerManagedKeyId : undefined;
            resourceInputs["token"] = state ? state.token : undefined;
            resourceInputs["workspaceId"] = state ? state.workspaceId : undefined;
            resourceInputs["workspaceName"] = state ? state.workspaceName : undefined;
            resourceInputs["workspaceStatus"] = state ? state.workspaceStatus : undefined;
            resourceInputs["workspaceStatusMessage"] = state ? state.workspaceStatusMessage : undefined;
            resourceInputs["workspaceUrl"] = state ? state.workspaceUrl : undefined;
        } else {
            const args = argsOrState as MwsWorkspacesArgs | undefined;
            if ((!args || args.accountId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'accountId'");
            }
            if ((!args || args.workspaceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'workspaceName'");
            }
            resourceInputs["accountId"] = args ? args.accountId : undefined;
            resourceInputs["awsRegion"] = args ? args.awsRegion : undefined;
            resourceInputs["cloud"] = args ? args.cloud : undefined;
            resourceInputs["cloudResourceBucket"] = args ? args.cloudResourceBucket : undefined;
            resourceInputs["creationTime"] = args ? args.creationTime : undefined;
            resourceInputs["credentialsId"] = args ? args.credentialsId : undefined;
            resourceInputs["customerManagedKeyId"] = args ? args.customerManagedKeyId : undefined;
            resourceInputs["deploymentName"] = args ? args.deploymentName : undefined;
            resourceInputs["externalCustomerInfo"] = args ? args.externalCustomerInfo : undefined;
            resourceInputs["isNoPublicIpEnabled"] = args ? args.isNoPublicIpEnabled : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["managedServicesCustomerManagedKeyId"] = args ? args.managedServicesCustomerManagedKeyId : undefined;
            resourceInputs["network"] = args ? args.network : undefined;
            resourceInputs["networkId"] = args ? args.networkId : undefined;
            resourceInputs["pricingTier"] = args ? args.pricingTier : undefined;
            resourceInputs["privateAccessSettingsId"] = args ? args.privateAccessSettingsId : undefined;
            resourceInputs["storageConfigurationId"] = args ? args.storageConfigurationId : undefined;
            resourceInputs["storageCustomerManagedKeyId"] = args ? args.storageCustomerManagedKeyId : undefined;
            resourceInputs["token"] = args ? args.token : undefined;
            resourceInputs["workspaceId"] = args ? args.workspaceId : undefined;
            resourceInputs["workspaceName"] = args ? args.workspaceName : undefined;
            resourceInputs["workspaceStatus"] = args ? args.workspaceStatus : undefined;
            resourceInputs["workspaceStatusMessage"] = args ? args.workspaceStatusMessage : undefined;
            resourceInputs["workspaceUrl"] = args ? args.workspaceUrl : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(MwsWorkspaces.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MwsWorkspaces resources.
 */
export interface MwsWorkspacesState {
    /**
     * Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/).
     */
    accountId?: pulumi.Input<string>;
    /**
     * AWS region of VPC
     */
    awsRegion?: pulumi.Input<string>;
    cloud?: pulumi.Input<string>;
    cloudResourceBucket?: pulumi.Input<inputs.MwsWorkspacesCloudResourceBucket>;
    /**
     * (Integer) time when workspace was created
     */
    creationTime?: pulumi.Input<number>;
    credentialsId?: pulumi.Input<string>;
    /**
     * @deprecated Use managed_services_customer_managed_key_id instead
     */
    customerManagedKeyId?: pulumi.Input<string>;
    /**
     * part of URL: `https://<deployment-name>.cloud.databricks.com`
     */
    deploymentName?: pulumi.Input<string>;
    externalCustomerInfo?: pulumi.Input<inputs.MwsWorkspacesExternalCustomerInfo>;
    isNoPublicIpEnabled?: pulumi.Input<boolean>;
    location?: pulumi.Input<string>;
    /**
     * `customerManagedKeyId` from customer managed keys with `useCases` set to `MANAGED_SERVICES`. This is used to encrypt the workspace's notebook and secret data in the control plane.
     */
    managedServicesCustomerManagedKeyId?: pulumi.Input<string>;
    network?: pulumi.Input<inputs.MwsWorkspacesNetwork>;
    networkId?: pulumi.Input<string>;
    pricingTier?: pulumi.Input<string>;
    /**
     * Canonical unique identifier of databricks.MwsPrivateAccessSettings in Databricks Account
     */
    privateAccessSettingsId?: pulumi.Input<string>;
    /**
     * `storageConfigurationId` from storage configuration
     */
    storageConfigurationId?: pulumi.Input<string>;
    storageCustomerManagedKeyId?: pulumi.Input<string>;
    token?: pulumi.Input<inputs.MwsWorkspacesToken>;
    workspaceId?: pulumi.Input<number>;
    /**
     * name of the workspace, will appear on UI
     */
    workspaceName?: pulumi.Input<string>;
    /**
     * (String) workspace status
     */
    workspaceStatus?: pulumi.Input<string>;
    /**
     * (String) updates on workspace status
     */
    workspaceStatusMessage?: pulumi.Input<string>;
    /**
     * (String) URL of the workspace
     */
    workspaceUrl?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a MwsWorkspaces resource.
 */
export interface MwsWorkspacesArgs {
    /**
     * Account Id that could be found in the bottom left corner of [Accounts Console](https://accounts.cloud.databricks.com/).
     */
    accountId: pulumi.Input<string>;
    /**
     * AWS region of VPC
     */
    awsRegion?: pulumi.Input<string>;
    cloud?: pulumi.Input<string>;
    cloudResourceBucket?: pulumi.Input<inputs.MwsWorkspacesCloudResourceBucket>;
    /**
     * (Integer) time when workspace was created
     */
    creationTime?: pulumi.Input<number>;
    credentialsId?: pulumi.Input<string>;
    /**
     * @deprecated Use managed_services_customer_managed_key_id instead
     */
    customerManagedKeyId?: pulumi.Input<string>;
    /**
     * part of URL: `https://<deployment-name>.cloud.databricks.com`
     */
    deploymentName?: pulumi.Input<string>;
    externalCustomerInfo?: pulumi.Input<inputs.MwsWorkspacesExternalCustomerInfo>;
    isNoPublicIpEnabled?: pulumi.Input<boolean>;
    location?: pulumi.Input<string>;
    /**
     * `customerManagedKeyId` from customer managed keys with `useCases` set to `MANAGED_SERVICES`. This is used to encrypt the workspace's notebook and secret data in the control plane.
     */
    managedServicesCustomerManagedKeyId?: pulumi.Input<string>;
    network?: pulumi.Input<inputs.MwsWorkspacesNetwork>;
    networkId?: pulumi.Input<string>;
    pricingTier?: pulumi.Input<string>;
    /**
     * Canonical unique identifier of databricks.MwsPrivateAccessSettings in Databricks Account
     */
    privateAccessSettingsId?: pulumi.Input<string>;
    /**
     * `storageConfigurationId` from storage configuration
     */
    storageConfigurationId?: pulumi.Input<string>;
    storageCustomerManagedKeyId?: pulumi.Input<string>;
    token?: pulumi.Input<inputs.MwsWorkspacesToken>;
    workspaceId?: pulumi.Input<number>;
    /**
     * name of the workspace, will appear on UI
     */
    workspaceName: pulumi.Input<string>;
    /**
     * (String) workspace status
     */
    workspaceStatus?: pulumi.Input<string>;
    /**
     * (String) updates on workspace status
     */
    workspaceStatusMessage?: pulumi.Input<string>;
    /**
     * (String) URL of the workspace
     */
    workspaceUrl?: pulumi.Input<string>;
}
