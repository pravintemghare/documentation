# Helm

- Package Manager for kubernetes
- To pack YAML files and distrubuting them in public & private repositories
- Bundle of YAML files are called Helm Charts
- Create your own helm charts with helm
- Push them to helm repository (Helm Hub) 
- Download and use existing one

- Templating Engine
    - Define a common blueprint
    - Dynamic values are replaced by placeholders

{{ .Value... }}

Values are created in ``values.yaml`` file
``--set`` to use when running command

- Directory structure for helm charts

-- chartname/  -- Directory with the chart name
    -- Charts.yaml -- meta information about charts
    -- values.yaml -- values for the template files
    -- charts -- chart dependencies
    -- templates -- the actual template file

Optional README or license files

- Can be used in with same applications in different environment

## Release Management 
- Create or change deployment
- Stores copy of configuration
- Keeping track of all chart execution

## Disadvantage for Helm
- Tiller has to much power in inside the K8's cluster
- Security Issues
- In helm version 3 the Tiller is removed and it solves the security concers but makes it difficult to use


- Difference in helm version 2 & 3
- Helm version is divided in 2 part: Client (helm CLI)  &  Server (Tiller)


### Commands
``helm search keyword``  - to search helm charts
``helm install chartname`` - to install helm charts
``helm install --values=new_values.yaml chartname`` - to give a specific values file to override default file
``helm install --set value=value1 chartname`` to explicitly set some values
``helm upgrade chartname`` - to upgrade the chart version to new
``helm rollback chartname`` to rollback a particular deployment