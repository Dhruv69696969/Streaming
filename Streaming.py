from datetime import datetime

class Subscription:
    def __init__(self, plan):
        self.plan = plan
        self.services = self.get_services()
    
    def get_services(self):
        if self.plan == 'Baasic':
            return ['Short Films']
        elif self.plan == 'Standard':
            return ['Short Films', 'Movies']
        elif self.plan == 'Premium':
            return ['Short Films', 'Movies', 'Series']
        else:
            return ['Invalid Plan']
    

class Content:
    def __init__(self, title, content_type):
        self.title = title
        self.content_type = content_type
    

class User(Content):
    
    user_count = 0
    
    def __init__(self, name, plan):
        self.name = name
        self.plan = plan
        self.subscription = Subscription(plan)
        self.user_count += 1
        self.watch_history = []
    
    def get_services(self):
        return self.subscription.services
    
    def get_user_name(self):
        return self.name
    
    def watch(self, Content):
        if Content.content_type in self.subscription.services:
            self.watch_history.append(Content.title)
            self.watch_history.append(datetime.now())
            print(f'Watching {Content.title}')
        else:
            print('You do not have access to this content')
        
    def get_watch_history(self):
        print(self.watch_history)



if __name__ == '__main__':
    user1 = User('John', 'Basic')
    user2 = User('Frank', 'Standard')
    user3 = User('Jane', 'Premium')
    user4 = User('Bob', 'Standard')
    
    short_film1 = Content('The Short Tale', 'Short Films')
    short_film2 = Content('Sing', 'Short Films')
    short_film3 = Content('Dance', 'Short Films')
    short_film4 = Content('The Short Tale 2', 'Short Films')
    short_film5 = Content('The Red Balloon', 'Short Fil#ms')
    movie1 = Content('The LEGO Movie', 'Movies')
    movie2 = Content('The LEGO Movie 2', 'Movies') 
    movie3 = Content('Harry Potter 1', 'Movies')
    movie4 = Content('Fantastic Beasts 1', 'Movies')
    movie5 = Content('Fantastic Beasts 2', 'Movies')
    series1 = Content('Severance', 'Series')
    series2 = Content('The Killing', 'Series')
    series3 = Content('The Crown', 'Series')
    series4 = Content('The Witcher', 'Series')
    series5 = Content('The Witcher 2', 'Series')
    series6 = Content('The Big Bang Theory', 'Series')
    
    user1.watch(short_film2)
    user2.watch(short_film3)
    user3.watch(short_film4)
    user4.watch(short_film5)

    user1.watch(movie1)
    user2.watch(movie2)
    user3.watch(movie4)
    user4.watch(movie5)
    
    user1.watch(series1)
    user2.watch(series3)
    user3.watch(series4)
    user4.watch(series5)
    
    user1.get_watch_history()
    user2.get_watch_history()
    user3.get_watch_history()
    user4.get_watch_history()
    
    print(user1.get_services())
    print('Services for user1\n')
    print(user2.get_services())
    print('Services for user2\n')
    print(user3.get_services())
    print('Services for user3\n')
    print(user4.get_services())
    print('Services for user4\n')
    
    print(user1.get_user_name())
    print(user2.get_user_name())
    print(user3.get_user_name())
    print(user4.get_user_name())
    
    print(User.user_count)
    
    print(user1.user_count)
    print(user2.user_count)
    print(user3.user_count)
    print(user4.user_count)
    
    print(user1.subscription.services)
    print(user2.subscription.services)
    print(user3.subscription.services)
    print(user4.subscription.services)
    
    print(user1.subscription.plan)
    print(user2.subscription.plan)
    print(user3.subscription.plan)
    print(user4.subscription.plan)
    
    print(user1.subscription.get_services())
    print(user2.subscription.get_services())
    print(user3.subscription.get_services())
    print(user4.subscription.get_services())
