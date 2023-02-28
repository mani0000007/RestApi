def api_create_cluster(db_url, node_type_id):
    url = db_url + "/api/2.0/clusters/create"
    ac_token = "dapi941bd5a60931894d044e5d138a828a53-3"
    header = {"Authorization": "Bearer " + ac_token, "Content-Type": "application/json"}

    payload = {
            "num_workers": 0,
            "cluster_name": "Mani Cluster",
            "spark_version": "11.3.x-scala2.12",
            "spark_conf": {
                "spark.master": "local[*, 4]",
                "spark.databricks.cluster.profile": "singleNode"
            },
            "azure_attributes": {
                "first_on_demand": 1,
                "availability": "ON_DEMAND_AZURE",
                "spot_bid_max_price": -1
            },
            "node_type_id": "Standard_DS3_v2",
            "ssh_public_keys": [],
            "custom_tags": {
                "ResourceClass": "SingleNode"
            },
            "spark_env_vars": {
                "PYSPARK_PYTHON": "/databricks/python3/bin/python3"
            },
            "autotermination_minutes": 120,
            "enable_elastic_disk": True,
            "cluster_source": "UI",
            "init_scripts": [],
            "single_user_name": "manikumar.neerugatti@auropro.com",
            "data_security_mode": "LEGACY_SINGLE_USER_STANDARD",
            "runtime_engine": "STANDARD"
        }

    response = requests.post(url, headers=header, json=payload).json()
    return response["cluster_id"]

db_url = "https://adb-7837751364337038.18.azuredatabricks.net"
node_type_id = "Standard_DS3_v2"
cluster_id = api_create_cluster(db_url, node_type_id)
print("Created cluster with ID {}".format(cluster_id))
 
