import math

def gravity_from_bh_radius(radius):
    return (radius / 5) ** 2 #the thing that does the dirty work, the gravity is proportional to the square of the radius, divided by 25 to get a more reasonable range of values. Adjust the divisor as needed to fit your specific requirements or constraints.


def generate_config(name, bh_radius):
    gravity = gravity_from_bh_radius(bh_radius)

    config = f"""
Singularity
{{
    name = {name}
    gravity = {gravity:.3f} 
}}
"""
    return config, gravity


# Example usage
if __name__ == "__main__":
    name = input("Black hole name: ")
    radius = float(input("Desired black hole radius: "))

    config_text, g = generate_config(name, radius)

    print("\n--- GENERATED CONFIG ---\n")
    print(config_text)
    print(f"Computed gravity: {g:.3f}")