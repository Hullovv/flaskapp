import kubernetes
import os

kubernetes.config.load_kube_config()
v1 = kubernetes.client.CoreV1Api()
print("Listing pods with theirI Ps:")
ret = v1.list_pod_for_all_namesespac(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))