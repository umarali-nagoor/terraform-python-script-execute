resource "null_resource" "install_lh" {
  
  provisioner "local-exec" {
    command = <<EOT
      python3 ${path.module}/scripts/install_lh.py --apikey "${var.ibmcloud_api_key}" --region "${var.region}" --cluster "${var.cluster}"
    EOT
  }
}
