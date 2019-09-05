from django.db import models


class Monster(models.Model):
    """
    This current outline is based on the json structure found
    here: https://gist.github.com/tkfu/9819e4ac6d529e225e9fc58b358c3479
    I would like to determine what the best strategy would be for
    storing this data in the future.
    """
    name = models.CharField(max_length=50)
    armor_class = models.IntegerField()
    hit_points = models.CharField(max_length=25)  # TODO: Better way? EX] hit_points = '135 (18d10 + 36)'
    speed = models.CharField(max_length=50)  # TODO: Better way? EX] speed = '30 ft., swim 40 ft.'
    # TODO: Determine if the stats can be stored in a better way
    STR = models.IntegerField()
    DEX = models.IntegerField()
    CON = models.IntegerField()
    INT = models.IntegerField()
    WIS = models.IntegerField()
    CHA = models.IntegerField()
    STR_mod = models.IntegerField()
    DEX_mod = models.IntegerField()
    CON_mod = models.IntegerField()
    INT_mod = models.IntegerField()
    WIS_mod = models.IntegerField()
    CHA_mod = models.IntegerField()
    saving_throws = models.CharField(max_length=50)  # TODO: Better way? EX] CON +6, STR +5, ...
    skills = models.CharField(max_length=100)  # TODO: Better way? EX] perception +3, history +2, ...
    senses = models.CharField(max_length=100)  # TODO: Better way? EX] Darkvision 120 ft.,  Passive Perception 20, ...
    languages = models.CharField(max_length=100)  # TODO: Better way? EX] Deep Speech, Telepathy 120 ft., ...
    challenge = models.IntegerField()
    experience = models.IntegerField()
    traits = models.TextField()  # Markdown input for formatting?
    actions = models.TextField()  # Markdown input for formatting?
    legendary_actions = models.TextField()  # Markdown input for formatting?
    img_url = models.CharField(max_length=255)  # TODO: Better way of storing a url?


