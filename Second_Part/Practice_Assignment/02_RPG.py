

class Weapon():
    
    def __init__(self, WeaponType):
        self.Weapon = WeaponType
    
    def __str__(self):
        return str(self.Weapon)
    
    def Damage(self):
        if self.Weapon == "dagger":
            return 4
        elif self.Weapon == "axe":
            return 6
        elif self.Weapon == "staff":
            return 6
        elif self.Weapon == "sword":
            return 10
        elif self.Weapon =="none":
            return 1
    
        
class Armor():
    
    def __init__(self, ArmorType):
        self.Armor = ArmorType
        
    def __str__(self):
        return str(self.Armor)
    
    def ArmorClass(self):
        if self.Armor == "leather":
            return 2
        elif self.Armor == "chain":
            return 5
        elif self.Armor == "plate":
            return 8
        elif self.Armor == "none":
            return 10










def checkForDefeat(char):
    if char.Health <= 0:
        return "%s has been defeated!"% (char.Name)
    else: 
        return "No"
                
                
                
                
                
                
                
class PRGCharacter():
        
    
    def __init__(self,name):
        self.Name = name
        self.Weapon = Weapon("none")
        self.Armor = Armor("none")
        
    def unwield(self, wp):
        self.Weapon = Weapon("none")
        print (str(self.Name) + " is no longer wielding anything.")
    
    def takeOffArmor(self, ar):
        self.Armor = Armor("none")
        print (str(self.Name) + " is no longer wearing anything.")
        
    def fight(self, other):
        print ("%s attacks %s with a(n) %s"%(str(self.Name),str(other.Name),str(self.Weapon)) )
        other.Health -= self.Weapon.Damage()
        print ("%s does %d damage to %s"%( str(self.Name), self.Weapon.Damage(), str(other.Name) ) )
        print ("%s is now down to %d health" %(str(other.Name), other.Health ) )
        
        Defeated = checkForDefeat(other)
        if Defeated != "No":
            print (Defeated)
                    
    def show(self):
        print(" "+str(self.Name))
        print("   Current Health: %d"%(self.Health) )
        print("   Current Spell Points: %d"%(self.SpellPoint) )
        print("   Wielding: %s"%(self.Weapon) )
        print("   Wearing: %s"%(self.Armor) )
        print("   Armor class: %d"%( self.Armor.ArmorClass()) )
        
        
        
class Fighter(PRGCharacter):
    
    MaxHealth = 40
    Health = 40
    SpellPoint = 0
    
    def wield(self, wp):
        self.Weapon = Weapon(str(wp))
        print (str(self.Name)+" is now wielding a(n) " + str(wp))
        
    def putOnArmor(self, ar):
        self.Armor = Armor(str(ar))
        print (str(self.Name)+" is now wearing " + str(ar))
        
        
        
        
        
        
        
class Wizard(PRGCharacter):
    
    MaxHealth = 16    
    Health = 16
    SpellPoint = 20
        
    def wield(self, wp):
        wpList = ["dagger", "staff", "none"]
        if str(wp) in wpList:
            self.Weapon = Weapon(str(wp))
            print (str(self.Name) + " is now wielding a(n) " + str(wp))
        else:
            print ("Weapon not allowed for this character class.")
            
    def putOnArmor(self, ar):
        if str(ar) != "none":
            print ("Armor not allowed for this character class.")   
    
    def castSpell(self, Spell, other):
        if Spell == "Fireball":
            if self.SpellPoint >= 3:
                
                print ("%s casts %s at %s"%(str(self.Name), Spell, str(other.Name)))
                self.SpellPoint -= 3
                other.Health -= 5
                
                print ("%s does %d damage to %s"%(str(self.Name), 5, str(other.Name) ))
                print ("%s is now down to %d health"%(str(other.Name), other.Health ))
                Defeated = checkForDefeat(other)
                if Defeated != "No":
                    print (Defeated)
                    
            else:
                print("Insufficient spell points")
                
        elif Spell == "Lightning Bolt":
            if self.SpellPoint >= 10:
                print ("%s casts %s at %s"%(str(self.Name), Spell, str(other.Name)))
                
                self.SpellPoint -= 10
                other.Health -= 10
                
                
                print ("%s does %d damage to %s"%(str(self.Name), 10, str(other.Name) ))
                print ("%s is now down to %d health"%(str(other.Name), other.Health ))
                Defeated = checkForDefeat(other)
                if Defeated != "No":
                    print (Defeated)
                    
            else:
                print("Insufficient spell points")
                
        elif Spell == "Heal":
            if self.SpellPoint >= 6:
                
                print ("%s casts %s at %s"%(str(self.Name), Spell, str(other.Name)))
                self.SpellPoint -= 6
                other.Health += 6
                if other.Health > other.MaxHealth:
                    healed = 6 - (other.Health - other.MaxHealth)
                    other.Health = other.MaxHealth
                    print ("%s heals %s for %d health points."%(str(self.Name),str(other.Name), healed )  )    
                else:
                    print ("%s heals %s for %d health points."%(str(self.Name),str(other.Name), 6 ) )
                    
                print ("%s is now at %d health"%(str(other.Name), other.Health) )
                
            else:
                print("Insufficient spell points")    
                
        else:
            print ("Unknown spell name. Spell failed.")
            

      
def main():
    
    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)
    
    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(chainMail)
    aragorn.wield(axe)
    print("")
    
    gandalf.show()
    print("")
    print("")
    aragorn.show()
    print("")

    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)
    print("")
    
    gandalf.show()
    print("")
    print("")
    aragorn.show()
    print("")
    
    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)
    print("")
    
    gandalf.show()
    print("")
    print("")
    aragorn.show()
    print("")
    
    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)
    gandalf.fight(aragorn)
    aragorn.fight(gandalf)
    print("")
    
    gandalf.show()
    print("")
    print("")
    aragorn.show()
    print("")
    
main()
