
import random
import string

def generate_usernames(count):
    results = set()

    while len(results) < count:
        letters = random.sample(string.ascii_lowercase, 2)
        number = random.choice(string.digits)

        username = ''.join(
            random.sample(letters + [number], 3)
        )

        results.add(username)

    return sorted(results)

if __name__ == "__main__":
    usernames = generate_usernames(1000)

    with open("usernames.txt", "w") as file:
        file.write("\n".join(usernames))

    print(f"Generated {len(usernames)} usernames")
  
