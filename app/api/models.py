from django.db import models


class Monster(models.Model):
    name = models.CharField(max_length=50)
    armor_class = models.ForeignKey('ArmorClass', on_delete=models.CASCADE, related_name='monsters')
    hit_points = models.CharField(max_length=25)
    STR = models.IntegerField()
    DEX = models.IntegerField()
    CON = models.IntegerField()
    INT = models.IntegerField()
    WIS = models.IntegerField()
    CHA = models.IntegerField()
    challenge = models.IntegerField()
    experience = models.IntegerField()
    condition_immunities = models.ManyToManyField('Condition', related_name='monsters', blank=True)
    traits = models.TextField(null=True, blank=True)
    actions = models.TextField(null=True, blank=True)
    legendary_actions = models.TextField(null=True, blank=True)
    reactions = models.TextField(null=True, blank=True)
    img_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class ArmorClass(models.Model):
    """
    Armor Class for monsters
    Example: { value: 16, note: 'Natural Armor' }
    """
    value = models.IntegerField()
    note = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'armor classes'
    
    def __str__(self):
        if self.note:
            return '{0} - {1}'.format(self.value, self.note)
        return self.value


class MovementType(models.Model):
    """
    Lookup table for movement types in Dungeons and Dragons
    Example: { name: 'Swimming' }
    """
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class MonsterMovementSpeed(models.Model):
    """
    Monster movement speeds for each movement type required
    Example: { monster: 'Angry Fish', movement_type: 'Swimming', value: 35 }
    """
    monster = models.ForeignKey('Monster', on_delete=models.CASCADE, related_name='speeds')
    movement_type = models.ForeignKey('MovementType', on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return '{0}: {1} - {2}'.format(self.monster.name, self.movement_type.name, self.value)


class AbilityScore(models.Model):
    """
    Lookup table for ability scores in Dungeons and Dragons
    Example: { name: 'Constitution' }
    """
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class MonsterSavingThrow(models.Model):
    """
    Monster saving throws and their associated modifiers
    Example: { monster: 'Angry Fish', ability_score: 'Constitution', value: -1 }
    """
    monster = models.ForeignKey('Monster', on_delete=models.CASCADE, related_name='saving_throws')
    ability_score = models.ForeignKey('AbilityScore', on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return '{0}: {1} - {2}'.format(self.monster.name, self.ability_score.name, self.value)


class Skill(models.Model):
    """
    Lookup table for skills in Dungeons and Dragons
    """
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class MonsterSkill(models.Model):
    """
    Monster skills and their associated modifiers
    Example: { monster: 'Angry Fish', skill: 'intimidation', value: 3 }
    """
    monster = models.ForeignKey('Monster', on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return '{0}: {1} - {2}'.format(self.monster.name, self.skill.name, self.value)


class Sense(models.Model):
    """
    Lookup table for senses in Dungeons and Dragons
    """
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class MonsterSense(models.Model):
    """
    Monster senses and their associated modifiers
    Example: { monster: 'Angry Fish', sense: 'darkvision', note: '15ft' }
    """
    monster = models.ForeignKey('Monster', on_delete=models.CASCADE, related_name='senses')
    sense = models.ForeignKey('Sense', on_delete=models.CASCADE)
    note = models.CharField(max_length=255)

    def __str__(self):
        return '{0}: {1} - {2}'.format(self.monster.name, self.sense.name, self.note)


class Language(models.Model):
    """
    Lookup table for languages in Dungeons and Dragons
    """
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name


class MonsterLanguage(models.Model):
    """
    Monster senses and their associated modifiers
    Example: { monster: 'Angry Fish', language: 'common', note: 'Cannot speak' }
    """
    monster = models.ForeignKey('Monster', on_delete=models.CASCADE, related_name='languages')
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    note = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if self.note:
            return '{0}: {1} - {2}'.format(self.monster.name, self.language.name, self.note)
        return '{0}: {1}'.format(self.monster.name, self.language.name)


class Condition(models.Model):
    """
    Lookup table for conditions in Dungeons and Dragons
    """
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name


class DamageType(models.Model):
    """
    Lookup table for damage types in Dungeons and Dragons
    """
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class MonsterDamageImmunity(models.Model):
    """
    Monster damage immunities and their associated modifiers
    Example: { monster: 'Angry Fish', damage: 'Cold', note: 'Bludgeoning from nonmagical attacks' }
    """
    monster = models.ForeignKey('Monster', on_delete=models.CASCADE, related_name='immunities')
    damage = models.ForeignKey('DamageType', on_delete=models.CASCADE)
    note = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'monster damage immunities'
    
    def __str__(self):
        return '{0}: {1} - {2}'.format(self.monster.name, self.damage.name, self.note)


class MonsterDamageResistance(models.Model):
    """
    Monster damage resistances and their associated modifiers
    Example: { monster: 'Angry Fish', damage: 'Cold', note: 'Bludgeoning from nonmagical attacks' }
    """
    monster = models.ForeignKey('Monster', on_delete=models.CASCADE, related_name='resistances')
    damage = models.ForeignKey('DamageType', on_delete=models.CASCADE)
    note = models.CharField(max_length=255)

    def __str__(self):
        return '{0}: {1} - {2}'.format(self.monster.name, self.damage.name, self.note)


class MonsterDamageVulnerability(models.Model):
    """
    Monster damage Vulnerabilities and their associated modifiers
    Example: { monster: 'Angry Fish', damage: 'Cold', note: 'Piercing from nonmagical attacks' }
    """
    monster = models.ForeignKey('Monster', on_delete=models.CASCADE, related_name='vulnerabilities')
    damage = models.ForeignKey('DamageType', on_delete=models.CASCADE)
    note = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'monster damage vulnerabilities'
    
    def __str__(self):
        return '{0}: {1} - {2}'.format(self.monster.name, self.damage.name, self.note)