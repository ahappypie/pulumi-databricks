// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks
{
    [DatabricksResourceType("databricks:index/azureAdlsGen1Mount:AzureAdlsGen1Mount")]
    public partial class AzureAdlsGen1Mount : Pulumi.CustomResource
    {
        [Output("clientId")]
        public Output<string> ClientId { get; private set; } = null!;

        [Output("clientSecretKey")]
        public Output<string> ClientSecretKey { get; private set; } = null!;

        [Output("clientSecretScope")]
        public Output<string> ClientSecretScope { get; private set; } = null!;

        [Output("clusterId")]
        public Output<string?> ClusterId { get; private set; } = null!;

        [Output("directory")]
        public Output<string> Directory { get; private set; } = null!;

        [Output("mountName")]
        public Output<string> MountName { get; private set; } = null!;

        [Output("source")]
        public Output<string> Source { get; private set; } = null!;

        [Output("sparkConfPrefix")]
        public Output<string?> SparkConfPrefix { get; private set; } = null!;

        [Output("storageResourceName")]
        public Output<string> StorageResourceName { get; private set; } = null!;

        [Output("tenantId")]
        public Output<string> TenantId { get; private set; } = null!;


        /// <summary>
        /// Create a AzureAdlsGen1Mount resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AzureAdlsGen1Mount(string name, AzureAdlsGen1MountArgs args, CustomResourceOptions? options = null)
            : base("databricks:index/azureAdlsGen1Mount:AzureAdlsGen1Mount", name, args ?? new AzureAdlsGen1MountArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AzureAdlsGen1Mount(string name, Input<string> id, AzureAdlsGen1MountState? state = null, CustomResourceOptions? options = null)
            : base("databricks:index/azureAdlsGen1Mount:AzureAdlsGen1Mount", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing AzureAdlsGen1Mount resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AzureAdlsGen1Mount Get(string name, Input<string> id, AzureAdlsGen1MountState? state = null, CustomResourceOptions? options = null)
        {
            return new AzureAdlsGen1Mount(name, id, state, options);
        }
    }

    public sealed class AzureAdlsGen1MountArgs : Pulumi.ResourceArgs
    {
        [Input("clientId", required: true)]
        public Input<string> ClientId { get; set; } = null!;

        [Input("clientSecretKey", required: true)]
        public Input<string> ClientSecretKey { get; set; } = null!;

        [Input("clientSecretScope", required: true)]
        public Input<string> ClientSecretScope { get; set; } = null!;

        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        [Input("directory")]
        public Input<string>? Directory { get; set; }

        [Input("mountName", required: true)]
        public Input<string> MountName { get; set; } = null!;

        [Input("sparkConfPrefix")]
        public Input<string>? SparkConfPrefix { get; set; }

        [Input("storageResourceName", required: true)]
        public Input<string> StorageResourceName { get; set; } = null!;

        [Input("tenantId", required: true)]
        public Input<string> TenantId { get; set; } = null!;

        public AzureAdlsGen1MountArgs()
        {
        }
    }

    public sealed class AzureAdlsGen1MountState : Pulumi.ResourceArgs
    {
        [Input("clientId")]
        public Input<string>? ClientId { get; set; }

        [Input("clientSecretKey")]
        public Input<string>? ClientSecretKey { get; set; }

        [Input("clientSecretScope")]
        public Input<string>? ClientSecretScope { get; set; }

        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        [Input("directory")]
        public Input<string>? Directory { get; set; }

        [Input("mountName")]
        public Input<string>? MountName { get; set; }

        [Input("source")]
        public Input<string>? Source { get; set; }

        [Input("sparkConfPrefix")]
        public Input<string>? SparkConfPrefix { get; set; }

        [Input("storageResourceName")]
        public Input<string>? StorageResourceName { get; set; }

        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        public AzureAdlsGen1MountState()
        {
        }
    }
}
