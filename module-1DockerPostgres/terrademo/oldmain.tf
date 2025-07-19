# terraform {
#   required_providers {
#     google = {
#       source  = "hashicorp/google"
#       version = "6.43.0"
#     }
#   }
# }

# provider "google" {
#   project = "terraform-basics-465801"
#   region  = "asia-south1"
# }

# # creating bucket
# resource "google_storage_bucket" "peace_out" {
#   name          = "peace_out"
#   location      = "asia-south1"
#   force_destroy = true

#   lifecycle_rule {
#     condition {
#       age = 1
#     }
#     action {
#       type = "AbortIncompleteMultipartUpload"
#     }
#   }

# }

# # creating bigquery dataset
# resource "google_bigquery_dataset" "demo_dataset" {
#   dataset_id = "demo_dataset"
# }