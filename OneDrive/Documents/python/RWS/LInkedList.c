#include<stdio.h>

struct node
{
	int info;
	struct nodee *link;
};
struct node* start=NULL;

void traverse()
{
	struct node* temp;
	if(start==NULL)
	printf("list is empty");
	else
	{
		temp=start;
		while(temp!=NULL)
		{
		printf("%d",temp->info);
		temp=temp->link;
	    }
    }
}


void insertAtFront()
{
	int data;
	struct node* temp;
	temp=malloc(sizeof(struct node));
	printf("enter the number to be inserted");
	scanf("%d",&data);
	temp->info=data;
	temp->link=start;
	start=temp;
}

void insertAtEnd()
{
	int data;
	struct node *temp,*head;
	temp=malloc(sizeof(struct node));
	printf("enter number to be inserted");
	scanf("%d",&data);
	temp->info=data;
	temp->link=NULL;
	head=start;
	while(head->link!=NULL){
		head=head->link;
	}
	head->link=temp;
}

void insertAtPosition()
{
	int data,pos,i=1;
	struct node *temp,*newnode;
	temp=malloc(sizeof(struct node));
	printf("enter postion and data");
	scanf("%d %d",&pos,&data);
	temp=start;
	newnode->info=data;
	newnode->link=NULL;
	while(i<pos-1){
		temp=temp->link;
		i++;
	}
	newnode->link=temp->link;
	temp->link=newnode;
}
void deleteFirst()
{
	if(start==NULL)
	{
		printf("list is empty");
	}
	else{
		int temp;
		temp=start;
		start=start->link;
		free(temp);
	}
}
void deleteEnd()
{
	struct node *prevnode,*temp;
	if(start==NULL)
	{
		printf("list is empty");
	}
	else{
		temp=start;
		while(temp->link!=NULL){
			prevnode=temp;
			temp=temp->link;
		}
		free(temp);
		prevnode->link=0;
	}
}

void deletePosition()
{
	struct node *temp,*position;
	int i=1,pos;
	if(start==NULL)
	{
		printf("list is empty");
	}
	else{
		printf("enter position");
		scanf("%d",&pos);
		position=malloc(sizeof(struct node));
		temp=start;
		while(i<pos-1)
		{
			temp=temp->link;
			i++;
		}
		position=temp->link;
		temp->link=position->link;
	    free(position);
	}




void maximum()
{
	int i;
	struct node *temp;
	if(start==NULL){
		printf("list is empty");
	}
	else{
		temp=start;
		int max=temp->info;
		while(temp->link!=NULL){
			if(max<temp->info)
			   max=temp->info;
			temp=temp->link;
		}
		printf("maximum number is %d",max);
	}
}


void mean()
{
	int i;
	struct node *temp;
	if(start==NULL)
	{
		printf("list is empty");
	}
	else{
		temp=start;
		int sum=0,count=0;
		float m;
		while(temp->link!=NULL)
		{
			sum+=temp->info;
			temp=temp->link;
			count++;
		}
		m=sum/count;
		printf("Mean is %f",m);
	}
}

void sort()
{
	struct node *current=start;
	struct node *index=NULL;
	int temp;
	if(start==NULL){
		return;
	}
	else{
		while(current!=NULL){
			while(current->link!=NULL){
				if(current->info>index->info){
					temp=current->info;
					current->info=index->info;
					index->info=temp;
				}
				index=index->link;
			}
			current=current->link;
		}
	}
	
}




int main()
{
    int choice;
    while (1) {
  
        printf("\n\t1  To see list\n");
        printf("\t2  For insertion at"
               " starting\n");
        printf("\t3  For insertion at"
               " end\n");
        printf("\t4  For insertion at "
               "any position\n");
        printf("\t5  For deletion of "
               "first element\n");
        printf("\t6  For deletion of "
               "last element\n");
        printf("\t7  For deletion of "
               "element at any position\n");
        printf("\t8  To find maximum among"
               " the elements\n");
        printf("\t9  To find mean of "
               "the elements\n");
        printf("\t10 To sort element\n");
        printf("\t11 To reverse the "
               "linked list\n");
        printf("\t12 To exit\n");
        printf("\nEnter Choice :\n");
        scanf("%d", &choice);
  
        switch (choice) {
        case 1:
            traverse();
            break;
        case 2:
            insertAtFront();
            break;
        case 3:
            insertAtEnd();
            break;
        case 4:
            insertAtPosition();
            break;
        case 5:
            deleteFirst();
            break;
        case 6:
            deleteEnd();
            break;
        case 7:
            deletePosition();
            break;
        case 8:
            maximum();
            break;
        case 9:
            mean();
            break;
        case 10:
            sort();
            break;
        case 12:
            exit(1);
            break;
        default:
            printf("Incorrect Choice\n");
        }
    }
    return 0;
}
}