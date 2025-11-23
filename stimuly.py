import random

NUM_PROFILES_PER_PARTICIPANT = 10

# These will be replaced later — but good for now
MALE_IMAGE_URLS = [
    "https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg",
    "hhttps://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg",
]

FEMALE_IMAGE_URLS = [
    "https://upload.wikimedia.org/wikipedia/commons/1/12/Kamala_Harris_Vice_Presidential_Portrait_2021.jpg","https://upload.wikimedia.org/wikipedia/commons/9/9c/Kamala_Harris_2023_Speaking.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/0/00/Kamala_Harris_DNC_2019.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/4/40/Kamala_Harris_in_the_Senate.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/7/79/Kamala_Harris_ceremony_2021.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/2/2e/Kamala_Harris_Portrait_Smile.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/6/6b/Kamala_Harris_Campaign_Stop_2024.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/5/52/Kamala_Harris_Office_2022.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/8/8a/Kamala_Harris_Rally_Speech_2019.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/6/61/Kamala_Harris_Interview_2020.jpg",
]

MALE_BIOS = [
    "Former business leader who enjoys golf, big gatherings, and lively conversations. I appreciate confidence, loyalty, and humor.",
    "I like staying active, meeting new people, and keeping things exciting. Looking for someone who’s fun, sharp, and enjoys a bit of adventure.",
    "Work keeps me busy, but I always make time for great food, good company, and strong discussions. Seeking someone warm and witty.",
    "Family-oriented, driven, and always planning the next big goal. I value honesty, passion, and ambition.",
    "I enjoy traveling, social events, and relaxing with friends. Looking for someone charismatic and open-hearted.",
    "Love the energy of big cities, great restaurants, and meaningful conversations. Seeking someone who knows what they want.",
    "Balanced between work and life: I enjoy sports, good stories, and memorable evenings. Looking for a thoughtful connection.",
    "Focused, committed, and generous with the people I care about. Hoping to meet someone grounded and kind.",
    "I appreciate confidence, humor, and someone who enjoys both quiet nights and spontaneous plans.",
    "Leader at heart, companion by choice. Looking for someone who’s supportive, honest, and ready for something real.",
]


FEMALE_BIOS = [
    "Dedicated professional who loves community, family time, and discovering new places. Looking for someone caring and thoughtful.",
    "I enjoy long walks, great conversations, and trying new foods. Seeking someone kind and emotionally intelligent.",
    "Passionate about my work but still love slow weekends, good music, and time with friends. Looking for sincerity and warmth.",
    "Balanced, curious, and always open to new experiences. Hoping to meet someone stable and communicative.",
    "I value compassion, humor, and authenticity. Ideal date? Coffee, a walk, and conversation that flows naturally.",
    "I love learning, exploring, and finding small joys in everyday life. Seeking someone genuine and open-minded.",
    "Family is important to me, as are loyalty, connection, and shared values. Looking for someone grounded and supportive.",
    "I enjoy travel, culture, and supporting the people I care about. Hoping to meet someone thoughtful and steady.",
    "Hardworking but playful when it matters — looking for someone respectful, warm, and ready for something intentional.",
    "I appreciate kindness, clear communication, and emotional maturity. Let’s build something meaningful if the connection is right.",
]

MALE_FIXED_CHOICES = [
    {"age": "24", "race": "White", "activities": ["Never smoking", "Socially drinking", "Hiking", "Tech"]},
    {"age": "25", "race": "Black", "activities": ["Occasionally smoking", "Socially drinking", "Movies", "Cooking"]},
    {"age": "26", "race": "Asian", "activities": ["Never smoking", "Never drinking", "Hiking", "Art", "Travel"]},
    {"age": "27", "race": "Latino", "activities": ["Never smoking", "Regularly drinking", "Movies", "Cooking", "Tech"]},
    {"age": "28", "race": "White", "activities": ["Occasionally smoking", "Socially drinking", "Hiking", "Travel"]},
    {"age": "29", "race": "Mixed Race", "activities": ["Never smoking", "Never drinking", "Movies", "Art"]},
    {"age": "30", "race": "Black", "activities": ["Regularly smoking", "Socially drinking", "Cooking", "Tech", "Travel"]},
    {"age": "31", "race": "Asian", "activities": ["Never smoking", "Socially drinking", "Hiking", "Movies", "Art"]},
    {"age": "24", "race": "Latino", "activities": ["Occasionally smoking", "Regularly drinking", "Tech", "Travel"]},
    {"age": "25", "race": "Other", "activities": ["Never smoking", "Never drinking", "Hiking", "Cooking", "Art"]},
]

FEMALE_FIXED_CHOICES = [
    {"age": "24", "race": "White", "activities": ["Never smoking", "Socially drinking", "Movies", "Art", "Travel"]},
    {"age": "25", "race": "Black", "activities": ["Never smoking", "Never drinking", "Hiking", "Cooking"]},
    {"age": "26", "race": "Asian", "activities": ["Occasionally smoking", "Socially drinking", "Movies", "Tech"]},
    {"age": "27", "race": "Latino", "activities": ["Never smoking", "Socially drinking", "Cooking", "Art", "Travel"]},
    {"age": "28", "race": "White", "activities": ["Never smoking", "Never drinking", "Hiking", "Movies", "Tech"]},
    {"age": "29", "race": "Mixed Race", "activities": ["Occasionally smoking", "Socially drinking", "Art", "Travel"]},
    {"age": "30", "race": "Black", "activities": ["Never smoking", "Regularly drinking", "Movies", "Cooking", "Tech"]},
    {"age": "31", "race": "Asian", "activities": ["Never smoking", "Socially drinking", "Hiking", "Art"]},
    {"age": "24", "race": "Latino", "activities": ["Occasionally smoking", "Never drinking", "Cooking", "Travel"]},
    {"age": "25", "race": "Other", "activities": ["Never smoking", "Socially drinking", "Movies", "Tech", "Art"]},
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