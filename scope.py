# Local Scope
def my_func():
    y = 5
    print(y)

my_func()

# Global Scope
y = 5
def my_func():
    print(y)

def my_other_func():
    print(y)

my_func()
my_other_func()

# Example 1
z = 5

def my_func():
    z = 3
    print(z)

my_func()
print(z)

# Example 2
z = 5

def my_func():
    z = 3

    def my_other_func():
        z = 2
        print(z)
    
    my_other_func()

    print(z)

my_func()

print(z)