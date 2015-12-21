#include <stdio.h>
#include <stdlib.h>

#define LOAD_FACTOR 0.5

typedef struct _NODE
{
	void *val;
	int key;
	struct _NODE *next;
} NODE;

typedef struct
{
	NODE *head;
	NODE *foot;
	int nodeCount;
} LINKED_LIST;

typedef struct
{
	NODE **buckets;
	int bucketsCount;  // m
	int elementsCount;  // n
	float loadFactor;
} LINKED_HASH_MAP;



void put(int key, void *val)
{

}

void *get(LINKED_HASH_MAP *lhm, int key)
{

}