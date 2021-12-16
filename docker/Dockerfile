FROM python:3.9-alpine3.14


WORKDIR /home/sec-tool


# Pull Trivy from public as binary
COPY --from=aquasec/trivy:latest /usr/local/bin/trivy /usr/local/bin/trivy


# Set non root userar
RUN adduser -D sec-tool && chown -R sec-tool /home/sec-tool
USER sec-tool


# Install Semgrep using Pip
RUN export PATH=/home/sec-tool/.local/bin:$PATH
RUN python3 -m pip install semgrep


# For offline vulnerability db
RUN mkdir -p /home/sec-tool/.cache/trivy/db


# DOwnload trivy vulnerabilty db and untar it to cache dir
RUN wget https://github.com/aquasecurity/trivy-db/releases/latest/download/trivy-offline.db.tgz -O /home/sec-tool/.cache/trivy/db/trivy-offline.db.tgz 
RUN tar -zxvf  /home/sec-tool/.cache/trivy/db/trivy-offline.db.tgz -C  /home/sec-tool/.cache/trivy/db
RUN rm /home/sec-tool/.cache/trivy/db/trivy-offline.db.tgz


# Download semgrep rule offline
RUN mkdir -p /home/sec-tool/semgrep-rules
RUN wget --no-check-certificate https://semgrep.dev/c/p/security-audit -O /home/sec-tool/semgrep-rules/security-audit
RUN wget --no-check-certificate https://semgrep.dev/c/p/secrets -O /home/sec-tool/semgrep-rules/secrets


COPY entrypoint.sh /home/sec-tool/entrypoint.sh
ENTRYPOINT [ "sh","/home/sec-tool/entrypoint.sh" ]
