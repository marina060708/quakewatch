{{- define "quakewatch.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{- define "quakewatch.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}

{{- define "quakewatch.labels" -}}
helm.sh/chart: "{{ .Chart.Name }}-{{ .Chart.Version }}"
app.kubernetes.io/name: "{{ include "quakewatch.name" . }}"
app.kubernetes.io/instance: "{{ .Release.Name }}"
app.kubernetes.io/version: "{{ .Chart.AppVersion }}"
app.kubernetes.io/managed-by: "{{ .Release.Service }}"
{{- end }}

{{/*
Expand the name of the chart.
*/}}
{{- define "quakewatch.chart" -}}
{{- printf "%s-%s" .Chart.Name (.Chart.Version | replace "+" "_") -}}
{{- end }}
