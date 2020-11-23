class Credentials:
  '''
  The class that generates the credentialsfor the user
  '''
  Credentials_list = []
  
  def __init__(self,service_provider,username,password):
    self.service_provider = service_provider
    self.username = username
    self.password = password
    
    def save_credentials(self):
      '''save user credentials into  the list
      '''
      credentials.credetials_list.append(self)
      
      def delete_credentials(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        Credentials.Credentials_list.remove(self)
        
        @classmethod 
        def display_credentials(cls):
          '''Returns the credential list
          '''
          return cls.credentials_list
        