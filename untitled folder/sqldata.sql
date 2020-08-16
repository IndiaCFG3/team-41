create table users (
  id integer primary key autoincrement,
  name varchar(100) not null,
  rcp_no integer not null,
  date_ varchar(100) not null,
  father varchar(100) not null,
  mother varchar(100) not null,
  dob varchar(100) not null,
  age int not null,
  gender varchar(100) not null,
  phone varchar(100) not null,
  email varchar(100),
  education varchar(100) not null,
  address varchar(100) not null,
  fam int not null,
  occupation varchar not null,
  monthly int not null,
  volunteer_id varchar not null,
  docs int not null,
  membership int not null
);

create table volunteers(
  id integer primary key autoincrement,
  name varchar(100) not null,
  rcp_no integer not null,
  date_ varchar(100) not null,
  father varchar(100) not null,
  mother varchar(100) not null,
  dob varchar(100) not null,
  age int not null,
  gender varchar(100) not null,
  phone varchar(100) not null,
  email varchar(100),
  education varchar(100) not null,
  address varchar(100) not null,
  fam int not null,
  occupation varchar not null,
  monthly int not null
)


create table membership(
  name varchar(100) not null,
  rcp_no integer not null,
  date_ varchar(100) not null,
  father varchar(100) not null,
  mother varchar(100) not null,
  dob varchar(100) not null,
  age int not null,
  gender varchar(100) not null,
  phone varchar(100) not null,
  email varchar(100),
  education varchar(100) not null,
  address varchar(100) not null,
  city varchar(100) not null,
  state varchar(100) not null,
  occupation varchar not null,
  monthly int not null,
  volunteer_id int not null,
)

create table membership(
  name varchar(100) not null,
  e_id integer not null,
  date_ varchar(100) not null,
  father varchar(100) not null,
  mother varchar(100) not null,
  dob varchar(100) not null,
  age int not null,
  gender varchar(100) not null,
  phone varchar(100) not null,
  email varchar(100),
  education varchar(100) not null,
  address varchar(100) not null,
  city varchar(100) not null,
  state varchar(100) not null,
  password varchar(100) not null,
  userrole int not null
)

create table schemes(
    name varchar(100) not null,
    description varchar(100) not null,
    lowerbound int not null,
    upperbound int not null,
    gender varchar(100) not null,
    adhar  int not null,
    pan int not null
)
