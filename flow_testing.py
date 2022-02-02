import os
from flow.base_flow import compose_alter_flow, compose_flow

# Just run in a local execution context
if 1 == 0:
    compose_flow().run()

# Easy paralell with Dask
if 1 == 0:
    # make the package available to dask by pip installing the code in the
    # environment dask is running in.
    # start dask scheduler and dask worker
    # dask-scheduler --host=172.20.156.37
    # dask-worker tcp://172.20.156.37:8786 --nthreads=1
    from prefect.executors import dask

    executor = dask.DaskExecutor(address="172.20.156.37:8786")
    compose_flow().run(executor=executor)

# Easy orchastration with Prefect
if 1 == 0:
    # project should be created, first time = prefect create project 'pre-play'
    from prefect.storage import Local
    from prefect.executors import dask

    f = compose_alter_flow()
    f.storage = Local(
        stored_as_script=True,
        path="/home/prinsn/Code/prefect/repo/pre-play/flow_testing.py",
    )
    f.executor = dask.LocalDaskExecutor(scheduler="processes")
    f.register(project_name="pre-play")


# Dockerize the environment where the flow is running in
if 1 == 0:
    # project should be created, first time = prefect create project 'pre-play'
    from prefect.storage import Local
    from prefect.executors import dask
    from prefect.run_configs import DockerRun

    f = compose_alter_flow()
    f.storage = Local(
        stored_as_script=True,
        path="/home/prinsn/Code/prefect/repo/pre-play/flow_testing.py",
    )
    f.executor = dask.LocalDaskExecutor(scheduler="processes")
    f.register(project_name="pre-play")


if 1 == 0:
    # project should be created, first time = prefect create project 'pre-play'
    from prefect.storage import Docker
    from prefect.executors import dask
    from prefect.run_configs import DockerRun

    f = compose_alter_flow()
    # We inject the dockerfile because the import in the flow location path script requires the
    # flow package to be there, this is installed in the base dockerfile
    # Storage must be docker, can no longer be Local, docker agent does not accept this
    f.storage = Docker(
        dockerfile="Dockerfile",
        ignore_healthchecks=True,
        stored_as_script=True,
        path="/APP/flow_testing.py",
    )

    f.run_config = DockerRun(image="pre-play:latest")

    f.executor = dask.LocalDaskExecutor(scheduler="processes")
    f.register(project_name="pre-play")

# Dockerize the environment where the flow is running in
if 1 == 1:
    # project should be created, first time = prefect create project 'pre-play'
    # export PREFECT__CONTEXT__SECRETS__GHPAT=$(cat ~/....)
    from prefect.storage import GitHub
    from prefect.executors import dask
    from prefect.run_configs import DockerRun
    f = compose_flow()
    f.storage = GitHub(
        repo="prinsniels/pre-play",  # name of repo
        path="flow_testing.py",  # location of flow file in repo
        access_token_secret="GHPAT"  # name of personal access token secret
    )
    f.executor = dask.LocalDaskExecutor(scheduler="processes")
    f.register(project_name="pre-play")
