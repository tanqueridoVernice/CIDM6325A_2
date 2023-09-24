# CIDM6325A_2

# Entity relationship diagrams

## Conceptual
This diagram shows the relationships of colleges, departments, the degrees each department offers, courses the different departments are offering and what courses are required for degree completion, and student information such as the degree they are pursuing and the courses they have taken.
```mermaid
erDiagram
    COLLEGE ||--|{ DEPARTMENT : has
    DEPARTMENT ||--|{ DEGREE : offers
    DEPARTMENT ||--|{ COURSE : offers
    DEGREE }|--|{ COURSE : requires
    STUDENT }|--|| DEGREE : "can have"
    STUDENT }|--|{ COURSE : has
```

## Logical
This diagram shows a more detailed version of the conceptual diagram. It includes the different attributes for each object and it also breaks down the many-to-many relationships we saw earlier on the conceptual diagram.

```mermaid
  erDiagram
    COLLEGE ||--|{ DEPARTMENT :" "

COLLEGE {
        a ID
        b name
}

    DEPARTMENT ||--|{ DEGREE : " "

DEPARTMENT {
a ID
b name
c college
}

DEPARTMENT ||--|{ COURSE : " "
COURSE {
a course_id
b name
c department_offering
d type
e credit_hours
}    

COURSE ||--|{DEGREE_COURSE : " "

DEGREE {
a ID
b name
b department_offering
}

DEGREE_COURSE {
a ID
b degreeID
c courseID
}
    DEGREE ||--|{ DEGREE_COURSE : " "
STUDENT {
a firstname
b lastname
c studentID
d department
e degree
}
STUDENT }|--|| DEGREE : " "
ENROLLED_IN {
a ID
b studentID
c courseID
d semester_taken
}
STUDENT ||--|{ ENROLLED_IN : " "
    COURSE ||--|{ ENROLLED_IN : " "
```
## Physical
This diagram shows the data type of each attribute and also indicates which ones are the primary and foreign keys.
```mermaid
  erDiagram
    COLLEGE ||--|{ DEPARTMENT :" "

COLLEGE {
        int ID PK
        str name
}

    DEPARTMENT ||--|{ DEGREE : " "

DEPARTMENT {
int ID PK
str name
str college FK
}

DEPARTMENT ||--|{ COURSE : " "
COURSE {
str course_id PK
str name
str department_offering FK
str type
int credit_hours
}    

COURSE ||--|{DEGREE_COURSE : " "

DEGREE {
str ID PK
str name
str department_offering FK
}

DEGREE_COURSE {
int ID PK
str degreeID FK
str courseID FK
}
    DEGREE ||--|{ DEGREE_COURSE : " "
STUDENT {
str firstname
str lastname
str studentID PK
str department FK
str degree FK
}
STUDENT }|--|| DEGREE : " "
ENROLLED_IN {
int ID PK
str studentID FK
str courseID FK
str semester_taken
}
STUDENT ||--|{ ENROLLED_IN : " "
    COURSE ||--|{ ENROLLED_IN : " "
```

