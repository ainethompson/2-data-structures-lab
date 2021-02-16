"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()
    file = open(filename)

    for line in file:  
      house = line.split('|')[2]
      
      if house:
        houses.add(house)

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []

    file = open(filename)

    for line in file:
      data = line.rstrip().split('|')

      full_name, group = f"{data[0]} {data[1]}", data[4]
   
      if group not in ('I', 'G') and cohort in ('All', group):
        students.append(full_name)

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    rosters = [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin, ghosts, instructors]

    file = open(filename)

    for line in file:
      data = line.rstrip().split('|')

      full_name, house, advisor, cohort = f"{data[0]} {data[1]}", data[2], data[3], data[4]

      if house == "Dumbledore's Army":
        dumbledores_army.append(full_name)
      elif house == "Gryffindor":
        gryffindor.append(full_name)
      elif house == "Hufflepuff":
        hufflepuff.append(full_name)
      elif house == "Ravenclaw":
        ravenclaw.append(full_name)
      elif house == "Slytherin":
        slytherin.append(full_name)
      elif cohort == "G":
        ghosts.append(full_name)
      elif cohort == "I":
        instructors.append(full_name)
 
    for item in rosters:
          item.sort()
 
    return rosters


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    file =  open(filename)

    for line in file:
      data = line.rstrip().split('|')

      full_name, house, advisor, cohort = f"{data[0]} {data[1]}", data[2], data[3], data[4]
      my_tuple = (full_name, house, advisor, cohort)

      all_data.append(my_tuple)

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """
    for full_name, _, _, cohort in all_data(filename):
        if full_name == name:
            return cohort


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    file =  open(filename)

    seen = set()
    dupes = set()

    for line in file:
      lname = line.rstrip().split('|')[1]

      if lname in seen:
        dupes.add(lname)

      seen.add(lname)

    return dupes


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """
#     find given student info
#     loop thru file
#     if name same as given name, set house and cohort to variables
#     
#     For student in file:
          # if house same as chosen_house and cohort same as chosen_cohort:
          # add student full name to housemates set
#     loop thru other students, add to set if same cohort and house

#  what about students before given student in the file, loop back?

    housemates = set()

    target_person = None

    for person in all_data(filename):
      full_name, house, _, cohort_name = person

      if full_name == name:
        target_person = person
        break

    if target_person:
      target_name, target_house, _, target_cohort = target_person

      for full_name, house, _, cohort_name in all_data(filename):
        if ((house, cohort_name) == (target_house, target_cohort) and
                  full_name != name):
          housemates.add(full_name)

    return housemates
        

##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
