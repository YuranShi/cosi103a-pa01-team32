'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json

class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''
    def __init__(self,courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("courses20-21.json","r",encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = tuple(courses)  # making it a tuple means it is immutable

    def lastname(self,names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self,emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def term(self,terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self,vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self,subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])

    def course(self, subject, course_num):
        ''' subject filters the courses by the subject and the course number '''
        return Schedule([course for course in self.courses if (course['code'][0] == subject and course['code'][1] == course_num)])

    def sort(self,field):
        if field=='subject':
            return Schedule(sorted(self.courses, key= lambda course: course['subject']))
        else:
            print("can't sort by "+str(field)+" yet")
            return self
    
    def title(self,phrase):
        '''title filters courses containing the phrase in their title'''
        return Schedule([course for course in self.courses if phrase in course['name']])
    
    def description(self,phrase):
        '''description filters courses containing the phrase in the description'''
        return Schedule([course for course in self.courses if phrase in course['description']])
    
    def days(self,days_of_week):
        '''days filters classes held on days_of_week'''
        return Schedule([course for course in self.courses if all(day in days_of_week for day in course['times']['days'])])

    def no_waiting(self):
        '''no_waiting filters courses has no one in the waiting list'''
        return Schedule([course for course in self.courses if course['waiting'] == 0])

