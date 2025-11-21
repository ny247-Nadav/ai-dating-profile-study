import random


MALE_IMAGE_URL = "https://fortune.com/img-assets/wp-content/uploads/2025/05/GettyImages-2215203788-e1747765808923.jpg?w=1440&q=75"
FEMALE_IMAGE_URL = "https://bidenwhitehouse.archives.gov/wp-content/uploads/2025/01/harris-profile-21.png"

BIOS = [
    # SAME 20 BIOS AS BEFORE
    "Teacher by day, amateur chef by night. I love quiet coffee shops, long walks, and Sunday brunch with friends. Looking for someone kind, grounded, and ready to laugh at bad puns.",
    "Tech worker who escapes screens with books, live music, and weekend hikes. I value honesty, curiosity, and good communication. Let’s see if we can make each other’s playlists better.",
    "NYC transplant who still gets excited about the skyline. Into movies, board games, and exploring new neighborhoods. Looking for a caring partner who enjoys both going out and staying in.",
    "Big fan of cozy dinners, wandering through museums, and talking about everything from podcasts to politics. Friends describe me as thoughtful, reliable, and a good listener.",
    "Fitness is my reset button—runs in the park, yoga classes, and trying new healthy recipes. I’m looking for someone warm, supportive, and open-minded about life and relationships.",
    "I love hosting friends, making way too much pasta, and discovering small local spots. Family and close friendships are a big part of my life. Looking for someone genuine and kind.",
    "Book lover, plant caretaker, and frequent movie re-watcher. I appreciate people who are emotionally mature, honest, and not afraid of real conversations.",
    "Weekdays are busy with work, but I always make time for friends, music, and good food. I’m hoping to meet someone who is thoughtful, affectionate, and looking for something real.",
    "I’m a mix of introvert and extrovert: I love evenings out with friends but also love quiet nights in. Looking for someone respectful, communicative, and emotionally intelligent.",
    "I enjoy traveling when I can, but I’m just as happy discovering new corners of my own city. I value kindness, stability, and a shared sense of humor.",
    "I’m close with my family and deeply value loyalty and support. My ideal evening is cooking together, sharing stories, and finding reasons to laugh about the day.",
    "Curious by nature—I love learning new things, whether it’s a recipe, a podcast topic, or a new neighborhood. Looking for a partner who is kind, patient, and open-hearted.",
    "Concerts, bookstores, and late-night conversations are my favorite kind of weekend. I appreciate people who are sincere, steady, and comfortable being themselves.",
    "I’m pretty grounded: I enjoy my work, take care of my people, and make time for small joys like coffee walks and sunsets. Hoping to meet someone who feels the same.",
    "I like to keep things balanced: staying active, seeing friends, and leaving space to just breathe. Looking for someone caring, thoughtful, and emotionally aware.",
    "I love trying new restaurants, discovering hidden parks, and planning small getaways. My ideal match is empathetic, communicative, and ready to build something meaningful.",
    "Friends would say I’m reliable, easygoing, and quietly funny. I’m happiest when I’m with good company, sharing food, stories, or a show we’re both into.",
    "I’m drawn to people who are honest, kind, and a little playful. I enjoy simple things: walks, coffee dates, and evenings where the conversation just flows.",
    "I like a slow morning, a good playlist, and a day that includes at least one small adventure. Looking for someone who is genuine, caring, and interested in a real connection.",
    "Life is busy but I try to prioritize what matters: relationships, health, and learning. If you’re thoughtful, kind, and ready for something sincere, we might get along well.",
]

NUM_PROFILES_PER_PARTICIPANT = 10


def build_profiles(attraction_preference: str):
    """
    Build 10 profiles based on participant's attraction:
    - "Men" → 10 male profiles
    - "Women" → 10 female profiles
    - "Both" → 5 male + 5 female shuffled
    """

    # Build 20 male profiles
    male_profiles = [
        {
            "profile_id": f"m{i}",
            "gender": "man",
            "image_url": MALE_IMAGE_URL,
            "bio": BIOS[i - 1],
        }
        for i in range(1, 21)
    ]

    # Build 20 female profiles
    female_profiles = [
        {
            "profile_id": f"w{i}",
            "gender": "woman",
            "image_url": FEMALE_IMAGE_URL,
            "bio": BIOS[i - 1],
        }
        for i in range(1, 21)
    ]

    if attraction_preference == "Men":
        return random.sample(male_profiles, NUM_PROFILES_PER_PARTICIPANT)

    if attraction_preference == "Women":
        return random.sample(female_profiles, NUM_PROFILES_PER_PARTICIPANT)

    # BOTH → randomly select 5 male + 5 female
    chosen_m = random.sample(male_profiles, 5)
    chosen_w = random.sample(female_profiles, 5)
    combined = chosen_m + chosen_w
    random.shuffle(combined)
    return combined
