# Anti-mirror-Apriori
Shopping cart analysis with a new Apriori algorithm called Anti-mirror-Apriori or AMpriori for short.

## Objective

The objective of this project is to build a novel apriori algorithm to do Market Basket Analysis(MBA) to recommend and up-sell items or groceries to a customer while shopping. 

## Description

A new technique of Anti-Mirroring is introduced to Apriori algorithm and results are compared and tabulated with respect to Time and Space complexity. 

## Input & Output

Input:  Market Basket items from customer purchases over a period of time
Output: Best Pairs or groups of items to purchase

## Tools Used

Python

## EXPERIMENTS & RESULTS

Experiments were done on both Mac OS X (Mountain Lion) & Windows 8 laptops running on Intel i5 Core processor with 4 GB RAM. Python, a high level programming language, is used for implementing the proposed Anti-mirror algorithm and its parent Apriori algorithm. The dataset used for comparing the performance of the proposed algorithm with Apriori algorithm is Groceries dataset. This dataset contains about 10,000 transactions of customers' buying behavior. This Groceries dataset comes in the form of a simple csv file 'groceries.csv'. This csv file contains 10,000 lines, each line represents a single transaction. In each transaction, the products that are bought during that transaction is listed by comma separated values. For example, if one line in the csv file states cereals,whole milk,yolk,cheese, then it means that during one transaction an anonymous customer(as this is not important for us) bought these products. Similarly, 10,000 of those transactions are recorded and forms our dataset for doing Market Basket Analysis. This helps us in finding both the frequent itemsets and then association rules between these products. This paper proposes to find a better Market Basket Analysis algorithm than an apriori algorithm.

## Dataset

The dataset contains 175 distinct items and 10,000 transactions. To benchmark the proposed algorithm, we need to create various sub-datasets from this mother dataset based on parameters like Number of distinct items and Number of Transactions. Each sub-dataset takes a form as "#items #transactions.csv". For example, "3i10t.csv" means this sub-dataset contains 3 distinct items and 10 transactions. Similarly, our largest dataset split is "175i100000t.csv" meaning 175 distinct items and 100,000 transactions. Thus, the groceries dataset is split into varied sized sub-datasets like 3i10t, 5i18t, 10i50t, 40i50t, 40i100t, 100i100t, 100i1000t, 100i2000t, 100i5000t, 175i10000t, 175i25000t, 175i50000t and 175i100000t.

Once the original dataset is split into varied sized datasets, each dataset needs to be tested with the Apriori algorithm and then with the proposed Anti-Mirror algorithm. Their Execution time and Memory Consumption are noted for each run. Each dataset is run for 10 times and their Average Execution Time and Average Memory Consumption parameters are noted and tabulated as shown below. ![here](https://github.com/subashgandyer/Anti-mirror-Apriori/blob/master/Time%20Graph.png) Memory computations are shown below. ![here](https://github.com/subashgandyer/Anti-mirror-Apriori/blob/master/Memory%20Graph.png) These tables show Average Time and Memory for both Apriori and Anti-Mirror algorithms. As it clearly shows that there is a clear winner in Apriori when the number of transactions are less than 1000.  Once the number of transactions increases to more than 10,000, we can clearly see that Anti-mirror is winning in terms of Execution Time. This also clearly states that Apriori is consuming less memory only when there are less number of transactions. Once the transactions are more, say 1000+, it behaves poorly as predicted theoretically. Anti-mirror is the Clear winner in this Memory Consumption metric as it is folding the number of transactions to be analyzed by almost half. The underlying principle of Mirroring played a vital role in reduction of memory consumed.
