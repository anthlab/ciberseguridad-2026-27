# Host 'pivote' del laboratorio de UT7: SSH accesible con credencial reutilizada del volcado AD.
# Incluye herramientas para que el alumnado instale/reviertan persistencia (cron, systemd no
# aplica en contenedor: se usa cron y authorized_keys, ambos revertibles y verificables).
FROM debian:12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openssh-server cron curl iproute2 iputils-ping netcat-openbsd sudo procps ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Usuario de servicio con la MISMA contraseña que en el volcado NTLM (svc-backup:Password1).
# Es el enganche narrativo: la credencial crackeada en HE-E13 abre este host en HE-E14.
RUN useradd -m -s /bin/bash svc-backup && \
    echo 'svc-backup:Password1' | chpasswd && \
    adduser svc-backup sudo && \
    echo 'svc-backup ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/svc-backup

# Endurecimiento mínimo REALISTA: permite password auth (para el login con la cred crackeada).
RUN mkdir -p /run/sshd && \
    sed -i 's/#\?PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config && \
    sed -i 's/#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config

EXPOSE 22
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
