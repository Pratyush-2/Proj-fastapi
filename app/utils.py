from . import schemas

def calculate_targets(profile: schemas.UserProfileCreate):
    """
    Calculates target calories, protein, carbs, and fats based on user profile.
    """
    if profile.gender.lower() == 'male':
        bmr = 88.362 + (13.397 * profile.weight_kg) + (4.799 * profile.height_cm) - (5.677 * profile.age)
    else:
        bmr = 447.593 + (9.247 * profile.weight_kg) + (3.098 * profile.height_cm) - (4.330 * profile.age)

    activity_multipliers = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'super_active': 1.9
    }
    
    activity_multiplier = activity_multipliers.get(profile.activity_level, 1.55)

    calories = bmr * activity_multiplier

    # Adjust calories based on goal
    if profile.goal == 'lose_weight':
        calories -= 500
    elif profile.goal == 'gain_weight':
        calories += 500

    # Calculate macronutrients
    protein = 1.9 * profile.weight_kg
    protein_calories = protein * 4
    
    fat_percentage = 0.25
    fat_calories = calories * fat_percentage
    fat = fat_calories / 9

    carb_calories = calories - protein_calories - fat_calories
    carbs = carb_calories / 4

    return round(calories), round(protein), round(carbs), round(fat)