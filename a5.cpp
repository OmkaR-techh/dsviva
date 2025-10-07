#include <iostream>
#include <string>
#include <limits>
using namespace std;

struct Student {
    int roll;
    string name;
    float marks;
    Student* next;
    Student(int r, string n, float m) { roll=r; name=n; marks=m; next=nullptr; }
};

class StudentList {
    Student* head;
public:
    StudentList() { head=nullptr; }

    void add(int r,string n,float m) {
        Student* node=new Student(r,n,m);
        if(!head) head=node;
        else { Student* t=head; while(t->next) t=t->next; t->next=node; }
        cout<<"Added "<<n<<"\n";
    }

    void display() {
        if(!head){ cout<<"No records\n"; return; }
        Student* t=head;
        cout<<"Roll\tName\tMarks\n";
        while(t){ cout<<t->roll<<"\t"<<t->name<<"\t"<<t->marks<<"\n"; t=t->next; }
    }

    Student* search(int r) {
        Student* t=head;
        while(t){ if(t->roll==r){ cout<<"Found "<<t->name<<"\n"; return t; } t=t->next; }
        cout<<"Not found\n"; return nullptr;
    }

    void update(int r,string n="",float m=-1){
        Student* t=search(r);
        if(t){ if(!n.empty()) t->name=n; if(m>=0) t->marks=m; cout<<"Updated\n"; }
    }

    void remove(int r){
        Student* t=head,*p=nullptr;
        while(t){ if(t->roll==r){ if(p) p->next=t->next; else head=t->next; delete t; cout<<"Deleted\n"; return; } p=t; t=t->next; }
        cout<<"Not found\n";
    }

    void sort(bool byMarks=false,bool desc=false){
        if(!head||!head->next) return;
        bool swapped;
        do{
            swapped=false;
            Student* t=head;
            while(t->next){
                bool cond=!byMarks? (!desc && t->roll>t->next->roll) || (desc && t->roll<t->next->roll)
                               : (!desc && t->marks>t->next->marks) || (desc && t->marks<t->next->marks);
                if(cond){ swap(t->roll,t->next->roll); swap(t->name,t->next->name); swap(t->marks,t->next->marks); swapped=true; }
                t=t->next;
            }
        }while(swapped);
        cout<<"Sorted\n";
    }
};

int main(){
    StudentList s;
    int ch;
    do{
        cout<<"\n1.Add 2.Delete 3.Update 4.Search 5.Display 6.Sort RollAsc 7.Sort MarksDesc 8.Exit\nChoice: ";
        if(!(cin>>ch)){ cin.clear(); cin.ignore(numeric_limits<streamsize>::max(),'\n'); cout<<"Invalid input\n"; continue; }
        cin.ignore(numeric_limits<streamsize>::max(),'\n');

        if(ch==1){
            int r; string n; float m;
            cout<<"Roll: "; cin>>r; cin.ignore(numeric_limits<streamsize>::max(),'\n');
            cout<<"Name: "; getline(cin,n);
            cout<<"Marks: "; cin>>m; cin.ignore(numeric_limits<streamsize>::max(),'\n');
            s.add(r,n,m);
        }
        else if(ch==2){
            int r; cout<<"Roll: "; cin>>r; cin.ignore(numeric_limits<streamsize>::max(),'\n'); s.remove(r);
        }
        else if(ch==3){
            int r; string n; float m=-1;
            cout<<"Roll: "; cin>>r; cin.ignore(numeric_limits<streamsize>::max(),'\n');
            cout<<"New Name (leave empty to skip): "; getline(cin,n);
            string tmp;
            cout<<"New Marks (leave empty to skip): "; getline(cin,tmp);
            if(!tmp.empty()){ try{ m=stof(tmp); } catch(...){ m=-1; } }
            s.update(r,n,m);
        }
        else if(ch==4){
            int r; cout<<"Roll: "; cin>>r; cin.ignore(numeric_limits<streamsize>::max(),'\n'); s.search(r);
        }
        else if(ch==5) s.display();
        else if(ch==6) s.sort(false,false);
        else if(ch==7) s.sort(true,true);
    }while(ch!=8);
    cout<<"Exiting...\n";
    return 0;
}
