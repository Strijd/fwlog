from firewall import ports

@compile
def port_list():
    return ({'squid': 'with-pf-enable',
             'ddclient': 'ssl-enabled',
             'minigupnpd': 'with-pf-enabled'
             }
            )