from .teachers import get_teachers, get_teacher, delete_teacher
from .courses import get_courses, get_course, delete_course
from .reviews import get_reviews, get_review, create_review, delete_review, update_review
from .users import get_users, get_user, update_user, delete_user

__all__ = ['get_users', 'get_user', 'update_user', 'delete_user', 'get_teachers', 'get_teacher', 'delete_teacher', 'get_courses', 'get_course',
           'delete_course', 'get_reviews', 'get_review', 'create_review', 'delete_review', 'update_review']
