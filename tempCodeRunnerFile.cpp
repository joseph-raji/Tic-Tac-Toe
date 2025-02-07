code complet:



#include <iostream>
using namespace std;


//Joseph raji 223496 et eric saad 202175

class MyList {
private:
	class Node {

	public:
		float value;
		Node* next;
	};
	Node* first;

public:
	MyList() {
		first = NULL;
	}

	Node* returnFirst() {
		return this->first;
	}

	int count() {
		// retourne le nombre d elements contenu dans la liste
		Node* n = first;
		int count(0);
		while (n != NULL) {
			n = n->next;
			++count;
		}
		return count;
	}

	void add(float x) {
		Node** t = &first;
		for (int i = 0; i < count(); ++i) {
			t = &((*t)->next);
		}
		Node* n = new Node();
		n->value = x;
		n->next = *t;
		*t = n;
	}

	void print() {
		// affiche les elements de la liste
		Node* curr = first;
		while (curr != NULL) {
			cout << curr->value << " ";
			curr = curr->next;
		}
		cout << endl;
	}

	Node* insertionSortList(Node* a) {
		Node* i = a->next;
		while (i != nullptr) {
			Node* key = i;
			Node* j = a;
			while (j != i) {
				if (key->value < j->value) {
					float temp = key->value;
					key->value = j->value;
					j->value = temp;
				}
				j = j->next;
			}
			i = i->next;
		}
		return first;
	}
 
	Node* MergeSort(Node* a) {
		Node* secondNode;

		if (a == NULL)
			return NULL;
		else if (a->next == NULL)
			return a;
		else {
			secondNode = Split(a);
			return Merge(MergeSort(a), MergeSort(secondNode));
		}
	}

	Node* Merge(Node* firstNode, Node* secondNode) {
		if (firstNode == NULL) return secondNode;
		else if (secondNode == NULL) return firstNode;
		else if (firstNode->value <= secondNode->value) //if I reverse the sign to >=, the behavior reverses
		{
			firstNode->next = Merge(firstNode->next, secondNode);
			return firstNode;
		}
		else {
			secondNode->next = Merge(firstNode, secondNode->next);
			return secondNode;
		}
	}

	Node* Split(Node* my_node) {
		Node* secondNode;

		if (my_node == NULL) return NULL;
		else if (my_node->next == NULL) return NULL;
		else {
			secondNode = my_node->next;
			my_node->next = secondNode->next;
			secondNode->next = Split(secondNode->next);
			return secondNode;
		}

	}

};






int main() {
	MyList l = MyList();
	for (int i = 0; i < 6; i++) {
		l.add(rand() % 1000);
	}

	l.print();
	l.MergeSort(l.returnFirst());
	l.print();

	return 0;

}