from pydantic import BaseModel

class User(BaseModel):
    age: int
    gender: str
    height_cm: float
    weight_kg: float
    fitness_goals: str
    fitness_level: str
    days_available:str 
    time_per_session_mins: int
    exercise_preferences: str
    gym_equipment:str
    