# Imagen de PRÁCTICA con malas configuraciones a propósito (para el análisis IaC).
# Checkov marcará, entre otros:
#   CKV_DOCKER_2  -> falta HEALTHCHECK
#   CKV_DOCKER_3  -> el contenedor corre como root (falta USER)
FROM python:3.9

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
# Falta: USER no-root y HEALTHCHECK. Se añaden en la solución para ver el diff.
CMD ["python", "app.py"]
