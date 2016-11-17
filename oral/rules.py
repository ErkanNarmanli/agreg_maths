import rules

@rules.predicate
def is_lesson_author(user, lesson):
    return lesson.author == user

rules.add_perm('oral', rules.always_allow)
rules.add_perm('oral.change_lesson', is_lesson_author)
rules.add_perm('oral.delete_lesson', is_lesson_author)
