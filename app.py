import redis


def main():
    try:
        r = redis.StrictRedis(host="localhost", port=6379, db=0)
        r.ping()
        print("Connected to Redis")
        return r
    except redis.ConnectionError:
        print("Connexion to Redis failed")


if __name__ == "__main__":
    main()
