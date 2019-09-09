from django.db import models


class Monster(models.Model):
    name = models.CharField(max_length=50)  # Monster name
    armor_class = models.ForeignKey('ArmorClass', on_delete=models.CASCADE, related_name='monsters')
    hit_points = models.CharField(max_length=25)
    STR = models.IntegerField()
    DEX = models.IntegerField()
    CON = models.IntegerField()
    INT = models.IntegerField()
    WIS = models.IntegerField()
    CHA = models.IntegerField()
    senses = models.CharField(max_length=100)  # TODO: Better way? EX] Darkvision 120 ft.,  Passive Perception 20, ...
    languages = models.CharField(max_length=100)  # TODO: Better way? EX] Deep Speech, Telepathy 120 ft., ...
    challenge = models.IntegerField()
    experience = models.IntegerField()
    traits = models.TextField()  # Markdown input for formatting?
    actions = models.TextField()  # Markdown input for formatting?
    legendary_actions = models.TextField()  # Markdown input for formatting?
    img_url = models.CharField(max_length=255)  # TODO: Better way of storing a url?


class ArmorClass(models.Model):
    """
    Armor Class for monsters
    Example: { value: 16, note: 'Natural Armor' }
    """
    value = models.IntegerField()   # AC value
    note = models.CharField(max_length=100) # Any note or explaination for AC


class MovementTypes(models.Model):
    """
    Lookup table for movement types in Dungeons and Dragons
    Example: { name: 'Swimming' }
    """
    name = models.CharField(max_length=25)  # Name of movement type


class MonsterMovementSpeed(models.Model):
    """
    Monster movement speeds for each movement type required
    Example: { monster: 'Angry Fish', movement_type: 'Swimming', value: 35 }
    """
    monster = models.ForeignKey('Monster', on_delete=models.CASCADE, related_name='speeds')
    movement_type = models.ForeignKey('MovementType', on_delete=models.CASCADE, related_name='speeds')
    value = models.IntegerField()   # The speed in ft. that the monster moves


class AbilityScore(models.Model):
    """
    Lookup table for ability scores in Dungeons and Dragons
    Example: { name: 'Constitution' }
    """
    name = models.CharField(max_length=15)  # Name of the ability score


class MonsterSavingThrow(models.Model):
    """
    Monster saving throws and their associated modifiers
    Example: { monster: 'Angry Fish', ability_score: 'Constitution', value: -1 }
    """
    monster = models.ForeignKey('Monster', on_delete=models.CASCADE, related_name='saving_throws')
    ability_score = models.ForeignKey('AbilityScore', on_delete=models.CASCADE, related_name='saving_throws')
    value = models.IntegerField()   # The roll modifier value for monster saving throws


class Skill(models.Model):
    """
    Lookup table for skills in Dungeons and Dragons
    """
    name = models.CharField(max_length=25)


class MonsterSkill(models.Model):
    monster = models.ForeignKey('Monster', on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE, related_name='skills')
    value = models.IntegerField()   # The roll modifier value for monster skills

# TODO: BUILD OUT THE MODELS FOR SENSES AND LANGUAGES!!