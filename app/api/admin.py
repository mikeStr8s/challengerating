from django.contrib import admin

import api.models as mdl


admin.site.register(mdl.Monster)
admin.site.register(mdl.ArmorClass)
admin.site.register(mdl.MovementType)
admin.site.register(mdl.MonsterMovementSpeed)
admin.site.register(mdl.AbilityScore)
admin.site.register(mdl.MonsterSavingThrow)
admin.site.register(mdl.Skill)
admin.site.register(mdl.MonsterSkill)
admin.site.register(mdl.Sense)
admin.site.register(mdl.MonsterSense)
admin.site.register(mdl.Language)
admin.site.register(mdl.MonsterLanguage)
admin.site.register(mdl.Condition)
admin.site.register(mdl.DamageType)
admin.site.register(mdl.MonsterDamageImmunity)
admin.site.register(mdl.MonsterDamageResistance)
admin.site.register(mdl.MonsterDamageVulnerability)