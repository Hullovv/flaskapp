{{- /* Args */ -}}
{{- $ReleaseName := .Release.Name -}}
{{- $flask := .Values.flaskapp -}}
{{- $mysql := .Values.mysql -}}

{{- /* PersistentVolume */ -}}
{{- define "PvName" -}}
{{- $ReleaseName := .Release.Name -}}
{{- printf "%s-%s" $ReleaseName .Values.pv.name -}}
{{- end -}}

{{- /* PersistentVolumeClaim */ -}}
{{- define "PvcName" -}}
{{- $ReleaseName := .Release.Name -}}
{{- printf "%s-%s" $ReleaseName .Values.pvc.name -}}
{{- end -}}

{{- /* Secrets */ -}}
{{- define "SecretsName" -}}
{{- $ReleaseName := .Release.Name -}}
{{- printf "%s-%s" $ReleaseName .Values.secrets.name -}}
{{- end -}}

{{- /* Flask */ -}}
{{- define "FlaskServiceName" -}}
{{- $ReleaseName := .Release.Name -}}
{{- $flask := .Values.flaskapp -}}
{{- printf "%s-%s" $ReleaseName $flask.ServiceName -}}
{{- end -}}
{{- define "FlaskDeploymentName" -}}
{{- $ReleaseName := .Release.Name -}}
{{- $flask := .Values.flaskapp -}}
{{- printf "%s-%s" $ReleaseName $flask.DeployName -}}
{{- end -}}

{{- /* Mysql */ -}}
{{- define "MysqlServiceName" -}}
{{- $ReleaseName := .Release.Name -}}
{{- $mysql := .Values.mysql -}}
{{- printf "%s-%s" $ReleaseName $mysql.ServiceName -}}
{{- end -}}
{{- define "MysqlDeploymentName" -}}
{{- $ReleaseName := .Release.Name -}}
{{- $mysql := .Values.mysql -}}
{{- printf "%s-%s" $ReleaseName $mysql.DeployName -}}
{{- end -}}
{{- define "MysqlVolumeName" -}}
{{- $ReleaseName := .Release.Name -}}
{{- $mysql := .Values.mysql -}}
{{- printf "%s-%s" $ReleaseName $mysql.VolumeName -}}
{{- end -}}