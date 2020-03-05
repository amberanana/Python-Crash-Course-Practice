# 6.3
# 6.3.1
user_0 = {
    'username': 'efermi',
    'first:': 'enrico',
    'last': 'fermi'
    }

for key, value in user_0.items():
    print('\nkey: ' + key)
    print("Value: " + value)

# for k, v in user_0.items()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# 6.3.2
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() +
              ", I see your favorite language is " + favorite_languages[name].title() + "!")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
if 'erin' not in favorite_languages.keys():
    print("Erin, please take your poll!")

# 6.3.3
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# 6.3.4
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("Then following language have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("The following language have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
