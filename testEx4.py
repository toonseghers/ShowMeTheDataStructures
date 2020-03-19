class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name



def is_user_in_group(user, group):

    try:
        users=group.get_users()
        user_in_group={}
        user=str(user)

        if len(users) > 0:
            for u in users:
                if u == user:
                    return True

        groups=group.get_groups()

        for g in groups:
            if g.name in user_in_group:
                return
            else:
                if is_user_in_group(user, g) == True:
                    return True
                else:
                    user_in_group[g.name]=False

        return False
    except TypeError:
        print("Stop")
        return

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Example 4
# Edge case
# No user inputed
is_user_in_group(parent)
