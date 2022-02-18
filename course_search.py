'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule
import sys

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5, 1000))  # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
'''

terms = {c['term'] for c in schedule.courses}


def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:
        command = input(">> (h for help) ")
        if command == 'quit':
            return
        elif command in ['h', 'help']:
            print(TOP_LEVEL_MENU)
            print('-' * 40 + '\n\n')
            continue
        elif command in ['r', 'reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5, 1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:" + str(terms) + ":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s', 'subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
        elif command in ['c', 'course']:
            subject = input("enter a course (subject-course_number):")
            schedule = schedule.course(subject.split('-')[0], subject.split('-')[1])
        elif command in ['i', 'instructor']:
            user_input = input("enter the email or the last name of the instructor:")
            if '@' in user_input:
                schedule = schedule.email([user_input])
            else:
                schedule = schedule.lastname([user_input])
        elif command in ['title']:
            title = input("enter the title of a course:")
            schedule = schedule.title(title)
        elif command in ['d', 'description']:
            desc = input("enter the description of a course:")
            schedule = schedule.description(desc)
        elif command in ['w', 'no_waiting']:
            schedule = schedule.no_waiting()
        elif command in ['d', 'days']:
            days_input = input("enter the days of the class")
            schedule = schedule.days(days_input)
        else:
            print('command', command, 'is not supported')
            continue

        print("courses has", len(schedule.courses), 'elements', end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n' * 3)


def print_course(course):
    '''
    print_course prints a brief description of the course 
    '''
    print(course['subject'], course['coursenum'], course['section'],
          course['name'], course['term'], course['instructor'])


if __name__ == '__main__':
    topmenu()
