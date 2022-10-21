from pycypher.plugin_loader import load_plugins
from pycypher.plugin_factory import instantiate as plugin_instantiate

def test_load_plugins():
    load_plugins()

    aes_cypher = plugin_instantiate({
      "type": "aes",
      "random_key": "1234567890"
    })

    rsa_cypher = plugin_instantiate({
      "type": "rsa",
      "keysize": 2048,
      "version": 2
    })

    # TODO: put some asserts here, later
    print(aes_cypher)
    print(rsa_cypher)
    print(aes_cypher.encrypt("UALTER"))
    print(rsa_cypher.encrypt("JUNIOR"))