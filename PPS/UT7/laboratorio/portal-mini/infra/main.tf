# Infraestructura como código de PRÁCTICA con fallos a propósito (para Checkov).
# NO se aplica: es un fichero para que el análisis IaC tenga algo que detectar.
# Hallazgos esperados (entre otros):
#   CKV_AWS_260 / CKV_AWS_24 -> grupo de seguridad con SSH (22) abierto a 0.0.0.0/0
#   CKV_AWS_20  / bucket público -> almacenamiento de evidencias legible por cualquiera

resource "aws_security_group" "portal" {
  name        = "portal-soc"
  description = "SG del portal SOC (laboratorio)"

  ingress {
    description = "SSH abierto al mundo (MAL)"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_s3_bucket" "evidencias" {
  bucket = "portal-soc-evidencias-lab"
}

resource "aws_s3_bucket_acl" "evidencias_acl" {
  bucket = aws_s3_bucket.evidencias.id
  acl    = "public-read" # bucket público (MAL): evidencias legibles por cualquiera
}
