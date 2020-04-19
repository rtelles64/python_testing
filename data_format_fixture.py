import pytest


@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]
    

def format_data_for_display(people):
    '''
    Formats data returned from an API endpoint.

    Parameters
    ----------
    people : list
        A list of people with a given name, family name, and
        job title
        
    Returns
    -------
    list
        A list of strings formatted to include the person's full
        name (given name followed by family name) and their title.
    '''
    return [
        f"{person['given_name']} {person['family_name']}:"
        f" {person['title']}"
        
        for person in people
    ]


def format_data_for_excel(people):
    '''
    Formats data returned from an API endpoint.

    Parameters
    ----------
    people : list
        A list of people with a given name, family name, and
        job title
        
    Returns
    -------
    str
        A string formatted to include the person's full
        name (given name followed by family name) and their title
        in comma-separated values.
    '''
    header = ','.join(people[0].keys())
    values = [','.join(person.values()) for person in people]

    # rejoin with new lines
    values = '\n'.join(values)

    return f"{header}\n{values}"


def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]


def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == (
        "given_name,family_name,title\n"
        "Alfonsa,Ruiz,Senior Software Engineer\n"
        "Sayid,Khan,Project Manager"
    )
