
create table users (
  id integer primary key autoincrement,
  name varchar(100) ,
  date_ varchar(100) ,
  father varchar(100) ,
  mother varchar(100) ,
  dob varchar(100) ,
  age int ,
  gender varchar(100) ,
  phone varchar(100) ,
  email varchar(100),
  education varchar(100) ,
  address varchar(100) ,
  fam int ,
  occupation varchar ,
  monthly int ,
  volunteer_id varchar ,
  docs int ,
  membership int,
  password varchar(100),
  documents varchar(200),
  isVolunteer int
);
-- isVolunteer will have value 1 if newly registered, 2 if verified by admin

create table volunteers(
  id integer primary key autoincrement,
  name varchar(100) not null,
  rcp_no integer,
  date_ varchar(100) ,
  father varchar(100),
  mother varchar(100) ,
  dob varchar(100) ,
  age int ,
  gender varchar(100) ,
  phone varchar(100) ,
  email varchar(100),
  education varchar(100) ,
  address varchar(100),
  fam int ,
  occupation varchar ,
  monthly int
);
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
);
create table schemes(
    id integer primary key autoincrement,
    name varchar(100) not null,
    description varchar(100) not null,
    lowerbound int not null,
    upperbound int not null,
    gender varchar(100) not null,
    adhar  int ,
    pan int 
);
create table login_users(
  login_ID varchar(100) not null,
  password varchar(100) not null
);
