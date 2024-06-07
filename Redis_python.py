import redis
r = redis.Redis(host = 'localhost', port = 6379, decode_responses = True)
r.set('foo', 'bar')
# res = r.get('foo')
# print(res)
r.hset('user-session:123', mapping={
    'name': 'John',
    'surname': 'Smith'
})
res = r.hgetall('user-session:123')
print(res)