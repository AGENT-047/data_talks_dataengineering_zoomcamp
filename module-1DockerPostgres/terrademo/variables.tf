variable "project" {
  description = "Project"
  default     = "terraform-basics-465801"
}

variable "bq_dataset_name" {
  description = "My Big Query Dataset Name"
  default     = "demo_dataset"
}


variable "gcs_bucket_name" {
  description = "My Bucket Name"
  default     = "peace_out"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

variable "region" {
  description = "Region"
  default     = "asia-south1"
}

variable "credentials" {
  description = "my credentials path"
  default     = "./keys/my-creds.json"
}

