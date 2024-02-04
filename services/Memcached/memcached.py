
import memcache


memcached_client = memcache.Client(['memcached:11211'], debug=0)


def get_with_memcached():
    mem_key='getAll'      
    result = memcached_client.get(mem_key)     
    if result:          
        print("Fetched from Memcached")          
        return result

def addToMemcached(data):
    print("data to ADD")
    print(data)          #[('kuba', 'kuba', 'kuba'), ('kuba2', 'kuba', 'kuba2')]
    print("data to ADD")
    memcached_client.set('getAll', data, time=3) 

       