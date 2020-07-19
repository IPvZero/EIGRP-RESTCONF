import requests
from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.apis import http_method


def testconf(task, router_url, headers):
    restconf_url = f"https://{task.host.hostname}/restconf/"

    task.run(
        task=http_method,
        name="RESTCONF PUT_POST",
        method="put",
        url=restconf_url + router_url,
        auth=("john", "cisco"),
        headers=headers["put_post"],
        verify=False,
        json=task.host["configure"]
)

def main():
    requests.packages.urllib3.disable_warnings()

    router_url = "data/Cisco-IOS-XE-native:native/Cisco-IOS-XE-native:router"
    headers = {
        "get": {"Accept": "application/yang-data+json"},
        "put_post": {
            "Content-Type": "application/yang-data+json",
            "Accept": "application/yang-data+json, application/yang-data.errors+json",
        },
    }

    nr = InitNornir()
    result = nr.run(task=testconf,name="PUSHING EIGRP VIA RESTCONF",router_url=router_url,headers=headers,)

    print_result(result)

if __name__ == "__main__":
    main()
