db.createUser(
  {
    user: 'iotuser',
    pwd: 'iotp4ssw0rd',
    roles: [
      {
        role: 'readWrite',
        db: 'identidrunk'
      }
    ]
  }
)
