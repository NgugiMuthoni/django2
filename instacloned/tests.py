from django.test import TestCase
from .models import Profile, Image, Likes, Comments
from django.contrib.auth.models import User

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.new_user = User(username = "beryl", email = "beryl@gmail.com", password = "show001")
        self.new_user.save()
        self.new_profile = Profile(photo = '/posts', bio = "hello world", user = self.new_user)
        self.new_profile.save()
        self.new_image = Image(picture = '/posts', caption = 'hello new world', posted = '05/30/2020', profile = self.new_profile)
        self.new_image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def tearDown(self):
        Image.objects.all().delete()

    def test_save_image(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_update_caption(self):
        self.new_image.save_image()
        kwargs = {'picture':'/posts', 'caption':'hello new world'}
        Image.update_caption(self.image.id, **kwargs)
        self.assertEqual("just a caption", self.image.caption)

    def test_delete_image(self):
        self.new_image.save_image()
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_get_image_id(self):
        image_id = id
        self.new_image.objects.get(pk=id)
        self.assertTrue(pk=id)

class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User(username = "beryl", email = "beryl@gmail.com", password = "show001")
        self.new_user.save()
        self.new_profile = Profile(photo = '/posts', bio = "hello world", user = self.new_user)
        self.new_profile.save()

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_method(self):
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_profile(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

class CommentsTestClass(TestCase):
    def setUp(self):
        self.new_user = User(username = "beryl", email = "beryl@gmail.com", password = "show001")
        self.new_user.save()
        self.new_profile = Profile(photo = '/posts', bio = "hello world", user = self.new_user)
        self.new_profile.save()
        self.new_comment = Comments(comment='hello django 3', image = self.image, user = self.new_profile, posted = auto_now())

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comments))

    def test_save_method(self):
        self.new_comment.save_comment()
        comments = Comments.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_comments(self):
        self.comments.save_comment()
        self.comments.delete_comment()
        comments = Comments.objects.all()
        self.assertTrue(len(comments) == 0)

    def tearDown(self):
        Comments.objects.all().delete()