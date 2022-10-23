from pycypher.plugin_loader import load_plugins
from pycypher.plugin_factory import instantiate as plugin_instantiate

def test_load_plugins():
    load_plugins()

    aes_cypher = plugin_instantiate({
      "type": "aes",
      "random_32_key": "Sixteen byte keySixteen byte key"
    })

    rsa_cypher = plugin_instantiate({
      "type": "rsa",
      "keysize": 512,
      "version": 2,
      "public_key": None,
      "private_key": None
    })

    # TODO: put some asserts here, later
    print(aes_cypher)
    print(rsa_cypher)
    print(aes_cypher.encrypt("UALTER"))
    print(rsa_cypher.encrypt("JUNIOR"))