// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks
{
    /// <summary>
    /// This resource creates [On-Behalf-Of tokens](https://docs.databricks.com/administration-guide/users-groups/service-principals.html#manage-personal-access-tokens-for-a-service-principal) for a databricks.ServicePrincipal in Databricks workspaces on AWS. It is very useful, when you want to provision resources within a workspace through narrowly-scoped service principal, that has no access to other workspaces within the same Databricks Account.
    /// 
    /// ## Related Resources
    /// 
    /// The following resources are often used in the same context:
    /// 
    /// * End to end workspace management guide.
    /// * databricks.Group data to retrieve information about databricks.Group members, entitlements and instance profiles.
    /// * databricks_group_member to attach users and groups as group members.
    /// * databricks.Permissions to manage [access control](https://docs.databricks.com/security/access-control/index.html) in Databricks workspace.
    /// * databricks.ServicePrincipal to manage [Service Principals](https://docs.databricks.com/administration-guide/users-groups/service-principals.html) that could be added to databricks.Group within workspace.
    /// * databricks.SqlPermissions to manage data object access control lists in Databricks workspaces for things like tables, views, databases, and [more](https://docs.databricks.com/security/access-control/table-acls/object-privileges.html).
    /// 
    /// ## Import
    /// 
    /// -&gt; **Note** Importing this resource is not currently supported.
    /// </summary>
    [DatabricksResourceType("databricks:index/oboToken:OboToken")]
    public partial class OboToken : Pulumi.CustomResource
    {
        /// <summary>
        /// Application ID of databricks.ServicePrincipal to create PAT token for.
        /// </summary>
        [Output("applicationId")]
        public Output<string> ApplicationId { get; private set; } = null!;

        /// <summary>
        /// Comment that describes the purpose of the token.
        /// </summary>
        [Output("comment")]
        public Output<string> Comment { get; private set; } = null!;

        /// <summary>
        /// The number of seconds before the token expires. Token resource is re-created when it expires.
        /// </summary>
        [Output("lifetimeSeconds")]
        public Output<int> LifetimeSeconds { get; private set; } = null!;

        /// <summary>
        /// **Sensitive** value of the newly-created token.
        /// </summary>
        [Output("tokenValue")]
        public Output<string> TokenValue { get; private set; } = null!;


        /// <summary>
        /// Create a OboToken resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public OboToken(string name, OboTokenArgs args, CustomResourceOptions? options = null)
            : base("databricks:index/oboToken:OboToken", name, args ?? new OboTokenArgs(), MakeResourceOptions(options, ""))
        {
        }

        private OboToken(string name, Input<string> id, OboTokenState? state = null, CustomResourceOptions? options = null)
            : base("databricks:index/oboToken:OboToken", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing OboToken resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static OboToken Get(string name, Input<string> id, OboTokenState? state = null, CustomResourceOptions? options = null)
        {
            return new OboToken(name, id, state, options);
        }
    }

    public sealed class OboTokenArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Application ID of databricks.ServicePrincipal to create PAT token for.
        /// </summary>
        [Input("applicationId", required: true)]
        public Input<string> ApplicationId { get; set; } = null!;

        /// <summary>
        /// Comment that describes the purpose of the token.
        /// </summary>
        [Input("comment", required: true)]
        public Input<string> Comment { get; set; } = null!;

        /// <summary>
        /// The number of seconds before the token expires. Token resource is re-created when it expires.
        /// </summary>
        [Input("lifetimeSeconds", required: true)]
        public Input<int> LifetimeSeconds { get; set; } = null!;

        public OboTokenArgs()
        {
        }
    }

    public sealed class OboTokenState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Application ID of databricks.ServicePrincipal to create PAT token for.
        /// </summary>
        [Input("applicationId")]
        public Input<string>? ApplicationId { get; set; }

        /// <summary>
        /// Comment that describes the purpose of the token.
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// The number of seconds before the token expires. Token resource is re-created when it expires.
        /// </summary>
        [Input("lifetimeSeconds")]
        public Input<int>? LifetimeSeconds { get; set; }

        /// <summary>
        /// **Sensitive** value of the newly-created token.
        /// </summary>
        [Input("tokenValue")]
        public Input<string>? TokenValue { get; set; }

        public OboTokenState()
        {
        }
    }
}
