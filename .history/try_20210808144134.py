
class ClubMember:

    def __init__(self, fn="Jane", ln="Doe", mem_id=-1):
        self.firstName = fn
        self.lastName = ln
        self.member_id = mem_id
        self.is_member = (mem_id != -1) 

    def member_status(self):
        if (self.is_member):
            status = " is "
        else:
            status = " is not "
        return self.firstName + " " + self.lastName + status + "a member"

members = [
    ClubMember(),
    ClubMember("Sam", "Samuelson", 1234),
    ClubMember(ln="Jacobs"),
    ClubMember("John", mem_id=6666)
]

for m in members:
    print(m.member_status())







