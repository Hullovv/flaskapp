load('ext://deployment', 'deployment_create')
load('ext://syncback', 'syncback')
load('ext://configmap', 'configmap_create')
load('ext://secret','secret_create_generic')

secret_settings(disable_scrub=True)
secret_create_generic(name='flask-secrets', from_file='secrets=k8s/secrets.yaml')

configmap_create('appmap', from_file='.local.env=./.local.env',)

k8s_yaml([
    'k8s/flask-balancer.yaml',
    'k8s/mysql-balancer.yaml', 'k8s/mysql-deployment.yaml','k8s/persistentvolume.yaml', 
    'k8s/persistentclaim.yaml',
    ])

k8s_resource('mysql-deploy', labels='Mysql', resource_deps=['mysql-pv-volume', 'mysql-pv-claim'], )


docker_build(
            'flaskapp', 
            extra_tag='flaskapp:latest',
            context='.',
            live_update=[sync('app', '/app'),],
            pull=True
            )

deployment_create(
    'flaskapp', 
    image='flaskapp',
    command=['sleep', '999999'],
    resource_deps=['appmap:ConfigMap:default'],
    
    # command=['python3', 'app.py', 'runserver', '--host', '0.0.0.0', '-d', '-r'], 
    )

k8s_resource(workload='flaskapp', new_name='flaskapp', labels='flaskapp',resource_deps=['flask-secrets', 'appmap:ConfigMap:default'])

syncback(
    'syncback-flask', 
    'flaskapp',
    '/app/',
    target_dir='app/',
    paths=['app.py','lib/','templates/'],
    labels='support',
    )
