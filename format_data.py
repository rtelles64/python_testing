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
        A list of strings formatted to include the person' full
        name (given name followed by family name) and their title.
    '''
    return [
        f"{person['given_name']} {person['family_name']}:"
        f" {person['title']}"
        
        for person in people
    ]


def test_format_data_for_display():
    '''
    Tests format_data_for_display function.
    '''
    people = [
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

    assert format_data_for_display(people) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]
