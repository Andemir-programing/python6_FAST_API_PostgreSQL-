from db import DBClientPerson
from db.session import Session

session = Session()
client = DBClientPerson(session)
mikhail = client.add_person("Mikhail", "I", False)
maria = client.add_person("Maria", "Dolgorukova", True, mikhail.id)
pelagiya = client.add_person("Pelagiya", "", False)
anna = client.add_person("Anna", "", False)
marfa = client.add_person("Marfa", "", False)
alexis = client.add_person("Alexis", "", False)
mariaMiloslavskaya = client.add_person("Maria", "Miloslavskaya", True, alexis.id)

client.update_person(mikhail.id, kids_ids=[pelagiya.id, anna.id, marfa.id, alexis.id])
client.update_person(maria.id, kids_ids=[pelagiya.id, anna.id, marfa.id, alexis.id])
"""
                                       Mikhail I  +  Maria Dolgorukova
                  1.Pelagiya  2.Anna  3.Marfa  4.Alexis + Maria Miloslavskaya
                                        1.Catherine  2.Feodosia  3.Feodor III+Marfa Apraksina
                                                                      1.Ivan V+Praskovia Saltykova  2.Sofia
                                                                    1.Peter I+Catherine  2.Feodosia   3.Natalya
                                                                1.Alexander  2.Pavel
"""