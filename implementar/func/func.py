from abc import ABCMeta,abstractmethod

class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class PersonSection(Section):
    def describe(self):
        print("Personal section")


class AlbumSection(Section):
    def describe(self):
        print("album Section")

class PatentSection(Section):
    def describe(self):
        print("Patent Section")

class PublicationSection(Section):
    def describe(self):
        print("Publication Section")

class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()
    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self,section):
        self.sections.append(section)

class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonSection())
        self.addSections(AlbumSection())

if __name__ == "__main__":
    profile_type = input("which profile you d like to create [linkedIn or facebook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile...",type(profile).__name__)
    print("profile has sections --",profile.getSections())
