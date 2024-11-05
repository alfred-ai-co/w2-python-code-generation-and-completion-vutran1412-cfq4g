from sqlalchemy.orm import Session
from app.db_models.base import Project, Ticket


# CRUD operations for Project
# Define a function called create_project that adds a new project record to the database. The function should accept a database session and two parameters: 'name' and 'description'. It should create a new instance of the 'Project' model with the provided 'name' and 'description', add it to the session, commit the transaction, refresh the instance, and return the newly created project.
def create_project(db: Session, name: str, description: str) -> Project:
    project = Project(name=name, description=description)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


# Define a function called get_project that retrieves a project record from the database by its ID. The function should accept a database session and a project ID as parameters. It should query the database for the project with the specified ID and return the first result found.
def get_project(db: Session, project_id: int) -> Project:
    return db.query(Project).filter(Project.id == project_id).first()


# Define a function called update_project that updates an existing project in the database. The function should accept a database session, a project ID, a name, and a description. It should query the database for the project with the specified ID, update its name and description, commit the changes, refresh the project instance, and return the updated project.
def update_project(db: Session, project_id: int, name: str, description: str) -> Project:
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
        project.name = name
        project.description = description
        db.commit()
        db.refresh(project)
    return project


# Define a function called delete_project that removes a project record from the database by its ID. The function should accept a database session and a project ID as parameters. It should first check if the project exists, then delete the project from the session and commit the transaction.
def delete_project(db: Session, project_id: int) -> Project:
    project = db.query(Project).filter(Project.id == project_id).first()
    if project:
        db.delete(project)
        db.commit()
    return project


# CRUD operations for Ticket
# Define a function called create_ticket that adds a new ticket record to the database. The function should accept a database session and the following parameters: 'project_id', 'title', 'description', 'status', and 'priority'. It should create a new instance of the 'Ticket' model with the provided values, add it to the session, commit the transaction, refresh the instance, and return the newly created ticket.
def create_ticket(db: Session, project_id: int, title: str, description: str, status: str, priority: str) -> Ticket:
    ticket = Ticket(project_id=project_id, title=title, description=description, status=status, priority=priority)
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


# Define a function called get_ticket that retrieves a ticket record from the database by its ID. The function should accept a database session and a ticket ID as parameters. It should query the database for the ticket with the specified ID and return the first result found.
def get_ticket(db: Session, ticket_id: int) -> Ticket:
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


# Defined a function called update_ticket that updates an existing ticket in the database. The function should accept a database session, a ticket ID, a project ID, a title, a description, a status, and a priority. It should query the database for the ticket with the specified ID, update its project ID, title, description, status, and priority, commit the changes, refresh the ticket instance, and return the updated ticket.
def update_ticket(db: Session, ticket_id: int, project_id: int, title: str, description: str, status: str, priority: str) -> Ticket:
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket:
        ticket.project_id = project_id
        ticket.title = title
        ticket.description = description
        ticket.status = status
        ticket.priority = priority
        db.commit()
        db.refresh(ticket)
    return ticket


# Define a function called delete_ticket that removes a ticket record from the database by its ID. The function should accept a database session and a ticket ID as parameters. It should first check if the ticket exists, then delete the ticket from the session and commit the transaction.
def delete_ticket(db: Session, ticket_id: int) -> Ticket:
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if ticket:
        db.delete(ticket)
        db.commit()
    return ticket
