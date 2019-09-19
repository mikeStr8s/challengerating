from rest_framework import serializers

import api.models as mdl


class MonsterListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = mdl.Monster
        fields = ['url', 'name']


class MonsterSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return {
            'name': obj.name,
            'armor_class': str(obj.armor_class),
            'hit_points': obj.hit_points,
            'stats': {
                'STR': obj.STR,
                'DEX': obj.DEX,
                'CON': obj.CON,
                'INT': obj.INT,
                'WIS': obj.WIS,
                'CHA': obj.CHA
            },
            'challenge': {
                'rating': obj.challenge,
                'exp': obj.experience
            },
            'movement': { str(m.movement_type): m.value for m in obj.speeds.all() },
            'saving_throws': { str(s.ability_score): s.value for s in obj.saving_throws.all() },
            'skills': { str(s.skill): s.value for s in obj.skills.all() },
            'senses': { str(s.sense): s.note for s in obj.senses.all() },
            'languages': { str(l.language): l.note for l in obj.languages.all() },
            'condition_immunities': [ str(c) for c in obj.condition_immunities.all() ],
            'traits': obj.traits,
            'actions': obj.actions,
            'legendary_actions': obj.legendary_actions,
            'reactions': obj.reactions,
            'img_url': obj.img_url
        }