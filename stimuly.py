import random

NUM_PROFILES_PER_PARTICIPANT = 10


MALE_IMAGE_URLS = [
    "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=400&fit=crop&crop=faces",  # White, 24, business professional
    "https://images.unsplash.com/photo-1506277886164-e25aa3f4ef7f?w=400&h=400&fit=crop&crop=faces",  # Black, 25, active/adventure
    "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&h=400&fit=crop&crop=faces",  # Asian, 26, cooking enthusiast
    "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&h=400&fit=crop&crop=faces",  # Latino, 27, travel enthusiast
    "https://images.unsplash.com/photo-1507591064344-4c6ce005b128?w=400&h=400&fit=crop&crop=faces",  # White, 28, travel/social
    "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&h=400&fit=crop&crop=faces",  # Mixed Race, 29, foodie
    "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=400&h=400&fit=crop&crop=faces",  # Black, 30, sports/movies
    "https://images.unsplash.com/photo-1521119989659-a83eee488004?w=400&h=400&fit=crop&crop=faces",  # Asian, 31, hiking/art
    "https://images.unsplash.com/photo-1508341591423-4347099e1f19?w=400&h=400&fit=crop&crop=faces",  # Latino, 24, cooking/movies
    "https://images.unsplash.com/photo-1519345182560-3f2917c472ef?w=400&h=400&fit=crop&crop=faces",  # Other, 25, tech enthusiast
]


FEMALE_IMAGE_URLS = [
    "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&h=400&fit=crop&crop=faces",  # White, 24, professional/travel
    "https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=400&h=400&fit=crop&crop=faces",  # Black, 25, hiking/cooking
    "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=400&h=400&fit=crop&crop=faces",  # Asian, 26, movies/art
    "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=400&h=400&fit=crop&crop=faces",  # Latino, 27, cooking/art/travel
    "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&h=400&fit=crop&crop=faces",  # White, 28, hiking
    "https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?w=400&h=400&fit=crop&crop=faces",  # Mixed Race, 29, tech/movies
    "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=400&h=400&fit=crop&crop=faces",  # Black, 30, cooking/movies
    "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?w=400&h=400&fit=crop&crop=faces",  # Asian, 31, cooking/travel
    "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=400&h=400&fit=crop&crop=faces",  # Latino, 24, cooking/art
    "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&h=400&fit=crop&crop=faces",  # Other, 25, tech/movies/art
]

MALE_BIOS = [
    "Former business leader who enjoys golf, big gatherings, and lively conversations. I appreciate confidence, loyalty, and humor. Love networking events and weekend rounds on the course.",
    "I like staying active, meeting new people, and keeping things exciting. You'll find me hiking trails on weekends or trying new adventure sports. Looking for someone who's fun, sharp, and enjoys a bit of adventure.",
    "Work keeps me busy, but I always make time for great food, good company, and strong discussions. I love cooking elaborate meals and exploring new restaurants. Seeking someone warm and witty.",
    "Family-oriented, driven, and always planning the next big goal. I value honesty, passion, and ambition. When I'm not working, I'm usually traveling or exploring new places.",
    "I enjoy traveling, social events, and relaxing with friends. Love discovering new cultures and cuisines. Looking for someone charismatic and open-hearted who shares my wanderlust.",
    "Love the energy of big cities, great restaurants, and meaningful conversations. I'm a foodie who enjoys cooking at home and trying new spots. Seeking someone who knows what they want.",
    "Balanced between work and life: I enjoy sports, good stories, and memorable evenings. I'm into movies, both watching and discussing them. Looking for a thoughtful connection.",
    "Focused, committed, and generous with the people I care about. I unwind by hiking in nature or enjoying quiet art galleries. Hoping to meet someone grounded and kind.",
    "I appreciate confidence, humor, and someone who enjoys both quiet nights and spontaneous plans. Love cooking together, watching movies, or just having deep conversations.",
    "Leader at heart, companion by choice. Tech enthusiast who loves building things and exploring new innovations. Looking for someone who's supportive, honest, and ready for something real.",
]


FEMALE_BIOS = [
    "Dedicated professional who loves community, family time, and discovering new places. I'm always planning my next travel adventure. Looking for someone caring and thoughtful.",
    "I enjoy long walks, great conversations, and trying new foods. You'll often find me hiking on weekends or experimenting in the kitchen. Seeking someone kind and emotionally intelligent.",
    "Passionate about my work but still love slow weekends, good music, and time with friends. I unwind by watching movies or visiting art galleries. Looking for sincerity and warmth.",
    "Balanced, curious, and always open to new experiences. I love exploring art, trying new cuisines, and traveling to new places. Hoping to meet someone stable and communicative.",
    "I value compassion, humor, and authenticity. Ideal date? Coffee, a walk, and conversation that flows naturally. I enjoy hiking and cooking together.",
    "I love learning, exploring, and finding small joys in everyday life. Tech and movies are my go-to for relaxation. Seeking someone genuine and open-minded.",
    "Family is important to me, as are loyalty, connection, and shared values. I enjoy cooking for loved ones and watching movies together. Looking for someone grounded and supportive.",
    "I enjoy travel, culture, and supporting the people I care about. Love exploring new places and trying local cuisines. Hoping to meet someone thoughtful and steady.",
    "Hardworking but playful when it matters — looking for someone respectful, warm, and ready for something intentional. I love cooking, art, and meaningful conversations.",
    "I appreciate kindness, clear communication, and emotional maturity. Tech enthusiast who loves movies and art. Let's build something meaningful if the connection is right.",
]

MALE_FIXED_CHOICES = [
    {"age": "24", "race": "White", "activities": ["Never smoking", "Socially drinking", "Tech"]},  # Golf, business, networking
    {"age": "25", "race": "Black", "activities": ["Occasionally smoking", "Socially drinking", "Hiking"]},  # Active, adventure sports
    {"age": "26", "race": "Asian", "activities": ["Never smoking", "Never drinking", "Cooking"]},  # Great food, cooking
    {"age": "27", "race": "Latino", "activities": ["Never smoking", "Regularly drinking", "Travel"]},  # Traveling, exploring
    {"age": "28", "race": "White", "activities": ["Occasionally smoking", "Socially drinking", "Travel"]},  # Traveling, social events
    {"age": "29", "race": "Mixed Race", "activities": ["Never smoking", "Never drinking", "Cooking"]},  # Foodie, restaurants
    {"age": "30", "race": "Black", "activities": ["Regularly smoking", "Socially drinking", "Movies"]},  # Sports, movies, stories
    {"age": "31", "race": "Asian", "activities": ["Never smoking", "Socially drinking", "Hiking", "Art"]},  # Hiking, art galleries
    {"age": "24", "race": "Latino", "activities": ["Occasionally smoking", "Regularly drinking", "Cooking", "Movies"]},  # Cooking, movies, conversations
    {"age": "25", "race": "Other", "activities": ["Never smoking", "Never drinking", "Tech"]},  # Tech enthusiast
]

FEMALE_FIXED_CHOICES = [
    {"age": "24", "race": "White", "activities": ["Never smoking", "Socially drinking", "Travel"]},  # Discovering new places, travel
    {"age": "25", "race": "Black", "activities": ["Never smoking", "Never drinking", "Hiking", "Cooking"]},  # Long walks, hiking, new foods
    {"age": "26", "race": "Asian", "activities": ["Occasionally smoking", "Socially drinking", "Movies", "Art"]},  # Good music, art galleries, movies
    {"age": "27", "race": "Latino", "activities": ["Never smoking", "Socially drinking", "Cooking", "Art", "Travel"]},  # New experiences, art, cuisines, travel
    {"age": "28", "race": "White", "activities": ["Never smoking", "Never drinking", "Hiking"]},  # Coffee, walks, hiking
    {"age": "29", "race": "Mixed Race", "activities": ["Occasionally smoking", "Socially drinking", "Tech", "Movies"]},  # Learning, exploring, tech, movies
    {"age": "30", "race": "Black", "activities": ["Never smoking", "Regularly drinking", "Cooking", "Movies"]},  # Family, cooking, movies
    {"age": "31", "race": "Asian", "activities": ["Never smoking", "Socially drinking", "Cooking", "Travel"]},  # Travel, culture, cuisines
    {"age": "24", "race": "Latino", "activities": ["Occasionally smoking", "Never drinking", "Cooking", "Art"]},  # Cooking, art, conversations
    {"age": "25", "race": "Other", "activities": ["Never smoking", "Socially drinking", "Tech", "Movies", "Art"]},  # Tech, movies, art
]


def build_profiles(attraction_preference: str):
    """
    Build 10 paired profiles (image + fixed-choice + bio), returned in random order.

    - Men   → 10 male profiles (random order)
    - Women → 10 female profiles (random order)
    - Both  → 5 male + 5 female (mixed + random order)
    """

    male_profiles = [
        {
            "profile_id": f"m{i+1}",
            "gender": "man",
            "image_url": MALE_IMAGE_URLS[i],
            "bio": MALE_BIOS[i],
            "fixed_choice": MALE_FIXED_CHOICES[i],
        }
        for i in range(10)
    ]

    female_profiles = [
        {
            "profile_id": f"w{i+1}",
            "gender": "woman",
            "image_url": FEMALE_IMAGE_URLS[i],
            "bio": FEMALE_BIOS[i],
            "fixed_choice": FEMALE_FIXED_CHOICES[i],
        }
        for i in range(10)
    ]

    if attraction_preference == "Men":
        profiles = male_profiles.copy()

    elif attraction_preference == "Women":
        profiles = female_profiles.copy()

    else:  # "Both"
        chosen_m = random.sample(male_profiles, 5)
        chosen_w = random.sample(female_profiles, 5)
        profiles = chosen_m + chosen_w

    random.shuffle(profiles)
    return profiles