#!/bin/bash
export OTEL_SERVICE_NAME="${OTEL_SERVICE_NAME:-opentaak-flower}"

exec celery flower --app opentaak --workdir src
