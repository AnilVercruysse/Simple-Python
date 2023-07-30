#Practical sheet 5 Exercise 5

initial_string = str(input('Enter the town or city '))

if initial_string == 'Dublin':
    print('You entered Dublin. Dublin is in Leinster')
elif initial_string == 'Belfast':
    print('You entered Belfast. Belfast is in Ulster')
elif initial_string == 'Cork':
    print('You entered Cork. Cork is in Munster')
elif initial_string == 'Limerick':
    print('You entered Limerick. Limerick is in Munster')
elif initial_string == 'Derry':
    print('You entered Derry. Derry is in Ulster')
elif initial_string == 'Galway':
    print('You entered Galway. Galway is in Connacht')
elif initial_string == 'Lisburn':
    print('You entered Lisburn. Lisburn is in Ulster')
elif initial_string == 'Kilkenny':
    print('You entered Kilkenny. Kilkenny is in Leinster')
elif initial_string == 'Waterford':
    print('You entered Waterford. Waterford is in Munster')
elif initial_string == 'Sligo':
    print('You entered Sligo. Sligo is in Connacht')
else:
    print('Sorry, I didn’t recognise that name.')
