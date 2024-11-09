from pydantic import BaseModel
from enum import Enum
from typing import Optional

class Allergies(Enum):
    # Common allergens that can trigger severe reactions in sensitive individuals
    PEANUT = "peanut"             # Found in peanuts and peanut-based products
    TREE_NUT = "tree_nut"         # Includes almonds, walnuts, cashews, hazelnuts, etc.
    MILK = "milk"                 # Found in dairy products, casein, whey
    FISH = "fish"                 # Includes fish like salmon, tuna, cod, etc.
    SHELLFISH = "shellfish"       # Includes crustaceans (shrimp, crab, lobster) and mollusks
    WHEAT = "wheat"               # Found in wheat-based products; also a source of gluten
    SOY = "soy"                   # Found in soybeans, tofu, soy sauce, and soy-based products
    GLUTEN = "gluten"             # Found in wheat, barley, rye, and other gluten-containing grains
    EGG = "egg"                   # Found in eggs and egg-based products
    SESAME = "sesame"             # Found in sesame seeds and sesame oil
    MUSTARD = "mustard"           # Found in mustard seeds, mustard sauces, and seasonings
    SULFITES = "sulfites"         # Preservatives found in wine, dried fruits, and some processed foods
    CORN = "corn"                 # Found in corn-based products like cornmeal, corn syrup, and cornstarch
    CELERY = "celery"             # Found in celery stalks, seeds, and related products
    LUPIN = "lupin"               # Found in lupin flour and some gluten-free products
    MOLLUSKS = "mollusks"         # Includes shellfish like clams, mussels, oysters, and scallops

class FoodIntolerance(Enum):
    # Food intolerances can lead to digestive discomfort and other mild to moderate reactions
    LACTOSE = "lactose"           # Found in milk and dairy products; issues due to lactase enzyme deficiency
    GLUTEN = "gluten"             # Found in wheat, barley, and rye; causes issues for gluten-sensitive individuals
    HISTAMINE = "histamine"       # Found in aged cheese, wine, and fermented products; affects histamine-sensitive individuals
    CAFFEINE = "caffeine"         # Found in coffee, tea, chocolate, and energy drinks; affects caffeine-sensitive individuals
    FRUCTOSE = "fructose"         # Found in fruits, honey, and some vegetables; issues in people with fructose malabsorption
    FODMAPS = "fodmaps"           # Found in certain fruits, vegetables, grains, and dairy; problematic for IBS sufferers
    SULFITES = "sulfites"         # Found in wine, dried fruits, and certain processed foods; can cause digestive and respiratory issues
    SALICYLATES = "salicylates"   # Found in certain fruits, vegetables, and spices; affects salicylate-sensitive individuals
    MSG = "msg"                   # Monosodium glutamate, found in some processed foods; can trigger symptoms in sensitive people
    CASEIN = "casein"             # A protein in milk; issues for people with casein intolerance or milk protein allergy
    YEAST = "yeast"               # Found in bread, beer, and fermented products; affects those with yeast intolerance
    NIGHTSHADES = "nightshades"   # Includes tomatoes, potatoes, peppers, eggplant; affects people sensitive to nightshades

class NutrientRestrictions(BaseModel):
    sugars_per_day: Optional[int] = None
    sodium_per_day: Optional[int] = None
    carbohydrates_per_day: Optional[int] = None
    cholesterol_per_day: Optional[int] = None
    saturated_fats_per_day: Optional[int] = None
    trans_fats_per_day: Optional[int] = None
    caffeine_per_day: Optional[int] = None
    alcohol_per_day: Optional[int] = None

    class Config:
        orm_mode = True

class MedicalCondition(Enum):
    # Diabetes: Limit sugar intake, refined carbs, and processed foods.
    DIABETES = "diabetes"  # Restricted: Sugar, refined carbohydrates

    # Hypertension: Reduce sodium intake, avoid processed and salty foods.
    HYPERTENSION = "hypertension"  # Restricted: Sodium, processed foods

    # High Cholesterol: Limit saturated fats, trans fats, and cholesterol-heavy foods.
    HIGH_CHOLESTEROL = "high_cholesterol"  # Restricted: Saturated fats, trans fats, cholesterol

    # Heart Disease: Focus on low-fat, low-sodium, and high-fiber foods.
    HEART_DISEASE = "heart_disease"  # Restricted: Saturated fats, sodium, processed meats

    # Kidney Disease: Limit protein, sodium, potassium, and phosphorus.
    KIDNEY_DISEASE = "kidney_disease"  # Restricted: Sodium, potassium, phosphorus, high protein

    # Liver Disease: Avoid alcohol, limit fats, and reduce salt.
    LIVER_DISEASE = "liver_disease"  # Restricted: Alcohol, saturated fats, sodium

    # Irritable Bowel Syndrome (IBS): Avoid FODMAPs, artificial sweeteners, and caffeine.
    IBS = "ibs"  # Restricted: FODMAPs, artificial sweeteners, caffeine

    # Celiac Disease: Strictly avoid gluten.
    CELIAC_DISEASE = "celiac_disease"  # Restricted: Gluten

    # Gout: Limit purine-rich foods like red meat and certain seafood.
    GOUT = "gout"  # Restricted: Purines (found in red meat, organ meats, certain seafood)

    # Osteoporosis: Limit sodium and caffeine; focus on calcium and vitamin D.
    OSTEOPOROSIS = "osteoporosis"  # Restricted: Sodium, caffeine

    # Anemia: Limit high-calcium foods with iron-rich meals (to improve iron absorption).
    ANEMIA = "anemia"  # Restricted: High calcium intake with iron-rich meals (calcium interferes with iron absorption)

    # Acid Reflux/GERD: Avoid acidic foods, caffeine, and fatty/spicy foods.
    GERD = "gerd"  # Restricted: Acidic foods, caffeine, fatty/spicy foods

    # Lactose Intolerance: Avoid lactose-containing dairy products.
    LACTOSE_INTOLERANCE = "lactose_intolerance"  # Restricted: Lactose (dairy products)

    # High Triglycerides: Reduce added sugars, alcohol, and refined carbohydrates.
    HIGH_TRIGLYCERIDES = "high_triglycerides"  # Restricted: Added sugars, alcohol, refined carbohydrates

    # Migraine: Avoid common migraine triggers like tyramine, caffeine, and alcohol.
    MIGRAINE = "migraine"  # Restricted: Tyramine, caffeine, alcohol

    # Polycystic Ovary Syndrome (PCOS): Limit sugar, refined carbs, and trans fats.
    PCOS = "pcos"  # Restricted: Sugar, refined carbohydrates, trans fats

    # Hypothyroidism: Limit soy, cruciferous vegetables in excess, and processed foods.
    HYPOTHYROIDISM = "hypothyroidism"  # Restricted: Soy, cruciferous vegetables (in large amounts)

    # Inflammatory Bowel Disease (IBD): Avoid high-fiber foods, spicy foods, and alcohol during flare-ups.
    IBD = "ibd"  # Restricted: High fiber, spicy foods, alcohol (during flare-ups)

    # Pregnancy: Avoid certain types of fish (high mercury), unpasteurized products, and undercooked meats.
    PREGNANCY = "pregnancy"  # Restricted: High-mercury fish, unpasteurized products, undercooked meats

    # Epilepsy (Ketogenic Diet): Low-carb, high-fat; avoid sugar and refined carbs.
    EPILEPSY = "epilepsy"  # Restricted: Sugar, refined carbohydrates (often on ketogenic diet)

    # Histamine Intolerance: Avoid histamine-rich foods like aged cheese, alcohol, and fermente

class DietaryPrefence(Enum):
    VEGAN = "vegan"
    VEGETARIAN = "vegetarian"
    HALAL = "halal"

class MedicalPreference(BaseModel):
    allergies: Optional[Allergies] = None
    medical_condition: Optional[MedicalCondition] = None
    food_intolerance: Optional[FoodIntolerance] = None
    dietary_preference: Optional[DietaryPrefence] = None

    