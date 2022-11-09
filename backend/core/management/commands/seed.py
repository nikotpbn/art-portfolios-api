from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from portfolio.models import Tag, TagGroup



class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("seeding data...")
        create_tag_groups(self)
        # create_color_tags(self)
        self.stdout.write("seeding finished.")

def create_tag_groups(self):
    create_tag_group(self, 'Author')
    create_tag_group(self, 'Color')
    create_tag_group(self, 'Material')
    create_tag_group(self, 'Generic')


def create_color_tags(self):
    create_tag(self, 'Black')
    create_tag(self, 'White')
    create_tag(self, 'Blue')
    create_tag(self, 'Red')
    create_tag(self, 'Green')
    create_tag(self, 'Yellow')
    create_tag(self, 'Purple')

def create_tag(self, name):
    try:
        tag = Tag.objects.get(name=name)
        self.stdout.write(f'Tag {tag.name} already exists, skipping creation...')

    except ObjectDoesNotExist:
        tag = Tag.objects.create(name=name, group=2)
        self.stdout.write(f'Creating Tag Object: {tag.name}')

def create_tag_group(self, name):
    try:
        tag_group = TagGroup.objects.get(name=name)
        self.stdout.write(f'TagGroup \"{tag_group.name}\" already exists, skipping creation...')

    except ObjectDoesNotExist:
        tag_group = TagGroup.objects.create(name=name)
        self.stdout.write(f'Creating TagGroup Object: {tag_group.name}')