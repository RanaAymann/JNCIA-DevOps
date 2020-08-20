from jnpr.junos import Device
from jnpr.junos.utils.config import Config

if __name__ == '__main__':

    dev = Device(host="10.1.1.1", user="lab", password="lab123")
    dev.open()
    conf = Config(dev)
    data = """ interfaces {
        ge-0/0/1 {
            unit 0 {
                family inet {
                    address 10.10.10.10/24
                    }
                    }
        }
    }"""
    conf.lock()
    conf.load(data, format='text')
    conf.pdiff()
    if conf.commit_check():
        conf.commit()
    else:
        conf.rollback()
    conf.unlock()
    dev.close()
