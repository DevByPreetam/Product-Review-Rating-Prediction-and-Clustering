from src.clustering.kmeans import predict_cluster

print("\n===================================")
print("      PRODUCT REVIEW CLUSTERING")
print("===================================")

while True:
    review = input("\nEnter your product review (or type 'exit' to quit): ")

    if review.lower() == "exit":
        print("Thank you!")
        break

    if not review.strip():
        print("Please enter a valid review.")
        continue

    cluster = predict_cluster(review)

    print(f"\nPredicted Cluster: {cluster}")
    print("-----------------------------------")