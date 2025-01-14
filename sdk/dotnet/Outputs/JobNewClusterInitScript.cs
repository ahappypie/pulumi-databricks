// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Databricks.Outputs
{

    [OutputType]
    public sealed class JobNewClusterInitScript
    {
        public readonly Outputs.JobNewClusterInitScriptDbfs? Dbfs;
        public readonly Outputs.JobNewClusterInitScriptFile? File;
        public readonly Outputs.JobNewClusterInitScriptS3? S3;

        [OutputConstructor]
        private JobNewClusterInitScript(
            Outputs.JobNewClusterInitScriptDbfs? dbfs,

            Outputs.JobNewClusterInitScriptFile? file,

            Outputs.JobNewClusterInitScriptS3? s3)
        {
            Dbfs = dbfs;
            File = file;
            S3 = s3;
        }
    }
}
