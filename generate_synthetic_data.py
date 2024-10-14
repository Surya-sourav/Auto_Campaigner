import random
import datetime
import csv
from faker import Faker
from tqdm import tqdm

# Initialize Faker
fake = Faker()

# Number of data points to generate
NUM_DATA_POINTS = 100_000

# Define categories and products
CATEGORIES = {
    'Electronics': ['Smartphone', 'Laptop', 'Headphones', 'Smartwatch', 'Camera'],
    'Fashion': ['T-Shirt', 'Jeans', 'Sneakers', 'Jacket', 'Watch'],
    'Home & Kitchen': ['Blender', 'Cookware Set', 'Coffee Maker', 'Air Fryer', 'Vacuum Cleaner'],
    'Books': ['Fiction Novel', 'Non-fiction Book', 'E-Reader', 'Magazine Subscription', 'Comic Book'],
    'Sports & Outdoors': ['Yoga Mat', 'Dumbbells', 'Running Shoes', 'Fitness Tracker', 'Bicycle'],
    'Beauty & Personal Care': ['Lipstick', 'Perfume', 'Moisturizer', 'Shampoo', 'Hair Dryer'],
    'Automotive': ['Car Charger', 'GPS Navigator', 'Car Cover', 'Air Freshener', 'Dash Cam'],
    'Toys & Games': ['Board Game', 'Puzzle', 'Action Figure', 'Doll', 'Lego Set'],
    'Health & Wellness': ['Vitamins', 'Supplement', 'First Aid Kit', 'Thermometer', 'Face Mask'],
    'Garden & Outdoor': ['Garden Tools', 'Grill', 'Lawn Mower', 'Plant Seeds', 'Patio Furniture']
}

OFFERS = [
    '10% off', '15% off', '20% off', 'Buy One Get One Free', 'Free Shipping',
    'Exclusive Discount', 'Limited-Time Offer', 'Clearance Sale', 'Special Promotion',
    'Loyalty Reward', 'Seasonal Sale', 'Holiday Special', 'New Arrival Discount'
]

GENDERS = ['Male', 'Female', 'Non-binary']
AGE_RANGE = (18, 70)

# Marketing message templates
MARKETING_TEMPLATES = [
    "Hi {Name}! {Greeting} Enjoy {Offer} on {Product}. {CallToAction}",
    "Hello {Name}, since you're in {Location}, we're offering you {Offer} on {Product}. {CallToAction}",
    "{Name}, exclusive deal for you! {Offer} on {Product}. {CallToAction}",
    "Dear {Name}, upgrade your {Category} with {Offer} on {Product}. {CallToAction}",
    "Hey {Name}, don't miss out on {Offer} on {Product}. Offer valid until {ExpiryDate}!",
    "{Name}, because you purchased {PastPurchase}, we thought you'd like {Product} at {Offer}. {CallToAction}"
]

CALL_TO_ACTIONS = [
    "Shop now and save big!",
    "Hurry, offer ends soon!",
    "Don't miss this exclusive deal!",
    "Limited stock available, act fast!",
    "Click here to claim your offer!",
    "Visit our store today!"
]

GREETINGS = [
    "Great news!",
    "Exciting offer just for you!",
    "Special announcement!",
    "We've got something special!",
    "Surprise!"
]

def generate_random_date(days_ahead=30):
    start_date = datetime.date.today()
    end_date = start_date + datetime.timedelta(days=days_ahead)
    random_date = start_date + datetime.timedelta(days=random.randint(1, days_ahead))
    return random_date.strftime("%B %d, %Y")

def generate_synthetic_data_point():
    # Customer Details
    name = fake.first_name()
    age = random.randint(*AGE_RANGE)
    gender = random.choice(GENDERS)
    location = fake.city()
    preferred_categories = random.sample(list(CATEGORIES.keys()), k=random.randint(1, 3))
    purchase_history = []
    for category in preferred_categories:
        product = random.choice(CATEGORIES[category])
        purchase_history.append(product)
    past_purchase = random.choice(purchase_history)

    # Current Offer
    category = random.choice(preferred_categories)
    product = random.choice(CATEGORIES[category])
    offer = random.choice(OFFERS)
    expiry_date = generate_random_date()

    # Input Text
    input_text = f"Name: {name}; Age: {age}; Gender: {gender}; Location: {location}; Preferred Categories: {', '.join(preferred_categories)}; Purchase History: {', '.join(purchase_history)}; Current Offer: {offer} on {product}."
    
    # Generate Marketing Message
    template = random.choice(MARKETING_TEMPLATES)
    greeting = random.choice(GREETINGS)
    call_to_action = random.choice(CALL_TO_ACTIONS)
    marketing_message = template.format(
        Name=name,
        Greeting=greeting,
        Offer=offer,
        Product=product,
        Category=category,
        Location=location,
        CallToAction=call_to_action,
        ExpiryDate=expiry_date,
        PastPurchase=past_purchase
    )

    return input_text, marketing_message

def generate_dataset(num_data_points):
    data = []
    for _ in tqdm(range(num_data_points), desc="Generating Data"):
        input_text, marketing_message = generate_synthetic_data_point()
        data.append({'input_text': input_text, 'target_text': marketing_message})
    return data

def save_dataset_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

# Generate the dataset
dataset = generate_dataset(NUM_DATA_POINTS)

# Save the dataset to a CSV file
save_dataset_to_csv(dataset, 'synthetic_marketing_dataset.csv')

print(f"Generated {NUM_DATA_POINTS} data points and saved to 'synthetic_marketing_dataset.csv'.")
