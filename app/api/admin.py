from django.contrib import admin

import api.models as mdl


class MonsterMovementSpeedInline(admin.TabularInline):
    model = mdl.MonsterMovementSpeed
    extra = 1


class MonsterDamageImmunityInline(admin.TabularInline):
    model = mdl.MonsterDamageImmunity
    extra = 1


class MonsterDamageResistanceInline(admin.TabularInline):
    model = mdl.MonsterDamageResistance
    extra = 1


class MonsterDamageVulnerabilityInline(admin.TabularInline):
    model = mdl.MonsterDamageVulnerability
    extra = 1


class MonsterSavingThrowInline(admin.TabularInline):
    model = mdl.MonsterSavingThrow
    extra = 1


class MonsterSkillInline(admin.TabularInline):
    model = mdl.MonsterSkill
    extra = 1


class MonsterSenseInline(admin.TabularInline):
    model = mdl.MonsterSense
    extra = 1


class MonsterLanguageInline(admin.TabularInline):
    model = mdl.MonsterLanguage
    extra = 1


class MonsterAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General Information', {
            'fields': (('name', 'armor_class', 'hit_points'), ('challenge', 'experience'), ('STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA'), 'condition_immunities')
        }),
        ('Actions', {
            'classes': ('collapse',),
            'fields': ('actions',)
        }),
        ('Reactions', {
            'classes': ('collapse',),
            'fields': ('reactions',)
        }),
        ('Traits', {
            'classes': ('collapse',),
            'fields': ('traits',)
        }),
        ('Legendary Actions', {
            'classes': ('collapse',),
            'fields': ('legendary_actions',)
        }),
    )
    inlines = [
        MonsterMovementSpeedInline,
        MonsterLanguageInline,
        MonsterSavingThrowInline,
        MonsterSkillInline,
        MonsterSenseInline,
        MonsterDamageImmunityInline,
        MonsterDamageResistanceInline,
        MonsterDamageVulnerabilityInline,
    ]

admin.site.register(mdl.Monster, MonsterAdmin)
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