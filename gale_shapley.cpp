#include<iostream>
#include<cstdio>
#include<cmath>
#include<fstream>
#include<string>
#include<sstream>
#include <stdlib.h>
#include<list>
#include<vector>
#include<map>
#include<iterator>
using namespace std;
struct student
{   string name;
    string current;
};
struct branch
{
    double sanctioned;
    double current;
    bool status;
    double least_in_curr_iter;
    double rejected_cutoff;
};

map<string,branch>strength;
map<string,student>details;
map<string,int>progress;
vector<string>list_of_branches;

bool acc_to_cpi(vector<string>a,vector<string>b)
{
    if((double)atof((a[3]).c_str()) >= (double)atof((b[3]).c_str()))
    {
        return true;
    }
    else return false;
}

int main()
{
    int line=0;
    list<vector<string> >input;
    string value;
    int num=0;
    int total_strength_current=0;
    int total_applied=0;
    string temp;
    string input_options ;
    string input_programmes;
    cout<<"Give input_options file : ";
    getline(cin,input_options);
    cout<<"Give input_programmes file : ";
    getline(cin,input_programmes);
    ifstream pref ( input_options );
        while ( !pref.eof() )
    {
        getline ( pref, value );
        if(value.size()!=0)
        {
            vector<string> strings;
            istringstream f(value);
            string s;
            while (getline(f, s, ','))
            {
                if(s.size()!=0)
                strings.push_back(s);
            }
            strings[0]+=49+line;
            input.push_back(strings);
            progress[strings[0]]=strings.size();
            student st;
            st.name = strings[1];
            st.current = strings[2];
            details[strings[0]]=st;
        }
        line++;
    }

    pref.close();

    ifstream stat(input_programmes);
    while ( !stat.eof() )
    {
        getline ( stat, value);
        if(value.size()!=0)
        {
            vector<string>parts;
            istringstream f(value);
            string s;
            while (getline(f, s, ','))
            {
                parts.push_back(s);
            }
            branch b;
            b.sanctioned = (double)atof((parts[1]).c_str());
            b.current = (double)atof((parts[2]).c_str());
            b.status = true;
            b.least_in_curr_iter = 11.0;
            b.rejected_cutoff  = -1.0;
            strength[parts[0]] = b;
            list_of_branches.push_back(parts[0]);
            total_strength_current+=b.current;
        }
    }
 
    stat.close();

    if(total_strength_current < line){
     cout<<"\nError:\nNo.of applied students for branch change are more than the total strength.\nCheck input_options file and input_programmes file.\n";
      return 0;
    }

    input.sort(acc_to_cpi);

    int count = 0;
    int first_pref = 0;

    do
    {
        count=0;
        for(list<vector<string> >::iterator it1=input.begin(); it1 != input.end(); ++it1)
        {
            if(((*it1)[4] == "SC" || (*it1)[4] == "ST" || (*it1)[4] == "PwD") && (double)atof(((*it1)[3]).c_str()) <7.00)
            {
            (*it1)[2] = "Ineligible";
            progress[(*it1)[0]]=-1;
                first_pref++;
            }

            if(((*it1)[4] == "GE" || (*it1)[4] == "OBC") && (double)atof(((*it1)[3]).c_str()) <8.00)
            {
            (*it1)[2] = "Ineligible";
            progress[(*it1)[0]]=-1;
                first_pref++;
            }

            if(progress[(*it1)[0]]!=-1 && progress[(*it1)[0]]!=5)
            {
            for(int i=5; i<progress[(*it1)[0]]; i++)
                {
                    if( ((strength[(*it1)[i]]).status || (strength[(*it1)[i]]).rejected_cutoff == (double)atof(((*it1)[3]).c_str())) &&
                        (double)atof(((*it1)[3]).c_str()) >= 9.00 &&
                        (((strength[(*it1)[2]]).current + 1) <= round(((strength[(*it1)[i]]).sanctioned)*1.1) ||
                        (double)atof(((*it1)[3]).c_str()) == (strength[(*it1)[i]]).least_in_curr_iter ) )
                    {
                        (strength[(*it1)[2]]).current--;
                        (strength[(*it1)[i]]).current++;
                        (*it1)[2]=(*it1)[i];
                        strength[(*it1)[i]].least_in_curr_iter = (double)atof(((*it1)[3]).c_str());
                        count++;
                        progress[(*it1)[0]] = i;
                        if(i==5){first_pref++;}
                        break;
                    }
                    else
                    {
                        if( ((strength[(*it1)[i]]).status || (strength[(*it1)[i]]).rejected_cutoff == (double)atof(((*it1)[3]).c_str())) &&
                            (((strength[(*it1)[2]]).current-1) >= round(((strength[(*it1)[2]]).sanctioned)*0.75) ||
                            (double)atof(((*it1)[3]).c_str()) == (strength[(*it1)[i]]).least_in_curr_iter) &&
                            (((strength[(*it1)[i]]).current + 1) <= round(((strength[(*it1)[i]]).sanctioned)*1.1) ||
                            (double)atof(((*it1)[3]).c_str()) == (strength[(*it1)[i]]).least_in_curr_iter ) )
                        {
                            (strength[(*it1)[2]]).current--;
                            (strength[(*it1)[i]]).current++;
                            (*it1)[2]=(*it1)[i];
                            strength[(*it1)[i]].least_in_curr_iter = (double)atof(((*it1)[3]).c_str());
                            count++;
                            progress[(*it1)[0]] = i;
                            if(i==5){first_pref++;}
                            break;
                        }
                        else
                        {
                            (strength[(*it1)[i]]).status = false;
                            if((strength[(*it1)[i]]).rejected_cutoff < (double)atof(((*it1)[3]).c_str()))
                            (strength[(*it1)[i]]).rejected_cutoff = (double)atof(((*it1)[3]).c_str());
                        }
                    }
                }
            }
        }

        for(int j=0; j<list_of_branches.size(); j++)
        {
            strength[list_of_branches[j]].status = true;
            strength[list_of_branches[j]].rejected_cutoff = -1.0;
        }
    }
    while(count != 0 && first_pref != input.size());

    ofstream allotfile ("allotment.csv");
    for(list<vector<string> >::iterator it1=input.begin(); it1 != input.end(); ++it1)
    {   if(details[(*it1)[0]].current == (*it1)[2]){(*it1)[2]="Branch Unchanged";}
        string s = details[(*it1)[0]].current;
        ((*it1)[0]).pop_back();
        allotfile<<(*it1)[0]<<","<<(*it1)[1]<<","<<s<<","<<(*it1)[2]<<" \n";
    }

    allotfile.close();
    ofstream strengthfile("output_stats.csv");

    map<string,branch>::iterator it;
    for(it = ++strength.begin();it != strength.end();it++){
         strengthfile<<(it->first)<<",";
         strengthfile<<(it->second).sanctioned<<","<<(it->second).current<<endl;
    }

    strengthfile.close();
}
