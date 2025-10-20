# Building a Course Platform

Build a Course Platform with Django, HTMX, TailwindCSS and Cloudinary.

## Overview

- Courses:
  - Title
  - Description
  - Thumbnail/Image
  - Access:
    - Anyone
    - Email required
    - Purchase required
    - User required (n/a)
  - Status:
    - Published
    - Coming Soon
    - Draft
  - Lessons
    - Title
    - Description
    - Video
    - Status: Published, Coming Soon, Draft
- Email verification for short-lived access
  - Views:
    - Collect user email
    - Verify user email
      - Activate session
  - Models:
    - Email
    - EmailVerificationToken
