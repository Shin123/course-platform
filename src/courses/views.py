from django.http import Http404
from django.shortcuts import render

import helpers

from . import services


def course_list_view(request):
    queryset = services.get_publish_courses()
    print(queryset)
    context = {"object_list": queryset}
    return render(request, "courses/course_list.html", context)


def course_detail_view(request, course_id=None, *args, **kwargs):
    course_obj = services.get_course_detail(course_id=course_id)
    print(course_obj, "sdsds")
    if course_obj is None:
        raise Http404
    lessons_queryset = services.get_course_lessons(course_obj)
    context = {
        "object": course_obj,
        "lessons_queryset": lessons_queryset,
    }
    return render(request, "courses/course_detail.html", context)


def lesson_detail_view(request, course_id, lesson_id, *args, **kwargs):
    lesson_obj = services.get_lesson_detail(course_id=course_id, lesson_id=lesson_id)
    if lesson_obj is None:
        raise Http404

    email_id_exists = request.session.get("email_id")
    print(email_id_exists, "email_id_exists")
    print(lesson_obj.requires_email, "lesson_obj.requires_email")
    if lesson_obj.requires_email and not email_id_exists:
        print(request.path)
        request.session["next_url"] = request.path
        return render(request, "courses/email-required.html", {})

    template_name = "courses/lesson-coming-soon.html"
    context = {"object": lesson_obj}

    if not lesson_obj.is_coming_soon and lesson_obj.has_video:
        """
        Lesson is published, go forward
        """
        template_name = "courses/lesson_detail.html"
        lesson_embed_html = helpers.get_cloudinary_video_object(
            lesson_obj, field_name="video", as_html=True, width=550, autoplay=False
        )
        context["video_embed"] = lesson_embed_html

    return render(request, template_name, context)
    # return JsonResponse(context)
